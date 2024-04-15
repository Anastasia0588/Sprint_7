import json
import requests
import allure

from urls import Url, Endpoint


class TestAcceptOrder:

    @allure.title('Принять заказ')
    def test_accept_order_success(self, current_login_password):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }
        response = requests.post(f"{Url.BASE_URL}{Endpoint.LOGIN}", data=payload)
        courier_id = response.json()["id"]
        print(response.status_code, response.json())

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"]
        }

        payload_string = json.dumps(payload)
        response = requests.post(f"{Url.BASE_URL}{Endpoint.ORDER}", data=payload_string)
        print(response.status_code, response.json())
        order_id = response.json()["track"]

        response = requests.put(f"{Url.BASE_URL}{Endpoint.ACCEPT_ORDER}{order_id}?courierId={courier_id}")

        assert response.status_code == 200 and 'order' in response.json()




