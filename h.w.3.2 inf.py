def inf(**kw):
    return ' '.join(kw.values())


print(inf(name=input("Введите имя: "), surname=input("Введите фамилию: "), birthday=input("Дата рождения: "),
          city=input("Введите город: "), email=input("Введите адрес эл.почты: "),
          ph_number=input("Введите номер телефона: ")))
