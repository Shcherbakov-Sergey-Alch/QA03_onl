from DIPLOM.tools.base_page import BasePage
from DIPLOM.tools.order_success_page_locators import OrderSuccessPageLocators


class OrderSuccessPage(BasePage):

    def check_order_success(self):
        el_title = self.find_element(OrderSuccessPageLocators.TITLE)
        return "Your order is successfully completed!" == el_title.text
