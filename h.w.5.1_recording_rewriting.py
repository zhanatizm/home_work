with open('temp_user_inf_1.txt', 'w', encoding='utf-8') as doc:
    while True:
        line = input('Введите строковые данные для записи в файл. (Завершение ввода - пустая строка): \n')
        if not line:
            break
        print(line, file=doc)
