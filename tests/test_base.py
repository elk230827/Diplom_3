import allure
import pytest
from selenium import webdriver
from chromedriver_py import binary_path

from config import BROWSER, EMAIL, LENTA_URL, LOGIN_URL, PASSWORD, URL

import config
from pages.home_page import HomePage
from pages.lenta_page import LentaPage
from pages.login_page import LoginPage

class BaseTest:
    def setup_method(self):
        if BROWSER == "Chrome":
            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.add_experimental_option("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled":  False,
                "profile.password_manager_leak_detection":  False
            })

            svc = webdriver.ChromeService(executable_path=binary_path)
            self.driver = webdriver.Chrome(service=svc, options=options)
        elif BROWSER == "Firefox":
            from selenium.webdriver.firefox.options import Options
            options = Options()
            from selenium.webdriver.firefox.service import Service
            service = Service(executable_path="geckodriver.exe")
            self.driver = webdriver.Firefox(options=options, service=service)
        else:
            raise Exception("Unsupported browser")
    def teardown_method(self):
        self.driver.quit()

    @allure.step("Go to home page")
    def home(self):
        self.driver.get(URL)
        home_page = HomePage(self.driver)
        home_page.check_header()
        return home_page

    @allure.step("Переход на страницу ленты")
    def lenta(self):
        self.login()
        self.driver.get(LENTA_URL)
        lenta = LentaPage(self.driver)
        lenta.check_header()
        return lenta

    @allure.step("Залогиниться")
    def login(self):
        self.driver.get(LOGIN_URL)
        login = LoginPage(self.driver)
        login.check_header()
        login.login(EMAIL, PASSWORD)
        # Происходит редирект на домашнюю страницу
        home = HomePage(self.driver)
        home.check_header()


        return home


