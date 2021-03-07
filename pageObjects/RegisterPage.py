from pageObjects.Common import Common


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.Common = Common(self.driver)

    def setTitle(self, title):
        if title == "Mr.":
            self.Common.WaitAndClickElementById("id_gender1")
        elif title == "Mrs.":
            self.Common.WaitAndClickElementById("id_gender2")

    def setFirstName(self, firstname):
        self.Common.WaitAndSendKeysToElementById("customer_firstname", firstname)

    def setLastName(self, lastname):
        self.Common.WaitAndSendKeysToElementById("customer_lastname", lastname)

    def setEmail(self, email):
        self.Common.WaitAndSendKeysToElementById("email", email)

    def setPassword(self, password):
        self.Common.WaitAndSendKeysToElementById("passwd", password)

    def setDateOfBirthDay(self, day):
        self.Common.SelectDropdownValueById("days", day)

    def setDateOfBirthMonth(self, month):
        self.Common.SelectDropdownValueById("months", month)

    def setDateOfBirthYear(self, year):
        self.Common.SelectDropdownValueById("years", year)

    def setAddressLine1(self, address):
        self.Common.WaitAndSendKeysToElementById("address1", address)

    def setCity(self, city):
        self.Common.WaitAndSendKeysToElementById("city", city)

    def setState(self, state):
        self.Common.SelectDropdownValueById("id_state", state)

    def setPostalCode(self, code):
        self.Common.WaitAndSendKeysToElementById("postcode", code)

    def setMobilePhone(self, phone):
        self.Common.WaitAndSendKeysToElementById("phone_mobile", phone)

    def setAlias(self, alias):
        self.Common.WaitAndSendKeysToElementById("alias", alias)

    def clickRegister(self):
        self.Common.WaitAndClickElementById("submitAccount")
