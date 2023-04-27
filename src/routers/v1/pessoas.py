from fastapi import APIRouter
from fastapi_versioning import versioned_api_route
from src.models.pessoa import Pessoa
from src.services.pessoa import PessoaService

pessoasrouter = APIRouter(
    prefix="/pessoas",
    tags=["pessoas"],
    redirect_slashes=False,
    route_class=versioned_api_route(1, 0)
)

@pessoasrouter.post("/", status_code=201)
async def add_pessoa(pessoa: Pessoa):
    return await PessoaService().adiciona_pessoa(pessoa)