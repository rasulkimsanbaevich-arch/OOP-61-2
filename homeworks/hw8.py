import sqlite3
connect = sqlite3.connect("school.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    score INTEGER,
    student_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")

connect.commit()
def create_student(name):
    cursor.execute(
        "INSERT INTO students(name) VALUES (?)",
        (name,)
    )
    connect.commit()
    print(f"Студент добавлен: {name}")

def create_grade(student_id, subject, score):
    cursor.execute(
        "INSERT INTO grades(student_id, subject, score) VALUES (?, ?, ?)",
        (student_id, subject, score)
    )
    connect.commit()
    print("Оценка добавлена")
# create_student("Aibek")
# create_student("Dana")
# create_grade(1, "Math", 90)
# create_grade(1, "Physics", 85)
# create_grade(2, "Math", 78)

def get_students_with_grades():
    cursor.execute("""
    SELECT students.name, grades.subject, grades.score
    FROM students
    LEFT JOIN grades ON students.id = grades.student_id
    """)
    data = cursor.fetchall()

    for row in data:
        print(f"NAME: {row[0]}, SUBJECT: {row[1]}, SCORE: {row[2]}")

# get_students_with_grades()


def grades_stats():
    cursor.execute("""
    SELECT 
        COUNT(score),
        MAX(score),
        AVG(score)
    FROM grades
    """)
    result = cursor.fetchone()
    print(f"COUNT: {result[0]}, MAX: {result[1]}, AVG: {result[2]}")

# grades_stats()

def grades_count_by_student():
    cursor.execute("""
    SELECT students.name, COUNT(grades.id)
    FROM students
    LEFT JOIN grades ON students.id = grades.student_id
    GROUP BY students.id
    """)
    data = cursor.fetchall()

    for row in data:
        print(f"STUDENT: {row[0]}, GRADES COUNT: {row[1]}")

# grades_count_by_student()

def students_with_math():
    cursor.execute("""
    SELECT name
    FROM students
    WHERE id IN (
        SELECT student_id
        FROM grades
        WHERE subject = 'Math'
    )
    """)
    data = cursor.fetchall()
    print("Students with Math:")
    for row in data:
        print(row[0])
# students_with_math()

def create_view():
    cursor.execute("""
    CREATE VIEW IF NOT EXISTS student_view AS
    SELECT students.name, grades.subject, grades.score
    FROM students
    LEFT JOIN grades ON students.id = grades.student_id
    """)
    connect.commit()
create_view()
def get_view_data():
    cursor.execute("SELECT * FROM student_view")
    data = cursor.fetchall()

    print(data)

get_view_data()






