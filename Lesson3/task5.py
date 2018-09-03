'''
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
'''

import random

size = int(input('Введите размер массива '))
limit = int(input('Введите лимит значений '))
input_list = [random.randint((-1)*limit, limit) for _ in range(size)]

# Находим первое отрицительное число, чтобы затем сравнивать с ним остальные
for i in range(len(input_list)):
    if input_list[i] < 0:
        max_negative_index = i
        max_negative = input_list[i]
        break

for k in range(len(input_list)):
    if input_list[k] < 0:
        if input_list[k] > max_negative:
            max_negative_index = k
            max_negative = input_list[k]

print(f'Максимальный отрицательный элемент массива {input_list} - {input_list[max_negative_index]} , его индекс - {max_negative_index}')