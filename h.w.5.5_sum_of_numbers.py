from random import randint
with open("I'm back.txt", mode = 'w+', encoding='utf-8') as new_doc:
    new_doc.write(' '.join([str(randint(1, 100)) for _ in range(1_000)]))
    new_doc.seek(0)
    print(f'Сумма чисел в файле равна: {sum(map(int, new_doc.readline().split()))}')