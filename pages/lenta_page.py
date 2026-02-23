from selenium.webdriver.common.by import By

import allure


from config import LENTA_URL
from pages.base_page import BasePage


class LentaPage(BasePage):
    header = (By.XPATH, '//h1[contains(text(), "Лента заказов")]')
    all_counter = (By.XPATH, '//p[contains(text(), "Выполнено за все время:")]/following-sibling::p[1]')
    day_counter = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня:")]/following-sibling::p[1]')
    in_progress = (By.XPATH, '//p[contains(text(), "В работе")]/following-sibling::ul[2]/li')
    URL = LENTA_URL

    @allure.step("Проверка хидера")
    def check_header(self):
        self.wait(self.header)
        header = self.find(*self.header)
        return header.is_displayed()

    @allure.step("Получить общий счетчик")
    def get_all_counter(self):
        cnt = self.find(*self.all_counter)
        return cnt

    @allure.step("Получить дневной счетчик")
    def get_day_counter(self):
        cnt = self.find(*self.day_counter)
        return cnt

    @allure.step("Получить заказы в работе")
    def get_in_progress(self):
        cnt = self.find(*self.in_progress)
        return cnt
