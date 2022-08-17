def fact(n):
    f = 1
    for i in range(n + 1):
        yield f'{i}! = {f}'
        f *= i + 1

# print(*fact(int(input("Факториал числа: "))), sep = "; ") #вывод в ряд
for el in fact(int(input("Факториал числа: "))):
    print(el)