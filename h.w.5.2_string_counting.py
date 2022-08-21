with open('text_4.txt', 'r', encoding='utf-8') as info:
    words = [f'В {count}-строке: "{line.strip()}" {len(line.split())} слова' for count, line in enumerate(info, 1)]
    print(*words, f'А строк всего: {len(words)}', sep='\n')
