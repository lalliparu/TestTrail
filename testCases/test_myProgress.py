from selenium import webdriver
from pageObjects.myProgress import myProgress
from utilities.readProperties import Readconfig
from pageObjects.loginPage import LoginPage
from pageObjects.myProfile import myProfile

class Test_005_MyProgress():
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUserName()
    password = Readconfig.getPassword()


    def test_myProgress(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = LoginPage(self.driver)
        self.LP.enterUserName(self.username)
        self.LP.enterPassWord(self.password)
        self.LP.clickSigninButton()
        self.MP = myProfile(self.driver)
        self.MP.clickUsernameLearner()
        #self.MP.clickButtonMyProfile()
        self.MYPRGS = myProgress(self.driver)
        self.MYPRGS.clickMyProgress()
        self.MYPRGS.clickCourseButton()
        self.MYPRGS.clickLearningActivities()
        self.MYPRGS.clickBudgetButton()
        self.MYPRGS.clickcertification()
        self.MYPRGS.clickTimeline()

