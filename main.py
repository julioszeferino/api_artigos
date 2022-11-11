from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router as api_router_v1

app = FastAPI(title="Curso API - Seguranca")

app.include_router(api_router_v1, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level='info')


# Token felicity
# podemos validar em https://jwt.io/
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjY4NzQxMjUzLCJpYXQiOjE2NjgxMzY0NTMsInN1YiI6IjIifQ.wtDsAOFPvO5XxGaCAH6EgvOksb1Mwd3OI14J4vmT6mU",
#   "token_type": "bearer"
# }


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjY4NzQyNzg1LCJpYXQiOjE2NjgxMzc5ODUsInN1YiI6IjQifQ.Kw6zhmGlXYbpOqOItQ9Vdn9BJyX9zuTv9FI6dcETDZM