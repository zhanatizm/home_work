subj_dict = {}
with open('учебная_программа.txt', encoding='utf-8') as doc:
    for line in doc:
        subj_t = []
        subj = ([el for el in line.split(" ")])
        for el in subj:
            subj_t.append(''.join(i for i in list(el) if i.isdigit()))
        subj_dict[line.split(':')[0]] = sum([int(i) for i in subj_t if i.isdigit()])
print(f"Общее количество занятий по предметам: {subj_dict}")
