import pytest
import requests
import allure

import test_data


class TestLoginCourier:

    def test_login_courier_success(self, current_login_password):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        response = requests.post(test_data.LOGIN_COURIER, data=payload)

        assert response.status_code == 200 and 'id' in response.json()


    @allure.title('Авторизация курьера, если одно из обязательных полей пропущено')
    @pytest.mark.parametrize("deleted_field", ["login", "password"])
    def test_login_courier_without_mandatory_fields(self, current_login_password, deleted_field):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        del payload[deleted_field]
        response = requests.post(test_data.LOGIN_COURIER, data=payload)

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
        response = requests.post(test_data.LOGIN_COURIER, data=payload)

        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Авторизация несуществующего пользователя')
    def test_login_not_existed_courier_failed(self,generate_login, generate_password):

        payload = {
            "login": generate_login,
            "password": generate_password,
        }

        response = requests.post(test_data.LOGIN_COURIER, data=payload)

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

        response = requests.post(test_data.LOGIN_COURIER, data=payload)

        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"
