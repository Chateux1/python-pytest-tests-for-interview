import pytest
from selenium import webdriver
from testCases.conftest import driver
from pageObjects.LoginPage import LoginPage
from pageObjects.RegisterPage import RegisterPage
from pageObjects.UserInfoPage import UserInfoPage
from utilities.readProperties import ReadConfig


class TestRegistration:

    username = "21-03-08-T0@email.com"
    password = "password"
    firstName = "SomeName"
    lastName = "SomeSurname"
    dateOfBirthDay = 11
    dateOfBirthMonth = "November"
    dateOfBirthYear = 1977
    address = "Some Address"
    city = "Some City"
    state = "Utah"
    postalCode = "12345"
    mobilePhone = "+37012312345"
    alias = "Some Alias"

    # This test is trying to create a new user
    # If a user already exists with the email that is provided above, then the test will crash and fail
    def test_register(self, driver):
        self.driver = driver
        self.driver.get(ReadConfig.getLoginURL())

        self.lp = LoginPage(self.driver)
        self.rp = RegisterPage(self.driver)
        self.uip = UserInfoPage(self.driver)

        self.lp.setUserNameRegister(self.username)
        self.lp.clickRegister()
        self.rp.setFirstName(self.firstName)
        self.rp.setLastName(self.lastName)
        self.rp.setPassword(self.password)
        self.rp.setDateOfBirthDay(self.dateOfBirthDay)
        self.rp.setDateOfBirthMonth(self.dateOfBirthMonth)
        self.rp.setDateOfBirthYear(self.dateOfBirthYear)
        self.rp.setAddressLine1(self.address)
        self.rp.setCity(self.city)
        self.rp.setState(self.state)
        self.rp.setPostalCode(self.postalCode)
        self.rp.setMobilePhone(self.mobilePhone)
        self.rp.setAlias(self.alias)
        self.rp.clickRegister()

        assert self.uip.getHeading1Title() == "MY ACCOUNT"
