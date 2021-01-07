from random import shuffle
from tkinter import Canvas, Tk
import time

bord_size = 3                       # размер строны
square_size = 80                    # размер ячеек (масштаб)
empty_square = bord_size ** 2       # количество ячеек

root = Tk()                         # библиотека рабочего окна
root.title(empty_square - 1)        # название игры


c = Canvas(root, width=bord_size * square_size, height=bord_size * square_size, bg='#0000FF')

#  bg - цвет фона основного окна, width - ширина основного окна, height - высота основного окна.
#  https://colorscheme.ru/html-colors.html неплохо отображены цвета. Хотя можно прото писпть blue или red

# c.pack()   ---------- >   Заполняет рабочее окно ячейками. Смысл нахождения тут не понял.


def get_inv_count():
    """ Функция считающая количество перемещений """
    inversions = 0
    inversion_board = board[:]
    inversion_board.remove(empty_square)
    for i in range(len(inversion_board)):
        first_item = inversion_board[i]
        for j in range(i+1, len(inversion_board)):
            second_item = inversion_board[j]
            if first_item > second_item:
                inversions += 1
    return inversions


def is_solvable():
    """ Функция определяющая имеет ли головоломка рещение """
    num_inversions = get_inv_count()
    if bord_size % 2 != 0:
        return num_inversions % 2 == 0
    else:
        empty_square_row = bord_size - (board.index(empty_square) // bord_size)
        if empty_square_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0


def get_empty_neighbor(index):
    # получаем индекс пустой клетки в списке
    empty_index = board.index(empty_square)
    # узнаем расстояние от пустой клетки до клетки по которой кликнули
    abs_value = abs(empty_index - index)
    # Если пустая клетка над или под клектой на которую кликнули
    # возвращаем индекс пустой клетки
    if abs_value == bord_size:
        return empty_index
    # Если пустая клетка слева или справа
    elif abs_value == 1:
        # Проверяем, чтобы блоки были в одном ряду
        max_index = max(index, empty_index)
        if max_index % bord_size != 0:
            return empty_index
    # Рядом с блоком не было пустого поля
    return index


def draw_board():

    c.delete('all')    # убирает все, что нарисовано на холсте (без неё остаётся копия перемещённой ячейки, как мусор)

    # i (строка) и j (столбец) будут координатами для каждой отдельной пятнашки
    print("Запуск функции заполнения ячеек")
    for i in range(bord_size):      # цикл по строкам
        print("i = ", i)
        for j in range(bord_size):  # цикл по столбцам
            print("   j = ", j)
            index = str(board[bord_size * i + j])       # получаем значение, которое рисуется на квадрате
            # если это не клетка которую мы хотим оставить пустой
            print("Значение = ", index)
            if index != str(empty_square):              # если index не равен максимальному из количества ячеек
                # рисуем квадрат по заданным координатам
                c.create_rectangle(j * square_size, i * square_size,
                                   j * square_size + square_size,
                                   i * square_size + square_size,
                                   fill='#43ABC9',
                                   outline='#FFFFFF')
                # пишем число в центре квадрата
                c.create_text(j * square_size + square_size / 2,
                              i * square_size + square_size / 2,
                              text=index,
                              font="Arial {} italic".format(int(square_size / 4)),
                              fill='#FFFFFF')


def show_vactory_plate():
    # Рисуем черный квадрат по центру поля
    c.create_rectangle(square_size / 5,
                       square_size * bord_size / 2 - 10 * bord_size,
                       bord_size * square_size - square_size / 5,
                       square_size * bord_size / 2 + 10 * bord_size,
                       fill='#000000',
                       outline='#FFFFFF')
    # Пишем красным текст Победа
    c.create_text(square_size * bord_size / 2, square_size * bord_size / 1.9,
                  text="ПОБЕДА!", font="Helvetica {} bold".format(int(10 * bord_size)), fill='#DC143C')


def click(event):
    # Получаем координаты клика
    x, y = event.x, event.y
    # Конвертируем координаты из пикселей в клеточки
    x = x // square_size
    y = y // square_size
    # Получаем индекс в списке объекта по которому мы нажали
    board_index = x + (y * bord_size)
    # Получаем индекс пустой клетки в списке.
    empty_index = get_empty_neighbor(board_index)
    # Меняем местами пустую клетку и клетку, по которой кликнули
    board[board_index], board[empty_index] = board[empty_index], board[board_index]
    # Перерисовываем игровое поле
    draw_board()
    # Если текущее состояние доски соответствует правильному - рисуем сообщение о победе
    if board == copy_correct_board:
        show_vactory_plate()
        print("РЕШЕНО")


c.bind('<Button-1>', click)     # '<Button-1>'-левая кл.мышки ('<Button-2>'-средняя '<Button-3>'-правая)
c.pack()                        # отрисовывает квадраты с цифрами внутри основного окна.


board = list(range(1, empty_square + 1))    # создаёт список от 1 до значения количества ячеек
print("Начальный список элементов ", board)

# copy_correct_board = board[:]      # создаёт копию упорядочненного списка при помощи board[:], аналог board.copy()
copy_correct_board = board.copy()
print("Копия нач. списка элементов", copy_correct_board)
# -------------------------------------------------------------------------------------------------------------------
draw_board()            # Тут то что я вставил и не могу понять... :-(
time.sleep(1)
# -------------------------------------------------------------------------------------------------------------------
shuffle(board)                       # перемешивает список в первый раз
draw_board()
print("Перемешанный список элементов", board)
print("Копия нач. списка элементов  ", copy_correct_board)

while not is_solvable():             # Проверяем условие на решаемость задачи и перемешиваем пока не выполнится условие
    shuffle(board)

draw_board()
root.mainloop()

