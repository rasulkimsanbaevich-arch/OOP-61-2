class User:
    default_role = "user"

    def __init__(self, name, role=None, subscribe=False):
        self.name = name
        self.role = role if role else self.default_role
        self.subscribe = subscribe

    @property
    def info(self):
        return f"{self.name} ({self.role})"

    @classmethod
    def create_guest(cls, name):
        return cls(name)

    @staticmethod
    def roles():
        return ["admin", "user"]


ROLE_COMMANDS = {
    "admin": ["start", "ban", "stop", "message"],
    "user": ["start", "message"]
}



def check_subscribe(func):
    def wrapper(self, user):
        if user.subscribe:
            return func(self, user)
        else:
            print(f"{user.name} не подписан на сервис")
    return wrapper


def permission_required(command):
    def decorator(func):
        def wrapper(self, user):
            if command not in ROLE_COMMANDS.get(user.role, []):
                print(f"Пользователь {user.name} не может выполнять команду \"{command}\"")
                return
            print(f"Команда \"{command}\" выполнена пользователем {user.name}")
            return func(self, user)
        return wrapper
    return decorator



class CommandHandler:

    @check_subscribe
    @permission_required("start")
    def start(self, user):
        print(f"{user.name} запустил систему")

    @check_subscribe
    @permission_required("ban")
    def ban(self, user):
        print(f"{user.name} забанил пользователя")

    @check_subscribe
    @permission_required("stop")
    def stop(self, user):
        print(f"{user.name} остановил систему")

    @check_subscribe
    @permission_required("message")
    def message(self, user):
        print(f"{user.name} отправил сообщение")



admin = User("Alice", "admin", True)
user = User("Bob", "user", True)
guest = User.create_guest("Guest")
handler = CommandHandler()

print("\n--- ADMIN ---")
handler.start(admin)
handler.ban(admin)
handler.stop(admin)

print("\n--- USER ---")
handler.start(user)
handler.ban(user)
handler.message(user)

print("\n--- GUEST ---")
handler.start(guest)