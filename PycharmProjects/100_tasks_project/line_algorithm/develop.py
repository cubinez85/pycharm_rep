# pupils = input('Количество школьников: ')
# apples = input('Количество яблок: ')
# pupils = int(pupils)
# apples = int(apples)
# apples_on_pupil = apples // pupils
# apples_in_basket = apples % pupils
# print(f'У каждого школьника будет по {apples_on_pupil} яблок')
# print(f'В корзине останется {apples_in_basket} яблок')


# apples = 15
# pupils = 10
# apples_on_pupils = int(apples // pupils)
# apples_in_basket = int(apples % pupils)
# print(apples_on_pupils)
# print(apples_in_basket)

# def apples_count(apples, pupils):
#     apples_on_pupils = int(apples // pupils)
#     apples_in_basket = int(apples % pupils)
#     print(apples_on_pupils)
#     print(apples_in_basket)
# apples_count(15, 10)


# y = chr(67)
# print(y)
# y = ord('a')
# print(y)

# number = input('Какую по счету букву алфавита вывести: ')
# number = int(number)
# first_letter_code = ord('A')
# your_letter_code = first_letter_code + number - 1
# your_letter = chr(your_letter_code)
# print(f'Это буква "{your_letter}"')

# def letter_print(number):
#     # number = int(number)
#     first_letter_code = ord('A')
#     your_letter_code = int(first_letter_code + number - 1)
#     your_letter = chr(your_letter_code)
#     return your_letter
# print(letter_print(12))



# import math
#
# def rectangle_S(a, b):
#     a = float(a)
#     b = float(b)
#     S = (a * b) / 2
#     return round(S, 2)
# print(rectangle_S(5.4, 2.1))
#
# def rectangle_P(a, b):
#     a = float(a)
#     b = float(b)
#     c = math.sqrt(a ** 2 + b ** 2)
#     P = a + b + c
#     return round(P, 2)
# print(rectangle_P(5.4, 2.1))

# a = input('Длина 1 катета равна: ')
# b = input('Длина 2 катета равна: ')
# a = float(a)
# b = float(b)
# c = math.sqrt(a ** 2 + b ** 2)
# S = (a * b) / 2
# P = a + b + c
# print("Площадь треугольника равна: %.2f" % S)
# print(f'Периметр треугольника равен: {round(P, 2)}см')

# from random import randint
# a = input('Нижняя граница: ')
# b = input('Верхняя граница: ')
# a = int(a)
# b = int(b) - 1
# n = randint(a, b)
# print(n)

# from random import randrange
# a = input('Нижняя граница: ')
# b = input('Верхняя граница: ')
# a = int(a)
# b = int(b)
# n = randrange(a, b)
# print(n)

# from random import random
# print(random())

# def f_random(tuple):
#     a, b = tuple
#     for i in range(a, b):
#         if a < b:
#             return randint(a, b)
# print(f_random((2, 6)))
#
# def f_randint():
#     a = 0.10
#     b = 0.50
#     dif = b - a
#     res = a + (random() * dif)
#     return round(res, 2)
# print(f_randint())

# a = input('Граница нижнего диапазона: ')
# b = input('Граница верхнего диапазона: ')
# a = float(a)
# b = float(b)
# dif = b - a
# res = random() * dif + a
# print(round(res, 2))

# def sum_randint():
#     a = 100
#     b = 999
#     res = randint(a, b)
#     d1 = res % 10
#     d3 = res // 100
#     d2 = (res % 100) // 10
#     s = d1 + d2 + d3
#     print('Случайное число: ', res)
#     print('Сумма его цифр: ', s)
# sum_randint()

# a = 999
# d1 = a % 10
# d3 = a // 100
# d2 = a % 100 // 10
# s = d1 + d2 + d3
# print(s)

# n = randint(100, 999)
# print('Случайное число: ', n)
# d1 = n // 100
# d2 = n % 100 // 10
# d3 = n % 10
# print('Сумма его цифр: ',d1 + d2 + d3)


# n = str(randint(100, 999))
# print(n)
# d1 = int(n[0])
# d2 = int(n[1])
# d3 = int(n[2])
# print(d1 + d2 + d3)

# def sum_randint(n):
#     sum = 0
#     for i in n:
#         if i.isdigit():
#             sum += int(i)
#     print(n)
#     print(sum)
# sum_randint(n=str(randint(100, 999)))

# import math
# r = input('Radius = ')
# r = float(r)
# ln = 2 * math.pi * r
# S = math.pi * math.pow(r, 2)
# print("Length = %.2f" % ln)
# print('Area =',round(S, 2))

# import math
# r = float(input('r = '))
# h = float(input('h = '))
# circles = math.pi * math.pow(r, 2) * 2
# side = 2 * math.pi * r * h
# S = circles + side
# print("Area = %.2f" % S)

# y = kx + b
# k = (y1 — y2) / (x1 — x2)
# b = y2 — k * x2
# def f_direct(x1, y1, x2, y2):
#     x1 = float(x1)
#     x2 = float(x2)
#     y1 = float(y1)
#     y2 = float(y2)
#     k = (y1 - y2) / (x1 - x2)
#     b = y2 - k * x2
#     print("y = %.2f * x + %.2f" % (k, b))
#
# f_direct(4.3, -1.2, -8.5, 4)

# print('Координаты точки A(x1; y1):')
# x1 = float(input('\tx1 = '))
# y1 = float(input('\ty1 = '))
# print('Координаты точки B(x2, y2):')
# x2 = float(input('\tx2 = '))
# y2 = float(input('\ty2 = '))
# print('Уравнение прямой, проходящей через эти точки: ')
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k * x2
# print("y = %.2f * x + %.2f" % (k, b))

# a = '101'
# b = '100'
# a = int(a, 2)
# b = int(b, 2)
# bit_or = a | b
# bit_and = a & b
# bit_xor = a ^ b
# print('%10s' % bin(bit_or))
# print('%10s' % bin(bit_and))
# print('%10s' % bin(bit_xor))





# n1 = input('Введите первое двоичное число: ')
# n2 = input('Введите второе двоичное число: ')
# n1 = int(n1, 2)
# n2 = int(n2, 2)
# bit_or = n1 | n2
# bit_and = n1 & n2
# bit_xor = n1 ^ n2
# print('Результат побитового OR: %10s' % bin(bit_or))
# print('Результат побитового AND: %10s' % bin(bit_and))
# print('Результат побитового XOR: %10s' % bin(bit_xor))