import mysql.connector as mysql
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def connect_db():
    db = mysql.connect(
        host='localhost',
        user='root',
        database='litecart')
    cursor = db.cursor()
    yield cursor
    db.close()
