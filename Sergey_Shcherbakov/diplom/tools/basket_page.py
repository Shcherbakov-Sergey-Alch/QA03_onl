from DIPLOM.tools.base_page import BasePage
from DIPLOM.tools.basket_page_locators import BasketPageLocators
from DIPLOM.tools.order_success_page import OrderSuccessPage


class BasketPage(BasePage):

    def get_unit_cost(self):
        el_un_cost = self.find_element(BasketPageLocators.UNIT_COST).text
        unit_cost = float(el_un_cost[1:])
        return unit_cost

    def get_total_sum(self):
        el_tot_sum = self.find_element(BasketPageLocators.TOTAL).text
        total_sum = float(el_tot_sum[1:])
        return total_sum

    def confirm_order(self):
        button_confirm_order = self.find_element(BasketPageLocators.BUTTON_CONFIRM_ORDER)
        button_confirm_order.click()
        return OrderSuccessPage(self.driver, self.driver.current_url)
