# Основа ДЗ - ДЗ №8 https://github.com/30nt/IntroProHillel/blob/main/Homeworks/lesson8.txt
#
# Суть задания - сздать класс EmailGenerator
#
# 1. При инициализации класса передавать два параметра - путь к файлу domains.txt и путь к файлу names.txt
# Пример:
# email_generator = EmailGenerator("domains.txt", "names.txt")
#
# 2. Атрибуты экземпляра класса: domains и names.
# Получаются с помощью методов get_domains() и get_names(). (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# self.domains = get_domains()
# self.names = get_names()
#
# 3. При выводе на печать экземпляра класса вывести количество элементов в атрибутах domains и names
# Пример:
# print(email_generator)
# >>>len domains = 8, len names = 34
#
# 4. Написать метод экземпляра класса generate_email() (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# email = email_generator.generate_email()
# print(email)
# >>>miller.249@sgdyyur.com

import os
import random
import string

my_dir = "c:/Files for Me"                      # моя рабочая директория
check_file = os.path.exists(my_dir)             # проверяю наличие папки по заданному пути.
print("Проверка наличия папки -->", check_file)
if check_file is False:                         # если папка не существувет, то создаём её.
    os.mkdir(my_dir)
os.chdir(my_dir)

path_d = "C:/Files for Me/domains.txt"
path_n = "C:/Files for Me/names.txt"


class EmailGenerator:
    def __init__(self, path_domains, path_names):
        self.path_domains = path_domains            # путь к файлу "domains.txt"
        self.path_names = path_names                # путь к файлу "names.txt"
        self.clear_d = self.write_domains()     # определение функции write_domains() и её результата clear_d
        self.clear_n = self.write_name()        # определение функции write_name() и её результата clear_d

    def write_domains(self):        # создание и обработка списка доменов
        cl = []
        with open(self.path_domains, "r") as file:
            [cl.append(line.strip()) for line in file.readlines()]
        clear_d = [cl[i].replace(".", "") for i in range(len(cl))]
        return clear_d

    def write_name(self):           # создание и обработка списка имён
        names_1 = []
        with open(self.path_names, "r") as file:
            [names_1.append(line.strip()) for line in file.readlines()]
        names_2 = []
        [names_2.append(names_1[dig].split("\t")) for dig in range(len(names_1))]   # разбивка по разделителю
        clear_n = []                                                                # создание списка имён
        [clear_n.append(number[1]) for number in names_2]
        return clear_n

    def rnd_email(self):           # генерация email с использованием данных из clear_d и clear_d (имён и доменов)
        rand_int = random.randint(100, 999)                                 # случайные числа от 100 до 999
        domains = self.clear_d[random.randint(0, len(self.clear_d) - 1)]    # случайные домены из cl_domains
        names = self.clear_n[random.randint(0, len(self.clear_n) - 1)]      # случайные имена из clear_name
        letters = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 7)))   # случ. буквы
        r_mail = f"{names}.{rand_int}@{letters}.{domains}"                  # сборка адреса из составляющих
        return r_mail


email_generator = EmailGenerator(path_d, path_n)

print("\n\n", "Проверка работы функций:")
dom = email_generator.write_domains()
print("Домены:", "\n", dom, "\n", "Количество доменов: ", len(dom))

nam = email_generator.write_name()
print("Имена:", "\n", nam, "\n", "Количество имён:", len(nam))

soap = email_generator.rnd_email()
print("\n", "Сгенерированный адрес:", soap, end="\n\n")

