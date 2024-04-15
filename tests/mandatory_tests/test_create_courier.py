import pytest
import requests
import allure
import helpers
from urls import Url, Endpoint


class TestCreateCourier:

    @allure.title('Создание курьера. Ожидается правильный код и текст ответа')
    def test_create_courier_success(self):

        payload = helpers.generate_login_password()

        response = requests.post(f"{Url.BASE_URL}{Endpoint.COURIER}", data=payload)

        assert response.status_code == 201 and response.json()["ok"] == True

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_existed_courier(self):

        payload = payload = helpers.generate_login_password()

        requests.post(f"{Url.BASE_URL}{Endpoint.COURIER}", data=payload)
        response = requests.post(f"{Url.BASE_URL}{Endpoint.COURIER}", data=payload)

        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется."
        # Баг. Возвращается другой текст в ответе: 'Этот логин уже используется. Попробуйте другой.'


    @allure.title('Создание курьера, если одно из обязательных полей пропущено')
    @pytest.mark.parametrize("deleted_field", ["login", "password"])
    def test_create_courier_without_mandatory_fields(self, deleted_field):

        payload = helpers.generate_login_password()

        del payload[deleted_field]
        response = requests.post(f"{Url.BASE_URL}{Endpoint.COURIER}", data=payload)

        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Создание курьера, если одно из обязательных полей не заполнено')
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_create_courier_empty_mandatory_fields(self, empty_field):

        payload = helpers.generate_login_password()

        payload[empty_field] = ""
        response = requests.post(f"{Url.BASE_URL}{Endpoint.COURIER}", data=payload)

        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

