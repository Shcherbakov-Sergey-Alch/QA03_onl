from DIPLOM.tools.base_page import BasePage
from DIPLOM.tools.duck_page import DuckPage
from DIPLOM.tools.ducks_page_locators import DucksPageLocators


class DucksPage(BasePage):

    def open_green_duck(self):
        green_duck = self.find_element(DucksPageLocators.GREEN_DUCK_LOCATOR)
        green_duck.click()
        return DuckPage(self.driver, self.driver.current_url)
