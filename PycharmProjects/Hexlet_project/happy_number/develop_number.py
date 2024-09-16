# def sum_of_square_digits(n):
#     sum_of_square = 0
#     for i in n:
#         if i.isdigit():
#             sum_of_square += int(i) ** 2
#     return sum_of_square
# print(sum_of_square_digits('20'))



# def sum_of_square_digits(n):
# 	result = 0
# 	while n > 0:
# 		last = n % 10
# 		result += last * last
# 		n = n // 10
# 	return result
# print(sum_of_square_digits(22))


# def is_happy_number(n):
# 	start = n
# 	result = 0
# 	while result != 1:
# 		result = sum_of_square_digits(n)
# 		n = result
# 		if result == start:
# 			return False
# 	return True
# print(is_happy_number(8))

# n = 12
# last = n % 10
# print(last)

# def happy_num(num):
#     seen = set()
#     while num != 1:
#         digits = [int(digit)**2 for digit in str(num)]
#         num = sum(digits)
#         if num in seen:
#             return False
#         seen.add(num)
#     return True
# print(happy_num(8))

# num = int(input('Введите число: '))
#
# if happy_num(num):
#     print(f"{num} счастливое число")
# else:
#     print(f"{num} не счастливое число")

# def sum_of_square_digits(n):
#     res = 0
#     while n > 0:
#         d = n % 10
#         res += d * d
#         n = n // 10
#     return res

# def is_happy_number(n):
#     for _ in range(10):
#         n = sum_of_square_digits(n)
#         if n == 1:
#             return True
#     return False
# print(is_happy_number(7))








