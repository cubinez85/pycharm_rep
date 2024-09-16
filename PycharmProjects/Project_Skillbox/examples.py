# num_1 = 5
# num_2 = 6
# res = num_1 + num_2
# print(res)

# def add(a, b):
#     result = a + b
#     return result
# add(num_1, num_2)


# def add(a, b):
#     result = a + b
#     return result
# print(add(1, 4))

# message = "Hello"
# user = 'cubinez85'
# message + ', ' + user
# print(message, user)

# users_list = []
# users_list.append('skillfactory@example.com')
# users_list.append('johndoe@example.com')
# users_list.append('vasia@mail.ru')
#
# print(len(users_list))


# def average(x,y):
#     return (x+y)/2
# c = average(4,8)
# print(c)

# def greeting(name):
# 	return "<h1> Привет, " + name + "! </h1>"
#
# greeting_first = greeting("cubinez85")
# print(greeting_first)


# def uppercase(func):                  # получение функции как аргумента
# 	def wrapper(name):            # вложенная функция-обёртка
#     	    return func(name).upper() # изменение поведения
# 	return wrapper                # возврат функции в обёртке
#
# @uppercase                  # добавление декоратора к изменяемой функции
# def greeting(name):
# 	return "<h1> Привет, " + name + "! </h1>"
#
# greeting_first = greeting("cubinez85")
# print(greeting_first)


# list_cars = ['toyota', 'volvo']
# print(len(list_cars))

# users_list = []
# users_list.append('skillfactory@example.com')
# users_list.append('johndoe@example.com')
# users_list.append('vasia@mail.ru')
#
# print(len(users_list))



# users_list = []

# class User:
#
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password

# user1 = User(login="user@mail.ru", password="1234")
# user2 = User(login="user@yandex.ru", password="qwerty")
# user3 = User(login="user@gmail.com", password="12qw")
#
# users_list.append(user1)
# users_list.append(user2)
# users_list.append(user3)
#
# for user in users_list:
#     print(user.login)


# users_list = []
#
# class User:
#
#     def __init__(self, greeting):
#         self.greeting = greeting
#
# user1 = User(greeting="Hello user1")
# user2 = User(greeting="Hello user2")
# user3 = User(greeting="Hello user3")
#
# users_list.append(user1)
# # users_list.append(user2)
# # users_list.append(user3)
#
# for user in users_list:
#     print(user1.greeting)


class User:
    def __init__(self, password):
        self.password = password
user_1 = User(password="user_1_passwd")
user_2 = User(password="user_2_passwd")
user_3 = User(password="user_3_passwd")
if user_1.password == 'user_1_passwd':
        print('Hello user_1')
elif user_2.password == 'user_2_passwd':
    print('Hello user_2')

elif user_3.password == 'user_3_passwd':
    print('Hello user_3')

else:
        print('Доступ запрещен')
