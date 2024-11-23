import sqlite3
#
# def create_connection(db_name):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_name)
#     except sqlite3.Error as e:
#         print(e)
#     return connection
#
# def create_table(connection, create_table_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_sql)
#     except sqlite3.Error as e:
#         print(e)


# def insert_employee(connection, employee):
#     sql = '''INSERT INTO employess (full_name, salary, hobby, birth_date, is_mariied)
#     VALUES (?, ?, ?, ?, ?)'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, employee)
#         connection.commit()
#     except sqlite3.Error as e:
#         print(e)



def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

# def insert_employee(db_name, employee):
#     sql = '''INSERT INTO employess (full_name, salary, hobby, birth_date, is_mariied)
#     VALUES (?, ?, ?, ?, ?)'''
#     try:
#         with sqlite3.connect(db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, employee)
#     except sqlite3.Error as e:
#         print(e)

def update_employee(db_name, employee):
    sql = '''UPDATE employess SET salary = ?, is_mariied = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
    except sqlite3.Error as e:
        print(e)

def delete_employee(db_name, id):
    sql = '''DELETE FROM employess WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)

def select_all_employees(db_name):
    sql = '''SELECT * FROM employess'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_employees_bysalary(db_name, salary_limit):
    sql = '''SELECT * FROM employess WHERE salary >= ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (salary_limit,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_employees_table = '''
CREATE TABLE employess (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(200) NOT NULL, 
    salary FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL, 
    is_mariied BOOLEAN DEFAULT FAULT
    )
'''

database_name = 'group_48.db'
# my_connection = create_connection(database_name)
# if my_connection is not None:
#     print('Successfully connected to database')
#     # create_table(my_connection, sql_to_create_employees_table)
#     insert_employee(my_connection, ('Jibek', 2400, 'programming', '2003-06-29', False ))
#     my_connection.close()

# create_table(database_name, sql_to_create_employees_table)
# insert_employee(database_name, ('Jibek Manasova', 2400, 'programming', '2003-06-29', False ))
# insert_employee(database_name, ('John Doe', 5000, 'marketing', '2015-02-14', True ))
# insert_employee(database_name, ('Alice Smith', 3200, 'sales', '2018-09-21', False ))
# insert_employee(database_name, ('Bob Johnson', 4500, 'hr', '2012-11-11', True ))
# insert_employee(database_name, ('Carlos Sanchez', 3500, 'finance', '2020-03-10', False ))
# insert_employee(database_name, ('Eve Turner', 6000, 'engineering', '2017-07-04', True ))
# insert_employee(database_name, ('Emma White', 2900, 'marketing', '2019-01-28', False ))
# insert_employee(database_name, ('David Brown', 5200, 'programming', '2014-06-18', True ))
# insert_employee(database_name, ('Sophia Green', 4300, 'operations', '2022-05-09', False ))
# insert_employee(database_name, ('James Lee', 4800, 'sales', '2011-03-12', True ))
# insert_employee(database_name, ('Olivia Harris', 2700, 'customer support', '2021-12-01', False ))
# insert_employee(database_name, ('Michael Clark', 5400, 'research', '2016-08-30', True ))
# insert_employee(database_name, ('Chloe Davis', 3800, 'engineering', '2013-04-07', False ))
# insert_employee(database_name, ('Liam Wilson', 5100, 'programming', '2023-06-15', True ))
# insert_employee(database_name, ('Mia Moore', 4600, 'finance', '2010-02-26', False ))
# insert_employee(database_name, ('Lucas Martinez', 5300, 'hr', '2018-10-08', True ))

# update_employee(database_name,(2500, True, 1))
# delete_employee(database_name, 2)
# select_all_employees(database_name)
select_employees_bysalary(database_name, 4000)