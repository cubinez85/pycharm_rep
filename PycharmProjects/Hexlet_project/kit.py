# def show_language():
#     print("Python")
#
#
# def say_hello():
#     print("Hello!")
#
#
# def say_bye():
#     print("Bye...")

# from random import randint
# string = 'abcde'
# random_index = randint(0, len(string) - 1)
# char = string[random_index]
# print(char)

# num_rendint = randint(0,2) - 1
# print(num_rendint)

# from random import choice

# string = 'abcde'
# char = choice(string)
# print(char)

# import random
# from random import choice
# def choice_from_range(text, start, end):
#     i = start
#     for i in text:
#         if i <= text[end]:
#             char = choice(text[start:end + 1])
#             return char
# text = "abcdef"
# print(choice_from_range(text, 2, 2))

# def choice_from_range(text, start, end):
#     return text[random.randint(start, end)]
# text = 'abcdef'
# print(choice_from_range(text,2, 2))

# def choice_from_range(text, start, end):
#     return choice(text[start:end + 1])
# text = 'abcdef'
# print(choice_from_range(text, 3, 5))

# def div_mod(a, b):
#     quotient = a // b
#     modulo = a % b
#     return (quotient, modulo)
# print(div_mod(10, 2))

# (a,) = (42,)
# print(a)

# def print_person_info(person):
#     name, age = person # разбираем переданный кортеж
#     return f'{name} is {age} years old'
#
# person_tuple = ('John', 30)
# print(print_person_info(person_tuple))

# name_and_age = ('Bob', 42)
# print(name_and_age[1])
# (name, age) = name_and_age

# def sort_pair(pair):
#     a, b = pair
#     if a <= b:
#         return (a, b)
#     else:
#         return (b, a)
# print(sort_pair((1, 2)))

# def person(a, b):
#     return (a, b)
# print(person(1, 2))


# def is_happy_ticket(string):
#     sum = 0
#     for i in string:
#         if i.isdigit():
#             sum += int(i)
#     return sum
# print(is_happy_ticket('123'))


# string = '123'
# s = sum(map(int, string))
# print(s)

# string = '123'
# sum = 0
# for i in string:
#     if i.isdigit():
#         sum += int(i)
# print(sum)