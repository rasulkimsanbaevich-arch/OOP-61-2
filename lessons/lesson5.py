# Статический метод (@staticmethod)


class Math:
    def __init__(self, d, c):
        self.d = d
        self.c = c


    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(j, i):
        return j - i


# print(Math.add(12, 12))
# print(Math.subtract(12, 1))

# метод класса (@classmethod)
class User:
    # Атрибуты класса
    default_role = "guest"
    def __init__(self, name, role):
        self.name = name
        self.role = role
    @classmethod
    def create_from_name(cls, name):
        return cls(name, cls.default_role)

    @classmethod
    def get_base_role(cls):
        return cls.default_role

    def get_name(self):
        return self.name
user_1 = User.create_from_name("User")



print(User.get_base_role())

18