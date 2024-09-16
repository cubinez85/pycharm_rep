# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Создаем таблицу tree_sport
# cursor.execute('''
# create table tree_hexlet (
#   id integer,
#   parent integer,
#   name text,
#
#   primary key (id),
#   foreign key (parent) references tree_hexlet(id)
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
# cursor.execute(
#     'INSERT INTO tree (parent, ФИО, Должность, Дата_приема_на_работу, Заработная_плата) VALUES ( ?, ?, ?, ?, ?)',
#     ('null', 'Зубов Егор Васильевич', 'Генеральный директор', '12.03.2012', '80000р45к')
# )
#
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()


# import sqlite3
#
# # Создаем подключение к базе данных (файл my_database.db будет создан)
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
# cursor.execute('SELECT * FROM tree_hexlet where id in (1, 2, 3, 8, 9, 14, 15, 20, 21, 26, 27)')
# users = cursor.fetchall()
#
# # Выводим результаты
# for user in users:
#   print(user)
#
# # Сохраняем изменения и закрываем соединение
# connection.close()

# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy import insert
# from sqlalchemy.orm import Session
# from sqlalchemy import ForeignKey
# from sqlalchemy import update
#
# engine = create_engine("sqlite+pysqlite:///my_database.db", echo=True)
#
# class Base(DeclarativeBase): pass
#
# class Person(Base):
#     __tablename__ = "data"
#     id = Column(Integer, primary_key=True, index=True)
#     parent = Column(Integer, ForeignKey("data.id"), nullable=True)
#     name = Column(String(128), nullable=False)
#
# Base.metadata.create_all(bind=engine)
#
# with Session(engine) as session:
#     session.execute(
#         update(Person),
#         [
#             {'id': 1, 'parent': 'null', 'name': 'Пупкин Василь Василич'},
#             {'id': 2, 'parent': 1, 'name': 'Хохлов Артём Вадимович'},
#             {'id': 3, 'parent': 2, 'name': 'Прокофьева Полина Всеволодовна'},
#             {'id': 4, 'parent': 2, 'name': 'Попова Елизавета Кирилловна'},
#             {'id': 5, 'parent': 2, 'name': 'Лыков Максим Артёмович'},
#             {'id': 6, 'parent': 2, 'name': 'Исаков Даниил Матвеевич'}
#
#
#
#         ],
#     )
#     session.commit()

# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Обновляем возраст пользователя "newuser"
# cursor.execute('UPDATE tree2 SET parent = ? WHERE id = ?', (2, 13))
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()

# myTree = ['a', ['b', ['d',['hello'],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
# print('left subtree = ', myTree[1])
# print('root = ', myTree[0])
# print('right subtree = ', myTree[2])
# def BinaryTree(r):
#     return [r, [], []]
# print(BinaryTree(r=myTree[0]))



# class Tree:
#     def __init__(self, cargo, left=None, right=None):
#         self.cargo = cargo
#         self.left  = left
#         self.right = right
#
#     def __str__(self):
#         return str(self.cargo)
#
#
# left = Tree(2)
# right = Tree(3)
# tree = Tree(1, left, right)

# print(tree)


# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Создаем таблицу tree_sport
# cursor.execute('''
# create table tree (
#   id integer,
#   parent integer,
#   ФИО text,
#   Должность text,
#   Дата_приема_на_работу text,
#   Заработная_плата text,
#
#   primary key (id),
#   foreign key (parent) references tree(id)
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
# cursor.execute('drop table tree_hexlet')
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
# cursor.execute('UPDATE tree SET Должность = ? WHERE id = ?', ('Директор', 1))
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
# cursor.execute(
#     'INSERT INTO tree (parent, ФИО, Должность, Дата_приема_на_работу, Заработная_плата) VALUES ( ?, ?, ?, ?, ?)',
#     (3, 'Бабушкин Матвей Макарович', 'водитель', '04.03.2020', '33000р')
# )


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
# cursor.execute('DELETE FROM tree WHERE id = ?', (2,))
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()