from fastapi import FastAPI
import uvicorn

app = FastAPI()

from src.paths import auth_router, order_router

app.include_router(auth_router)
app.include_router(order_router)

if __name__ == "__main__":
    uvicorn.run(
        app = "main:app",
        host = "localhost",
        port = 8000,
        reload = True
    )