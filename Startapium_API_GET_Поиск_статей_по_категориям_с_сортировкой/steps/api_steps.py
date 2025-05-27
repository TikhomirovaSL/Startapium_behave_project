import requests
from behave import given, when, then
import json


@given('URL API-запрос "{url}"')
def step_given_url(context, url):
    context.url = url

@given('Заданы параметры')
def step_given_set_params(context):
    # Таблица параметров из feature-файла
    context.params = {}
    for row in context.table:
        context.params[row['ключ']] = row['значение']


@when('Пользователь отправляет GET-запрос с параметрами')
def step_when_send_request_with_params(context):
    context.response = requests.get(context.url, params=context.params)
    print("\n=== Отправленный запрос ===")
    print(f"URL: {context.response.url}")  # Показываем финальный URL с параметрами
    print("===========================")


@then('Получен статус-код 200')
def step_then_check_status(context):
    assert context.response.status_code == 200, f"Ожидался статус-код 200, но получен {context.response.status_code}"

@then('В ответе есть данные статьи/статей: id, title и status')
def step_then_check_response_content(context):
    response_json = context.response.json()
    articles = response_json["data"]
    for article in articles:
        # Проверяем ключи
        assert "id" in article, f"Поле 'id' отсутствует в статье: {article}"
        assert "title" in article, f"Поле 'title' отсутствует в статье: {article}"
        assert "status" in article, f"Поле 'status' отсутствует в статье: {article}"

        # Выводим информацию в терминал для каждой статьи
        print(f"ID: {article['id']} | Заголовок: {article['title']} | Статус: {article['status']}")

