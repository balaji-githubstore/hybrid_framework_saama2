import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def db_load1():
    print("connect db")


@pytest.fixture(scope="package")
def db_load2():
    print("clear data")


@pytest.fixture(scope="module")
def db_load3():
    print("clear data in db")


@pytest.fixture(scope="class")
def browser_config(request):
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://opensource-demo.orangehrmlive.com/')
    request.cls.driver = driver
    request.cls.my_name = 'bala'
    yield
    driver.quit()
