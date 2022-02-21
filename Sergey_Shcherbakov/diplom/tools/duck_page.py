from DIPLOM.tools.base_page import BasePage
from DIPLOM.tools.duck_page_locators import DuckPageLocators
from DIPLOM.tools.constans import COUNT


class DuckPage(BasePage):

    def add_duck(self):
        add_quantity = self.find_element(DuckPageLocators.QUANTITY_DUCK)
        add_quantity.clear()
        add_quantity.send_keys(COUNT)
        add_duck_in_basket = self.find_element(DuckPageLocators.BUTTON_ADD)
        add_duck_in_basket.click()

    def get_price(self):
        price_duck = self.find_element(DuckPageLocators.PRICE).text
        price_int = int(price_duck[1:])
        return price_int
