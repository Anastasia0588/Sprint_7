import pytest
import requests
import json
import allure

import test_data

class TestCreateOrder:

    @allure.title('Создание заказа с разными цветами')
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_orders_with_different_colors(self, color):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }

        payload_string = json.dumps(payload)
        response = requests.post(test_data.CREATE_ORDER, data=payload_string)

        assert response.status_code == 201 and "track" in response.json()
