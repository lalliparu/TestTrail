from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_ID = "username"
    textbox_password_ID = "password"
    #link_pswRq_xpath = "//span[text()='Password Requirements']"
    #link_resetPasswd_xpath = "//span[text()='Reset Password']"
    button_signin_xpath = "//span[text()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_ID).send_keys(username)

    def enterPassWord(self, password):
        self.driver.find_element(By.ID, self.textbox_password_ID).send_keys(password)

    def clickSigninButton(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()
