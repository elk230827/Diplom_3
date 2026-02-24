
import allure
from config import URL
from pages.home_page import HomePage
from pages.lenta_page import LentaPage


class TestLenta:

    @allure.title("при создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_lenta_all_time_counter(self, login):
        driver = login.driver
        lenta = LentaPage(driver).open()

        start = int(lenta.get_all_counter().text)
        driver.get(URL)
        home = HomePage(driver).open()
        home.click_order()
        home.get_order_number()
        
        lenta = LentaPage(driver).open()
 
        end = int(lenta.get_all_counter().text)
        assert end == start + 1

    @allure.title("при создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_lenta_day_counter(self, login):
        driver = login.driver
        lenta = LentaPage(driver).open()

        start = int(lenta.get_day_counter().text)
        home = HomePage(driver).open()
        home.click_order()
        home.get_order_number()

        lenta = LentaPage(driver).open()

        end = int(lenta.get_day_counter().text)
        assert end == start + 1

    @allure.title("после оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_in_progress(self, login):
        driver = login.driver
        
        home = HomePage(driver).open()
        home.click_order()

        number = home.get_order_number().text

        lenta = LentaPage(driver).open()
        in_progress = lenta.get_in_progress().text
        assert number in in_progress 


