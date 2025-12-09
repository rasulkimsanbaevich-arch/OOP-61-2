#1
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
        super().__init__(self, name, lvl, hp)
        self.mp = mp
    def action(self):
        return  f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BanckAccount:
    def __init__(self, hero, bank_name, balance, password):
        self.hero = hero
        self.bank_name = bank_name
        self._balance = balance
        self.__password = password

    def login(self, password):
        if password == self.__password:
            return self._balance
        return "False password"
    def full_info(self):
        return f"Name hero: {self.hero}, hero's balance {self._balance}"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self, lvl):
        return lvl * 10

