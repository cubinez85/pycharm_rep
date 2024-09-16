# def num(n):
#     n = int(abs(n))
#     count = 0
#     sum = 0
#     while n > 0:
#         n //= 10
#         count += 1
#         sum += count
#     return count
# print(num(23))

# def num(n):
#     n = str(abs(n))
#     count = 0
#     sum = 0
#     pow = 1
#     for i in n:
#         count += 1
#         sum += int(i)
#         pow *= int(i)
#     return count
# print(num(66456))


# def even_nam(n):
#     n = abs(int(n))
#     even = 0
#     # odd = 0
#     while n > 0:
#         if n % 2 == 0:
#             even += 1
#         # else:
#         #     odd += 1
#         n //= 10
#     return even
# print(even_nam(1234))

# def even_num(n):
#     n = str(abs(n))
#     even = 0
#     for i in n:
#         if int(i) % 2 == 0:
#             even += 1
#     return even
# print(even_num(-123456))

# n = input('Введите число: ')
# even = 0
# odd = 0
# for i in n:
#     if int(i) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f'even = {even}\nodd = {odd}')

# def sum_num(n):
#     sum = 0
#     count = 0
#     pow = 1
#     while n > 0:
#         digit = n % 10
#         n //= 10
#         count += 1
#         sum += digit
#         pow *= digit
#     return pow
# print(sum_num(66))

# def reverse_num(n):
#     m = 0
#     while n > 0:
#         digit = n % 10
#         n //= 10
#         m = m * 10
#         m += digit
#     print(m)
# reverse_num(123)

# n = '123'
# res = ''.join(reversed(n))
# print(res)

# def reverse_num(n):
#     res = ''
#     for i in n:
#         res = i + res
#     print(res)
# reverse_num("123")

# print('Py', end='')
# print('thon')

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print('%4d' % (i * j), end='')
#         j += 1
#     print()
#     i += 1

# def multy_table():
#     for i in range(1, 10):
#         for j in range(1, 10):
#             print('%4d' % (i * j), end='')
#         print()
# multy_table()

# from random import randint
# secret_num = randint(1, 100)
# user_num = 0
# try_count = 1
# while secret_num != user_num:
#     print(f'{try_count}- я попытка: ', end='')
#     user_num = int(input())
#     if user_num < secret_num:
#         print('Слишком мало')
#     elif user_num > secret_num:
#         print('Слишком много')
#     else:
#         print('Вы угадали')
#         try_count += 1

# fib1 = 1
# fib2 = 1
# i = 0
# print('Введите номер элемента ряда Фибоначчи: ', end='')
# n = int(input())
# while i < n -2:
#     fib1, fib2 = fib2, fib1 + fib2
#     i += 1
# print(fib2)

# fib1 = fib2 = 1
# n = int(input())
# if n < 2:
#     quit()
# print(fib1, end='')
# print(fib2, end='')
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end='')
# print()

# for i in range(32, 127):
#     print(chr(i), end='')
#     if (i -1) % 10 == 0:
#         print()
# print()

# for i in range(5):
#     if i == 0 or i == 4:
#         for j in range(20):
#             print('%', end='')
#     else:
#         print('%', end='')
#         for j in range(1, 19):
#             print(' ', end='')
#         print('%', end='')
#     print()

# x1 = float(input('Точка начала отрезка: '))
# x2 = float(input('Точка конца отрезка: '))
# step = float(input('Шаг: '))
#
# if x1 > x2:
#     x1, x2 = x2, x1
# print('Функция: y = -3x ** 2 - 4x + 20')
# print('x       y')
# while x1 <= x2:
#     y = -3 * x1 ** 2 - 4 * x1 + 20
#     print('%5.2f | %7.2f' % (x1, y))
#     x1 += step

# def f_table(x1, x2, step):
#     if x1 > x2:
#         x1, x2 = x2, x1
#     while x1 <= x2:
#         y = -3 * x1 ** 2 - 4 * x1 +20
#         x1 += step
#         print('%5.2f | %7.2f' % (x1, y))
# f_table(-1, 2.9, 0.7)

# def f_multy(a, n):
#     res = a
#     for i in range(1, n):
#         res = res * (a + i)
#     return res
# print(f_multy(0.8, 4))

# def f_multy(a, n):
#     res = a
#     i = 1
#     while i < n:
#         res *= (a + i)
#         i += 1
#     return res
# print(f_multy(0.8, 4))

# def f_count(n):
#     a = 1
#     i = 0
#     sum = 0
#     while i < n:
#         sum += a
#         a = a / -2
#         i += 1
#     return sum
# print(f_count(5))

# num_list = [-3, -6, -34, 0, 5, 7, 34, 45]
# print(num_list)
# for i in range(len(num_list)):
#     if num_list[i] > 0:
#         num_list[i] = 1
#     elif num_list[i] < 0:
#         num_list[i] = -1
# print(num_list)



