class PaymentInfo:
    def __init__(self, name, email, address, country, city, zip, cardName, cardNum, expmonth, expyear, cvv, totalpaid, date):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__country = country
        self.__city = city
        self.__zip = zip
        self.__cardName = cardName
        self.__cardNum = cardNum
        self.__expmonth = expmonth
        self.__expyear = expyear
        self.__cvv = cvv
        self.__totalpaid = totalpaid
        self.__date = date

    def get_date(self):
        return self.__date
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city

    def get_zip(self):
        return self.__zip

    def get_cardName(self):
        return self.__cardName

    def get_cardNum(self):
        return self.__cardNum

    def get_expmonth(self):
        return self.__expmonth

    def get_expyear(self):
        return self.__expyear

    def get_cvv(self):
        return self.__cvv

    def get_totalpaid(self):
        return self.__totalpaid



    def set_date(self,date):
        self.__date = date
    def set_name(self,name):
        self.__name = name

    def set_email(self,email):
        self.__email = email

    def set_address(self,address):
        self.__address = address

    def set_country(self,country):
        self.__country = country

    def set_city(self,city):
        self.__city = city

    def set_zip(self,zip):
        self.__zip = zip

    def set_cardName(self,cardName):
        self.__cardName = cardName

    def set_cardNum(self,cardNum):
        self.__cardNum = cardNum

    def set_expmonth(self,expmonth):
        self.__expmonth = expmonth

    def set_expyear(self,expyear):
        self.__expyear = expyear

    def set_cvv(self,cvv):
        self.__cvv = cvv

    def set_totalpaid(self,totalpaid):
        self.__totalpaid = totalpaid

