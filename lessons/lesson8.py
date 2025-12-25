import sqlite3

from colorama import Cursor

connect = sqlite3.connect("shop.db")
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50)
    )
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT, 
        total INTEGER,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
        )
        ''')
connect.commit()

def create_user(name):
    cursor.execute('INSERT INTO users(name) VALUES (?)', (name,))
    connect.commit()
    print(f"Пользователь создан {name}!")


def create_order(user_id, product_name, total):
    cursor.execute('INSERT INTO orders(user_id, product, total) VALUES (?, ?, ?)', (user_id, product_name, total))
    connect.commit()
    print(f"Заказ создан {product_name}!")

# create_user("Ardager")
# create_user("Arzybek")
# create_user("Oleg")
# create_user("Slava")
# create_order(1, "Iphone17pro-max", 1200)
# create_order(2, "MI 17", 800)
# create_order(5, "Google Phone 10pro", 1000)


def get_user_orders():
    cursor.execute('''
    SELECT users.name, orders.product,  orders.total
    FROM users RIGHT JOIN orders ON users.id = orders.user_id''')

    users = cursor.fetchall()

    for i in users:
        print(f"NAME: {i[0]}, PRODUCT: {i[1]}, TOTAL: {i[2]}")

# get_user_orders()

# MAX(), MIN(), AVG(), COUNT(), SUM()

def mx_total():
    cursor.execute('SELECT SUM(total) FROM orders')
    order = cursor.fetchone()
    print(order)
# mx_total()


def get_user_order():
    cursor.execute('''
    SELECT user_id, COUNT(*)
    FROM orders
    GROUP BY user_id''')
    users = cursor.fetchall()
    print(users)
get_user_order()
52


