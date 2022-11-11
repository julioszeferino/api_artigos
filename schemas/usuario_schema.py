from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema

# schema com os dados basicos do usuario
class UsuarioSchemaBase(BaseModel):
    
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        orm_mode = True

# quando o usuario for cadastrar, ele vai informar os dados anteriores e a senha
# mas pra devolver os dados na response, nos geralmente nao vamos mostrar a senha
# por isso e importante criar schemas alternativos
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]

class UsuarioSchemaUp(UsuarioSchemaBase):
    # sao opcionais porque nao vou alterar todos os dados do usuario sempre
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]


