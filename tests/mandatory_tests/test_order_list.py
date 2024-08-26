import requests
import allure

from urls import Url, Endpoint


class TestOrderList:

    @allure.title('Получение списка заказов')
    def test_get_order_list(self):

        response = requests.get(f"{Url.BASE_URL}{Endpoint.ORDER}")
        assert response.status_code == 200 and "orders" in response.json()
