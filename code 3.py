# Задача 1 ##############

value_1 = int(input("1. Введите целое число (для деления или умножения): "))
new_value = value_1 / 2 if value_1 < 100 else value_1 * 2
print(new_value)

# Задача 2 ##############

value_1 = int(input("2. Введите целое число (для преобразования в 1 или 0): "))
new_value = 1 if value_1 < 100 else 0
print(new_value)

# Задача 3 ##############

value_1 = int(input("3. Введите целое число (для преобразования в True или False): "))
new_value = True if value_1 < 100 else False
print(new_value)

# Задача 4 ##############

my_str = str(input("4. Введите строчное значение (для преобразования в заглавные): "))
new_my_str = my_str.upper()
print(new_my_str)

# Задача 5 ##############

my_str = str(input("5. Введите строчное значение (для преобразования в строчные): "))
new_my_str = my_str.lower()
print(new_my_str)

# Задача 6 ##############

my_str = str(input("6. Введите строчное значение (меньше 5 - удвоение): "))
ny = len(my_str)
if ny < 5:
    new_my_str = my_str * 2
else:
    new_my_str = my_str
print(new_my_str)

# Задача 7 ##############

my_str = str(input("7. Введите строчное значение (меньше 5 - добавление перевёрнутой): "))
new_my_str = my_str + my_str[:: - 1] if len(my_str) < 5 else my_str
print(new_my_str)

# Задача 8 ##############

my_str = "Test 44string 123 QWE / / /!! !"
res = ""
for symbol in my_str:
    if symbol.isdigit() or symbol.isalpha():
        res += symbol
print("только буквы и цифры:", res, sep="")

# Задача 9 ##############

my_str = "Test 44string 123 QWE/ / /!! !"
res = ""
for symbol in my_str:
    if not(symbol.isdigit() or symbol.isalpha()):
        res += symbol
print("не буквы и не цифры:", res, sep="")

# Задача 10 ##############

my_str = "Test 44string 123 QWE/ / /!! !"
res = ""
for symbol in my_str:
    #   если строго только пробелы то if not(symbol.isdigit() or symbol.isalpha() or symbol == " "):
    if not(symbol.isdigit() or symbol.isalpha() or symbol.isspace()):
        res += symbol
print("не буквы, не цифры и не пробелы:", res, sep="")
