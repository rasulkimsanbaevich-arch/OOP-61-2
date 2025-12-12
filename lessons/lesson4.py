# Dunder methods
# Магические методы

class Test:
    def __init__(self, name = "John Doe"):
        self.name = name

    # def __str__(self):
#     #     return self.name
# my_obj = Test()
# my_str = "My str"
#
# print(my_obj)
# print(my_str)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# +
    def __add__(v2, v1):
        print(v2.x + v1.x)
# <
    def __lt__(self, other):
        print(self.x < other.x)

# >
    # def __gt__(self, other):

# ==
    # def __eq__(self, other):
v1 = Vector(22, 22)
v2 = Vector(23, 23)

v3 = v1 < v2



class Mylist:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 2

    # def __str__(self):
    #     return self.value
    # def __setitem__(self, key, value):
    #     list_my = self.value
    #     list_my[key] = value


my_list = Mylist()
print(my_list.count)
my_list()
my_list()
print(my_list.count)


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def __to_som(self, data):
        print("Переводим на сом")
        return data

    def __add__(self, other):
        if self.currency != other.currency:
            print("Валюта не совпадает!")
        return self.amount + other.amount

class News:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.view_count = 0
    def __call__(self, user, *args, **kwargs):
        self.view_count += 1



