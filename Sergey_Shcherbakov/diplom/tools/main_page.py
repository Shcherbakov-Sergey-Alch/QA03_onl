from DIPLOM.tools.base_page import BasePage
from DIPLOM.tools.constans import EMAIL, PASSWORD
from DIPLOM.tools.ducks_page import DucksPage
from DIPLOM.tools.main_page_locators import MainPageLocators
from DIPLOM.tools.basket_page import BasketPage


class MainPage (BasePage):
    URL = "http://localhost/litecart/en/"

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def login_user(self):
        self.open()
        user_email = self.find_element(MainPageLocators.EMAIL_LOCATOR)
        user_email.send_keys(EMAIL)
        user_password = self.find_element(MainPageLocators.PASSWORD_LOCATOR)
        user_password.send_keys(PASSWORD)
        button_login = self.find_element(MainPageLocators.BUTTON_LOGIN_LOCATOR)
        button_login.click()
        return self.driver.current_url

    def open_category_ducks(self):
        category_ducks = self.find_element(MainPageLocators.CATEGORY_DUCKS)
        category_ducks.click()
        return DucksPage(self.driver, self.driver.current_url)

    def open_basket(self):
        basket = self.find_element(MainPageLocators.BASKET_LOCATOR)
        basket.click()
        return BasketPage(self.driver, self.driver.current_url)
