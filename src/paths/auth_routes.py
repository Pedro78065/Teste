from fastapi import APIRouter, Depends, HTTPException
from src.models.mysql_models import table_user, insert_user, select_user_fromEmail
from src.schemas.schemas import UserSchema

auth_router = APIRouter(prefix = "/auth", tags = ["Auth"])

@auth_router.get("/")
async def home():
    return {"mensagem": "está no àr"}


@auth_router.post("/create-account")
async def criar_conta(usuario_schema: UserSchema, session = Depends(table_user)):
    try:
        session
        email = select_user_fromEmail(usuario_schema.email)
        if usuario_schema == email["email"]:
            raise HTTPException(status_code = 409, detail = "Um usuário com esse email já existe")
        else:
            insert_user(usuario_schema.nome, usuario_schema.email, usuario_schema.senha, usuario_schema.ativo, usuario_schema.admin)
            return {"mensagem": f"usuário {usuario_schema.nome} cadastrado com sucesso"}
    except Exception as e:
        print(f"Error:{e}")

