import sqlite3

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
#

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(db_name, products):
    sql = '''INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)


def update_products_quantity(db_name, products):
    sql = '''UPDATE products SET quantity =? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,products)
    except sqlite3.Error as e:
        print(e)

def update_products_price(db_name, products):
    sql = '''UPDATE products SET price =? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,products)
    except sqlite3.Error as e:
        print(e)


def delete_product(db_name, id):
    sql = '''DELETE FROM products WHERE id= ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)

def select_all_products(db_name):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_all_products_by_quantity_and_price(db_name, limit):
    sql = '''SELECT * FROM products WHERE price<? and quantity>?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, limit)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_all_products_by_name(db_name):
    sql = '''SELECT * FROM products WHERE product_title LIKE '%milk%'
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
    )
'''

database_name = 'hw.db'
# my_connection = create_connection(database_name)
# if my_connection is not None:
#     print('Successfully connected to database')
#     create_table(my_connection, sql_to_create_products_table)
# create_table(database_name, sql_to_create_products_table)


# insert_products(database_name,('2% Milk ', 120, 150))
# insert_products(database_name, ('heavy Cream', 120, 150))
# insert_products(database_name, ('almond Milk', 80, 200))
# insert_products(database_name, ('eggs', 50, 300))
# insert_products(database_name, ('butter', 200, 100))
# insert_products(database_name, ('cheese', 150, 80))
# insert_products(database_name, ('soy Milk ', 90, 250))
# insert_products(database_name, ('orange juice', 180, 130))
# insert_products(database_name, ('apples juice', 75, 180))
# insert_products(database_name, ('bananas', 60, 220))
# insert_products(database_name, ('carrot juice', 40, 300))
# insert_products(database_name, ('coconut milk', 55, 400))
# insert_products(database_name, ('tomatoes', 70, 350))
# insert_products(database_name, ('coconut water', 250, 120))
# insert_products(database_name, ('lactose-free milk', 350, 80))
# insert_products(database_name, ('coffee', 400, 90))


# update_products_quantity(database_name, (75, 1))
# update_products_price(database_name, (80, 2))
# delete_product(database_name, 13)
# select_all_products(database_name)
# select_all_products_by_quantity_and_price(database_name,(200, 200))
select_all_products_by_name(database_name)