# Sprint_7
## Финальный проект 7 спринта
В этом проекте тесты API учебного сервиса [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/)

[Документация](qa-scooter.praktikum-services.ru/docs/.)

## Тесты
обязательные:  
test_create_courier.py - тесты на создание курьера  
test_login_courier.py - тесты авторизации курьера  
test_create_order.py - тесты создания заказа  
test_order_list.py - тесты получения списка заказов  

дополнительные:  
test_delete_courier.py - тесты удаления курьера  
test_accept_order.py - тесты на принятие заказа  
test_get_order_by_number.py - тесты поиска заказа по номеру  

### Запустить тесты
запустить все тесты:
```bash
pytest -v tests
```
зпустить все тесты с генерацией отчетов  
```bash
pytest tests --alluredir=allure_results 
```
обязательные:
```bash
pytest tests/mandatory_tests --alluredir=allure_results 
```
дополнительные: 
```bash
pytest tests/additional_tests --alluredir=allure_results 
```
сформировать отчет:
```bash
allure serve allure_results 
```