import random
from tkinter import *


class My15:

    def __init__(self, side_size):
        self.size = side_size
        self.my_15 = self._generate_15()
        self.row, self.col = self.get_space()
        self._print_15()

    def _generate_15(self):
        my_15_gen = []   # Поменял название переменной, чтоб PC перестал указывать что такое название уже есть снаружи.
        all_values = [str(i) for i in range(1, self.size ** 2)] + [""]
        for row_number in range(self.size):
            my_15_gen.append(all_values[self.size * row_number: self.size * (row_number + 1)])
        return my_15_gen

    def _print_15(self):
        for row in self.my_15:
            line = " ".join([f"{val:2}" for val in row])
            print("\t\t", line)

    def get_space(self):
        row_ = 0
        col_ = 0
        for i, row in enumerate(self.my_15):
            if '' in row:
                row_ = i
                for j, col in enumerate(row):
                    if '' == col:
                        col_ = j
        return row_, col_

    def move_down(self):
        if self.row == self.size - 1:
            return
        self.my_15[self.row][self.col], self.my_15[self.row + 1][self.col] = self.my_15[self.row + 1][self.col], \
                                                                             self.my_15[self.row][self.col]
        self.row += 1

    def move_up(self):
        if self.row == 0:
            return
        self.my_15[self.row][self.col], self.my_15[self.row - 1][self.col] = self.my_15[self.row - 1][self.col], \
                                                                             self.my_15[self.row][self.col]
        self.row -= 1

    def move_right(self):
        if self.col == self.size - 1:
            return
        self.my_15[self.row][self.col], self.my_15[self.row][self.col + 1] = self.my_15[self.row][self.col + 1], \
                                                                             self.my_15[self.row][self.col]
        self.col += 1

    def move_left(self):
        if self.col == 0:
            return
        self.my_15[self.row][self.col], self.my_15[self.row][self.col - 1] = self.my_15[self.row][self.col - 1], \
                                                                             self.my_15[self.row][self.col]
        self.col -= 1


def draw_15_table(my_15n):
    for row_index, row in enumerate(my_15n.my_15):
        for col_index, col in enumerate(row):
            label = Entry(root, width=2, fg='white', bg='black', font=('Arial', 50, 'bold'), justify='center')
            label.config(highlightbackground="black")
            label.grid(row=row_index, column=col_index)
            label.insert(END, col)


def left(event):
    my_15.move_left()
    draw_15_table(my_15)


def right(event):
    my_15.move_right()
    draw_15_table(my_15)


def up(event):
    my_15.move_up()
    draw_15_table(my_15)


def down(event):
    my_15.move_down()
    draw_15_table(my_15)


def rnd_mixer():    # Метод блуждающей ячейки. Можно придумать другое название :-)
    value = 0
    value_d = 0
    while value != size_of_sides ** 3:  # Чем больше значений, тем дольше (больше) нужно перемешивать. Можно иначе.
        my_str = random.getrandbits(3)              # Генерирует бинарное значение кода (неплохо работала при заплнении
        # значений "1" и "0" в 9 ДЗ для CSV файла). Значение каждого разряда отвечает за определённое действие.
        code = str(bin(my_str)[2::]).zfill(3)       # Восстанавливаем нули
        print("сгенерированный код", code)

        step = random.randint(1, size_of_sides // 2)     # Определяем случайный шаг для перемещений. Для повышения
        # коэффициента полезного действия можно (если нужно и если в этом есть какой-то смысл) доработать взяв привязку
        # из положения пустой ячейки.
        # Это позволит уменьшить количество пустых биений, когда значение шага перемещения будет выходить за границы
        # значений при перемещении в заданном направлении. Пока уменшил эту вероятность путём деления на 2. Да и
        # не хотелось сильно влазить в код и усложнять его :-) Нужно ли усложнение программы ради этого? :-)
        # ------------------------------ Оставляю принты для лучшей визуализации процесса --------------------------
        if code[0] == "0":
            print("right ", step)
            [my_15.move_right() for _ in range(step)]
        else:
            print("left ", step)
            [my_15.move_left() for _ in range(step)]
        if code[1] == "0":
            print("down ", step)
            [my_15.move_down() for _ in range(step)]
        else:
            print("up ", step)
            [my_15.move_up() for _ in range(step)]
        value += int(code[2])        # Количество циклов не меньше чем value (0 не учитывается). Просто как вариант.
        # По Гауссу, это даёт, примерно, удваивание значения цикла. Было интересно поэксперементировать.
        # Мы же учимся ;-). Можно не использовать в дальнейшем. Или придумать другое применение.
        value_d += 1        # Для определения реального количества циклов. В дальнейшем можно не использовать.
        print("Цикл = ", value_d)
        my_15._print_15()


size_of_sides = random.randint(4, 10)       # размер строны поля игры, чтоб не менять каждый раз при отладке rnd_mixer
window_name = str(size_of_sides ** 2 - 1)   # Как кто-то заметил на лекции, должно отображаться если это 99-шки :-))
my_15 = My15(side_size=size_of_sides)       # Вводим значение размера строн нашей матрицы
rnd_mixer()                                 # Запуск функции перемешивания значений в рандомном порядке
root = Tk()
root.title(window_name)
root.geometry(f"{78*size_of_sides}x{82*size_of_sides}")   # ---------> без этой строки в "Widows 10"
#  сразу открывается окно требуемых размеров. Но раз это входило в ДЗ, то его выполнил :-) Цифры подобрал имперически.
root.configure(background='black')
draw_15_table(my_15)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()
