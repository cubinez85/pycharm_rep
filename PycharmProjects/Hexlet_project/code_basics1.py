# print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')

# print('Winter' + ' came' + ' for' + ' the' + ' House' + ' of' + ' Frey' + '.')

# print(chr(37))

# motto = 'What Is Dead May Never Die!'
# print(motto)

# euros_count = 100
#
# # BEGIN (write your solution here)
# # euros_per_dollars = 1.25
# # dollars_count = euros_count * euros_per_dollars
# # dollars_per_yuans = 6.91
# # yuans_count = dollars_count * dollars_per_yuans
# # print('100 euros = ' + str(yuans_count) + ' yuans')

# info = "We couldn't verify your mother's maiden name."
# intro = "Here is important information about your account security."
#
# first_name = 'Joffrey'
# greeting = 'Hello'
# print(greeting + ', ' + first_name + '!')
# print(intro + '\n' + info)

# first_num = 20
# second_num = -100
# print(first_num * second_num)

# king = "Rooms in King Balon's Castle:"
# rooms_count = 6 * 17
# print(f'{king}\n{rooms_count}')

# stark = 'Arya'
# print(f'Do you want to eat, {stark}?')

# magic = '\nyou'
# print(magic[1])

# text = '''Lannister, Targaryen, Baratheon, Stark, Tyrell...
# they're all just spokes on a wheel.
# This one's on top, then that one's on top, and on and on it spins,
# crushing those on the ground.'''
# print(text)

# one = 'Naharis'
# two = 'Mormont'
# three = 'Sand'
# print(f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}')

# value = 2.9
# # print(f'{int(value)}' + ' times')
# int_value = int(value)
# str_value = str(int_value)
# print(str_value + ' times')

# company1 = 'Apple'
# company2 = 'Samsung'
# # print(len(company1 + company2))
# company1_len = len(company1)
# company2_len = len(company2)
# print(company1_len + company2_len)

#
# number = 23.34
# print(float.hex(number))

# print(int(1.6))

# number = 10.1234
# result = round(number, 2)
#print(result)
# print(round(number, 2))
#
# text = 'Never forget what you are, for surely the world will not'
# # result = f'''First: {text[0]}
# # Last: {text[-1]}'''
# result = f'First: {text[0]}\nLast: {text[-1]}'
# print(result)


# print(min(3, 10, 22, -3, 0))

from random import random
# result = random() * 10
# print(round(result))
# print(round(random() * 10))

# motto = 'Family, Duty, Honor'
# print(type(motto))

# text = 'a MIND needs Books as a Sword needS a WHETSTONE.'
# print(text.upper())

# x = -4
# print(abs(x))

# name = 'Tirion'
# print(name)

# first_name = '  Grigor   \n'
# print(first_name.strip())

# text = 'Never forget what you are, for surely the world will not'
# print(f'Index Of N: {text.find('N')}\nIndex Of ,: {text.find(',')}')
# print('Index Of N: ' + str(text.find('N')),'\n''Index Of ,: ' + str(text.find(',')))
# print(f'''Index Of N: {text.find('N')}
# Index Of ,: {text.find(',')}''')

# text = 'When \t\n you play a \t\n game of thrones you win or you die.'
# print(text[5:15].strip().__len__())
# print(len(text[5:15].strip()))

# def print_motto():
#     text = 'Winter is coming'
#     print(text)
# print_motto()

# def say_hurray_three_times():
#     return 'hurray! hurray! hurray!'
# hurray = say_hurray_three_times()
#
# print(hurray)

# def say_hurray_three_times():
#     word = 'hurray!'
#     return f'{word} {word} {word}'
# print(say_hurray_three_times())

# def truncate(text, length):
#     return text[:length] + '...'
# print(truncate(text='hexlet', length=3))

# def truncate(text, length):
#     result = f"{text[:length]}..."
#     return result
# print(truncate(text='hexlet', length=3))

# def replace(text='hexlet'):
#     return text.replace('h', 'f')
# print(replace())



# def get_hidden_card(card, length=4):
#     return '*' * len(card[:length]) + card[-4:]
# card = '1234123412341234'
# print(get_hidden_card(card, 3))

# def get_hidden_card(card_number, stars_count=4):
#     visible_digits_line = card_number[-4:]
#     return f"{'*' * stars_count}{visible_digits_line}"

# def trim_and_repeat(text, offset=0, repetitions=1):
#     return text[offset:] * repetitions
# text = "hexlet"
# print(trim_and_repeat(text, 3, 2))


# def trim_and_repeat(text, offset=0, repetitions=1):
#     return f'{text[offset:] * repetitions}'
# text = 'hexlet'
# print(trim_and_repeat(text))

# def  word_multiply(text: str, x: int) -> str:
#     return f'{text * x}'
# text: str = 'hexlet'
# print(word_multiply(text, 2))

# def is_pensioner(age):
#     return age >= 60
# print(is_pensioner(age=59))

# def is_mister(string):
#     return string == 'Mister'
# print(is_mister('Missis'))

# def is_international_phone(num: str) -> str:
#     first_number: str = num[0]
#     return first_number == '+'
# print(is_international_phone(num='234567890'))

# def is_international_phone(phone):
#     return phone[0] == '+'
# print(is_international_phone(phone='+12345678'))

# def is_first_letter_an_a(string):
#     first_letter = string[0]
#     return first_letter == 'a'
# print(is_first_letter_an_a(string='apple'))



