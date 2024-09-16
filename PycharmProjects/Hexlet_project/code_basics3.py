# def print_numbers(last_number):
#     i = 4
#     while i <= last_number:
#         print(i)
#         i = i -1
#
#     print('finished!')
# print(print_numbers(last_number=4))

# def print_numbers(last_number):
#     i = last_number
#     while i > 0:
#         print(i)
#         i = i -1
#     print('finished!')
#
# print_numbers(last_number=4)

# def sum_numbers_from_range(start, finish):
#     i = start
#     sum = 0
#     while i <= finish:
#         sum = sum + i
#         i = i + 1
#     return sum
# print(sum_numbers_from_range(start=2, finish=5))

# def multiply_numbers_from_range(start, finish):
#     i = start
#     result = 1
#     while i <= finish:
#         result = result * i
#         i = i + 1
#     return result
# print(multiply_numbers_from_range(start=2, finish=5))

# def join_numbers_from_range(start, finish):
#
#     i = 1
#     while i <= finish:
#         i = i + 1
#     return
# print(join_numbers_from_range(start=5, finish=7))

# i = 4
# while i<7:
#   i=i+1
#   print(i,end='')
# def join_numbers_from_range(n, m):
#     n = int(input('n: '))
#     m = int(input('m: '))
#     result = (end='')
#        while n <= m:
#
#
#            n += 1
#     return r
# print(join_numbers_from_range(n=2, m=4))

# def join_numbers_from_range(start, end):
#     return ''.join(map(str, range(start, end + 1)))
# print(join_numbers_from_range(5, 7))

# def join_numbers_from_range(start, end):
#     i = start
#     result = ''
#     while i <= end:
#         result = result + str(i)
#         i = i + 1
#     return result
# print(join_numbers_from_range(start=5, end=7))

# def join_numbers_from_range(start, finish):
#     result = ""
#     i = start
#     while i <= finish:
#         result += str(i)
#         i = i + 1
#     return result
# print(join_numbers_from_range(start=5, finish=7))

# def print_name_by_symbol(name):
#     i = 0
#     while i < len(name):
#         print(name[i])
#         i = i + 1
# name = 'Arya'[::-1]
# print_name_by_symbol(name)


# def f(word):
#     i = 0
#     while i < len(word):
#         print(word[i])
#         i = i + 1
#
# word = 'abcde'[::-1]
# f(word)
# def f(word):
#     i = len(word)
#
#     while i > 0:
#        print(word[::-1])
#        i = i -i
# word = 'abcde'
# f(word)

# def print_reversed_word_by_symbol(word):
#     i = len(word) - 1
#     while i >= 0:
#         print(word[i])
#         i = i - 1
#
# word = 'abcde'
# print_reversed_word_by_symbol(word)

# word = 'hello'
# i = len(word) - 1
# print(word[i])

# index = 0
# string = 'hello'
# print(string[index])

# def count_chars(string, char):
#     index = 0
#     count = 0
#     while index < len(string):
#         if string.lower()[index] == char.lower():
#             count = count + 1
#         index = index + 1
#     return count
# print(count_chars(string='HexlEt', char='E'))

# string = 'hello'
# index = len(string[:-1])
# print(string[index])

# def my_substr(string, length):
#     index = len(string[:0])
#     total_string = ''
#     while index <= 0:
#         current_char = string[index:length]
#         total_string = total_string + current_char
#         index = index + 1
#     return total_string
# string = 'Winter is coming'
# print(my_substr(string, length=8))

# def my_substr(string, length):
#     result_string = ''
#     index = 0
#     while index < length:
#         result_string = result_string + string[index]
#         index = index + 1
#
#     return result_string
# string = 'hello'
# print(my_substr(string, length=2))

# def is_arguments_for_substr_correct(string, index, length):
#     if index < 0:
#         return False
#     elif length < 0:
#         return False
#     elif index > len(string) - 1:
#         return False
#     elif index + length > len(string):
#         return False
#     return True
# string = 'Sansa Stark'
# print(is_arguments_for_substr_correct(string, index=4, length=4))

# def is_arguments_for_substr_correct(string, index, length):
#     return not (length < 0 or index < 0 or index >= len(string) or length + index > len(string))
# string = 'Sansa Stark'
# print(is_arguments_for_substr_correct(string, index=4, length=4))

# def filter_string(text, char):
#     index = 0
#     result = ''
#     while index < len(text):
#         current_char = text[index]
#         if current_char != char:
#             result = f'{result}{current_char}'
#         index += 1
#     return result
#
# text = 'If I look back I am lost'
# print(filter_string(text, char='l'))

# x = 9
# y = 2
# print(x % y)

# def is_prime(number):
#     if number < 2:
#         return False
#     divider = 2
#     while divider <= number / 2:
#         if number % divider == 0:
#             return False
#         divider += 1
#     return True
# print(is_prime(number=9))

#


# def f(text, char):
#     index = 0
#     if char != text[index]:
#         return char in text
#     while index <= len(text):
#         if char == text[index]:
#             return True
#         if char == text[index].lower():
#             return True
#         index += 1
#     return
# text = 'Hello'
# print(f(text, char='L'))