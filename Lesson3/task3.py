'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random

import random

size = int(input('Введите размер массива '))
limit = int(input('Введите лимит значений '))
l = [random.randint(1, limit) for _ in range(size)]

max_ind = 0
min_ind = 0

for i in range(len(l)):
    if l[i] > l[max_ind]:
        max_ind = i
    elif l[i] < l[min_ind]:
        min_ind = i

print(f'Исходный массив: {l}')

l[max_ind], l[min_ind] = l[min_ind], l[max_ind]

print(f'Полученный массив: {l}')