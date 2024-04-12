from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/cadastrar-usuario")


## Definicação das classes por meio do pydantic
## CLASSES
class CadastrarNovoCliente(BaseModel):
    id: int
    first_name: str
    email: str
    telephone: str
    desired_product: str


class CadastrarNovoCliente(BaseModel):
    id: int
    first_name: str
    email: str
    telephone: str
    desired_product: str



@router.get("/", response_model=List[CadastrarNovoCliente])
def listar_contas():
    return [
        CadastrarNovoCliente(
            id = 1, first_name="Mathew", email="matheus_banochi@gmail.com",
            telephone="+55(11) 95877-3554", desired_product="Boxe cloves"
        ),
        CadastrarNovoCliente(
            id = 2, first_name="Victoria", email="victoria_wesley@gmail.com",
            telephone="+55(11) 95277-3354", desired_product="MacBook Air PRO"
        )
    ]


@router.post("/", response_model=CadastrarNovoCliente, status_code=201)
def criar_usuario(users: CadastrarNovoCliente):
    return CadastrarNovoCliente(
        id=3,
        first_name = users.first_name,
        email = users.email,
        telephone = users.telephone,
        desired_product = users.desired_product 
    )