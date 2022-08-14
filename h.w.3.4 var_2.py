def exp(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            return "Проверьте корректность данных (число больше 0, степень меньше 0"
        else:
            c = 1
            for _ in range(abs(y)):
                c = c / x
            print("Возведение числа ", x, "в степень ", y, ": ")
            return round(c, 200)
    except ValueError:
        return "Проверьте корректность данных!"


n1 = input("Введите действительное положительное число, x = ")
n2 = input("Введите целое отрицательное число, y = ")

print(exp(n1, n2))
