from selenium.webdriver.common.by import By


class MainPageLocators:
    EMAIL_LOCATOR = (By.XPATH, "//input[@name='email']")
    PASSWORD_LOCATOR = (By.XPATH, "//input[@name='password']")
    BUTTON_LOGIN_LOCATOR = (By.XPATH, "//button[(@type='submit') and (@name='login')]")
    CATEGORY_DUCKS = (By.XPATH, "//a[@href='http://localhost/litecart/en/rubber-ducks-c-1/']")
    BASKET_LOCATOR = (By.XPATH, "//span[@class='quantity']")
