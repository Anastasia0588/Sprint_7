import pytest
import requests
import allure
import test_data


class TestCreateCourier:

    @allure.title('Создание курьера. Ожидается правильный код и текст ответа')
    def test_create_courier_success(self, generate_login, generate_password, generate_firstname):

        payload = {
            "login": generate_login,
            "password": generate_password,
            "firstName": generate_firstname
        }

        response = requests.post(test_data.CREATE_COURIER, data=payload)

        assert response.status_code == 201 and response.json()["ok"] == True

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_existed_courier(self, generate_login, generate_password, generate_firstname):

        payload = {
            "login": generate_login,
            "password": generate_password,
            "firstName": generate_firstname
        }

        requests.post(test_data.CREATE_COURIER, data=payload)
        response = requests.post(test_data.CREATE_COURIER, data=payload)

        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется."
        # Баг. Возвращается другой текст в ответе: 'Этот логин уже используется. Попробуйте другой.'


    @allure.title('Создание курьера, если одно из обязательных полей пропущено')
    @pytest.mark.parametrize("deleted_field", ["login", "password"])
    def test_create_courier_without_mandatory_fields(self, generate_login, generate_password, generate_firstname, deleted_field):

        payload = {
            "login": generate_login,
            "password": generate_password,
            "firstName": generate_firstname
        }

        del payload[deleted_field]
        response = requests.post(test_data.CREATE_COURIER, data=payload)

        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Создание курьера, если одно из обязательных полей не заполнено')
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_create_courier_empty_mandatory_fields(self, generate_login, generate_password, generate_firstname, empty_field):

        payload = {
            "login": generate_login,
            "password": generate_password,
            "firstName": generate_firstname
        }

        payload[empty_field] = ""
        response = requests.post(test_data.CREATE_COURIER, data=payload)

        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

