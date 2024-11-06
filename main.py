from random import randint
from tkinter import *

SIZE = 9
VARIABLE = ["1", "2", "3", "4", "5","6" , "7", "8", "9"]


class Game:
    list_complexity = {"easy": 5, "medium": 10, "hard": 20}
    # Конструктор класса принимает параметр complexity,
    # который определяет уровень сложности, и создает окно приложения на его основе.
    def __init__(self, complexity):
        self.window = Tk()
        self.window.geometry("300x300")
        self.harder = self.create_level(complexity)
        self.window.mainloop()

    # Принимает complexity и вызывает функции генерации уровня,
    # записывая их в GUI-объекты Entry и Label (для неизменяемых/стартовых значений).
    def create_level(self, complexity):
        list_items = []
        for row in range(SIZE):
            list_row = []
            list_items.append(list_row)
            self.window.grid_rowconfigure(row, weight=1)
            # Разрешает растягивание столбцов при изменении размера окна
            self.window.grid_columnconfigure(row, weight=1)
            for column in range(SIZE):
                entry = Entry(self.window)
                # sticky="nsew" растягивает элемент по размеру окна
                entry.grid(row=row, column=column, sticky="nsew")
                list_row.append(entry)



# Создает квадратный список для дальнейшей реализации,
# в правую нижнюю ячейку помещает False для проверки заполнения.
# Возвращает квадратный список.
def full_sudoku():
    list_item = []
    for row in range(SIZE):
        list_row = []
        list_item.append(list_row)
        for column in range(SIZE):
            list_row.append(f"{row},{column}")

    list_item[8][8] = False
    return list_item

#Принимает квадратный список для судоку, в который нужно сгенерировать уникальные значение по стобцам, рядам и блокам
#Возвращает заполненый квадратный список судоку

# функция на которой завис, нужно реализовать заполнения квадратного списка с возможностью backtreking и измения пути,
# при тех вариантах, когда выбранное значение не проходит проверку на уникальность,
# для этого нужно использовать рекурсию и каждую запись " Фикксировать" вызовом нового заполнения
def generate_sudoku(list_sudoku, row=0, column=0):
    is_generate = list_sudoku[8][8]

    if not is_generate:
        for rows in range(row,len(list_sudoku)):
            for columns in range(column,len(list_sudoku)):
                used_values = VARIABLE
                while used_values:
                    iter = randint(0, len(used_values) - 1)
                    value = used_values[iter]
                    check_repeats(used_values, iter)
                    if check_value(value, row, column, list_sudoku):
                        list_sudoku[row][column] = value
    else:
        return list_sudoku





# Функция принимает  список значений и  используемый индекс с этого списка, для того чтобы оставить только уникальные значения
# Возвращает список без значения, которое будет использовано в судоку на шагу записи
def check_repeats(check_list, iter):
    if iter == len(check_list) - 1:
        check_list = check_list[:iter]
    elif iter == 0:
        check_list = check_list[iter + 1:]
    elif iter != 0 and iter != len(check_list) - 1:
        check_list = check_list[0:iter] + check_list[iter + 1:]
    return check_list


def print_2D(square_list):
    for row in square_list:
        for column in range(len(row)):
            print("|", row[column], end='')
            if column in [2, 5]:
                print(end='')
        print()

# Принимает значение, индекс ряда и список для проверки ли есть значение уже в ряду.
# Возвращает False если значение уже используеться и True, если такого нет.
def check_line(value, row, full_list):
    if value in full_list[row]:
        return False
    return True

# Принимает значение, индекс стобца и список для проверки ли есть значение уже в стобце.
# Возвращает False если значение уже используеться и True, если такого нет.
def check_row(value, column, full_list):
    for row in full_list:
        if value in row[column]:
            return False
        return True

# Принимает значение, индексы ряда и стобца и сам список для проверки уникальности значения в своем блоке 3х3
# Возвращает False если значение уже используеться и True, если такого нет.
def check_block(value, row, column, full_list):
    # вызываем ф-цию для получения координат блока для проверки
    block = get_block(row, column, full_list)
    start_row, start_column, end_row, end_column = block[0], block[1], block[2], block[3]
    for rows in range(start_row, end_row + 1):
        for lines in range(start_column, end_column + 1):
            if value == full_list[rows][lines]:
                return False
    return True

# Принимает значение, индексы ряда и стобца и сам список для проверки уникальности значения в ряду, стобце и своем блоке
# Возвращает False если значение уже используеться и True, если такого нет.
def check_value(value, row, column, full_list):
    return (check_block(value, row, column, full_list) \
            and check_row(value, column, full_list)\
            and check_line(value,row,full_list))


# ф-ция для  возврата блока для проверки
def get_block(row, column):
    range_block = []
    if row < 3 and column < 3:
        range_block = [0, 0, 2, 2]
    elif row < 3 and column < 6:
        range_block = [0, 3, 2, 5]
    elif row < 3 and column < 9:
        range_block = [0, 6, 2, 8]
    elif row < 6 and column < 3:
        range_block = [3, 0, 5, 2]

    elif row < 6 and column < 6:
        range_block = [3, 3, 5, 5]

    elif row < 6 and column < 9:
        range_block = [3, 6, 5, 8]

    elif row < 9 and column < 3:
        range_block = [6, 0, 8, 2]
    elif row < 9 and column < 6:
        range_block = [6, 3, 8, 5]
    elif row < 9 and column < 9:
        range_block = [5, 6, 8, 8]
    return range_block


sudoku = full_sudoku()
print_2D(sudoku)

# generate_sudoku(sudoku)
# print()
# print_2D(sudoku)


# used_values = VARIABLE
# while used_values:
#     iter = randint(0, len(used_values) - 1)
#     value = used_values[iter]
#     print(value,used_values)
#     used_values=check_repeats(used_values, iter)
