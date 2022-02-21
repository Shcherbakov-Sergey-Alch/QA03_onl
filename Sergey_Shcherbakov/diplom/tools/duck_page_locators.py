from selenium.webdriver.common.by import By


class DuckPageLocators:
    QUANTITY_DUCK = (By.XPATH, "//input[(@type='number') and (@name='quantity')]")
    PRICE = (By.XPATH, "//span[@itemprop='price']")
    BUTTON_ADD = (By.XPATH, "//button[(@type='submit') and (@name='add_cart_product')]")

