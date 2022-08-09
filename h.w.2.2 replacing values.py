l = input("Ваш список: ").split()
l_length = len(l)
for i in range(0, l_length - 1, 2):
    l[i], l[i + 1] = l[i + 1], l[i]
print("Значения элементов списка изменены: " + str(l))
