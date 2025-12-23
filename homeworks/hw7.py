import sqlite3 # 18:31

connect = sqlite3.connect("library.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS library(
    name VARCHAR(70) NOT NULL,
    author VARCHAR (100) NOT NULL,
    year INTEGER NOT NULL)
    ''')
connect.commit()

def create_book(name, author, year):
    cursor.execute(
            'INSERT INTO library (name, author, year) VALUES (?,?,?)',
            (name, author, year)
    )
    connect.commit()
    print("Книга добавлен!")
# create_book("The Double", "Fedor Dostoevsky", 1861)


def get_book():
    cursor.execute(('SELECT name, year FROM library'))
    books = cursor.fetchall()
    # print(books)

get_book()

def update_book(row_id, year):
    cursor.execute('UPDATE library SET year = ? WHERE rowid = ?',
    (year, row_id))
    connect.commit()
    print("Год обновлен")
# update_book(1, 1866)

def delete_book(row_id):
    cursor.execute('DELETE FROM library WHERE rowid = ?',
                   (row_id,))
    connect.commit()
    print("Книга удален!")
# delete_book(3)

def get_by_rowid(row_id):
    cursor.execute('SELECT name, year FROM library WHERE rowid = ? ',
                   (row_id,))
    book = cursor.fetchone()
    print(book)
    connect.commit()



get_by_rowid(4)





