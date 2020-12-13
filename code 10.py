# Задания:
# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"

import os
import json
import re

wey = "c:/Files for Me"
os.chdir(wey)
list_dir = os.listdir(wey)  # смотрит по данному адресу

# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# ---------------------------------------------------------------------------------------------------------------

file_f = "data.json"  # Название файла, в котором нахоятся данные


def read_jsn(file_jsn):
    with open(file_jsn, "r", encoding='utf-8') as file:  # Чтение из файла для проверки
        data_jsn = json.load(file)
    return data_jsn


data_from_f = read_jsn(file_f)
print("1. Проверка считывани данных из файла data.json", "\n")
print(data_from_f)
print("\n")

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# ---------------------------------------------------------------------------------------------------------------


def by_name(dic):
    value = dic["name"]
    d_name = re.findall(r'\w+', value)[-1]
    return d_name


new_list_n = sorted(data_from_f, key=by_name)

# Проверка работы функции сортировки данных по ФАМИЛИИ ---------------->
print("2. Проверка сортировки словаря по фамилии", "\n")
for i in range(len(new_list_n)):
    print("\t", i, "Имя", new_list_n[i]["name"])
print("\n")

# 3. Написать функцию сортировки по дате смерти из поля "years". Сокращение BC. - это означает до н.э.
# ---------------------------------------------------------------------------------------------------------------


def by_date(dic):
    d_dat = dic["years"]
    res_d = re.findall(r'\d+', d_dat)
    d_years = []
    for dig in res_d:
        if " BC" in d_dat:
            d_years.append(-1 * int(dig))
        else:
            d_years.append(int(dig))
    d_end = sorted(d_years)[-1]
    return d_end


new_list_d = sorted(data_from_f, key=by_date)

# Проверка работы функции сортировки данных end date ---------------->
print("3. Проверка сортировки словаря по end date", "\n")
for i in range(len(new_list_d)):
    print("\t", i, new_list_d[i]["name"], "\t"*2, "Дата", new_list_d[i]["years"])
print("\n")

# 4. Написать функцию сортировки по количеству слов в поле "text"
# ---------------------------------------------------------------------------------------------------------------


def by_word_count(dic):
    value = dic["text"].replace("‘", "")
    word_count = re.findall(r'\w+', value)
    return len(word_count)


new_list_st = sorted(data_from_f, key=by_word_count)

# Проверка работы функции сортировки данных по полю текст ---------------->
print("4. Проверка сорт. словаря по кол. слов:", "\n")
for num in range(len(new_list_st)):
    print("\t", num, "Слов =", len(new_list_st[num]["text"].split()), "Имя", data_from_f[num]["name"])
