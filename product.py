class Product:
    def __init__(self, product_id, name, image, type, price, unit, stock, description):
        self.__product_id = product_id
        self.__name = name
        self.__image = image
        self.__type = type
        self.__price = price
        self.__unit = unit
        self.__stock = stock
        self.__description = description

    # accessor methods
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_image(self):
        return self.__image

    def get_type(self):
        return self.__type

    def get_price(self):
        return self.__price

    def get_unit(self):
        return self.__unit

    def get_stock(self):
        return self.__stock

    def get_description(self):
        return self.__description

    # mutator methods
    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_name(self, name):
        self.__name = name

    def set_image(self, image):
        self.__image = image

    def set_type(self, type):
        self.__type = type

    def set_price(self, price):
        self.__price = price

    def set_unit(self, unit):
        self.__unit = unit

    def set_stock(self, stock):
        self.__stock = stock

    def set_description(self, description):
        self.__description = description

    def add_stock(self, stock):
        self.__stock += stock

    def sell_stock(self, stock):
        if stock >= self.__stock:
            return 0
        else:
            self.__stock -= stock

    def get_unitNo(self):
        unitNo = ""
        for char in self.__unit:
            if char.isdigit():
                unitNo += char
        return int(unitNo)

    def get_unitType(self):
        unitNo = len(str(self.get_unitNo()))
        unitType = self.__unit[unitNo:]
        return unitType

    def subtract_stock(self, amount):
        stock = self.get_stock()
        if amount.isdigit():
            if amount <= stock:
                self.set_stock(stock-amount)
            else:
                print("Not enough stock.")
        else:
            print("Amount entered must be an integer.")
