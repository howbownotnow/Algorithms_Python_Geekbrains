'''Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования
предприятий, чья прибыль выше среднего и отдельно вывести наименования
предприятий, чья прибыль ниже среднего.
'''

import collections

n = int(input('Введите количество предприятий '))

income_list = collections.defaultdict(list)

for i in range(n):
    company = input('Введите название предприятия ')

    for j in range(4):
        income_list[company].append(int(input(f'Введите его прибыль за {j+1} квартал ')))

    # Добавляем последним элементом в список суммарный доход за год
    else:
        income_list[company].append(sum(income_list[company]))

avg_income = 0

for income in income_list.values():
    avg_income += income[4] / len(income_list)


print(f'Средняя прибыль за год составляет {avg_income}')

print('Предиприятия с прибылью выше среднего:')
for company, income in income_list.items():
    if income[4] >= avg_income:
        print(company)

print('Предиприятия с прибылью ниже среднего:')
for company, income in income_list.items():
    if income[4] < avg_income:
        print(company)
