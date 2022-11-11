from fastapi.testclient import TestClient
import json
 
URL_T = "/api/v1/veiculos/"
payload = json.dumps({
  "modelo": "oi",
  "marca": "string",
  "status": "string",
  "placa": "string",
  "ano_a": 0,
  "modelo_a": "string",
  "chassi": "string",
  "quilometragem": 0,
  "npatrimonio": "string",
  "autor": "string",
  "idfazenda": 1
})
 
 
 
def test_get_veiculos(client: TestClient) -> None:
    response = client.get(URL_T)
    body = response.json()
    assert response.status_code == 200
 
def test_post_veiculo(client: TestClient) -> None:
    response = client.post(URL_T, json=payload)
    print(response.json())
    assert response.status_code == 201
    assert response.json() == payload
