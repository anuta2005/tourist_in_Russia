'''Задание:
Python, SQLite
Не меньше 10 записей
Не менее 7 столбцов
Без макроопераций(не вставлять сразу 10 добавлений, 10 удалений, 10 …)
По 4/5 обновление, удаление, 10 добавлений
'''

def create_new_note(new_city_name, new_date, new_population, new_time, new_region, new_sight, new_max_temp, new_min_temp):
    connection = sq.connect('data_base_1.db')
    cursor = connection.cursor()
    new_city_n = (new_city_name, new_date, new_population, new_time, new_region, new_sight, new_max_temp, new_min_temp)
    request_to_insert_data = '''INSERT INTO cities(name, date, \
                              population, time_zone, region, sight, \
                              max_temp, min_temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''

    cursor.execute(request_to_insert_data, new_city_n)
    connection.commit()
    cursor.close()
    connection.close()

def show_all():
    connection = sq.connect('data_base_1.db')
    cursor = connection.cursor()
    request_to_read_data = "SELECT * FROM cities"
    cursor.execute(request_to_read_data)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def delete_city(number_of_city):
    connection = sq.connect('data_base_1.db')
    cursor = connection.cursor()
    city_id_to_delete = number_of_city
    request_to_delete_data = "DELETE FROM cities WHERE city_id = ?"
    cursor.execute(request_to_delete_data, (city_id_to_delete,))
    connection.commit()
    cursor.close()
    connection.close()

def update_indexes():
    connection = sq.connect('data_base_1.db')
    cursor = connection.cursor()
    request_to_read_data_5 = '''SELECT city_id FROM cities'''
    cursor.execute(request_to_read_data_5)
    id_cities = cursor.fetchall()
    for city_id_to_update_new in range(1, len(id_cities) + 1):
        request_to_update_new = '''UPDATE cities SET city_id = ? WHERE city_id = ?'''
        cursor.execute(request_to_update_new, (city_id_to_update_new, id_cities[city_id_to_update_new - 1][0]))
        connection.commit()
    cursor.close()
    connection.close()

def update_city(new_date, new_population, new_time, new_region, new_sight, new_max_temp, new_min_temp, city_id_to_update):
    connection = sq.connect('data_base_1.db')
    cursor = connection.cursor()
    request_to_update_1 = '''UPDATE cities SET date = ?, population = ?, time_zone = ?, region = ?, 
    sight = ?, max_temp = ?, min_temp = ? WHERE city_id = ?'''
    cursor.execute(request_to_update_1, (new_date, new_population, new_time, new_region, new_sight,
                                         new_max_temp, new_min_temp, city_id_to_update))
    connection.commit()
    cursor.close()
    connection.close()

import sqlite3 as sq
connection = sq.connect('data_base_1.db')
cursor = connection.cursor()
# id
# название города
# дата основания
# население
# часовой пояс
# регион
# достопримечательность
# максимальная температура
# минимальная температура
cities_tb = '''
CREATE TABLE IF NOT EXISTS cities(
city_id INTEGER PRIMARY KEY AUTOINCREMENT,  
name TEXT NOT NULL,
date TEXT, 
population INTEGER CHECK(population > 0), 
time_zone TEXT, 
region TEXT, 
sight TEXT, 
max_temp INTEGER, 
min_temp INTEGER
)'''


cursor.execute(cities_tb)
connection.commit()

# cursor.execute("ALTER TABLE cities city_id PRIMARY KEY")
# connection.commit()

# cursor.execute("ALTER TABLE cities ALTER COLUMN city_id INTEGER", 12)
# connection.commit

connection.commit()

request_to_read_data = "SELECT * FROM cities"
cursor.execute(request_to_read_data)
data = cursor.fetchall()

print("START TABLE:")
for row in data:
    print(row)



new_city = ('Москва', '1147', 13149000, '+3',
'Москва', 'Красная Площадь', 38.2, -41.3)
request_to_insert_data = '''
INSERT INTO cities(name, date, population, \
time_zone, region, sight, max_temp, min_temp) 
VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
# cursor.execute(request_to_insert_data, new_city)
# connection.commit()

request_to_read_data = "SELECT * FROM cities"
# cursor.execute(request_to_read_data)
# data = cursor.fetchall()

for row in data:
    print(row)

product_id_to_delete = 4
request_to_delete_data = "DELETE FROM cities WHERE city_id = ?"
# cursor.execute(request_to_delete_data, (product_id_to_delete,))

product_id_to_delete_1 = 3
request_to_delete_data_1 = "DELETE FROM cities WHERE city_id = ?"
# cursor.execute(request_to_delete_data_1, (product_id_to_delete_1,))

product_id_to_delete_2 = 2
request_to_delete_data_2 = "DELETE FROM cities WHERE city_id = ?"
# cursor.execute(request_to_delete_data_2, (product_id_to_delete_2, ))

city_id_to_delete = 2
request_to_delete_3 = "DELETE FROM cities WHERE city_id = ?"
# cursor.execute(request_to_delete_3, (city_id_to_delete, ))
# connection.commit()

new_city_1 = ('Санкт-Петербург', '1703', 5597763,
              '+3', 'Санкт-Петербург', 'Дворцовая Площадь', 37.1, -41)
request_to_insert_data = '''INSERT INTO cities(name, date, \
                          population, time_zone, region, sight, \
                          max_temp, min_temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''

# cursor.execute(request_to_insert_data, new_city_1)
# connection.commit()

new_city_2 = ('Казань', 1318604,
              '+3', 'Руспублика Татарстан', 'Казанский кремль', 39.0, -46.8)
request_to_insert_data_2 = '''INSERT INTO cities(name, population, time_zone, 
            region, sight, max_temp, min_temp) VALUES(?, ?, ?, ?, ?, ?, ?)'''
# cursor.execute(request_to_insert_data_2, new_city_2)
# connection.commit()

request_to_read_data_3 = '''SELECT * FROM cities'''
# cursor.execute(request_to_read_data_3)
data = cursor.fetchall()
for row in data:
    print(row)

new_city_3 = ('Пятигорск', '1780',
              '+3', 'Ставропольский край', 'Провал', 40.0, -33)

request_to_insert_data_3 = '''INSERT INTO cities(name, date, time_zone, 
            region, sight, max_temp, min_temp) VALUES(?, ?, ?, ?, ?, ?, ?)'''
# cursor.execute(request_to_insert_data_3, new_city_3)
# connection.commit()

new_city_4 = ('Набережные Челны', '1626', 545750,
              '+3', 'Машиностроительный завод «КАМАЗ»', 26.2, -15)
request_to_insert_data_4 = '''INSERT INTO cities(name, date, population, time_zone, 
            sight, max_temp, min_temp) VALUES(?, ?, ?, ?, ?, ?, ?)'''
# cursor.execute(request_to_insert_data_4, new_city_4)
# connection.commit()

new_city_5 = ('Новосибирск', '1893', 1633851,
              '+7', 'Музей мировой погребальной культуры', 40.0, -51)
request_to_insert_data_5 = '''INSERT INTO cities(name, date, population, time_zone, 
            sight, max_temp, min_temp) VALUES(?, ?, ?, ?, ?, ?, ?)'''
# cursor.execute(request_to_insert_data_5, new_city_5)
# connection.commit()

new_city_6 = ('Йошкар-Ола', '1584', 274715,
              '+3', 'Республика Марий Эл', 'Заповедник «Большая Кокшага»', 40.0, -47)
request_to_insert_data_6 = '''INSERT INTO cities(name, date, population, time_zone, 
            region, sight, max_temp, min_temp) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
# cursor.execute(request_to_insert_data_6, new_city_6)
# connection.commit()


request_to_read_data_4 = """SELECT * FROM cities"""
# cursor.execute(request_to_read_data_4)
data = cursor.fetchall()
for row in data:
    print(row)
new_city_7 = ('Липецк', 485260,
              '+3', 'Липецкая область', 'Быханов Сад', 34.9, -30.4)
request_to_insert_data_7 = '''INSERT INTO cities(name, population, time_zone, 
            region, sight, max_temp, min_temp) VALUES(?, ?, ?, ?, ?, ?, ?)'''
# cursor.execute(request_to_insert_data_7, new_city_7)
# connection.commit()

new_city_8 = ('Кострома', '1152', 265761,
              '+3', 'Костромская область', 'Пожарная каланча', 32, -50)
request_to_insert_data_8 = '''INSERT INTO cities(name, date, population, time_zone, 
            region, sight, max_temp, min_temp) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
# cursor.execute(request_to_insert_data_8, new_city_8)
# connection.commit()

new_city_9 = ('Калининград', '1255', 489584,
              '+2', 'Калининградская область', 'Замок Кёнинсберг', 36.5, -33.3)
request_to_insert_data_9 = '''INSERT INTO cities(name, date, population, time_zone, 
            region, sight, max_temp, min_temp) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
# connection.execute(request_to_insert_data_9, new_city_9)
# connection.commit()

new_city_10 = ('Иркутск', '1661', 606369,
              '+8', 'Иркутская область', 'Иркутский музей декабристов', 42.8, -14)
request_to_insert_data_10 = '''INSERT INTO cities(name, date, population, time_zone, 
            region, sight, max_temp, min_temp) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
# cursor.execute(request_to_insert_data_10, new_city_10)
# connection.commit()

city_id_to_delete_4 = 7
request_to_delete_4 = "DELETE FROM cities WHERE city_id = ?"
# cursor.execute(request_to_delete_4, (city_id_to_delete_4, ))
# connection.commit()

city_id_to_delete_5 = 8
request_to_delete_5 = "DELETE FROM cities WHERE city_id = ?"
# cursor.execute(request_to_delete_5, (city_id_to_delete_5, ))
# connection.commit()



# request_to_read_data_5 = "SELECT city_id, name FROM cities"
# cursor.execute(request_to_read_data_5)
# data = cursor.fetchall()
# cities_list = []
# index_to_delete_list = []
# for row in data:
#     if row[1] in cities_list:
#         index_to_delete_list.append(row[0])
#     else:
#         cities_list.append(row[1])
# print(index_to_delete_list)
#
# for index_to_delete in index_to_delete_list:
#     request_to_delete_new = "DELETE FROM cities WHERE city_id = ?"
#     cursor.execute(request_to_delete_new, (index_to_delete,))
#     connection.commit()



new_city_date = 1005
city_id_to_update = 9
request_to_update = '''UPDATE cities SET date = ? WHERE city_id = ?'''
# cursor.execute(request_to_update, (new_city_date, city_id_to_update))
# connection.commit()

new_city_population = 144955
city_id_to_update_1 = 10
request_to_update_1 = '''UPDATE cities SET population = ? WHERE city_id = ?'''
# cursor.execute(request_to_update_1, (new_city_population, city_id_to_update_1))
# connection.commit()

new_city_region = "Республика Татарстан"
city_id_to_update_2 = 5
request_to_update_2 = '''UPDATE cities SET region = ? WHERE city_id = ?'''
#cursor.execute(request_to_update_2, (new_city_region, city_id_to_update_2))
#connection.commit()

new_city_region_1 = "Новосибирская область"
city_id_to_update_3 = 6
request_to_update_3 = '''UPDATE cities SET region = ? WHERE city_id = ?'''
#cursor.execute(request_to_update_3, (new_city_region_1, city_id_to_update_3))
#connection.commit()



new_city_date_1 = "1703"
city_id_to_update_4 = 14
request_to_update_4 = '''UPDATE cities SET date = ? WHERE city_id = ?'''
# cursor.execute(request_to_update_4, (new_city_date_1, city_id_to_update_4))
# connection.commit()

new_city_region_2 = "Липецкая область"
city_id_to_update_5 = 14
request_to_update_5 = '''UPDATE cities SET region = ? WHERE city_id = ?'''
# cursor.execute(request_to_update_5, (new_city_region_2, city_id_to_update_5))
# connection.commit()





request_to_update_new = '''UPDATE cities SET city_id = ? WHERE city_id = ?'''
# cursor.execute(request_to_update_new, (12,26))
# connection.commit()

request_to_update_new = '''UPDATE cities SET city_id = ? WHERE city_id = ?'''
# cursor.execute(request_to_update_new, (13,27))
# connection.commit()

request_to_update_new = '''UPDATE cities SET city_id = ? WHERE city_id = ?'''
# cursor.execute(request_to_update_new, (13,14))
# connection.commit()


request_to_read_data_1 = "SELECT * FROM cities"
cursor.execute(request_to_read_data_1)

print("\nFINAL TABLE:")
data_1 = cursor.fetchall()
for row in data_1:
    print(row)


cursor.close()
connection.close()