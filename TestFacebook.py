#region---------------------------------I M P O R T S----------------------------------------
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
#endregion



class TestFacebook():

#region----------------------------C O N S T R U C T O R--------------------------------------
    def __init__(self, nameBrawser):
          self.nameBrawser = nameBrawser
#endregion

#region----------------------------M E T H O D S----------------------------------------------
    def startTest(self):
        if self.nameBrawser == "Chrom":
            driver = webdriver.Chrome()
            self.test(driver)
            driver.quit()
        else:
            webdriver.Edge()



    def test(self,driver):
        self.facebookAuthorization(driver)
        self.goToMyProfile(driver)
        self.findeMyFriends(driver)


    def facebookAuthorization(self, driver):

        driver.get("https://www.facebook.com/login")
        inputUserName = driver.find_element_by_id("email")
        inputUserName.send_keys("****************")
        inputPassword = driver.find_element_by_id("pass")
        inputPassword.send_keys("****************")
        buttonLogin = driver.find_element_by_id("loginbutton")
        buttonLogin.click()


    def goToMyProfile(self,driver):
        action = ActionChains(driver)
        action.move_by_offset(200,200).perform()
        action.click().perform()
        linkToMyProfile =  driver.find_element_by_partial_link_text("Андрей")
        linkToMyProfile.click()


    def findeMyFriends(self, driver):
         linkToMyProfile = driver.find_element_by_partial_link_text("Друзья").click()


# endregion
