import allure

import config
from pages.home_page import HomePage
from pages.lenta_page import LentaPage


class TestHome:

    @allure.title("переход по клику на «Конструктор»")
    def test_constructor_link(self, driver):
        # Перейдем на страницу лента закаказов
        # так как конструктор является домешней страницей
        lenta = LentaPage(driver)
        lenta.check_header()
        lenta.click_cnst()
        cnst = HomePage(driver)
        assert cnst.check_header()

    @allure.title("переход по клику на раздел «Лента заказов»")
    def test_lenta_link(self, driver):
        driver.get(config.URL)
        home = HomePage(driver)
        home.check_header()
        home.click_lenta()
        cnst = LentaPage(driver)
        assert cnst.check_header()

    @allure.title("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_constructor_ingredient(self, home):
        ings = home.get_ingredients()
        ings[0].click()
        assert home.check_ingredient_popup()

    @allure.title("всплывающее окно закрывается кликом по крестику")
    def test_constructor_ingredient_popup_close(self, home):
        ings = home.get_ingredients()
        ings[0].click()
        home.check_ingredient_popup()
        home.close_ingredient_popup()
        assert home.check_ingredient_popup() == False

    @allure.title("при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.")
    def test_ing_counter_on_add_to_basket(self, home):
        ings = home.get_ingredients()
        home.drag_ingredient_to_basket(ings[0])
        cnts = home.get_ing_counters()
        # так как нулевой элемент это булки
        # они доабавляются 2 раза
        assert cnts[0].text == "2"



