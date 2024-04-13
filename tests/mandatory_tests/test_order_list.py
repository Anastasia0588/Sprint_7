import requests
import allure

import test_data


class TestOrderList:

    @allure.title('Получение списка заказов')
    def test_get_order_list(self):

        response = requests.get(test_data.ORDER_LIST)
        assert response.status_code == 200 and "orders" in response.json()
