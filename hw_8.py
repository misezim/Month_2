import sqlite3

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_countries(db_name, countries):
    sql = '''INSERT INTO countries (title)
    VALUES (?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (countries,))
    except sqlite3.Error as e:
        print(e)

def create_table_cities(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def insert_cities(db_name, cities):
    sql = '''INSERT INTO cities (title, area, country_id)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, cities)
    except sqlite3.Error as e:
        print(e)

def create_table_students(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_students(db_name, students):
    sql = '''INSERT INTO students (first_name, last_name, city_id)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, students)
    except sqlite3.Error as e:
        print(e)


"""the hardest part"""
def get_cities(db_name):
    sql = '''SELECT id, title FROM cities'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)

def get_students_by_city_id(db_name, city_id):
    sql = '''
    SELECT students.first_name, students.last_name, countries.title AS country, 
    cities.title AS city,
    cities.area
    FROM students
    JOIN cities ON students.city_id = cities.id
    JOIN countries ON cities.country_id = countries.id
    WHERE cities.id = ?
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (city_id,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)






sql_to_create_countries_table = '''
CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL
    )
'''

sql_to_create_cities_table = '''
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    area DECIMAL(10,2) DEFAULT 0,
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES countries(id)
)
'''

sql_to_create_students_table = '''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(id)
)
'''


database_name = 'hw_8.db'
# create_table(database_name, sql_to_create_countries_table)
# insert_countries(database_name, 'Кыргызстан')
# insert_countries(database_name, 'Россия')
# insert_countries(database_name, 'Казахстан')

# create_table_cities(database_name, sql_to_create_cities_table)
# insert_cities(database_name, ('Бишкек', 127.0, 1))
# insert_cities(database_name, ('Ош', 182.0, 1))
# insert_cities(database_name, ('Москва', 2561.5, 2))
# insert_cities(database_name, ('Санкт-Петербург', 1439.0, 2))
# insert_cities(database_name, ('Алматы', 682.0, 3))
# insert_cities(database_name, ('Нур-Султан', 722.0, 3))
# insert_cities(database_name, ('Шымкент', 1170.0, 3))

# create_table_students(database_name, sql_to_create_students_table)
# insert_students(database_name, ('Айжан', 'Сыдыкова', 1))
# insert_students(database_name, ('Эрмек', 'Кожомкулов', 2))
# insert_students(database_name, ('Анна', 'Иванова', 3))
# insert_students(database_name, ('Алексей', 'Петров', 3))
# insert_students(database_name, ('Мария', 'Смирнова', 4))
# insert_students(database_name, ('Дмитрий', 'Кузнецов', 4))
# insert_students(database_name, ('Ержан', 'Султанов', 5))
# insert_students(database_name, ('Алия', 'Турсунова', 5))
# insert_students(database_name, ('Арман', 'Мухамедов', 6))
# insert_students(database_name, ('Жанара', 'Тилекова', 6))
# insert_students(database_name, ('Сауле', 'Байзакова', 7))
# insert_students(database_name, ('Айбек', 'Жусупов', 7))
# insert_students(database_name, ('Гульназ', 'Абдраимова', 1))
# insert_students(database_name, ('Эльдар', 'Бекмурзаев', 2))
# insert_students(database_name, ('Ольга', 'Морозова', 3))

print("Вы можете отобразить список учеников по выбранному id города"
    " из перечня городов ниже, для выхода из программы введите 0:")
cities = get_cities(database_name)

for city in cities:
    print(f"{city[0]}: {city[1]}")


while True:
    city_id = input("Введите id города: ")
    if city_id == '0':
        break

    try:
        city_id = int(city_id)
    except ValueError:
        print("Пожалуйста, введите корректный id города.")
        continue

    students = get_students_by_city_id(database_name, city_id)
    if students:
        print(f"Ученики в городе {city_id}:")
        for student in students:
            print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]} km2")
    else:
        print(f"Нет учеников в городе с id {city_id}")

