from selenium import webdriver
from pageObjects.enrollandUnenrollCourse import myCourse
from utilities.readProperties import Readconfig
from pageObjects.loginPage import LoginPage

class Test_002_EnAndUnEnrollCourse:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUserName()
    password = Readconfig.getPassword()
    searchText = Readconfig.getSearchText()

    def test_EnAndUnEnrollCourse(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.LP = LoginPage(self.driver)
        self.LP.enterUserName(self.username)
        self.LP.enterPassWord(self.password)
        self.LP.clickSigninButton()
        self.MYCourse = myCourse(self.driver)
        self.MYCourse.clickMyCourseButton()
        self.MYCourse.clickMYCourseCatalogButton()
        self.MYCourse.enterTextInSearchTextBox(self.searchText)
        #self.MYCourse.clickViewCourseButton()
        self.MYCourse.clickGetThisCourseButton()
        self.MYCourse.clickGetThisCourseButton()
        #self.MYCourse.clickResumeCourseButton()
        #self.MYCourse.clickKeyDefinitionLink()
        self.MYCourse.clickBackToMYCourse()
        self.MYCourse.clickMyCourseButton()
        #self.MYCourse.clickViewCourseButton()

        self.MYCourse.clickEyeButtonGetMYCourse()
        self.MYCourse.clickUnEnRollLink()
        #self.driver.execute_script("window.scrollTo(0,5000)")
        self.MYCourse.clickPOpUpUnENRollButton()
