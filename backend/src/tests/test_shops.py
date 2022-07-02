from fastapi.testclient import TestClient

from src.main import app

class TestShops:
    client = TestClient(app)

    def test_make_shops(self):
        response = self.client.get("/shops/makeshops")
        assert response.status_code == 201

    def test_get_shops(self):
        response = self.client.get("/shops")
        
        assert response.status_code == 200
        print(f"Get shop list response: {response.json()}")