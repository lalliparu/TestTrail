from selenium import webdriver
from pageObjects.calendarEvents import CalendarEvents
from utilities.readProperties import Readconfig
from pageObjects.loginPage import LoginPage


class Test_003_calendarEvents:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUserName()
    password = Readconfig.getPassword()

    def test_calendarEvents(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = LoginPage(self.driver)
        self.LP.enterUserName(self.username)
        self.LP.enterPassWord(self.password)
        self.LP.clickSigninButton()
        self.calEve = CalendarEvents(self.driver)
        self.calEve.clickCalendarButton()
        self.calEve.dropdownMyEventsBox()
        self.calEve.selectAvailableEvents()
        self.calEve.clickButtonExport()
        self.calEve.clickPrivateAdderes()
        self.calEve.clickResetAdderes()
        self.calEve.clickReset()


