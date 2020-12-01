# # 2) Создать словарь triangle в который записать точки A B C (ключи),
# # и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random
# # в диапазоне от -10 до 10 по каждой оси.
#
# import random
#
#
# def xyz():
#     x_y_z = tuple([random.randrange(-10, 10) for _ in range(3)])
#     return x_y_z
#
#
# triangle = {"A": xyz(), "B": xyz(), "C": xyz()}
# print(triangle)
#
# # 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# # с тремя символами * вначале и в конце строки.
# # Пример:
# # my_str = 'I'm the string'
# # Печатает ***I'm the string***
#
# my_str = "I'm the string"
#
# def my_print(str_d):
#     print("***" + str_d + "***")
#
#
# my_print(my_str)


# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.

persons = [{"name": "John", "age": 15}, {"name": "John", "age": 30}, {"name": "Jack", "age": 45}]

# per_1 = persons[0]
# per_2 = persons[1]
# per_3 = persons[2]
#
# print(per_1["name"])
# print(per_2["name"])
# print(per_3["name"])

for dig in range(len(persons)):
    print(persons[dig]["name"])


aaa = 0

for dig in range(len(persons)):
    print(persons[dig]["age"])
    aaa += persons[dig]["age"]
print(aaa/len(persons))




# def create_ip():
#     ip = ".".join([str(random.randrange(256)) for _ in range(4)])
#     # print("---->", ip_1) # ООООЧЕНЬ плохо
#     return ip
#
#
# def create_list_ip(count: int):
#     return [create_ip() for _ in range(count)]
#
# def special_print(*args):
#     new_list = []
#     for str_ in args:
#         if random.randrange(2):
#             str_ = str_[::-1]
#         new_list.append(str_)
#     print(*new_list)
#
# special_print("QWE", "ASD", "ZXC", "wer", "xcvbnmm")
#
# ip_1 = ".".join([str(random.randrange(-10, 10)) for _ in range(3)])
# ip_2 = ".".join([str(random.randrange(-10, 10)) for _ in range(3)])
# ip_3 = ".".join([str(random.randrange(-10, 10)) for _ in range(3)])
#
# print(ip_1, ip_2, ip_3, sep="\n")
# print(ip_1, type(ip_1))