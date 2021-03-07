from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions


class Common:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def WaitForElementById(self, id):
        return self.wait.until(ExpectedConditions.visibility_of_element_located((By.ID, id)))

    def WaitForElementByXpath(self, xpath):
        return self.wait.until(ExpectedConditions.visibility_of_element_located((By.XPATH, xpath)))

    def WaitAndGetElementTextById(self, id):
        return self.WaitForElementById(id).text

    def WaitAndGetElementTextByXpath(self, xpath):
        return self.WaitForElementByXpath(xpath).text

    def WaitAndClickElementByXpath(self, xpath):
        self.WaitForElementByXpath(xpath).click()

    def WaitAndClickElementById(self, id):
        self.WaitForElementById(id).click()

    def WaitAndSendKeysToElementById(self, id, keys):
        # Check if the value passed is not empty
        # This is needed because some tests will have empty data
        # send_keys fails if the parameter is empty
        if keys:
            self.WaitForElementById(id).clear()
            self.WaitForElementById(id).send_keys(keys)

    def SelectDropdownValueById(self, id, value):
        xpath = f"//*[@id='{id}']/option[contains(text(), '{value}')]"
        self.WaitAndClickElementByXpath(xpath)

    def IsSelectedById(self, id):
        xpath = f"//*[@id = '{id}']/span"
        return "checked" in self.WaitForElementByXpath(xpath).get_attribute("class")
