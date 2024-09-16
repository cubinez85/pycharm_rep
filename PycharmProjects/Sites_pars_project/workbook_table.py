from openpyxl import Workbook

table = [[1, 2, 3], [4, 5, 6]]
#Создаем объект "книги"
work_book = Workbook()

# Создаем объект "листа"
work_sheet = work_book.active

# Для каждой строки row в списке table: присоединить строку к листу
for row in table:
    work_sheet.append(row)
    work_book.save('table.xlsx')

# numbers = [1, 2, 3]
#
# for elem in numbers:
#     print(elem)

# work_book = Workbook()
# work_sheet = work_book.active
#
# # Коллекция для генерации таблицы
# numbers = [1, 2, 3, 4, 5]
#
# for elem in numbers:
#     row = [elem, elem * 2, elem ** 2]
#     print(row)
#     work_sheet.append(row)
#
# work_book.save('numbers.xlsx')

