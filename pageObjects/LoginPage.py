from selenium import webdriver
from pageObjects.Common import Common


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.Common = Common(self.driver)

    def setUserNameSignIn(self, username):
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(username)

    def setPasswordSignIn(self, password):
        self.driver.find_element_by_id("passwd").clear()
        self.driver.find_element_by_id("passwd").send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id("SubmitLogin").click()

    def setUserNameRegister(self, username):
        self.driver.find_element_by_id("email_create").clear()
        self.driver.find_element_by_id("email_create").send_keys(username)

    def clickRegister(self):
        self.driver.find_element_by_id("SubmitCreate").click()
