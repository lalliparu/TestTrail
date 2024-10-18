import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class myProfile:
    button_usernameLearner_xpath = "//div[@class='user-name css-avzndl']"
    button_myProfile_xpath = "//p[text()='My profile']"
    button_firstName_id = "name"
    button_lastName_id = "surname"
    button_email_id = "email"
    button_Bio_id = "description"
    button_company_id = "1"
    button_TermsOfUse_id = "react-select-2-option-0"
    button_agreeWithPriStatement = "//div[@class='selected option-md css-8eyxtc-option']"
    dropdown_button_xpath = "(//div[@class='css-ja49ej'])[3]"
    button_Profile_xpath = "//div[text()='TestRail Partner']"
    button_username_id = "username"
    button_saveChange_xpath = "//span[@class='btn-text'][1]"

    def __init__(self,driver):
        self.driver = driver

    def clickUsernameLearner(self):
        self.driver.find_element(By.XPATH, self.button_usernameLearner_xpath).click()
        time.sleep(2)
    def clickButtonMyProfile(self):
        drp = self.driver.find_element(By.XPATH, self.button_myProfile_xpath)
        drp.click()

        time.sleep(2)
    def typeButtonFirstName(self,FirstName1):
        self.driver.find_element(By.ID, self.button_firstName_id).clear()
        self.driver.find_element(By.ID, self.button_firstName_id).send_keys(FirstName1)
    def typeButtonLastName(self,LastName1):
        self.driver.find_element(By.ID, self.button_lastName_id).clear()
        self.driver.find_element(By.ID, self.button_lastName_id).send_keys(LastName1)
    def typeEmailButton(self, Email):
        self.driver.find_element(By.ID, self.button_email_id).clear()
        time.sleep(1)
        self.driver.find_element(By.ID, self.button_email_id).send_keys(Email)
    def typeBioYourSelf(self, Bio):
        self.driver.find_element(By.ID, self.button_Bio_id).clear()
        self.driver.find_element(By.ID, self.button_Bio_id).send_keys(Bio)
    def typeCompanyId(self, Company):
        self.driver.find_element(By.ID, self.button_company_id).clear()
        self.driver.find_element(By.ID, self.button_company_id).send_keys(Company)
        time.sleep(1)
        #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.execute_script("window.scrollTo(0, 500)", "")
        time.sleep(2)
    '''def typeTermsOfUse(self, Yes1):
        #self.driver.find_element(By.XPATH, "//div[text()='Yes'][1]").clear()
        ele = self.driver.find_element(By.ID, "react-select-2-option-0")
        ele.send_keys(Yes1)'''
    '''def typeAgreeWithPriStatement(self, Yes2):
        #self.driver.find_element(By.XPATH, self.button_agreeWithPriStatement).clear()
        #self.driver.find_element(By.XPATH, self.button_agreeWithPriStatement).send_keys(Yes2)'''

    def selectProfile(self):
        #self.driver.find_element(By.XPATH, self.button_Profile_xpath).clear()
        self.driver.find_element(By.XPATH, self.dropdown_button_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.button_Profile_xpath).click()
        #self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #self.driver.find_element(By.XPATH, "//div[text()='TestRail User']")
    def typeUserName(self, userName):
        self.driver.find_element(By.ID, self.button_username_id).clear()
        self.driver.find_element(By.ID, self.button_username_id).send_keys(userName)
        time.sleep(2)
    def clickSaveChange(self):
        self.driver.find_element(By.XPATH, self.button_saveChange_xpath).click()






