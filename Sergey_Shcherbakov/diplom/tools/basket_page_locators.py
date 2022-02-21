from selenium.webdriver.common.by import By


class BasketPageLocators:
    ITEMS_LOCATOR = (By.XPATH, "//div[@id='box-checkout-cart']")
    BUTTON_CONFIRM_ORDER = (By.XPATH, "//button[(@type='submit') and (@name='confirm_order')]")
    UNIT_COST = (By.XPATH, "//td[@class='unit-cost']")
    TOTAL = (By.XPATH, "//td[@class='sum']")
