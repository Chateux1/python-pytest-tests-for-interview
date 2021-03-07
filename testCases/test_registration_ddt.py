import pytest
from selenium import webdriver
from testCases.conftest import driver
from pageObjects.LoginPage import LoginPage
from pageObjects.RegisterPage import RegisterPage
from pageObjects.UserInfoPage import UserInfoPage
from utilities.readProperties import ReadConfig
from utilities import XLUtils


class TestRegistrationDDT:

    data_path = ".\\TestData\\LoginData.xlsx"
    sheet_name = "Registration Info"

    # This test is using user information from ./TestData/LoginData.xlsx
    # As the test is trying to create a new user, the test might crash and fail if the users already exist
    # In order for this test to succeed, unique emails should be provided in the file in the first column
    def test_register_ddt(self, driver):
        self.driver = driver
        self.driver.get(ReadConfig.getLoginURL())

        self.lp = LoginPage(self.driver)
        self.rp = RegisterPage(self.driver)
        self.uip = UserInfoPage(self.driver)

        test_status = []
        expected_title = "MY ACCOUNT"
        rows = XLUtils.getRowCount(self.data_path, self.sheet_name)

        for r in range(2, rows + 1):
            data = []
            columns = XLUtils.getColumnCount(self.data_path, self.sheet_name)
            for c in range(1, columns + 1):
                data.append(XLUtils.readData(self.data_path, self.sheet_name, r, c))

            self.lp.setUserNameRegister(data[0])
            self.lp.clickRegister()
            self.rp.setFirstName(data[1])
            self.rp.setLastName(data[2])
            self.rp.setPassword(data[3])
            self.rp.setDateOfBirthDay(data[4])
            self.rp.setDateOfBirthMonth(data[5])
            self.rp.setDateOfBirthYear(data[6])
            self.rp.setAddressLine1(data[7])
            self.rp.setCity(data[8])
            self.rp.setState(data[9])
            self.rp.setPostalCode(data[10])
            self.rp.setMobilePhone(data[11])
            self.rp.setAlias(data[12])
            self.rp.clickRegister()

            expected_result = data[13]
            actual_title = self.uip.getHeading1Title()

            if actual_title == expected_title:
                if expected_result == "Pass":
                    self.uip.clickLogOut()
                    self.driver.get(ReadConfig.getLoginURL())
                    test_status.append("Pass")
                if expected_result == "Fail":
                    self.uip.clickLogOut()
                    self.driver.get(ReadConfig.getLoginURL())
                    test_status.append("Fail")
            if actual_title != expected_title:
                if expected_result == "Pass":
                    self.driver.get(ReadConfig.getLoginURL())
                    test_status.append("Fail")
                if expected_result == "Fail":
                    self.driver.get(ReadConfig.getLoginURL())
                    test_status.append("Pass")

        assert "Fail" not in test_status
