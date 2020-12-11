import random
import csv
import os
import json
import string

my_dir = "c:/Files for Me"
os.chdir(my_dir)

# file_name = "111.json"        # | Для облегчения проверки
# file_name = "111.csv"         # |
# file_name = "111.txt"         # |

file_name = input("Введите название файла для генерации файла: ")

try:

    point = file_name.rindex(".")
    index = file_name[point:].lower()
    if index == ".txt":         # ############################################################################### TXT

        def words():    # Генерация случайных букв
            var_1 = random.randint(1, 10)
            let_abc = "".join(random.choice(string.ascii_lowercase) for _ in range(var_1))
            if var_1 <= 5:
                let_abc = let_abc.title()
            return let_abc

        out_mark = [" ", ". ", "! ", "\n", "? "]
        in_mark = [", ", " - ", ": ", "; "]
        txt_s = ""
        flag = 0

        while flag != 1:                    # генерация рандомного текста до 1000 знакомест
            var = random.randint(1, 2)      # случайный выбор числа или набора букв
            if var == 1:
                i_n = random.randint(0, len(in_mark) - 1)
                w_n = words()               # добавление набора букв
                ttt = w_n + in_mark[i_n]    # + добавление знаков внутристочных
            else:
                rand_int = random.randint(0, 999)  # случайные числа от 0 до 999
                i_v = random.randint(0, len(out_mark) - 1)
                d_n = str(rand_int)                 # добавление набора цифр
                ttt = d_n + out_mark[i_v]        # + добавление знаков окончания строки, перхода на др.строку
            if len(txt_s) + len(ttt) <= 1000:    # проверка количетва знакомест
                txt_s = txt_s + ttt     # создание текста из набра цифр, наборов букв и различных знаков
            else:
                flag = 1

        data_list = list(txt_s)
        with open(file_name, "w") as file:
            for line in data_list:
                file.write(f"{line}")
        with open(file_name, "r") as file:
            data = []
            for line in file.readlines():
                data.append(line.strip())
            print("Считка из файла", data, sep="\n")
            print("Количество знакомест", len(data_list))

    elif index == ".csv":           # ############################################################################ CSV
        def csv_d(s):
            my_str = random.getrandbits(s)          # генерируем бинарные значения числа размером s разрядов
            code = str(bin(my_str)[2::]).zfill(s)   # делаем срез получ. знач. и восстанавливаем нули в начале
            value_data = []
            my_str = ""
            for i in range(s):                      # разбиваем строку на элементы, потом перезаписываем с разделителем
                my_str = my_str + code[i]
                if i != m - 1:                      # чтоб не записало разделитель к концу строки
                    my_str = my_str + ";"           # по разделителю - интересно было проверять в Exel
            value_data.append(my_str)
            return value_data

        n = random.randint(3, 10)  # генерируем количество строк
        m = random.randint(3, 10)  # генерируем количество столбцов
        val_new = list()
        for _ in range(n):  # записываем данные в количестве n случайных строк из 1 и 0
            val_new.append(csv_d(m))

        with open(file_name, "w", newline="") as csv_file:  # записываем данные в файл
            writer = csv.writer(csv_file)
            writer.writerows(val_new)
        data = []
        with open(file_name, "r", newline="") as csv_file:  # считываем то безобразие что получилось чтоб убедиться
            reader = csv.reader(csv_file)
            for line in reader:
                data.append(line)
        print("Считка из файла", data, sep="\n")

    elif index == ".json":          # ########################################################################### JSON
        def key_d(var_1):  # генерирует строки (ключи заданного размера)
            let_abc = "".join(random.choice(string.ascii_lowercase) for _ in range(var_1))  # случ. буквы
            return let_abc


        def dig_d():
            rand_code = random.randint(0, 2)
            if rand_code == 0:
                data_j = random.randint(-100, 100)      # случайные числа от -100 до 100
            elif rand_code == 1:
                data_j = random.uniform(0, 1)           # случайные числа с запятой от 0 до 1
            else:
                a = [True, False]
                data_j = random.choice(a)
            return data_j


        def jsn():
            number_of_keys = random.randint(5, 20)
            my_dict = {key_d(5): dig_d() for _ in range(number_of_keys)}    # генерация ключей из 5 симв. и данных
            return my_dict


        person = jsn()
        with open(file_name, "w") as file:        # запись того что получилось в файл
            json.dump(person, file)
        with open(file_name, "r") as file:        # Чтение из файла для проверки
            person_json = json.load(file)
        print("Проверка записи", person_json, "\n", type(person_json), "\n", "Количество элементов", len(person_json))
    else:
        print("Введите корректное расширение файла (.txt, .json, .csv)")

except ValueError:
    print("Введите КОРРЕКТНОЕ значение названия")
