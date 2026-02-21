from selenium.webdriver.common.by import By

import allure


from pages.base_page import BasePage


class HomePage(BasePage):
    header = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')
    ingredients = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]' )
    ing_popup = (By.XPATH, '//h2[contains(text(), "Детали ингредиента")]' )
    popup_close = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]' )
    basket = (By.XPATH, '//li[contains(@class, "BurgerConstructor_basket__listItem")]' )
    ing_counter = (By.XPATH, '//p[contains(@class, "counter_counter")]' )
    order_button = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')
    order_number = (By.XPATH, '//h2[contains(@class, "Modal_modal__title")]')


    @allure.step("Проверка хидера")
    def check_header(self):
        self.wait(self.header)
        header = self.find(*self.header)
        return header.is_displayed()

    @allure.step("Получить список ингридентов")
    def get_ingredients(self):

        out = self.find_all(*self.ingredients)
        return out

    @allure.step("Проверить попап с ингридентами")
    def check_ingredient_popup(self):

        popup = self.find(*self.ing_popup)
        return popup.is_displayed()

    @allure.step("Закрыть попап ингредиентов")
    def close_ingredient_popup(self):
        popup = self.find(*self.popup_close)
        popup.click()
        self.wait_disappear(self.ing_popup)
        
    @allure.step("Тащить ингредиент в заказ")
    def drag_ingredient_to_basket(self, ing):
        basket = self.find(*self.basket)
        self.drag(ing, basket)

    @allure.step("Получить счетчики ингредиентов")
    def get_ing_counters(self):
        out = self.find_all(*self.ing_counter)
        return out

    @allure.step("Оформить заказ")
    def click_order(self):
        self.wait(self.order_button)
        button = self.find(*self.order_button)
        button.click()

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        self.wait(self.order_number)
        number = self.find(*self.order_number)
        return number
