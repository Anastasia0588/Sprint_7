import requests
import allure

import test_data


class TestCreateOrder:

    @allure.title('Успешное даление курьера')
    def test_delete_courier_success(self, current_login_password):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        response = requests.post(test_data.LOGIN_COURIER, data=payload)
        id = response.json()["id"]
        payload = {"id": id}

        response = requests.delete(f'{test_data.DELETE_COURIER}{id}', data=payload)

        assert response.status_code == 200 and response.json()["ok"] == True


    @allure.title("Удаление курьера без указания id")
    def test_delete_courier_without_id_failed(self):

        response = requests.delete(test_data.DELETE_COURIER)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для удаления курьера"
        # баг, в ответе возвращается код 404


    @allure.title("Удаление курьера c несуществующим id")
    def test_delete_courier_not_existed_id_failed(self, current_login_password):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        response = requests.post(test_data.LOGIN_COURIER, data=payload)
        id = response.json()["id"]

        payload = {"id": id}

        response = requests.delete(f'{test_data.DELETE_COURIER}{id}123', data=payload)

        assert response.status_code == 404 and response.json()["message"] == "Курьера с таким id нет."
