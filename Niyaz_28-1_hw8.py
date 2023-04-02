import sqlite3

def create_connection(name):
    conn = None
    try:
        conn = sqlite3.connect(name)
        return conn
    except sqlite3.Error:
        print(sqlite3.Error)

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error:
        print(sqlite3.Error)

def create_country(conn, countr:tuple):
    try:
        sql = '''INSERT INTO countries(title) VALUES (?)'''
        cursor = conn.cursor()
        cursor.execute(sql, countr)
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)

def create_city(conn, city:tuple):
    try:
        sql = '''INSERT INTO cities(title, area, country_id) VALUES (?,?,?)'''
        cursor = conn.cursor()
        cursor.execute(sql, city)
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)

def create_employee(conn, employee:tuple):
    try:
        sql = '''INSERT INTO employees (fisrt_name, last_name, city_id) VALUES (?,?,?)'''
        cursor = conn.cursor()
        cursor.execute(sql, employee)
        conn.commit()
    except sqlite3.Error:
        print(sqlite3.Error)
database = 'hw8.db'


create_table_countries = "CREATE TABLE countries (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL)"
create_table_cities = '''CREATE TABLE cities(
id INTEGER PRIMARY KEY AUROINCREMENT,
title TEXT NOT NULL,
area FLOAT DEFAULT 0,
country_id INTEGER, 
FOREIGN KEY (country_id) REFERENCES countries(id)
)'''
create_table_employees = '''CREATE TABLE employees(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
city_id INTEGER,
FOREIGN KEY (city_id) REFERENCES cities(id)
)'''

connection = create_connection(database)
create_table(connection, create_table_countries)
create_table(connection, create_table_cities)
create_table(connection, create_table_employees)
# create_country(connection, ('Kyrgyzstan'))
create_city(connection, ('Bishkek', 127, 1))
# ('Osh', 128, 1),
# ('Almaty', 217, 2),
# ('Nur-sultan', 298, 2),
# ('Ankara', 300, 3),
# ('Izmir', 286, 3),
# ('Naryn', 95, 1))
create_employee(connection, ('Artem', 'Kim', 1))
# ('Max', 'Artemov', 2),
# ('Viktor', 'Sidirov', 1),
# ('Petr', 'Petrov', 3),
# ('Anton', 'Antonov', 2),
# ('Vladimir', 'Vladimirov',1)
# ('Betul', 'Yildiz', 1),
# ('Burhan', 'Inandi', 2),
# ('Leyla', 'Alieva', 3),
# ('Andrii', 'Bilenkyi', 2),
# ('Alim', 'Vindiza', 1),
# ('Azamat', 'Botoev', 2),
# ('Alihan', 'Niiazov', 3),
# ('Olga', 'Li', 2),
# ('Polina', 'Pogadayeva', 3),
# ('Aslan', 'Matyanyu', 1)

def employees_in_city_id():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    city_id = int(input('Вы можете посмотреть затрудников, выход == 0:'))
    for city in cities:
        print(city[0], city[1])
        if city_id == 0:
            break
        cursor.execute("SELECT employees.first_name, employees.last_name, coutries.title, cities.title FROM employess"
                       "JOIN cities ON employees.city_id=cities_id JOIN countries ON cities.country_id=coutries_id "
                       "WHERE cities_id=?, (city_id,)"
                       )
        employees = cursor.fetchall()
        for employee in employees:
            print(employee[0], employees[1], employee[2])


employees_in_city_id()