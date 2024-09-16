# def is_happy_ticket(string):
#     sum = 0
#     for i in string:
#         if i.isdigit():
#             sum += int(i)
#     return sum
# print(is_happy_ticket('123'))


# string = '1234'
# length = len(string) // 2
# s = sum(map(int, string[:length]))
# print(s)

# def is_happy_ticket(string):
#     length = len(string) // 2
#     string_half1 = sum(map(int, string[:length]))
#     string_half2 = sum(map(int, string[length:]))
#     if string_half1 == string_half2 and len(string) % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_happy_ticket('1212'))


