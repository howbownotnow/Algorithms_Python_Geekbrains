'''
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
'''

import random

size = int(input('Введите размер массива '))
limit = int(input('Введите лимит значений '))
l = [random.randint((-1)*limit, limit) for _ in range(size)]

# Находим первое отрицительное число, чтобы затем сравнивать с ним остальные
for i in range(len(l)):
    if l[i] < 0:
        max_negative_index = i
        max_negative = l[i]
        break

for k in range(len(l)):
    if l[k] < 0:
        if l[k] > max_negative:
            max_negative_index = k
            max_negative = l[k]

print(f'Максимальный отрицательный элемент массива {l} - {l[max_negative_index]} , его индекс - {max_negative_index}')