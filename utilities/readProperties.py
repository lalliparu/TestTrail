import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\munil\\PycharmProjects\\pythonProject_RevDoc\\Configurations\\config.ini")

class Readconfig:
   @staticmethod
   def getApplicationURL():
       url = config.get('basic info','baseURL')
       return url

   @staticmethod
   def getUserName():
       username = config.get('basic info', 'username')
       return username

   @staticmethod
   def getPassword():
        password = config.get('basic info', 'password')
        return password

   @staticmethod
   def getSearchText():
       searchtext = config.get('basic info', 'searchText')
       return searchtext

   @staticmethod
   def getSelect():
       select = config.get('basic info', 'select')
       return select

   @staticmethod
   def getText():
       text = config.get('basic info', 'text')
       return text

   @staticmethod
   def getText1():
        text1 = config.get('basic info', 'text1')
        return text1
   @staticmethod
   def getfirstName1():
       FirstName1 = config.get('basic info', 'FirstName1')
       return FirstName1
   @staticmethod
   def getlastName1():
       LastName1 = config.get('basic info', 'LastName1')
       return LastName1
   @staticmethod
   def geteMail():
       Email = config.get('basic info','Email')
       return Email
   @staticmethod
   def getbio():
       Bio = config.get('basic info', 'Bio')
       return Bio
   @staticmethod
   def getcompany():
       Company = config.get('basic info', 'Company')
       return Company
   @staticmethod
   def getTerOfUse():
       Yes1 = config.get('basic info', 'Yes1')
       return Yes1
   @staticmethod
   def getAgreeWithPri():
       Yes2 = config.get('basic info', 'Yes2')
       return Yes2
   @staticmethod
   def getTestProfile():
       text3 = config.get('basic info', 'text3')
       return text3
   @staticmethod
   def getUserName():
       userName1 = config.get('basic info', 'userName1')
       return userName1






