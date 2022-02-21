import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DIPLOM.tools.main_page import MainPage
from DIPLOM.tools.constans import EMAIL, COUNT
from DIPLOM.tools.db_steps import LitercartDB
from DIPLOM.tools.main_page_locators import MainPageLocators


@allure.story("Check fulfillment order")
def test_order(driver):
    driver.maximize_window()  # увеличение окна браузера
    with allure.step('Open main page'):
        main_page = MainPage(driver)
    with allure.step('Login user'):
        main_page.login_user()
    with allure.step('Open page ducks'):
        ducks_page = main_page.open_category_ducks()
    with allure.step('Open page green ducks'):
        green_duck_page = ducks_page.open_green_duck()
    with allure.step('Get price for duck'):
        price_duck = green_duck_page.get_price()
    with allure.step('Add duck in basket'):
        green_duck_page.add_duck()
    # ожидание обновления количества уток в корзине
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(MainPageLocators.BASKET_LOCATOR, COUNT))
    with allure.step('Open basket page'):
        basket_page = main_page.open_basket()
    driver.execute_script("window.scrollTo(0, 1000)")
    with allure.step('Get price for duck'):
        unit_cost = basket_page.get_unit_cost()
    with allure.step('Assert price'):
        assert price_duck == unit_cost, 'Wrong price!'
    with allure.step('Get total price'):
        total_sum = basket_page.get_total_sum()
    with allure.step('Assert total price'):
        assert unit_cost * int(COUNT) == total_sum, 'Wrong total price!'
    with allure.step('Confirm order'):
        order_page = basket_page.confirm_order()
    with allure.step('Check success order'):
        assert order_page.check_order_success()


@allure.story("Check order in database")
def test_order_db(cursor):
    with allure.step('Get order data'):
        order_id = LitercartDB.find_order_id_by_email(cursor, EMAIL)
    with allure.step('Check order in database'):
        assert len(order_id) == 1, 'Order does not exist'
    with allure.step("Delete order"):
        LitercartDB.delete_order_by_email(cursor, EMAIL)
