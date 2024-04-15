import requests
import random
import string
import allure

from urls import Url, Endpoint


@allure.step("Генерация данных для регистрации нового курьера")
def generate_login_password():

    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload

@allure.step("Регистрации нового курьера возвращает список из логина и пароля")
# если регистрация не удалась, возвращает пустой список
def register_new_courier(login, password):

    payload = {
        "login": login,
        "password": password,
    }

    # создаём список, чтобы метод мог его вернуть
    login_pass = {}

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f"{Url.BASE_URL}{Endpoint.COURIER}", data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass["login"] = login
        login_pass["password"] = password

    # возвращаем список
    return login_pass