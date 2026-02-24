import allure


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class BasePage:
    cnst_link = (By.XPATH, '//a[p[contains(text(), "Конструктор")]]')
    lenta_link = (By.XPATH, '//a[p[contains(text(), "Лента Заказов")]]')
    header = (By.XPATH, '//h1')

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.URL)
        self.wait(self.header)
        return self


    @allure.step("Кликнуть на конструктор")
    def click_cnst(self):
        link = self.find(*self.cnst_link)
        link.click()

    @allure.step("Кликнуть на ленту заказов")
    def click_lenta(self):
        link = self.find(*self.lenta_link)
        link.click()


    @allure.step("Скроллимся к {locator}")
    def scroll_to_elment(self, locator):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(locator).perform()

    def find(self, type, locator):
        return self.driver.find_element(type,locator)

    def find_all(self, type, locator):
        return self.driver.find_elements(type,locator)

    @allure.step("Подождать появление элемента")
    def wait(self, locator):
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(locator) )

    @allure.step("Подождать пропадание элемента")
    def wait_disappear(self, locator):
        WebDriverWait(self.driver, 10).until( EC.invisibility_of_element_located(locator) )

    def swtich_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        if len(self.driver.window_handles) > 1:
            
            for window_handle in self.driver.window_handles:
                if window_handle != self.driver.current_window_handle:
                    self. driver.switch_to.window(window_handle)
                    break
    
    @allure.step("Тащить элемент")
    def drag(self, source, target):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
