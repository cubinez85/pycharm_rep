# if answer == 10 or answer == 11:
#     return "Good!"
# elif answer == 12:
#     return "Better!"
# else:
#     return "Bad..."


# def f(answer):
#     match answer:
#         case 10 | 11:
#             return 'Good'
#         case 12:
#             return 'Better'
#         case _:
#             return 'Bad...'
# print(f(11))

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
# print(get_number_explanation(8))

# def greet():
#     count = 0
#     while count < 5:
#         print('Hello!')
#         count += 1
#
#
# greet()

# def print_numbers(num):
#     i = num
#     while i > 0:
#         print(i)
#         i -= 1
#     print('finished!')
# print(print_numbers(4))

# def is_num_even(num):
#     if num % 2 == 0:
#         print('yes')
#     else:
#         print('no')
# print(is_num_even(8))

# def multiply_numbers_from_range(start, finish):
#     i = start
#     multiply = 1
#
#     while i <= finish:
#         multiply *= i
#
#         i += 1
#     return multiply
#
# print(multiply_numbers_from_range(3, 5))

# def join_numbers_from_range(start, finish):
#     i = start
#     result = ''
#     while i <= finish:
#
#         result += str(i)
#         i += 1
#     return result
# print(join_numbers_from_range(5, 10))

# x = 3
# y = 5
# i = x
# result = ''
# while i <= y:
#     result = result + str(i)
#     print(result)
#     i += 1


# def my_substr(string, length):
#     i = 0
#     direct_string = ''
#     while i < length:
#
#         direct_string = direct_string + string[i]
#         i += 1
#     return direct_string
# string = 'If I look back I am lost'
# print(my_substr(string, 7))

# def count_chars(string, char):
#     i = 0
#     count = 0
#     while i < len(string):
#         if string[i] == char:
#             count += 1
#         i += 1
#     return count
# string = 'Fear cuts deeper than swords.'
# print(count_chars(string, 'c'))


# def has_char(string, char):
#     i = 0
#     # if char != string[i]:
#     #     return char in string
#     while i <= len(string):
#         if char == string[i]:
#             return True
#         if char == string[i].lower():
#             return True
#         if char == string[i].upper():
#             return True
#         i += 1
#     return False
# string = 'Hello'


# print(has_char(string, 'w'))



# def has_char(string, char):
#     i = 0
#     while i < len(string):
#         if char.lower() == string[i].lower():
#             return True
        # if string[i].lower() == char.lower():
        #     return True
        # if char == string[i].lower():
        #     return True
        # if char == string[i].upper():
        #     return True
        # i += 1
#     return False
# string = 'Hello'
# print(has_char(string, 'O'))



# text = 'code'
# for symbol in text:
#     print(symbol)

# def f(text):
#     # result = ''
#     for i in text:
#         print(i)
#         # result = i + result
#     return
# print(f('hello'))


# def sum(numbers):
#     result = 0
#     for num in numbers:
#         result += int(num)
#     return result
# print(sum('12345'))


# text = 'hello'
# print(text.replace('e', 'w'))

# def filter_string(text, char):
#
#     result = ''
#     for index in text:
#
#         if index.lower() != char.lower():
#             result += index
#
#     return result
#
# text = 'I look back if you are lost'
# print(filter_string(text, char='I'))


# def filter_string(text, char):
#     result = ''
#     text = text.strip()
#     for index in text:
#         if index.lower() != char.lower():
#             result += index
#     return result.strip()
#
# text = 'I look back if you are lost'
# print(filter_string(text, char='I'))


# def sum_of_series(start, finish):
#     result = 0
#     n = start
#     while n <= finish:
#         print('new iteration !!!!')
#         print(n)
#         result = result + n
#         n = n + 1
#     return result
# print(sum_of_series(3, 5))

# def is_palindrome(string):
#     reversed_string = ''
#
#     for i in range(len(string), 0, -1):
#         print('new iteration !!!!')
#         print(i)
#         reversed_string += string[i-1]
#         if string == reversed_string:
#             return True
#
#     return False
#
# print(is_palindrome(''))


# def is_palindrome(string):
#     reversed_string = ''.join(reversed(string))
#     if reversed_string == string:
#         return True
#     return False
# print(is_palindrome('a'))

# def is_palindrome(word):
#     result = ''
#     for char in word:
#         result = char + result
#     if result == word:
#         return True
#     else:
#         return False
# print(is_palindrome('ab'))