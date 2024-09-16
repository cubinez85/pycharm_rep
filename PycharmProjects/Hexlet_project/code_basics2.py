# def is_good_apartment(area, street):
#   return area >= 100 or (area >= 80 and street == 'Main Street')
# print(is_good_apartment(area=56, street='ertyu'))

# def is_leap_year(year):
#   return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
# print(is_leap_year(year=2012))

# def is_palindrome(word):
#   reversed_word = word[::-1]
#   return reversed_word.lower() == word.lower()
# print(is_palindrome(word='Шалаш'))

# import sys
# sys.setrecursionlimit(3000)
# def has_capital_letter(string):
#
#   def is_correct_password(password):
#      length = len(password)
#      return length > 8 and has_capital_letter(password)
#
#   print(is_correct_password('Qwerty'))
# has_capital_letter(string='Qwerty')

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(2000))
# def outer_func():
#     def inner_func():
#         print("Hello, World!")
#     inner_func()
# outer_func()

# def is_not_palindrome(word):
#   reversed_word = word[::-1]
#   return reversed_word.lower() != word.lower()
#
#   def is_palindrome(word):
#     reversed_word = word[::-1]
#     return reversed_word.lower() == word.lower()
#   print(is_palindrome(word='Шалаш'))
# print(not is_not_palindrome(word='Шала'))

# def is_palindrome(word):
#   lower_word = word.lower()
#   return lower_word == lower_word[::-1]
# print(is_palindrome(word='Exe'))
#
#
# def is_not_palindrome(word):
#   return not is_palindrome(word)
# print(is_not_palindrome(word='Exe'))

# def outer_func(text):
#     return text
#
# def inner_func(text):
#     return outer_func(text)
# print(inner_func(text='hexlet'))

# def outer_func():
#     def inner_func(text):
#         return text
#     print(inner_func(text='hexlet'))
# outer_func()

# number = 10
# result = number % 2 == 0 and 'yes' or 'no'
# print(result)

# print(0 or 42 and "False" or '')

# def test(value):
#     return value == 'first' or value == 'second'
# print(test(value='first'))

# def string_or_not(value):
#     result = str(value)
#     return value == result and 'yes' or 'no'
# print(string_or_not(value='hexlet'))
# print(isinstance(2, str))

# def string_or_not(value):
#     return isinstance(value, str) and 'yes' or 'no'
# print(string_or_not(value=3))
# print(isinstance('hexlet', str))


# x = 2
# print(isinstance(x, str))

# def guess_number(var):
#     if var == 42:
#         return 'You win!'
#     return 'Try again!'
# print(guess_number(var=40))

# def normalize_url(addr):
#     var = addr[:7]
#     var2 = addr[:8]
#     if var == 'http://':
#         return 'https://' + addr[7:]
#     else:
#         if var2 == 'https://':
#             return 'https://' + addr[8:]
#         else:
#             if var2 != 'https://':
#                 return 'https://' + addr
#
# print(normalize_url(addr='yandex.ru'))

# def normalize_url(url):
#     prefix = 'https://'
#     if url[:8] == prefix:
#         return url
#     else:
#         if url[:7] == 'http://':
#             return prefix + url[7:]
#         else:
#             return prefix + url
# print(normalize_url(url='cubinez.ru'))


# number = 11
#
# if number > 10:
#     print("Number is greater than 10")
# else:
#     if number == 10:
#         print("Number is exactly 10")
#     else:
#         print("Number is less than 10")


# def get_type_of_sentence(sentence):
#     last_char = sentence[-1]
#
#     if last_char != '?':
#         sentence_type = 'normal'
#     else:
#         sentence_type = 'question'
#
#     return "Sentence is " + sentence_type
# print(get_type_of_sentence(sentence='winter is comming'))

# def who_is_this_house_to_starks(family):
#     if family == 'Karstark' or family == 'Tully':
#         return 'friend'
#     elif family == 'Lannister' or family == 'Frey':
#         return 'enemy'
#     else:
#         return 'neutral'
#
# print(who_is_this_house_to_starks(family='Bob'))


# def abs(number):
#     if number >= 0:
#         return number
#     return -number
# print(abs(number=-1))

# def flip_flop(text):
#     if text == 'flip':
#         return 'flop'
#     elif text == 'flop':
#         return 'flip'
# print(flip_flop(text='flip'))

# def get_type_of_sentence(sentence):
#     last_char = sentence[-1]
#     return 'question' if last_char == '?' else 'normal'
# print(get_type_of_sentence(sentence='hexlet'))r

# def flip_flop(text):
#     return 'flip' if text == 'flop' else 'flop'
# print(flip_flop(text='flop'))

# def test(status):
#     if status == 'paid':
#         return 'normal'
#     elif status == 'new':
#         return 'ok'
#     elif status == 'stop':
#         return 'bad'
#     else:
#         return 'crush'
#
# print(test(status='start'))

# def test(status):
#     match status:
#         case 'paid':
#             return 'normal'
#         case 'new':
#             return 'ok'
#         case 'stop':
#             return 'bad'
#         case _:
#             return 'crush'
# print(test(status='start'))

# def test(status):
#     result = ''
#     match status:
#         case 1:
#             result = 'paid'
#         case 2:
#             result = 'new'
#         case 3:
#             result = 'stop'
#         case _:
#             result = 'crush'
#     return result
#
# print(test(status=1))

# def test(status):
#     match status:
#         case 1:
#             return "paid"
#         case 2:
#             return 'new'
#         case 3:
#             return 'stop'
#         case _:
#             return 'crush'
# print(test(status=3))

# def get_number_explanation(num):
#     match num:
#         case 666:
#             return 'devil number'
#         case 42:
#             return 'answer for everything'
#         case 7:
#             return 'prime number'
#         case _:
#             return 'just a number'
# print(get_number_explanation(num=7))













