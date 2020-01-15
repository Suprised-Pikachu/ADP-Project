import random
user_id = random.randint(1, 99999999999999999999)


class User:

    def __init__(self, userName, email, password, cfmPassword, userType):
        User.countID = user_id
        self.__userID = User.countID
        self.__userName = userName
        self.__email = email
        self.__password = password
        self.__cfmPassword = cfmPassword
        self.__userType = userType

    def get_userID(self):
        return self.__userID

    def get_userName(self):
        return self.__userName

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_cfmPassword(self):
        return self.__cfmPassword

    def get_userType(self):
        return self.__userType

    def set_userID(self, userID):
        self.__userID = userID

    def set_userName(self, userName):
        self.__userName = userName

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_cfmPassword(self, cfmPassword):
        self.__cfmPassword = cfmPassword

    def set_userType(self, userType):
        self.__userType = userType


event_id = random.randint(1, 99999999999999999999)


class Event:

    def __init__(self, eventName, date, details, requirements, remarks):
        Event.countID = event_id
        self.__eventID = Event.countID
        self.__eventName = eventName
        self.__date = date
        self.__details = details
        self.__requirements = requirements
        self.__remarks = remarks

    def get_eventID(self):
        return self.__eventID

    def get_eventName(self):
        return self.__eventName

    def get_date(self):
        return self.__date

    def get_details(self):
        return self.__details

    def get_requirements(self):
        return self.__requirements

    def get_remarks(self):
        return self.__remarks

    def set_eventID(self, eventID):
        self.__eventID = eventID

    def set_eventName(self, eventName):
        self.__eventName = eventName

    def set_date(self, date):
        self.__date = date

    def set_details(self, details):
        self.__details = details

    def set_requirements(self, requirements):
        self.__requirements = requirements

    def set_remarks(self, remarks):
        self.__remarks = remarks
