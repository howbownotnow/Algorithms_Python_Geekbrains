'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random

m, n = map(int, input('Введите количество строк и столбцов матрицы ').split())
limit = int(input('Введите лимит значений '))

matr = [[random.randint(1, limit) for _ in range(n)] for _ in range(m)]

for line in matr:
    print(line)

min_col = [limit + 1] * n
max_min = 0

for line in matr:
    for i, elem in enumerate(line):
        if elem < min_col[i]:
            min_col[i] = elem
            
for elem in min_col:
    if elem > max_min:
        max_min = elem

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_min}')