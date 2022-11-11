from pytz import timezone

from typing import Optional, List
from pydantic import EmailStr # valida email
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt

from models.usuario_model import UsuarioModel
from core.configs import settings
from core.security import verificar_senha


# criando um endpoint para a autenticacao
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login"
    )

async def autenticar(email: EmailStr, senha: str, bd: AsyncSession) -> Optional[UsuarioModel]:
    """
    Funcao responsavel por autenticar o usuario, recebe as credenciais e valida
    no banco de dados.
    """
    async with bd as session:
        query = select(UsuarioModel).where(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        # verificando a existencia do usuario
        if not usuario:
            return None

        # verificando a validade da senha
        if not verificar_senha(senha, usuario.senha):
            return None

        return usuario


def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    # https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    payload = {}

    timezone_sp = timezone('America/Sao_Paulo')
    expira = datetime.now(tz=timezone_sp) + tempo_vida # data de expiracao do token

    payload["type"] = tipo_token
    payload["exp"] = expira
    payload["iat"] = datetime.now(tz=timezone_sp) # data de criacao do token
    payload["sub"] = str(sub) # identificador do usuario

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


def criar_token_acesso(sub: str) -> str:
    """
    https://jwt.io/
    """
    return _criar_token(
        tipo_token="access_token",
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )