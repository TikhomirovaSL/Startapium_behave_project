from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Настройка браузера
def setup_browser(context):
    driver_path = r"C:\Users\rassa\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\yandexdriver.exe"
    options = Options()
    options.binary_location = r"C:\Users\rassa\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    options.add_argument("--start-maximized")
    service = Service(driver_path)
    context.browser = webdriver.Chrome(service=service, options=options)


# Шаг для открытия веб-сайта
@given('Website "{url}"')
def step_impl(context, url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    setup_browser(context)
    context.browser.get(url)


@then(u'Пользователь нажимает на кнопку "{text}"')
def step_impl(context, text):
    # Ожидание появления и кликабельности элемента span
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, f'//span[text()="{text}"]'))
    )
    button = context.browser.find_element(By.XPATH, f'//span[text()="{text}"]')
    button.click()

@then(u'Открывается вкладка Проекты с текстом "{text}"')
def step_impl(context, text):
    # Ожидание появления текста в span
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{text}")]'))
    )
    result = context.browser.find_element(By.XPATH, f'//span[contains(text(), "{text}")]')
    assert result.is_displayed()

    # Закрываем браузер после теста
    context.browser.quit()