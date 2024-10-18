import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLog import LogGen


class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUserName()
    password = Readconfig.getPassword()
    log = LogGen.loggen()

    @pytest.mark.parametrize("username, password", [("munilalitha01", "T0day@123"),("munilalitha02", "T0day@123")])
    def test_Login(self, setup, username, password):
        self.log.info("test case started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = LoginPage(self.driver)
        self.LP.enterUserName(username)
        self.LP.enterPassWord(password)
        self.LP.clickSigninButton()
