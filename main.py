from fastapi import FastAPI
import uvicorn 
from cadastrar_usuario.router import cadastrar_usuario_router
from perfil.router import perfil_router
from cadastrar_usuario.models.cadastrar_usuario_models import CadastrarUsuario
from shared.database import Base, engine

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def home_page():
    return "<h1>Wellcome to Home Page</h1>"


app.include_router(cadastrar_usuario_router.router)
app.include_router(perfil_router.router_perfil)


if __name__ == "__main__":
    uvicorn.run(app, port=8002)