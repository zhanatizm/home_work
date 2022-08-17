from itertools import cycle, count

head = int(input('Введите начальное число: '))
tail = head * 2 + 1
print("генерируем числа: ")
for i in count(head):
    if i < tail:
        print(i)
    else:
        break
del i
print("выводим элементы списка: ")
just_list = [a for a in range(tail)]
count = 0
for b in cycle(just_list):
    if count < tail:
        print(b)
        count += 1
    else:
        break
