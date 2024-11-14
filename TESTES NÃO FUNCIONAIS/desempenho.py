from locust import HttpUser, task, between

class EcommerceUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def access_cart(self):
        self.client.get("/cart")

    @task
    def add_to_cart(self):
        self.client.post("/cart", json={"product_id": "123", "quantity": 1})

        