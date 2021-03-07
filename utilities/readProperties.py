import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig:

    @staticmethod
    def getLoginURL():
        return config.get('common info', 'loginURL')

    @staticmethod
    def getUsername():
        return config.get('sample user info', 'username')

    @staticmethod
    def getPassword():
        return config.get('sample user info', 'password')

    @staticmethod
    def getFirstName():
        return config.get('sample user info', 'firstName')

    @staticmethod
    def getLastName():
        return config.get('sample user info', 'lastName')

    @staticmethod
    def getDateOfBirthDay():
        return config.get('sample user info', 'dateOfBirthDay')

    @staticmethod
    def getDateOfBirthMonth():
        return config.get('sample user info', 'dateOfBirthMonth')

    @staticmethod
    def getDateOfBirthYear():
        return config.get('sample user info', 'dateOfBirthYear')

    @staticmethod
    def getAddress():
        return config.get('sample user info', 'address')

    @staticmethod
    def getCity():
        return config.get('sample user info', 'city')

    @staticmethod
    def getState():
        return config.get('sample user info', 'state')

    @staticmethod
    def getMobilePhone():
        return config.get('sample user info', 'mobilePhone')

    @staticmethod
    def getAlias():
        return config.get('sample user info', 'alias')
