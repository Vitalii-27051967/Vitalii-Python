value_1 = input("Введите число: ")
value_1 = int(value_1)

if value_1 % 5 == 0:
    print("умноженное на 2 значение = ", value_1 * 2)
else:
    print("Значение = ", 0)

###############################

value_2 = input("Введите номер месяца: ")
value_2 = int(value_2)

if value_2 == 1:
    print("Январь")
elif value_2 == 2:
    print("Февраль")
elif value_2 == 3:
    print("Март")
elif value_2 == 4:
    print("Апрель")
elif value_2 == 5:
    print("Май")
elif value_2 == 6:
    print("Июнь")
elif value_2 == 7:
    print("Июль")
elif value_2 == 8:
    print("Август")
elif value_2 == 9:
    print("Сентябрь")
elif value_2 == 10:
    print("Октябрь")
elif value_2 == 11:
    print("Ноябрь")
elif value_2 == 12:
    print("Декабрь")
elif value_2 > 12:
    print("Нет такого месяца!!!")

###############################

value_3 = input("Введите название месяца: ")
value_3 = str(value_3)

if value_3 == "Январь" or value_3 == "январь":
    print("Количество дней =",31)
elif value_3 == "Февраль" or value_3 == "февраль":
    print("Количество дней =",28)
elif value_3 == "Март" or value_3 == "март":
    print("Количество дней =",31)
elif value_3 == "Апрель" or value_3 == "апрель":
    print("Количество дней =",30)
elif value_3 == "Май" or value_3 == "май":
    print("Количество дней =",31)
elif value_3 == "Июнь" or value_3 == "июнь":
    print("Количество дней =",30)
elif value_3 == "Июль" or value_3 == "июль":
    print("Количество дней =",31)
elif value_3 == "Август" or value_3 == "август":
    print("Количество дней =",31)
elif value_3 == "Сентябрь" or value_3 == "сентябрь":
    print("Количество дней =",30)
elif value_3 == "Октябрь" or value_3 == "октябрь":
    print("Количество дней =",31)
elif value_3 == "Ноябрь" or value_3 == "ноябрь":
    print("Количество дней =",30)
elif value_3 == "Декабрь" or value_3 == "декабрь":
    print("Количество дней =",31)
else:
    print("Нет такого месяца в русском языке!!!")

###############################
