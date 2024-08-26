import json
import requests
import allure

from urls import Url, Endpoint

class TestGetOrderByNumber:

    @allure.title('Успешное получение заказа по его номеру')
    def test_get_order_by_number_success(self, ):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": []
        }

        payload_string = json.dumps(payload)
        response = requests.post(f"{Url.BASE_URL}{Endpoint.ORDER}", data=payload_string)
        order_id = response.json()["track"]
        response = requests.post(f"{Url.BASE_URL}{Endpoint.GET_ORDER_BY_NUMBER}?t={order_id}")

        assert response.status_code == 200 and 'order' in response.json()
