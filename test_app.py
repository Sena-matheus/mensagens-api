import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_mensagens(client):
    response = client.get('/mensagens')
    assert response.status_code == 200
    assert "mensagens" in response.get_json()

def test_get_mensagem_aleatoria(client):
    response = client.get('/mensagens?aleatoria=true')
    assert response.status_code == 200
    assert "mensagem" in response.get_json()

def test_post_mensagem_sucesso(client):
    nova = {"mensagem": "Acredite em você!"}
    response = client.post('/mensagens', json=nova)
    assert response.status_code == 201
    assert response.get_json()["status"] == "sucesso"

def test_post_mensagem_vazia(client):
    response = client.post('/mensagens', json={"mensagem": ""})
    assert response.status_code == 400
    assert response.get_json()["erro"] == "Mensagem não pode estar vazia."