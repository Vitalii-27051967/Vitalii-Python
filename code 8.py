# 1. Написать функцию, которая считывает из файла domains.txt
# названия некоторых интернет доменов и возвращает их в виде списка строк (названия возвращать без точки).
#
# 2. Написать функцию, которая считывает данные из файла names.txt
# и возвращает список всех фамилий из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии)
#
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2.
# Строку и число генерировать случайным образом. Буквы могут повторяться.
# Пример: miller.249@sgdyyur.com


import os
import random
import string

my_dir = "c:/Files for Me"
os.chdir(my_dir)
list_dir = os.listdir(my_dir)   # смотрит по данному адресу
print("Файлы по пути my_dir", list_dir, sep="\n", end="\n\n")

file_domains = "domains.txt"
file_names = "names.txt"


def read_file(name_file):
    data = []
    with open(name_file, "r") as file:
        for line in file.readlines():
            data.append(line.strip())
    return data


clear_domains = []            # создание списка доменов
file_1 = read_file(file_domains)
[clear_domains.append(file_1[dig].replace(".", "")) for dig in range(len(file_1))]      # Убираем точки
names_1 = read_file(file_names)            # создание списка c имёнами
names_2 = []
[names_2.append(names_1[dig].split("\t")) for dig in range(len(names_1))]  # разбивка по разделителю
clear_name = []                             # создание списка имён
[clear_name.append(number[1]) for number in names_2]
rand_int = random.randint(100, 999)         # случайные числа от 100 до 999
domains = clear_domains[random.randint(0, len(clear_domains)-1)]  # случайные домены из clear_domains
names = clear_name[random.randint(0, len(clear_name)-1)]  # случайные имена из clear_name
letters = "".join(random.choice(string.ascii_lowercase) for x in range(random.randint(5, 7)))   # случайные буквы
rand_mail = f"{names}.{rand_int}@{letters}.{domains}"       # переменная, если с ней нужно дальше работать
print("Сгенерированный адрес", rand_mail, "\n", "Тип данных", type(rand_mail))
