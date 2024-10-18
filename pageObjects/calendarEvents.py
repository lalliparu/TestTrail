from selenium import webdriver
from selenium.webdriver.common.by import By


class CalendarEvents:
    button_calendar_xpath = "//div[text()='Calendar']"
    dropdown_My_events_box_xpath = "(//div[@class=' css-3r8cho-indicatorContainer'])[2]"
    select_available_Events_xpath = "//div[text()='Available events']"
    button_Export_xpath = "//span[text()='Export']"
    click_privateAdderes_xpath = "//span[text()='Private address']"
    button_resetAdderes_xpath = "//span[text()='Reset address']"
    button_reset_xpath = "//span[text()='Reset']"

    def __init__(self, driver):
        self.driver = driver

    def clickCalendarButton(self):
        self.driver.find_element(By.XPATH, self.button_calendar_xpath).click()

    def dropdownMyEventsBox(self):
        self.driver.find_element(By.XPATH, self.dropdown_My_events_box_xpath).click()

    def selectAvailableEvents(self):
        self.driver.find_element(By.XPATH, self.select_available_Events_xpath).click()
    def clickButtonExport(self):
        self.driver.find_element(By.XPATH, self.button_Export_xpath).click()
    def clickPrivateAdderes(self):
        self.driver.find_element(By.XPATH, self.click_privateAdderes_xpath).click()
    def clickResetAdderes(self):
        self.driver.find_element(By.XPATH, self.button_resetAdderes_xpath).click()
    def clickReset(self):
        self.driver.find_element(By.XPATH, self.button_reset_xpath).click()
