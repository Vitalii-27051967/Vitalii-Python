# 1. Дано целое число (int). Определить сколько нулей в этом числе.
##########################################################
### Вариант 1
print("Задание 1, вариант решения 1", end="\n\n")
try:
    value_1 = input("Введите целое число для определения количества нулей в нём: ")
    value_str = str(value_1)
    my_value = 0
    for symb in value_str:
        if int(symb) == 0:
            my_value += 1
    print("Количество нолей в числе: ", my_value)
except ValueError:
    print("Это не целое число")
print(end="\n\n")

### Вариант 2

print("Задание 1, вариант решения 2", end="\n\n")
my_string = input("Введите целое число для определения количества нулей в нём: ")
old_str = len(my_string)
my_list = my_string.split("0")
my_string = ''.join(my_list)
new_str = len(my_string)
print("Количество нолей в числе: ", old_str - new_str)


# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
###########################################################

print("Задание 2", end="\n\n")
value = input("Введи целое число для определения количества нулей в конце этого числа: ")
try:
    int_value = int(value)
    revers_str = str(int_value)[::-1]
    revers_str_clean = str(int(revers_str))
    result = len(revers_str) - len(revers_str_clean)
    print("Количество нолей в конце числа: ", result)
except ValueError:
    print("Это не целое число")
print(end="\n\n")


# 3. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]
###########################################################

print("Задание 3", end="\n\n")
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = []
for symbol in my_list_1:
    if symbol % 2 == 0:
        my_result.append(symbol)
for symbol in my_list_2:
    if symbol % 2 != 0:
        my_result.append(symbol)
print(my_result)
print(end="\n\n")


# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
###########################################################

print("Задание 4", end="\n\n")
my_list = [1, 2, 3, 4]
new_list = my_list[1::].copy()
new_list.append(my_list[0])
print(new_list)
print(end="\n\n")


# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
###########################################################

print("Задание 5", end="\n\n")
my_list = [1, 2, 3, 4]
my_list.append(my_list[0])
my_list.pop(0)
print("Результат перестановки: ", my_list)
print(end="\n\n")


# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.
###########################################################

print("Задание 6", end="\n\n")
my_string = "43 больше чем 34 но меньше чем 56"
my_result = 0
array = my_string.split(" ")
for string in array:
    if string.isdigit():
        my_result += int(string)
print("Сумма чисел из списка:", my_result)
print(end="\n\n")


# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
###########################################################

print("Задание 7", end="\n\n")
my_str = 'abcde'
my_new_str = my_str
my_list = []
aaa = 0
if len(my_new_str) % 2 != 0:
    my_new_str = my_str + "_"
while aaa != len(my_new_str):
    my_list.append(my_new_str[aaa:aaa+2:])
    aaa += 2
print(my_list)
print(end="\n\n")

# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
###########################################################

print("Задание 8", end="\n\n")
my_str = "My long string"
l_limit = "o"
r_limit = "t"
dig = 0
dig_l = 0
dig_r = 0
while my_str[dig] != l_limit:
    dig += 1
    dig_l = dig
while my_str[dig] != r_limit:
    dig += 1
    dig_r = dig
sub_str = my_str[dig_l + 1:dig_r:]
print("Часть строки: ", sub_str)
print(end="\n\n")


# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
###########################################################

print("Задание 9", end="\n\n")
my_str = "My long string"
l_limit = "o"
r_limit = "g"
dig = 0
dig_l = 0
dig_r = 0
while my_str[dig] != l_limit:
    dig += 1
    dig_l = dig
dig_n = len(my_str) - 1
while my_str[dig_n] == r_limit:
    dig_n -= 1
    dig_r = dig_n
sub_str = my_str[dig_l + 1:dig_r + 1:]
print("Часть строки: ", sub_str)
print(end="\n\n")

# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
###########################################################

print("Задание 10", end="\n\n")
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
dig = len(my_list)
dig_1 = 0
my_res = 0
while dig_1 != dig - 2:
    if my_list[dig_1 + 1] > my_list[dig_1] + my_list[dig_1 + 2]:
        my_res += 1
    dig_1 += 1
print("Количество выполнения условия: ", my_res)
