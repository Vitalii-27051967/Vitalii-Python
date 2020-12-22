# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

import csv
import os
import requests
import time
import re

my_dir = "c:/Files for Me"                      # моя рабочая директория
check_file = os.path.exists(my_dir)             # проверяем наличие папки по заданному пути.
print("Проверка наличия папки -->", check_file)
if check_file is False:                         # если папка не существувет, то создаём её.
    os.mkdir("c:/Files for Me")
os.chdir(my_dir)
file_name = "111.csv"                           # Имя файла как по умолчанию :-)


def data_line():
    time.sleep(2)        # Замедляем обращение к серверу для уменьшения количества повторов. Жалеем нервы сервера :-)
    url = "http://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "key": 1,
              "lang": "ru"}
    r = requests.get(url, params=params)
    quote = r.json()
    quote_text = quote["quoteText"]
    quote_author = quote["quoteAuthor"]
    url_txt = quote['quoteLink']
    str_d = [quote_author, quote_text, url_txt]
    return str_d


str_value = list()
number_of_lines = input("Количество цитат = ")      # Количество цитат
num_clear = re.findall(r'\d+', number_of_lines)     # минимальная защита он некорректного ввода
num_clear = int(num_clear[0])

num = 0
repeat = list()
while num != int(num_clear):
    value = data_line()                # Получение строки с цитатой
    print(num, value[0])
    following = (value[-1][-11:-1:])   # Поскольку мы учимся, интересно было проверку на повтор выполнить по хвосту URL
    if value[0] != "":
        if repeat.count(following) != 1:    # Проверка на повтор текста по хвосту URL
            str_value.append(value)
            repeat.append(value[-1][-11:-1:])
            num += 1
        else:
            print(num, "Совпадение по тексту", repeat, following)
    else:
        print(num, "Нет автора")

# смотрим порядок размещения до сортировки. Просто для наглядности работы функции. Необязательная часть.
print("\n", "Начальный список:")
for num in range(num_clear):
    print("\t", num, str_value[num][0].ljust(30, " "), "->",  str_value[num][2])

# Сортировка по автору в алфавитном порядке и проверка перед записью в файл.
str_value = sorted(str_value)
print("\n", "Проверка сортировки:")
for i in range(len(str_value)):
    print("\t", i, str_value[i][0].ljust(30, " "), "->", str_value[i][2])
print("\n")

#   Добавляется "Sep=," в начало файла для корректного чтения Exel (Windows 10).
#   Если этого не сделать, то при наличии в тексте символа ";" (точка с запятой) Exel при чтении файла автоматом
#   разрывает строку по этому символу и следующую часть строки помещает в следующую ячейку, затирая находящуюся
#   в ней информацию (URL). Типа танца с бубном для Exel (Windows 10). С этой вставкой работает без проблем.

headline = [['sep=', ''], ["Author", "Quote", "URL"]]    # Добаляем указание разделителя и заглавную строку (headline)
str_value = headline + str_value
with open(file_name, "w", newline="") as csv_file:       # записываем данные в файл
    writer = csv.writer(csv_file)
    writer.writerows(str_value)

data = []
with open(file_name, "r", newline="") as csv_file:       # считываем данные для проверки
    reader = csv.reader(csv_file)
    for line in reader:
        data.append(line)
print("Проверка записи", data, sep="\n")
