def exp(x, y):
    try:
        expon = x ** y
    except TypeError:
        return "Проверьте корректность данных"
    return expon


print(exp(float(input("Введите число: ")), float(input("В какую степень возвести: "))))
