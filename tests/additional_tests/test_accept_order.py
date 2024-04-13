import json
import requests
import allure
import test_data


class TestAcceptOrder:

    @allure.title('Принять заказ')
    def test_accept_order_success(self, current_login_password):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }
        response = requests.post(test_data.LOGIN_COURIER, data=payload)
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
        response = requests.post(test_data.CREATE_ORDER, data=payload_string)
        print(response.status_code, response.json())
        order_id = response.json()["track"]

        print(f"{test_data.ACCEPT_ORDER}{order_id}?courierId={courier_id}")

        response = requests.put(f"{test_data.ACCEPT_ORDER}{order_id}?courierId={courier_id}")
        print(response.status_code, response.json())
        assert response.status_code == 200




