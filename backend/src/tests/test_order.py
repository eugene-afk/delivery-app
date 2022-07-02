from fastapi.testclient import TestClient

from src.main import app

class TestOrder:
    client = TestClient(app)

    def test_add_order(self):
        response = self.client.post(
            "/orders/",
            json={
                "email": "somemail@com.com", 
                "phone": "0568885544", 
                "name": "Petro",
                "address": "Pushkina Street, 5",
                "shop_id": 1,
                "amount": "500",
                "order_products": [
                    {
                        "product_id": 1,
                        "qty": 2
                    },
                    {
                        "product_id": 3,
                        "qty": 3
                    },
                    {
                        "product_id": 4,
                        "qty": 1
                    }
                ]
            },
        )

        assert response.status_code == 200
        print(f"Add new order response: {response.json()}")

    def test_get_orders_by_email(self):
        response = self.client.get("/orders?search=somemail@com.com")

        print(f"Get orders by email response: {response.json()}")
        assert response.status_code == 200

    def test_get_orders_by_email_error(self):
        response = self.client.get("/orders?search=somdsemail@com.com")

        print(f"Get orders by email response: {response.json()}")
        assert response.json() == []
        assert response.status_code == 200
