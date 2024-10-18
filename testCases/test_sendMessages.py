from selenium import webdriver
from pageObjects.sendMessages import sendMessage
from utilities.readProperties import Readconfig
from pageObjects.loginPage import LoginPage

class Test_003_SendMessages:
      baseUrl = Readconfig.getApplicationURL()
      username = Readconfig.getUserName()
      password = Readconfig.getPassword()
      select = Readconfig.getSelect()
      text = Readconfig.getText()
      text1 = Readconfig.getText1()

      def test_sendMessages(self,setup):
            self.driver = setup
            self.driver.get(self.baseUrl)
            self.LP = LoginPage(self.driver)
            self.LP.enterUserName(self.username)
            self.LP.enterPassWord(self.password)
            self.LP.clickSigninButton()
            self.SendM = sendMessage(self.driver)
            self.SendM.clickMessageButton()
            self.SendM.clickNewMessageButton()
            self.SendM.selectSentToSysAdmin(self.select)
            self.SendM.typeSubject(self.text)
            self.SendM.typeHereMessage(self.text1)


