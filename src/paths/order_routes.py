from fastapi import APIRouter

order_router = APIRouter(prefix = "/order", tags = ["Order"])

@order_router.get("/")
async def home():
    return {"mensagem": "está no àr"}