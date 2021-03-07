from pageObjects.Common import Common


class UserInfoPage:

    def __init__(self, driver):
        self.driver = driver
        self.Common = Common(self.driver)

    def openPersonalInformationSection(self):
        xpath = "//a[@title = 'Information']"
        self.Common.WaitAndClickElementByXpath(xpath)

    def getSocialTitle(self):
        id_mr = "uniform-id_gender1"
        id_mrs = "uniform-id_gender2"

        if self.Common.IsSelectedById(id_mr) is True:
            return "Mr."
        elif self.Common.IsSelectedById(id_mrs) is True:
            return "Mrs."
        else:
            return ""

    def getFirstName(self):
        return self.Common.WaitForElementById("firstname").get_attribute("value")

    def getLastName(self):
        return self.Common.WaitForElementById("lastname").get_attribute("value")

    def getEmail(self):
        return self.Common.WaitForElementById("email").get_attribute("value")

    def getDateOfBirthDays(self):
        xpath = "//*[@id = 'uniform-days']/span"
        return self.Common.WaitAndGetElementTextByXpath(xpath).strip()

    def getDateOfBirthMonths(self):
        xpath = "//*[@id = 'uniform-months']/span"
        return self.Common.WaitAndGetElementTextByXpath(xpath).strip()

    def getDateOfBirthYears(self):
        xpath = "//*[@id = 'uniform-years']/span"
        return self.Common.WaitAndGetElementTextByXpath(xpath).strip()

    def getCurrentPassword(self):
        return self.Common.WaitForElementById("old_passwd").get_attribute("value")

    def getConfirmation(self):
        return self.Common.WaitForElementById("confirmation").get_attribute("value")

    def clickLogOut(self):
        xpath = "//a[@title = 'Log me out']"
        self.Common.WaitAndClickElementByXpath(xpath)

    def getHeading1Title(self):
        xpath = "//*[@id='center_column']/h1"
        return self.Common.WaitAndGetElementTextByXpath(xpath)
