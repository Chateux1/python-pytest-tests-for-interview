import pytest
from selenium import webdriver
from testCases.conftest import driver
from pageObjects.LoginPage import LoginPage
from pageObjects.UserInfoPage import UserInfoPage
from utilities.readProperties import ReadConfig


class TestLoginBasic:

    def test_login(self, driver):
        self.driver = driver
        self.driver.get(ReadConfig.getLoginURL())

        self.lp = LoginPage(self.driver)
        self.uip = UserInfoPage(self.driver)

        self.lp.setUserNameSignIn(ReadConfig.getUsername())
        self.lp.setPasswordSignIn(ReadConfig.getPassword())
        self.lp.clickLogin()
        assert self.uip.getHeading1Title() == "MY ACCOUNT"

    def test_personal_info(self, driver):
        self.driver = driver
        self.driver.get(ReadConfig.getLoginURL())

        self.lp = LoginPage(self.driver)
        self.uip = UserInfoPage(self.driver)

        self.lp.setUserNameSignIn(ReadConfig.getUsername())
        self.lp.setPasswordSignIn(ReadConfig.getPassword())
        self.lp.clickLogin()
        self.uip.openPersonalInformationSection()
        assert self.uip.getFirstName() == ReadConfig.getFirstName()
        assert self.uip.getLastName() == ReadConfig.getLastName()
        assert self.uip.getEmail() == ReadConfig.getUsername()
        assert self.uip.getDateOfBirthDays() == ReadConfig.getDateOfBirthDay()
        assert self.uip.getDateOfBirthMonths() == ReadConfig.getDateOfBirthMonth()
        assert self.uip.getDateOfBirthYears() == ReadConfig.getDateOfBirthYear()
        assert self.uip.getCurrentPassword() == ""
        assert self.uip.getConfirmation() == ""
