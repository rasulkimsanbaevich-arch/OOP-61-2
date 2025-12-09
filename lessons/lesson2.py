class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f"{self.name}{self.lvl}"


class MageHero(Hero):
    pass













