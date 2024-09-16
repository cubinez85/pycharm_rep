# i = 0
# while i < 5:
#     print(i)
#     i += 1

# text = 'Winter is coming'
# i = len(text)
# result = ''
# while i > 0:
#     result = result + text[:i]
#     print(result)
#     i -= i

# text = 'code'
# for symbol in text:
#     print(symbol)

# def direct_string(text):
#     result = ''
#     for char in text:
#         result = result + char
#     return result.upper()
# text = 'hello'
# print(direct_string(text))

# def reverse_string(text):
#     result = ''
#     for char in text:
#         result = char + result
#     return result
# text = 'hello'
# print(reverse_string(text))


# def filter_string(text, char):
#     index = 0
#     result = ''
#     for current_char in text:
#         current_char = text[index]
#         if current_char.upper() != char.upper():
#             result = f'{result}{current_char}'
#         index += 1
#     return result
# text = 'hello'
# print(filter_string(text, char='H'))



# def print_table_of_squares(start, end):
#     end = end + 1
#     result = ''
#
#     for i in range(start, end):
#         count = i ** 2
#         result += f'square of {i} is {count}\n'
#     print(result)
#
#
# print_table_of_squares(start=1, end=3)

# def print_table_of_squares(start, end):
#     result = ''
#     for i in range(start, end + 1):
#         list = [f'square of {i} is {i*i} ']
#         result += '\n'.join(list)
#
#     return result
# print(print_table_of_squares(start=1, end=3))


# print_table_of_square = lambda s, e: '\n'.join(f'square of {i} is {i*i}' for i in range(s, e + 1))
#
# print(print_table_of_square(s=1, e=3))

# x = 2
# y = 5
# i = x - 1
# while i < y:
#
#     i += 1
#     print(i)

# def print_table_of_squares(start, end):
#     i = start -1
#     result = ''
#     while i < end:
#         i += 1
#         count = i ** 2
#         result += f'square of {i} is {count}\n'
#     return result
# print(print_table_of_squares(start=1, end=3))


# def replace(text, start, to):
#     return text.replace(start, to)
# print(replace(text='hello', start='he', to='my'))

# def get_hidden_card(card, length=4):
#     return '*' * length + card[-4:]
# print(get_hidden_card(card='1234567812345678'))

# def trim_and_repeat(text, offset=0, repetitions=1):
#
#     return text[offset:] * repetitions
# text = 'python'
# print(trim_and_repeat(text))


# def letter_multiply(text: str, sym: str, num: int) -> str:
#     return text.replace(sym, sym * num)
# text = 'python'
# print(letter_multiply(text, sym='t',num=2 ))

# age = 5
#
# def generate():
#     age = 8
#
# generate()
#
# result = age
# print(result)

# age = 5
#
# def f():
#     age = 10
#     return age + 3
#
# result = f()
# print(result)

# age = 5
#
# def f():
#     return age + 3
# result = f()
# print(result)

# men_count = 10
# women_count = 15
#
#
# def get_people_count():
#     men_count = 5
#     women_count = 5
#     result = men_count + women_count
#     return result
# print(get_people_count())

# men_count = 10
# women_count = 15
#
#
# def get_people_count():
#     men_count = 4
#     print(men_count + women_count)
#
#
# get_people_count()

# def get_age_difference(age1 :int, age2 :int) -> int:
#     count = abs(age1 - age2)
#     return f'The age difference is {count}'
# print(get_age_difference(28, 23))

# def has_upper_case(string):
#
#     return string != string.lower()
#
# print(has_upper_case('hEllo'))

# import string
# def has_special_chars(string):
# def is_strong_password(password):
#     length = len(password)
#
#     return (length > 8 and length < 20 and password != password.lower())
# print(is_strong_password(password='qwertydfghjK12@'))


# def is_leap_year(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
# print(is_leap_year(2017))


# name = 234
# value = name or ''
# print(value)

# def string_or_not(param):
#
#     return isinstance(param, str) and 'yes' or 'no'
# print(string_or_not(False))


# num = 6
# result = num + 1 if num % 2 != 0 else 1 - num
# print(result)


# def normalize_url(addr):
#
#     https = 'https://'
#
#     if addr[:8] == https:
#         return addr
#     elif addr[:7] == 'http://':
#         return f'{https}{addr[8:]}'
#     else:
#         return f'{https}{addr}'
#
# print(normalize_url('yandex.ru'))




















