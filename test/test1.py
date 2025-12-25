#1
from abc import ABC, abstractmethod
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp= hp


    def action(self):
        return f"{self.name} готов к бою!"

#2
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__( name, lvl, hp)
        self.mp = mp
    def action(self):
        return  f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(Hero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    bank_name = "Simba"
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password):
        if password == self.__password:
            return f"Добро пожаловать, {self.hero.name}!"
        else:
            return "Неверный пароль!"
    def full_info(self):
        return f"Name hero: {self.hero}, hero's balance {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    @staticmethod
    def bonus_for_level(lvl):
        return lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            total = self._balance + other._balance
            return f"Сумма балансов: {total} SOM"
        else:
            return "Ошибка: герои разных типов!"

    def __eq__(self, other):
        return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl

#5
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": f"{phone}"}

if __name__ == "__main__":
    mage1 = MageHero("Merlin", 80, 100, 150)
    mage2 = MageHero("Merlin", 80, 100, 200)
    warrior = WarriorHero("Conan", 50, 900)

    print(mage1.action())
    print(mage2.action())
    print(warrior.action())

    acc1 = BankAccount(mage1, 5000, "1234", "Simba")
    acc2 = BankAccount(mage2, 3000, "0000", "Simba")
    acc3 = BankAccount(warrior, 2500, "1111", "Simba")

    print(acc1)
    print(acc2)

    print("Банк:", acc1.get_bank_name())
    print("Бонус за уровень:", acc1.bonus_for_level(mage1.lvl), "SOM")

    print("\n=== Проверка __add__ ===")
    print("Сумма счетов двух магов:", acc1 + acc2)
    print("Сумма мага и воина:", acc1 + acc3)

    print("\n=== Проверка __eq__ ===")
    print("Mage1 == Mage2 ?", acc1 == acc2)
    print("Mage1 == Warrior ?", acc1 == acc3)

    print(f"Бонус за {warrior.lvl} уровень: {BankAccount.bonus_for_level(warrior.lvl)} SOM")

    sms = KGSms()
    print(sms.send_otp("+996777123456"))



