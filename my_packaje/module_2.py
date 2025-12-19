from lessons.lesson2 import MageHero
import random
class Test:

    pass
class Hero:
    # конструктор класса
    def __init__(self, name, lvl, hp):
        # атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp



    def base_action(self):
        return f"base action {self.name}"

__all__ =  (
    "Hero",
    "Test"
)