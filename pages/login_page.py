from selenium.webdriver.common.by import By

import allure

from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


class LoginPage(BasePage):
    header = (By.XPATH, '//h2[contains(text(), "Вход")]')
    name_field = (By.XPATH, '//input[contains(@name, "name")]' )
    password_field = (By.XPATH, '//input[contains(@name, "Пароль")]' )
    enter_button = (By.XPATH, '//button[contains(text(), "Войти")]' )

    @allure.step("Проверка хидера")
    def check_header(self):
        self.wait(self.header)
        header = self.find(*self.header)
        return header.is_displayed()

    @allure.step("Залогиниться")
    def login(self, name, password):
        name_element = self.find(*self.name_field)
        name_element.send_keys(name)
        pswd = self.find(*self.password_field)
        pswd.send_keys(password)
        button = self.find(*self.enter_button)
        button.click()