from fastapi.testclient import TestClient


def test_example_200(api_client: TestClient):
    """
    GET /example/aaa OK
    """
    response = api_client.get("/example/aaa")
    assert response.json() == {"responseValue": "AAA"}
