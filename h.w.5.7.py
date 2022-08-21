import json

with open("for_7th_task.json", "w", encoding="utf-8") as doc_2, open("text_7.txt", encoding="utf-8") as doc:
    income = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in doc}
    income_filter = [i for i in income.values() if i > 0]
    average_income = [income, {'average_profit': round(sum(income_filter) / len(income_filter))}]
    json.dump(average_income, doc_2, ensure_ascii=False, indent=4)
