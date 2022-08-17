from sys import argv
def wage():
    try:
        name, hours_worked, hourly_wage, prize = argv
        hours_worked = float(hours_worked)
        hourly_wage = float(hourly_wage)
        prize = float(prize)
        print(f'заработная плата сотрудника:  {hours_worked * hourly_wage + prize}')
    except ValueError:
        print("Введите числа!")
wage()