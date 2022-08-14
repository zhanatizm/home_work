def charset_f(word):
    l_char = "abcdefghijklmnopqrstuvwxyz "
    return word.title() if not set(word).difference(l_char) else "ошибка входных данных"


list_of_words = input("Введите строку из слов: ").split()
a = []
for word in list_of_words:
    a.append(charset_f(word))
print(' '.join(a))