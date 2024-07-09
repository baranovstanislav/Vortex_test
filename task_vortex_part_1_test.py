import pytest
import requests
import allure

SERVICE_URL = "https://reqres.in/api/users"


@allure.description('Позитивный тест на метод "get:single"')
def test_get_single_user_positive():
    user_id = 2
    response = requests.get(f'{SERVICE_URL}/{user_id}')
    data = response.json()

    with allure.step('Проверка статуса кода'):
        assert response.status_code == 200, "Код статуса не равен 200"

    with allure.step('Проверка id'):
        assert data['data']['id'] == user_id, 'ID не совпадает'

    with allure.step('Проверка наличия email'):
        assert 'email' in data['data'], "Отсутсвует запись email"
        assert data['data']['email'] != '', "Строка email не заполнена"

    with allure.step('Проверка наличия имени'):
        assert 'first_name' in data['data'], "Отсутсвует запись first_name"
        assert data['data']['first_name'] != '', "Строка first_name не заполнена"

    with allure.step('Проверка наличия фамилии'):
        assert 'last_name' in data['data'], "Отсутсвуют запись last_name"
        assert data['data']['last_name'] != '', "Строка last_name не заполнена"

    with allure.step('Проверка наличия аватарки'):
        assert 'avatar' in data['data'], "Отсутсвует запись avatar"
        assert data['data']['avatar'] != '', "Строка avatar не заполнена"


@allure.description('Позитивный тест на метод "post:create"')
def test_post_create_user_positive():
    payload = {
        "name": "Ivan",
        "job": "QA"
    }
    response = requests.post(f"{SERVICE_URL}", json=payload)
    data = response.json()

    with allure.step('Проверка статуса кода'):
        assert response.status_code == 201, "Код статуса не равен 201"

    with allure.step('Проверка имени'):
        assert data['name'] == payload['name'], "Имя созданного пользователя не совпадает"

    with allure.step('Проверка должности'):
        assert data['job'] == payload['job'], "Должность созданного пользователя не совпадает"

    with allure.step('Проверка id'):
        assert 'id' in data, "В ответе отсутствует запись id"
        assert data["id"] != '', "Строка id не заполнена"

    with allure.step('Проверка наличия даты создания пользователя'):
        assert 'createdAt' in data, "В ответе отсутствует запись createdAt"
        assert data["createdAt"] != '', "Строка createdAt не заполнена"


@allure.description('Позитивный тест на метод "put:update"')
def test_put_update_user_positive():
    user_id = 2
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(f"{SERVICE_URL}/{user_id}", json=payload)
    data = response.json()

    with allure.step('Проверка статуса кода'):
        assert response.status_code == 200, "Код статуса не равен 200"

    with allure.step('Проверка имени'):
        assert data['name'] == payload['name'], "Имя не совпадает"

    with allure.step('Проверка должности'):
        assert data['job'] == payload['job'], "Работа не совпадает"

    with allure.step('Проверка наличия даты обновления данных пользователя'):
        assert 'updatedAt' in data, "В ответе отсутствует запись updatedAt"
        assert data["updatedAt"] != '', "Строка updatedAt не заполнена"
