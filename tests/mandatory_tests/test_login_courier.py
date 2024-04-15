import pytest
import requests
import allure

import helpers
from urls import Url, Endpoint


class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_login_courier_success(self, current_login_password):
        print(current_login_password)

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        response = requests.post(f"{Url.BASE_URL}{Endpoint.LOGIN}", data=payload)

        assert response.status_code == 200 and 'id' in response.json()


    @allure.title('Авторизация курьера, если одно из обязательных полей пропущено')
    @pytest.mark.parametrize("deleted_field", ["login", "password"])
    def test_login_courier_without_mandatory_fields(self, current_login_password, deleted_field):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        del payload[deleted_field]
        response = requests.post(f"{Url.BASE_URL}{Endpoint.LOGIN}", data=payload)

        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"
        # Баг. В ответе возвращается ошибка 504, если не задан password


    @allure.title('Авторизация курьера, если одно из обязательных полей не заполнено')
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_login_courier_empty_mandatory_fields(self, current_login_password, empty_field):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        payload[empty_field] = ""
        response = requests.post(f"{Url.BASE_URL}{Endpoint.LOGIN}", data=payload)

        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"


    @allure.title('Авторизация несуществующего пользователя')
    def test_login_not_existed_courier_failed(self):

        payload = helpers.generate_login_password()
        del payload["firstName"]

        response = requests.post(f"{Url.BASE_URL}{Endpoint.LOGIN}", data=payload)

        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"


    @allure.title('Авторизация с неправильно введенными данными')
    @pytest.mark.parametrize("edited_field", ["login", "password"])
    def test_login_wrong_creds_failed(self, current_login_password, edited_field):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        payload[edited_field] += "1"
        print(payload)

        response = requests.post(f"{Url.BASE_URL}{Endpoint.LOGIN}", data=payload)

        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"
