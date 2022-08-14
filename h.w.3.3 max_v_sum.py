def sum_max_v(n1, n2, n3):
    try:
        n_list = list(map(float, [n1, n2, n3]))
        n_list.remove(min(n_list))
        return sum(n_list)
    except (TypeError, ValueError):
        return "Проверьте корректность данных"


print(sum_max_v(input("1-аргумент: "), input("2-аргумент: "), input("3-аргумент: ")))