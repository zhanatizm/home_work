users_dict = {"One": "Один", "Two": "Два", "Three": "три", "Four": "Четыре"}
with open('Я_родился.txt', 'w', encoding='utf-8') as new_doc:
    with open('text_4.txt', encoding='utf-8') as users_doc:
        new_doc.writelines([line.replace(line.split()[0], users_dict.get(line.split()[0])) for line in users_doc])
