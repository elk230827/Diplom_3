from selenium.webdriver.common.by import By

import allure

from selenium.common.exceptions import NoSuchElementException
import logging

from pages.base_page import BasePage
from test_data import HOME_HEADER, QA


class HomePage(BasePage):
    header = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')
    ingredients = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]' )
    ing_popup = (By.XPATH, '//h2[contains(text(), "Детали ингредиента")]' )
    popup_close = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]' )
    basket = (By.XPATH, '//li[contains(@class, "BurgerConstructor_basket__listItem")]' )
    ing_counter = (By.XPATH, '//p[contains(@class, "counter_counter")]' )
    order_button = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')
    order_number = (By.XPATH, '//h2[contains(@class, "Modal_modal__title")]')


    """
    Modal_modal__contentBox__sCy8X 
    <button class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg">Оформить заказ</button>
    <div class="counter_counter__ZNLkj counter_default__28sqi"><p class="counter_counter__num__3nue1">1</p></div>
<ul class="BurgerConstructor_basket__list__l9dp_"><li class="BurgerConstructor_basket__listItem__aWMu1 mr-4"><div class="constructor-element constructor-element_pos_top"><span class="constructor-element__row"><img class="constructor-element__image" src="./static/media/loading.89540200.svg" alt="Перетяните булочку сюда (верх)"><span class="constructor-element__text">Перетяните булочку сюда (верх)</span><span class="constructor-element__price">0<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#F2F2F3"><path d="M10.3849 2.65561C10.5818 2.18895 10.0397 1.75899 9.63011 2.05689L1.41184 8.03382C1.15309 8.222 1.00001 8.52262 1.00001 8.84256V13.4828C1.00001 13.6932 1.13171 13.8811 1.32948 13.9529L4.15637 14.9785C4.65685 15.1601 5.21185 14.9177 5.41879 14.4271L10.3849 2.65561Z"></path><path d="M1.62116 15.9076C1.32217 15.7916 1.00001 16.0122 1 16.3329C1 16.4889 1.07968 16.634 1.21127 16.7178L10.2307 22.4574C10.3326 22.5223 10.4408 22.3844 10.3536 22.3008L5.22556 17.3879C5.13043 17.2968 5.01823 17.2254 4.89541 17.1777L1.62116 15.9076Z"></path><path d="M13.6465 22.3008C13.5592 22.3844 13.6674 22.5223 13.7693 22.4574L22.7887 16.7178C22.9203 16.634 23 16.4889 23 16.3329C23 16.0122 22.6778 15.7916 22.3788 15.9076L19.1046 17.1777C18.9818 17.2254 18.8696 17.2968 18.7745 17.3879L13.6465 22.3008Z"></path><path d="M22.6705 13.9529C22.8683 13.8811 23 13.6932 23 13.4828V8.84256C23 8.52262 22.8469 8.222 22.5882 8.03382L14.3699 2.05689C13.9603 1.75899 13.4183 2.18895 13.6151 2.65561L18.5812 14.4271C18.7882 14.9177 19.3432 15.1601 19.8436 14.9785L22.6705 13.9529Z"></path><path d="M12.7142 20.9615C12.3221 21.3616 11.6779 21.3616 11.2858 20.9615L7.10635 16.6968C6.83068 16.4155 6.7458 15.9986 6.88954 15.6319L11.069 4.97004C11.4009 4.12332 12.5991 4.12333 12.931 4.97004L17.1105 15.6319C17.2542 15.9986 17.1693 16.4155 16.8937 16.6968L12.7142 20.9615Z"></path></svg></span><span class="constructor-element__action pr-2"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#8585AD"><path fill-rule="evenodd" clip-rule="evenodd" d="M6 7V10H4C2.89543 10 2 10.8954 2 12V21C2 22.1046 2.89543 23 4 23H20C21.1046 23 22 22.1046 22 21V12C22 10.8954 21.1046 10 20 10H18V7C18 3.68629 15.3137 1 12 1C8.68632 1 6 3.68629 6 7ZM12 3C9.79088 3 8 4.79086 8 7V10H16V7C16 4.79086 14.2091 3 12 3ZM13 15C13 14.4477 12.5523 14 12 14C11.4477 14 11 14.4477 11 15V18C11 18.5523 11.4477 19 12 19C12.5523 19 13 18.5523 13 18V15Z"></path></svg></span></span></div></li><span class="BurgerConstructor_basket__listContainer__3P_AM"></span><li class="BurgerConstructor_basket__listItem__aWMu1 mr-4"><div class="constructor-element constructor-element_pos_bottom"><span class="constructor-element__row"><img class="constructor-element__image" src="./static/media/loading.89540200.svg" alt="Перетяните булочку сюда (низ)"><span class="constructor-element__text">Перетяните булочку сюда (низ)</span><span class="constructor-element__price">0<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#F2F2F3"><path d="M10.3849 2.65561C10.5818 2.18895 10.0397 1.75899 9.63011 2.05689L1.41184 8.03382C1.15309 8.222 1.00001 8.52262 1.00001 8.84256V13.4828C1.00001 13.6932 1.13171 13.8811 1.32948 13.9529L4.15637 14.9785C4.65685 15.1601 5.21185 14.9177 5.41879 14.4271L10.3849 2.65561Z"></path><path d="M1.62116 15.9076C1.32217 15.7916 1.00001 16.0122 1 16.3329C1 16.4889 1.07968 16.634 1.21127 16.7178L10.2307 22.4574C10.3326 22.5223 10.4408 22.3844 10.3536 22.3008L5.22556 17.3879C5.13043 17.2968 5.01823 17.2254 4.89541 17.1777L1.62116 15.9076Z"></path><path d="M13.6465 22.3008C13.5592 22.3844 13.6674 22.5223 13.7693 22.4574L22.7887 16.7178C22.9203 16.634 23 16.4889 23 16.3329C23 16.0122 22.6778 15.7916 22.3788 15.9076L19.1046 17.1777C18.9818 17.2254 18.8696 17.2968 18.7745 17.3879L13.6465 22.3008Z"></path><path d="M22.6705 13.9529C22.8683 13.8811 23 13.6932 23 13.4828V8.84256C23 8.52262 22.8469 8.222 22.5882 8.03382L14.3699 2.05689C13.9603 1.75899 13.4183 2.18895 13.6151 2.65561L18.5812 14.4271C18.7882 14.9177 19.3432 15.1601 19.8436 14.9785L22.6705 13.9529Z"></path><path d="M12.7142 20.9615C12.3221 21.3616 11.6779 21.3616 11.2858 20.9615L7.10635 16.6968C6.83068 16.4155 6.7458 15.9986 6.88954 15.6319L11.069 4.97004C11.4009 4.12332 12.5991 4.12333 12.931 4.97004L17.1105 15.6319C17.2542 15.9986 17.1693 16.4155 16.8937 16.6968L12.7142 20.9615Z"></path></svg></span><span class="constructor-element__action pr-2"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#8585AD"><path fill-rule="evenodd" clip-rule="evenodd" d="M6 7V10H4C2.89543 10 2 10.8954 2 12V21C2 22.1046 2.89543 23 4 23H20C21.1046 23 22 22.1046 22 21V12C22 10.8954 21.1046 10 20 10H18V7C18 3.68629 15.3137 1 12 1C8.68632 1 6 3.68629 6 7ZM12 3C9.79088 3 8 4.79086 8 7V10H16V7C16 4.79086 14.2091 3 12 3ZM13 15C13 14.4477 12.5523 14 12 14C11.4477 14 11 14.4477 11 15V18C11 18.5523 11.4477 19 12 19C12.5523 19 13 185523 13 18V15Z"></path></svg></span></span></div></li></ul>

    """

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

    @allure.step("Тащить ингредиент в заказ")
    def check(self, ing):
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
