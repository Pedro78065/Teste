from fastapi import APIRouter, Depends, HTTPException
from src.models.mysql_models import select_user_all, insert_user
from src.schemas.schemas import UserSchema
from src.dependencies.dependencies import pegar_table

auth_router = APIRouter(prefix = "/auth", tags = ["Auth"])

@auth_router.get("/")
async def home():
    return {"mensagem": "está no àr"}


@auth_router.post("/create-account")
async def criar_conta(usuario_schema: UserSchema, session = Depends(pegar_table)):
    session
    try:
        emails = [email[0] for email in select_user_all()]
        if usuario_schema.email in emails:
            raise HTTPException(status_code = 403, detail = "Já existe um usuário com esse email")
        else:
            insert_user(usuario_schema.nome, usuario_schema.email, usuario_schema.senha, usuario_schema.ativo, usuario_schema.admin)
            return {"mensagem": f"Usuário {usuario_schema.email} adicionado com sucesso"}
    except Exception as e:
        print(f"Error:{e}")


