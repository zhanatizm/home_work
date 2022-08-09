seasons_list = ['ЗИМА', 'ВЕСНА', 'ЛЕТО', 'ОСЕНЬ']
month = int(input("Введите число месяца (от 0 до 12): "))
if month == 12 or month == 1 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
else:
    print("Проверьте корректность введенных данных.")
