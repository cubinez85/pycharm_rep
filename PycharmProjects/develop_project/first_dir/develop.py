# text = 'hello,world'
# var = text.split(',')
# for i in var:
#     print(i)
#
# def f():
#     text = 'hello,world'
#     var = text.split(',')
#     for i in var:
#         return i
#     return
# print(f())

# def f():
#     text = "hello,world,ura"
#     return text.split(",")
# for i in f():
#     print(i)

# a = [
#         [93.400000000000006, "high"],
#         [98.600000000000009, 99.0, "high"],
#         [111.60000000000001, 112.5, "high"]
# ]
#
# with open('sample.txt', 'a') as outfile:
#     for sublist in a:
#         outfile.write('{}\n'.format(sublist))
#         print(sublist)

# import sqlite3
#
# # Создаем подключение к базе данных (файл my_database.db будет создан)
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()
#
# # Выводим результаты
# for user in users:
#   print(user)
#
# # Сохраняем изменения и закрываем соединение
# connection.close()



# from sqlalchemy import create_engine
# from sqlalchemy import text
#
# engine = create_engine("sqlite+pysqlite:///my_database.db", echo=True)
#
# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE IF NOT EXISTS some_table (x int, y int)"))
#     # conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),[{"x": 6, "y": 8}, {"x": 9, "y": 10}],)
#     conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [{"x": 11, "y": 12}, {"x": 13, "y": 14}], )
#     conn.commit()
#     result = conn.execute(text("SELECT x, y FROM some_table"))
#     for row in result:
#         print(f'x: {row.x}  y: {row.y}')
    # print(result.fetchall())


# from sqlalchemy import create_engine
# from sqlalchemy import MetaData
# from sqlalchemy import Table, Column, Integer, String
# from sqlalchemy import ForeignKey
# engine = create_engine("sqlite+pysqlite:///my_database.db", echo=True)
# metadata_obj = MetaData()
#
# user_table = Table(
#     "user_account",
#      metadata_obj,
# Column("id", Integer, primary_key=True),
#       Column("name", String(30)),
#       Column("fullname", String),
# )
#
# address_table = Table(
#      "address",
#      metadata_obj,
#      Column("id", Integer, primary_key=True),
#      Column("user_id", ForeignKey("user_account.id"), nullable=False),
#      Column("email_address", String, nullable=False),
# )
# metadata_obj.create_all(engine)



# from sqlalchemy import create_engine
# from sqlalchemy import  Column, Integer, String
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy import insert
#
# engine = create_engine("sqlite+pysqlite:///my_database.db", echo=True)
#
# class Base(DeclarativeBase): pass
#
# class Person(Base):
#     __tablename__ = "people"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(64), unique=True, index=True)
#     age = Column(String(128))
#
# Base.metadata.create_all(bind=engine)
#
# stmt = insert(Person).values(name='Petr', age='23')
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()
#     # print(result)

#
# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy import insert
# from sqlalchemy import text
# from sqlalchemy.orm import Session
#
# engine = create_engine("sqlite+pysqlite:///my_database.db", echo=True)
#
# class Base(DeclarativeBase): pass
#
# class Person(Base):
#     __tablename__ = "people"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(64), unique=True, index=True)
#     age = Column(String(128))
#
# Base.metadata.create_all(bind=engine)
#
# with Session(engine) as session:
#     session.execute(
#         insert(Person),
#         [
#             {'name': 'qweerty', 'age': '34'},
#             {'name': 'werty', 'age': '45'}
#
#         ],
#     )
#     session.commit()


# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy import insert
# from sqlalchemy import text
# from sqlalchemy.orm import Session
#
# engine = create_engine("sqlite+pysqlite:///my_database.db", echo=True)
#
# class Base(DeclarativeBase): pass
#
# class Person(Base):
#     __tablename__ = "people"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(64), unique=True, index=True)
#     age = Column(String(128))
#
# Base.metadata.create_all(bind=engine)
#
# with engine.connect() as conn:
#     conn.execute(
#         text('INSERT INTO people (name, age) VALUES (:name, :age)'),
#         [{'name': 'QWER', 'age': '23'},
#          {'name': 'dfg', 'age': '24'}
#
#         ],
#     )
#     conn.commit()


# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Удаляем пользователя "newuser"
# cursor.execute('drop table test_table')
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()


# import sqlite3;
#
# con = sqlite3.connect("my_database.db")
# cursor = con.cursor()
#
# # данные для добавления
# people = [("Bob", 23), ("Jon", 34), ("Elise", 32)]
# cursor.executemany("INSERT INTO people (name, age) VALUES (?, ?)", people)
#
# con.commit()

# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Создаем таблицу tree_sport
# cursor.execute('''
# create table data (
#   id integer,
#   tree_id integer,
#   data text,
#
#   primary key (id),
#   foreign key (tree_id) references tree(id)
#     on update cascade on delete cascade
# )
# ''')
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()


# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Добавляем нового пользователя
# cursor.execute('INSERT INTO data (tree_id, data) VALUES ( ?, ?)', ( 2, 'пилот'))
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()

# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Удаляем пользователя "newuser"
# cursor.execute('DELETE FROM data WHERE id = ?', (13,))
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()

# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Обновляем возраст пользователя "newuser"
# cursor.execute('UPDATE data SET tree_id = ? WHERE id = ?', ('null', 23))
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()

# import sqlite3
#
# # Создаем подключение к базе данных (файл my_database.db будет создан)
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
# cursor.execute('SELECT * FROM tree union all select * from data')
# users = cursor.fetchall()
#
# # Выводим результаты
# for user in users:
#   print(user)
#
# # Сохраняем изменения и закрываем соединение
# connection.close()

# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Обновляем возраст пользователя "newuser"
# cursor.execute('drop table people')
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()

