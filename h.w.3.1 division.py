def delenie(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
        dev = n1 / n2
    except ValueError:
        return "делим числа на числа, проверьте корректность данных"
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return round(dev, 5)


print(delenie(input("Делимое - "), input("Делитель - ")))
