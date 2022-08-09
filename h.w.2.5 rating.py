users_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Исходный рейтинг - {users_list}")
users_new_digit = int(input("Введите новое натуральное число (от бесконечности до 0): "))
while users_new_digit != int:
    for i in range(len(users_list)):
        if users_list[i] == users_new_digit:
            users_list.insert(i + 1, users_new_digit)
            break
        elif users_new_digit <= 0:
            print("!ТОЛЬКО НАТУРАЛЬНЫЕ ЧИСЛА!")
            break
        elif users_list[0] < users_new_digit:
            users_list.insert(0, users_new_digit)
        elif users_list[-1] > users_new_digit:
            users_list.append(users_new_digit)
    else:
        print("!ТОЛЬКО НАТУРАЛЬНЫЕ ЧИСЛА!")
    print(f"Обновлённый список - {users_list}")
    users_new_digit = int(input("Введите новое натуральное число (от бесконечности до 0): "))
