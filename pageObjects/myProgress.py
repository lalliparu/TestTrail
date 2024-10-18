import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class myProgress:
    button_myProgress_xpath = "//p[text()='My progress']"
    button_course_xpath = "//a[text()='Courses']"
    button_learningActivities_xpath = "//a[text()='Learning activities']"
    button_Budget_xpath = "//a[text()='Badges']"
    button_certification_xpath = "//a[text()='Certificates']"
    button_Timeline_xpath = "//a[text()='Timeline']"

    def __init__(self, driver):
       self.driver = driver
    def clickMyProgress(self):
       drp = self.driver.find_element(By.XPATH, self.button_myProgress_xpath)
       drp.click()
       time.sleep(2)

    def clickCourseButton(self):
        self.driver.find_element(By.XPATH, self.button_course_xpath).click()
        time.sleep(2)
    def clickLearningActivities(self):
        self.driver.find_element(By.XPATH, self.button_learningActivities_xpath).click()
    def clickBudgetButton(self):
        self.driver.find_element(By.XPATH, self.button_Budget_xpath).click()
    def clickcertification(self):
        self.driver.find_element(By.XPATH, self.button_certification_xpath).click()
    def clickTimeline(self):
        self.driver.find_element(By.XPATH, self.button_Timeline_xpath).click()


