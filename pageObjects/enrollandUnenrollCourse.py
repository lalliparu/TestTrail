import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class myCourse:
    button_MyCourses_xpath = "//div[text()='My courses']"
    button_MYCoursesCatalog_xpath = "//span[text()='Go to Course catalog']"
    button_SearchButton_ID = "sender-search"
    #button_ViewCourse_xpath = "//span[text()='View course']"
    button_GetThisCourse_xpath = "//span[text()='Get this course']"
    button_ResumeCourse_xpath = "//span[text()='Resume course']"
    link_KeyDefinition_xpath = "//span[text()='1.2 Key Definitions']"
    click_back_toMYCourse_xpath = "(//span[@class='btn-text'])[1]"
    click_eye_button_getMYCourse_xpath = "(//span[@class='btn-text'])[6]"
    #button_ViewCourse_xpath = "//span[text()='View course']"
    click_unEnroll_link_xpath = '//span[text()="Unenroll from course"]'
    button_popUp_unEnroll_xpath = "//span[text()='Unenroll']"

    def __init__(self, driver):
        self.driver = driver

    def clickMyCourseButton(self):
        self.driver.find_element(By.XPATH, self.button_MyCourses_xpath).click()

    def clickMYCourseCatalogButton(self):
        self.driver.find_element(By.XPATH, self.button_MYCoursesCatalog_xpath).click()

    def enterTextInSearchTextBox(self, searchtext):
        self.driver.find_element(By.ID, self.button_SearchButton_ID).send_keys(searchtext)

    #def clickViewCourseButton(self):
        #self.driver.find_element(By.XPATH, self.button_ViewCourse_xpath).click()

    def clickGetThisCourseButton(self):
        self.driver.find_element(By.XPATH, self.button_GetThisCourse_xpath).click()

    '''def clickResumeCourseButton(self):
        self.driver.find_element(By.XPATH, self.button_ResumeCourse_xpath).click()

    def clickKeyDefinitionLink(self):
        self.driver.find_element(By.XPATH, self.link_KeyDefinition_xpath).click()'''

    def clickBackToMYCourse(self):
        self.driver.find_element(By.XPATH, self.click_back_toMYCourse_xpath).click()
        time.sleep(2)

    #def clickViewCourseButton(self):

        #self.driver.find_element(By.XPATH, self.button_ViewCourse_xpath).click()

    def clickEyeButtonGetMYCourse(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//h2[contains(.,'Admin')]").click()
        time.sleep(1)
        #self.driver.find_element(By.XPATH, self.button_ResumeCourse_xpath).click()

        '''destination = self.driver.find_element(By.XPATH, self.button_ResumeCourse_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(destination).click().perform()'''
        #self.driver.find_element(By.XPATH, self.click_eye_button_getMYCourse_xpath).click()



    def clickUnEnRollLink(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        self.driver.find_element(By.XPATH, self.click_unEnroll_link_xpath).click()

    def clickPOpUpUnENRollButton(self):
        self.driver.find_element(By.XPATH, self.button_popUp_unEnroll_xpath).click()
