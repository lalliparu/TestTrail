from selenium import webdriver



from pageObjects.myProfile import myProfile
from utilities.readProperties import Readconfig
from pageObjects.loginPage import LoginPage

class Test_004_myProfile:
    baseUrl = Readconfig.getApplicationURL()
    username = Readconfig.getUserName()
    password = Readconfig.getPassword()
    FirstName1 = Readconfig.getfirstName1()
    LastName1 = Readconfig.getlastName1()
    Email = Readconfig.geteMail()
    Bio = Readconfig.getbio()
    Company = Readconfig.getcompany()
    Yes1 = Readconfig.getTerOfUse()
    Yes2 = Readconfig.getAgreeWithPri()
    #text3 = Readconfig.getTestProfile()
    userName1 = Readconfig.getUserName()




    def test_myProfile(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.LP =LoginPage(self.driver)
        self.LP.enterUserName(self.username)
        self.LP.enterPassWord(self.password)
        self.LP.clickSigninButton()
        self.MP = myProfile(self.driver)
        self.MP.clickUsernameLearner()
        self.MP.clickButtonMyProfile()
        self.MP.typeButtonFirstName(self.FirstName1)
        self.MP.typeButtonLastName(self.LastName1)
        self.MP.typeEmailButton(self.Email)
        self.MP.typeBioYourSelf(self.Bio)
        self.MP.typeCompanyId(self.Company)
        #self.MP.typeTermsOfUse(self.Yes1)
        #self.MP.typeAgreeWithPriStatement(self.Yes2)
        self.MP.selectProfile()
        self.MP.typeUserName(self.userName1)
        self.MP.clickSaveChange()




































































