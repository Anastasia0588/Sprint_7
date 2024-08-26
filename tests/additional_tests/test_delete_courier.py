import requests
import allure

from urls import Url, Endpoint


class TestDeleteOrder:

    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self, current_login_password):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        response = requests.post(f"{Url.BASE_URL}{Endpoint.LOGIN}", data=payload)
        courier_id = response.json()["id"]
        payload = {"id": courier_id}

        response = requests.delete(f"{Url.BASE_URL}{Endpoint.DELETE_COURIER}{courier_id}", data=payload)

        assert response.status_code == 200 and response.json()["ok"] is True


    @allure.title("Удаление курьера без указания id")
    def test_delete_courier_without_id_failed(self):

        response = requests.delete(f"{Url.BASE_URL}{Endpoint.DELETE_COURIER}")
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для удаления курьера"
        # баг, в ответе возвращается код 404


    @allure.title("Удаление курьера c несуществующим id")
    def test_delete_courier_not_existed_id_failed(self, current_login_password):

        payload = {
            "login": current_login_password["login"],
            "password": current_login_password["password"]
        }

        response = requests.post(f"{Url.BASE_URL}{Endpoint.LOGIN}", data=payload)
        courier_id = response.json()["id"]
        payload = {"id": courier_id}

        response = requests.delete(f"{Url.BASE_URL}{Endpoint.DELETE_COURIER}{courier_id}123", data=payload)

        assert response.status_code == 404 and response.json()["message"] == "Курьера с таким id нет."
