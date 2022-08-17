import functools

new_list = [el for el in range(100, 1001) if el % 2 == 0]
product_of_multiplication = functools.reduce(lambda a, b: a * b, new_list)
print(
    f'Cписок чётных чисел от 100 до 1000 \n {new_list} \n Результат умножения элементов списка: \n {product_of_multiplication}')
