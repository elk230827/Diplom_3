from selenium.webdriver.common.by import By

import allure

from selenium.common.exceptions import NoSuchElementException
import logging

from pages.base_page import BasePage
from test_data import HOME_HEADER, QA


class LoginPage(BasePage):
    header = (By.XPATH, '//h2[contains(text(), "Вход")]')
    name = (By.XPATH, '//input[contains(@name, "name")]' )
    password = (By.XPATH, '//input[contains(@name, "Пароль")]' )
    enter_button = (By.XPATH, '//button[contains(text(), "Войти")]' )

    @allure.step("Проверка хидера")
    def check_header(self):
        self.wait(self.header)
        header = self.find(*self.header)
        return header.is_displayed()

    @allure.step("Залогиниться")
    def login(self, name, password):
        n = self.find(*self.name)
        n.send_keys(name)
        p = self.find(*self.password)
        p.send_keys(password)
        button = self.find(*self.enter_button)
        button.click()