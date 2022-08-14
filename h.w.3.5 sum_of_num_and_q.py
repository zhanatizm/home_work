def sum_func():
    c = 0
    while True:
        err = False
        in_list = input("Введите числа через пробел, q для выхода: ").split()
        for num in in_list:
            if num.lower() == "q":
                return c
            else:
                try:
                    c += int(num)
                except ValueError:
                    err = True
        if err:
            print("Проверьте корректность данных!")
        print(f"Сумма чисел = {c}")

print(sum_func())