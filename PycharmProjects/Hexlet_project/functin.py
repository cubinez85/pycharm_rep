# def show_greeting():
#     text = 'Hello Hexlet!'
#     print(text)
# show_greeting()

# def noop():
#     pass
#
# noop()

# def print_motto():
#     text = 'Winter is coming'
#     print(text)
# print_motto()

# def save_email():
#     email = ' CuBINez85@MAIl.RU  '
#     print(email.strip().lower())
# # save_email()

# def save_email():
#     email = ' CuBINez85@MAIl.RU  '
#     trimmed_email = email.strip()
#     prepared_email = trimmed_email.lower()
#     print(prepared_email)

# def greeting():
#     return 'Hello Hexlet!'
# message = greeting()
# # print(message.upper())
#
# def greeting_with_return_and_printing():
#     print('Я появлюсь в консоли')
#     return 'Hello, Hexlet!'
# message = greeting_with_return_and_printing()

# def greeting():
#     message = 'Hello, Hexlet!'
#     return message
# print(greeting())

# def run():
#     return 5
#     return 10
#
#
# # Что будет выведено на экран?
# print(run())

# def multiply():
#    return 2 * 3
#
#
# result = multiply()
#
# print(result)

# def multiply():
#     print(2 * 3)
#
#
# multiply()

# def say_hurray_three_times():
#     return 'hurray! hurray! hurray!'
# result = say_hurray_three_times()
# print(result)

# def get_last_char(string):
#     return string[-1]
# text = 'Winter is coming'
#
# print(get_last_char(string=text).strip())

# def count(round):
#     return round
# var = round(10.23456, 3)
# print(count(round=var))

# def print_question(word):
#     return word + '!'
# print(print_question(word='hello'))

# def print_question(text):
#     print(text + '?')

# def print_question(word):
#  print(word + '?')

# def print_question(text):
#     return text
# print(print_question(text='hello'))

# def sum(a, b):
#  result = a + b
#  return result
# print(sum(a=1, b=2))

# def truncate(text, length):
#     return text[:length]+('...')
# print(truncate('text', 2))

# def pow(x, base=2):
#     return x ** base
# print(pow(3, 4))

# def my_print(text):
#     return text
# print(my_print(text='Hexlet'.upper()))

# def sum(x, a=2, b=3, c=4):
#     return x + a + b + c
# print(sum(x=5))

# max(1, 2, 3)
# #     return 1, 2, 3
# print(max(1, 2, 3))

# def multiply_two(multiplier=2):
#     print(2 * multiplier)
#
#
# multiply_

# def get_hidden_card(y="*" * 4, x='2034399002125581'):
#     return y + x[12:]
# print(get_hidden_card())

# def card_hide(card):
#     return '*' * len(card[:-4]) + card[-4:]
# card = '1234123412341234'
# print(card_hide(card))

# def get_hidden_card(card, length=4):
#     return '*' * len(card[:length]) + card[-4:]
#
# print(get_hidden_card('1234123412341234'))

# def get_hidden_card(card):
#     return card
# number = 4
# var = '1234123412341234'
# card = "*" * number + var[12:]
# print(get_hidden_card(card))

# def truncate(text, length):
#     return text[:length]+('...')
# print(truncate('text', 4))

# def truncate(text, length):
#     return text[:length]
# text = 'My text'
# print(truncate(text, 2))

# def truncate(text='My text', length=2):
#     return text[:length]
#
# print(truncate())

# def print_params(a=1, b=2, c=None, d=4):
#     return a, b, c, d
# print(print_params(d=8))

# def print_param(a, b=4):
#     return a, b
# print(print_param(a=3))

# def trim_and_repeat(text, offset=0, repetitions=1):
#     return text[offset:] * repetitions
# text = 'python'
#
# print(trim_and_repeat(text, offset=3, repetitions=2))

