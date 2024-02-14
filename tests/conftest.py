import os
from selene import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from rutube_kids.utils import attach
from dotenv import load_dotenv

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption("--browser_version", default="100.0")


@pytest.fixture(scope='function')
def browser_config(request):
    browser_version = request.config.getoption("--browser_version")
    browser_version = (
        browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    )
    browser.config.base_url = 'https://kids.rutube.ru'
    browser.config.window_width = 1440
    browser.config.window_height = 900
    options = Options()

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    # Дополнительные опции
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument(
        "--disable-notifications-prompt"
    )  # Блокировка уведомлений в адресной строке

    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    # Использовать класс Remote из модуля selenium.webdriver, а не selene.support.webdriver
    login_selenoid = os.getenv('LOGIN')
    password_selenoid = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login_selenoid}:{password_selenoid}@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
