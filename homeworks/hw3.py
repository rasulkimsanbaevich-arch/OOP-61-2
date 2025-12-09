class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self._price = price
        self.__discount =discount


    def get_price(self):
        self._price = self._price * (1-self.__discount / 100)
        return  f"Your discount is {self._price}"

    def set_discount(self):
        if self.__discount <= 50:
            return  self.get_price()
        return "EROR"


    def apply_extra_discount(self, secret_code):
        if secret_code == "VIP123":
            self._price 
            return self.set_discount()

        return "неверный код"






sugar = Product("sugar", 100, 25)


print(sugar.set_discount())
print(sugar.apply_extra_discount("VIP123"))



#2
from abc import ABC
class PaymentMethod:
    pass