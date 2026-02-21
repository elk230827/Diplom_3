from time import sleep

import allure
from tests.test_base import BaseTest


class TestLenta(BaseTest):

    @allure.title("при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_lenta_all_time_counter(self):
        lenta = self.lenta()
        start = int(lenta.get_all_counter().text)
        home = self.home()
        home.click_order()
        home.get_order_number()
        lenta = self.lenta()
        end = int(lenta.get_all_counter().text)
        assert end == start + 1

    @allure.title("при создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_lenta_day_counter(self):
        lenta = self.lenta()
        start = int(lenta.get_day_counter().text)
        home = self.home()
        home.click_order()
        home.get_order_number()
        lenta = self.lenta()
        end = int(lenta.get_day_counter().text)
        assert end == start + 1

    @allure.title("после оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_in_progress(self):
        lenta = self.lenta()
        home = self.home()
        home.click_order()
        number = home.get_order_number().text
        lenta = self.lenta()
        in_progress = lenta.get_in_progress().text
        assert number in in_progress 


