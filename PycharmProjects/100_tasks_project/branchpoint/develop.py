# x = float(input('Введите значение x: '))
# if x > 0:
#     y = x - 0.5
# elif x < 0:
#     y = abs(x)
# else:
#     y = 0
# print('%.2f' % y)

# def f_equal(x):
#     if x > 0:
#         y = x - 0.5
#     elif x < 0:
#         y = abs(x)
#     elif x == 0:
#         y = 0
#     print('%.2f' % y)
# f_equal(2.34)


# print('m - масса, d - плотность, v - объем')
# flag = input('Что вычислить: ')
# if flag == 'm':
#     d = float(input('Плотность: '))
#     v = float(input('Объем: '))
#     print('Масса равна: %.2f' % (d * v))
# elif flag == 'd':
#     m = float(input('Масса: '))
#     v = float(input('Объем: '))
#     print('Плотность равна: %.2f' % (m / v ))
# elif flag == 'v':
#     m = float(input('Масса: '))
#     d = float(input('Плотность: '))
#     print('Объем равен: %.2f' % (m / d))

# figure = input('Выберите фигуру (1 - прямоугольник, 2 - треугольник, 3 - круг): ')
# if figure == '1':
#     print('Длины сторон прямоугольника: ')
#     a = float(input('a = '))
#     b = float(input('b = '))
#     print('Area: %.2f' % (a * b))
# if figure == '2':
#     a = float(input('a = '))
#     b = float(input('b = '))
#     c = float(input('c = '))
#     p = (a + b + c) / 2
#     import math
#     print('Area: %.2f' % math.sqrt(p * (p - a) * (p - b) * (p - c)))
# if figure == '3':
#     r = float(input('r = '))
#     import math
#     print('Area: %.2f' % (math.pi * r ** 2))

# print('Введите значения предполагаемого треугольника: ')
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# flag = ''
# if a + b >= c:
#     if b + c >= a:
#         if a + c >= b:
#             print('Треугольник существует')
#         else:
#             flag = 'a'
#     else:
#         flag = 'b'
# else:
#     flag = 'c'
# if flag != '':
#     print('Треугольник НЕ существует')
#     print(f'Сторона "{flag}" длиннее двух других')

# import math
# print('Введите координаты точки и радиуса круга :')
# x_point = float(input('x = '))
# y_point = float(input('y = '))
# r_circle = float(input('R = '))
# hypotenuse = math.sqrt(x_point ** 2 + y_point **2)
# if hypotenuse <= r_circle:
#     print('Точка принадлежит кругу')
# else:
#     print('Точка НЕ принадлежит кругу')

# print('Введите значения чисел "a" и "b" :')
# a = float(input('a = '))
# b = float(input('b = '))
# print('Выберите арифметическую операцию: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление')
# flag = input('')
# if flag == '1':
#     print(a + b)
# elif flag == '2':
#     print(a - b)
# elif flag == '3':
#     print('%.2f' % (a * b))
# else:
#     if b != 0:
#         print('%.2f' % (a / b))
#     else:
#         print('Ошибка')

# s = input('Знак (+, -, *, /): ')
# if s in ('+', '-', '*', '/'):
#     a = float(input('a = '))
#     b = float(input('b = '))
#     match s:
#         case '+':
#             print('%.2f' % (a + b))
#         case '-':
#             print('%.2f' % (a - b))
#         case '*':
#             print('%.2f' % (a * b))
#         case'/':
#             if b != 0:
#                 print('%.2f' % (a / b))
#             else:
#                 print('Деление на 0!')
# else:
#     print('Неверный знак операции')

# year = int(input())
# if year % 4 != 0:
#     print('Обычный')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('Високосный')
#     else:
#         print('Обычный')
# else:
#     print('Високосный')

# def is_leap_year(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
# print(is_leap_year(2024))

# t = float(input('t = '))
# sign = input('Это цельсии(1) или фаренгейты(2)? ')
# if sign == '1':
#     t = t * (9 / 5) + 32
#     print('%dF' % round(t))
# if sign == '2':
#     t = (t -32) * (5 /9)
#     print('%dC' % round(t))














