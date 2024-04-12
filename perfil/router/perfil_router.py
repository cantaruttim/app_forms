from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router_perfil = APIRouter(prefix="/perfil")

@router_perfil.get("/{first_name}")
async def perfil(first_name : str):
    texto_saudacao = f"Olá, {first_name}! Seja muito bem-vindo!"
    return texto_saudacao