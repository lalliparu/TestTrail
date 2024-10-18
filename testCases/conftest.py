import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(15)
        driver.maximize_window()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
    elif browser == 'Edge':
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
        driver.maximize_window()

    else:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    request.config.getoption("--browser")
