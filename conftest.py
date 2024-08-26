import pytest
import requests
import helpers

from helpers import register_new_courier
from urls import Url, Endpoint


@pytest.fixture(scope='function')
def current_login_password():
    payload = helpers.generate_login_password()
    del payload["firstName"]
    yield register_new_courier(payload["login"], payload["password"])
    response = requests.post(f"{Url.BASE_URL}{Endpoint.LOGIN}", data=payload)
    if response.status_code == 200:
        courier_id = response.json()["id"]
        payload = {"id": courier_id}
        requests.delete(f"{Url.BASE_URL}{Endpoint.DELETE_COURIER}{courier_id}", data=payload)
