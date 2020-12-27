# 2. Дан файл authors.txt
#
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая список строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Miserables.
#
# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
#
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]
#
# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

import os
import re
import json
import calendar

my_dir = "c:/Files for Me"                      # моя рабочая директория
check_file = os.path.exists(my_dir)             # проверяю наличие папки по заданному пути.
print("Проверка наличия папки -->", check_file)
if check_file is False:                         # если папка не существувет, то создаём её.
    os.mkdir("c:/Files for Me")
os.chdir(my_dir)

file_name = "authors.txt"                       # Имя файла по умолчанию для чтения
file_data_json = "authors_json.json"            # Название файла для записи данных JSON
#  _______________________________________________________________________________________________________________
#   2.1) написать функцию, которая считывает данные из этого файла "authors.txt"


def get_list_authors(filename):
    with open(filename, "r", encoding='utf-8') as file:
        data_f = []
        for line in file.readlines():
            data_f.append(line.strip())        # Строка данных считанных из файла
    return data_f
#  _______________________________________________________________________________________________________________
# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей


def get_dict_authors(data):
    def sep(str_txt):                         # Делает разбивку текста на дату и автора
        d_bd = str_txt.split("-")             # отделяем дату от текста
        data_begin_end = d_bd[0]        # дата
        d_bd = d_bd[1].split("'s")      # отделяем автора из текста
        author_from_text = d_bd[0]      # автор
        return data_begin_end, author_from_text

    def dig_month(dat_txt):             # Преобразует дату с текстом к числовому формату dd/mm/yyyy
        part_2_d = ""
        part = dat_txt[0].split()                               # Разбиваем дату на составляющие
        part_1 = "".join(re.findall(r'\d+', part[0])).zfill(2)  # Число месяца приводим к формату DD /mm/yyyy
        part_2 = "".join(re.findall(r'\D+', part[1]))           # Месяц в текстовом формате
        part_3 = "".join(re.findall(r'\d+', part[2]))           # Год
        for month_digit, month_text in enumerate(calendar.month_name):   # Делаем замену TXT названий мес. на DIG
            if part_2 == month_text:
                part_2_d = str(month_digit).zfill(2)                     # Приводим месяц к формату dd/ MM /yyyy
        dat_d = f"{part_1}/{part_2_d}/{part_3}"
        return dat_d

    data_be = []
    begin = dict()
    dict_begin_full = []

    for num in data:
        if re.search(r"\bbirthday\b", num.lower()) and re.search(r"'s", num.lower()) \
                or re.search(r"\bdeath\b", num.lower()):
            data_be.append(sep(num))
            begin["name"] = sep(num)[1].lstrip()        # запись в словарь автора
            begin["date"] = dig_month(sep(num))         # запись в словарь нормализованной даты
            sss = begin.copy()
            dict_begin_full.append(sss)

    return dict_begin_full
#  ---------------------------------------------------------------------------------------------------------------
# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.


def write_json(file_dat, dict_beg):
    with open(file_dat, "w") as file:
        json.dump(dict_beg, file)
    return
#  ---------------------------------------------------------------------------------------------------------------
# Чтение данных из файла для проверки


def reader_file(file_json):
    with open(file_json, "r") as file:
        for_check = json.load(file)
    return for_check
#  ---------------------------------------------------------------------------------------------------------------
# пошаговое выполнение программы


authors_list = get_list_authors(file_name)      # чтение данных TXT из файла
authors_dict = get_dict_authors(authors_list)   # создание списка словарей
write_json(file_data_json, authors_dict)        # запись данных в файл "authors_json.json"
check_record = reader_file(file_data_json)      # проверка записи в файл

#  ---------------------------------------------------------------------------------------------------------------
# Проверка работы

print("\t\n", "Считанные данные из файла: ", end="\n\n")
[print(dat) for dat in authors_list]

print("\n\t", "Проверка обработки данных 'name....date':", end="\n\n")
[print(num_1["name"].ljust(25, "."), num_1["date"]) for num_1 in authors_dict]

print("\n\t", "Проверка записи в файл:", end="\n\n")
[print(value) for value in check_record]
