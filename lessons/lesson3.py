#инкапсуляция
import random
class BanckAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        return "не верный пароль"
    def get_money(self, password, amount):
        if password == self.__password:
            self._balance -= amount
            return self._balance
        return ("не верный пароль")
    def _random_password(self):
        return random.randint(100000, 999999)
    def reset_password(self, old_password):
        if self.__password == old_password:
            new_pass = self._random_password()
            self.__password = new_pass
            return self.__password



ardager = BanckAccount("Ardager", 100, "qwerty123")

print(ardager._BanckAccount__password)
print(ardager.reset_password("qwerty123"))
print(ardager._BanckAccount__password)


#абстракция
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def voice(self):
        pass

class Dog(Animal):
    def move(self):
        return "ходит"
    def voice(self):
        return "гав гав"

my_dog = Dog()
class User:
    def __init__(self,name, country):
        self.name = name
        self.country = country
luffi = User("Luffi", "KG")

class ABCSendOTP(ABC):

    @abstractmethod
    def send_otp(self):
        pass

class KGSendOTP(ABCSendOTP):
    @abstractmethod
    def send_otp(self):
        sms = "<Text>1234</Text><PhoneNumber>+996509787878</PhoneNumber>"

class RUSendOTP(ABCSendOTP):
    @abstractmethod
    def send_otp(self):
        sms = {
            "text": "1234",
            "PhoneNumber": "+777689987"
        }

class Register:
    def __init__(self, country1, country2):
        self.country1 = country1
        self.country2 = country2
    def register(self, user):
        if user.country == self.country1:
            self.country1.send_otp()
        elif user.country == self.country2:
            self.country2.send_otp()
register = Register(KGSendOTP)