users_string = input("Введите данные в виде строки: ")
users_word = []
num = 1
for i in range(users_string.count(' ') + 1):
    users_word = users_string.split()
    if len(str(users_word)) <= 10:
        print(f" {num} {users_word[i]}")
        num += 1
    else:
        print(f" {num} {users_word[i][0:10]}")
        num += 1
