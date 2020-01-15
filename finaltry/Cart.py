class Cart:
    countcart = 0
    def __init__(self,itemId,name,quantity,price,type,unit,uType,image):
        #'122','apple',600,10,'veg',600,'g'
        Cart.countcart += 1
        self.__itemId = itemId
        self.__name = name
        self.__quantity = quantity
        self.__price = float(price)
        self.set_cost(quantity,price,unit,uType)
        self.__type = type
        self.__unit = unit
        self.__uType = uType
        self.__image = image
    def set_itemId(self,itemId):
        self.__itemId = itemId
    def set_name(self,name):
        self.__name = name
    def set_quantity(self,quantity):
        self.__quantity = quantity
    def set_price(self,price):
        self.__price = round(price,2)
    def set_type(self,type):
        self.__type = type
    def set_unit(self,unit):
        self.__unit = unit
    def set_uType(self,uType):
        self.__uType = uType
    def set_cost(self,quantity,price,unit,uType):
        if uType == "kg" or uType =="per packet" or uType =="per box":
            cost = (quantity/unit)*float(price)
            self.__cost = round(cost,3)
        elif uType == "g":
            cost = float(price)*(quantity/unit)
            self.__cost = round(cost,3)
        else:
            self.__cost = 0
    def set_image(self,image):
        self.__image = image


    def get_name(self):
        return self.__name
    def get_quantity(self):
        return self.__quantity
    def get_price(self):
        return self.__price
    def get_cost(self):
        return self.__cost
    def get_itemId(self):
        return self.__itemId
    def get_type(self):
        return self.__type
    def get_unit(self):
        return self.__unit
    def get_uType(self):
        return self.__uType
    def get_image(self):
        return self.__image
