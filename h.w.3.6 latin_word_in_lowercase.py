def f():
    for word in input("Введите слова в латинице и в нижнем регистре: ").split():
        c = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                c += 1
        print(word.title() if c == len(word) else f"Только слова на латинице и в нижнем регистре!")


f()
