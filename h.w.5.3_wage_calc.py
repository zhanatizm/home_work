def wage_cal():
    wages = {}
    try:
        with open('text_3.txt', 'r', encoding='utf-8') as doc:
            for line in doc:
                wages[line.split()[0]] = float(line.split()[1])
            print('Сотрудники с ЗП менее 20тыс: ')
            for name, wage in wages.items():
                if wage < 20_000:
                    print(name)
            print(f'Средняя ЗП сотрудников = {sum(wages.values()) / len(wages)}')
    except IOError:
        print("Файл не найден")


wage_cal()
