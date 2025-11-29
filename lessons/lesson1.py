class Hero:
    # конструктор класса
    def __init__(self, name, lvl, hp):
        # атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def base_action(self):
        return f"base action {self.name}"

# экземпляр класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 100, 100)

just_text = str("just text")
print(kirito.name)
print(asuna.hp)
print(kirito.base_action())
1:30

