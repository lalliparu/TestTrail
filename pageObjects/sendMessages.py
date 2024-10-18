import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class sendMessage:
    button_messages_xpath = "//button[@class='messages action-btn ghost css-86xq4m']"
    button_newMessages_xpath = "//span[text()='New message']"
    #button_sentTo_xpath = "(//div[@class =' css-zhmsqa-control'])[2]"
    #button_sentTo_id = "react-select-3-placeholder"
    button_subject_id = "subject"
    button_typeHereMessage_xpath = "(//span[@class='fr-placeholder'])"
    button_send_xpath = "(//span[@class='btn-text'])[7]"

    def __init__(self, driver):
        self.driver = driver

    def clickMessageButton(self):
        self.driver.find_element(By.XPATH, self.button_messages_xpath).click()
        time.sleep(4)

    def clickNewMessageButton(self):
        self.driver.find_element(By.XPATH, self.button_newMessages_xpath).click()
        time.sleep(2)

    def selectSentToSysAdmin(self, select):
        self.driver.find_element(By.XPATH, "(//div[contains(@class, 'custom-input')])[2]").click()
        enter = self.driver.find_element(By.XPATH, "(//input[contains(@id, 'react-select')])[2]")
        enter.send_keys('System administrators')

        #self.driver.find_element(By.XPATH, "(//div[contains(@class, 'custom-input')])[2]").send_keys(select)
        #self.driver.find_element(By.XPATH, "//div[@data-value='system']").click()
        #enter = self.driver.find_element(By.XPATH, "(//div[contains(@class, 'custom-input')])[2]")
        #time.sleep(4)
        #enter.send_keys('System administrators')
        #self.driver.find_element(By.ID, "subject").send_keys(text)

    def typeSubject(self, text):
        self.driver.find_element(By.ID, "subject").send_keys(text)
        #self.driver.find_element(By.ID, self.button_subject_id).send_keys(text)
        time.sleep(2)

    def typeHereMessage(self, text1):

        #self.driver.find_element(By.XPATH, self.button_typeHereMessage_xpath).send_keys(text1)
        self.driver.find_element(By.XPATH, "//div[@class='fr-element fr-view']").send_keys(text1)
        time.sleep(2)

    def clickTheSendButton(self):
        self.driver.find_element(By.XPATH, self.button_send_xpath).click()




