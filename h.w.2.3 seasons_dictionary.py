seasons_dictionary = {1: 'ЗИМА', 2: 'ВЕСНА', 3: 'ЛЕТО', 4: 'ОСЕНЬ'}
month = int(input("Введите число месяца (от 0 до 12): "))
if month == 12 or month == 1 or month == 2:
    print(seasons_dictionary.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seasons_dictionary.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dictionary.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dictionary.get(3))
else:
    print("Проверьте корректность введенных данных.")
