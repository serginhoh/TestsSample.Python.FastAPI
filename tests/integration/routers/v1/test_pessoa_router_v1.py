from fastapi.testclient import TestClient
from src.app import app
from src.models.pessoa import Pessoa
from datetime import datetime

client = TestClient(app)

def test_pessoa_router_v1_post_deve_retornar_http_201():
    #arrange
    json = {"nome": "teste", "aniversario": "2000-01-01"}

    #act
    response = client.post('/v1/pessoas/', json=json, headers={"X-Token": "coneofsilence"})

    #assert
    assert response.status_code == 201
    assert response.json() == json

def test_pessoa_router_v1_post_deve_retornar_http_422():
    #arrange
    json = {"nome": "", "aniversario": "2000-01-01"}
    resultjson = {
        "detail": [
            {
            "loc": [
                "body",
                "nome"
            ],
            "msg": "Nome não pode ser vazio",
            "type": "value_error"
            }
        ]
    }

    #act
    response = client.post('/v1/pessoas/', json=json, headers={"X-Token": "coneofsilence"})

    #assert
    assert response.status_code == 422
    assert response.json() == resultjson