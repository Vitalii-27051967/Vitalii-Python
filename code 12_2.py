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
import calendar
import json

my_dir = "c:/Files for Me"                      # моя рабочая директория
check_file = os.path.exists(my_dir)             # проверяем наличие папки по заданному пути.
print("Проверка наличия папки -->", check_file)
if check_file is False:                         # если папка не существувет, то создаём её.
    os.mkdir("c:/Files for Me")
os.chdir(my_dir)
file_name = "authors.txt"                       # Имя файла как по умолчанию :-)
file_data_json = "authors_json.json"

#  _______________________________________________________________________________________________________________
#   2.1) написать функцию, которая считывает данные из этого файла "authors.txt"

with open(file_name, "r", encoding='utf-8') as file:
    data = []
    for line in file.readlines():
        data.append(line.strip())                       # Строка данных считанных их файла
print("\t\n", "Считанные данные из файла: ", end="\n\n")
[print(dat) for dat in data]
print(end="\n\n")


#  _______________________________________________________________________________________________________________
# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей

def sep(n):
    d_bd = n.split("-")             # отделяем дату от текста
    d_bd_1 = d_bd[0]
    d_bd = d_bd[1].split("'s")      # отделяем автора из текста
    d_bd_2 = d_bd[0]
    return d_bd_1, d_bd_2


def dig_month(n):
    part_2_d = ""
    part = n[0].split()                                         # Разбиваем дату на составляющие
    part_1 = "".join(re.findall(r'\d+', part[0])).zfill(2)      # Число месяца
    part_2 = "".join(re.findall(r'\D+', part[1]))               # Месяц
    part_3 = "".join(re.findall(r'\d+', part[2]))       # Год
    for k, v in enumerate(calendar.month_name):         # Делаем замену текстовых названий мес. на цифровые
        if part_2 == v:
            part_2_d = str(k).zfill(2)
    dat_d = f"{part_1}/{part_2_d}/{part_3}"
    return dat_d


data_begin = []
begin = dict()
dict_begin_full = []

for num in data:
    if re.search(r"\bbirthday\b", num.lower()) and re.search(r"'s", num.lower())\
            or re.search(r"\bdeath\b", num.lower()):
        data_begin.append(sep(num))
        date_in_dig = dig_month(sep(num))
        begin["name"] = sep(num)[1].lstrip()
        begin["date"] = dig_month(sep(num))
        sss = begin.copy()
        dict_begin_full.append(sss)

print("\n\t", "Проверка обработки данных:", end="\n\n")
[print(num_1["name"].ljust(25, " "), num_1["date"]) for num_1 in dict_begin_full]


#  ---------------------------------------------------------------------------------------------------------------
# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

with open(file_data_json, "w") as file:        # запись данных в файл
    json.dump(dict_begin_full, file)

with open(file_data_json, "r") as file:        # Чтение данных из файла для проверки
    for_check = json.load(file)
print("\n\t", "Проверка записи в файл:", end="\n\n")
[print(value) for value in for_check]
