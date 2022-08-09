init_time = int(input("Введите время в секундах: "))
hours = init_time // 3600
minutes = (init_time % 3600) // 60
seconds = init_time % 60
print("Преобразование времени в секундах в формате 'чч:мм:сс' - {}:{}:{}".format(hours, minutes, seconds))
