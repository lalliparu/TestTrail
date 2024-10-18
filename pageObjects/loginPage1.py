from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage1:
    textbox_username_ID = "Email"
    textbox_password_ID = "Password"
    #Checkbox_remember_id = "RememberMe"
    button_signin_xpath = "//button[text()='Log in']"

    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_ID).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_ID).send_keys(password)

    def clickSigninButton(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()

