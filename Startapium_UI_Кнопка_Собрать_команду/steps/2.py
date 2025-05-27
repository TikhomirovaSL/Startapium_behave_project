from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def setup_browser(context):
    driver_path = r"C:\Users\rassa\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\yandexdriver.exe"
    options = Options()
    options.binary_location = r"C:\Users\rassa\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    options.add_argument("--start-maximized")
    options.add_argument("--disable-password-manager-reauthentication")  # Отключение менеджера паролей
    options.add_argument("--disable-save-password-bubble")  # Отключение всплывающего окна сохранения паролей
    service = Service(driver_path)
    context.browser = webdriver.Chrome(service=service, options=options)


@given('Website "{url}"')
def step_impl(context, url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    setup_browser(context)
    context.browser.get(url)

@then(u'Пользователь нажимает кнопку в правом верхнем углу экрана "{text}"')
def step_impl(context, text):

    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, f'//span[text()="{text}"]'))
    )
    button = context.browser.find_element(By.XPATH, f'//span[text()="{text}"]')
    button.click()

@then(u'Пользователь вводит логин "{username}" и пароль "{password}" и нажимает на кнопку "{button_text}"')
def step_impl(context, username, password, button_text):

        username_field = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Введите email"]')) 
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Введите пароль"]'))
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//p[text()="Войти"]'))
        )
        context.browser.execute_script("arguments[0].scrollIntoView();", login_button)  # Скроллим к кнопке
        login_button.click()

@then(u'Пользователь на главной странице нажимает кнопку "Собрать команду"')
def step_impl(context):

    collect_team_button = WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, '//a[span[text()="Собрать команду"]]'))
    )
    # Используем JavaScript для перехода на /new-project
    context.browser.execute_script("window.location.href = arguments[0].href;", collect_team_button)
    WebDriverWait(context.browser, 10).until(
        EC.url_contains("/new-project")
    )

@then(u'Открывается вкладка создания проекта с текстом "{text}"')
def step_impl(context, text):

        WebDriverWait(context.browser, 15).until(
            EC.presence_of_element_located((By.XPATH, f'//*[contains(text(), "{text}")]'))
        )
    


    