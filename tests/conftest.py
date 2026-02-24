from selenium import webdriver

from config import BROWSER, EMAIL, LOGIN_URL, PASSWORD, URL
from chromedriver_py import binary_path

from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest

@pytest.fixture
def driver():
    driver = None
    if BROWSER == "Chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled":  False,
            "profile.password_manager_leak_detection":  False
        })

        svc = webdriver.ChromeService(executable_path=binary_path)
        driver = webdriver.Chrome(service=svc, options=options)
    elif BROWSER == "Firefox":
        from selenium.webdriver.firefox.options import Options
        options = Options()
        from selenium.webdriver.firefox.service import Service
        service = Service(executable_path="geckodriver.exe")
        driver = webdriver.Firefox(options=options, service=service)
    else:
        raise Exception("Unsupported browser")
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    driver.get(URL)
    home_page = HomePage(driver)
    home_page.check_header()
    return home_page

@pytest.fixture
def login(driver):
    driver.get(LOGIN_URL)
    login = LoginPage(driver)
    login.check_header()
    login.login(EMAIL, PASSWORD)
    # Происходит редирект на домашнюю страницу
    home = HomePage(driver)
    home.check_header()

    return home

