'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random

size = int(input('Введите размер массива '))
limit = int(input('Введите лимит значений '))
input_list = [random.randint(1, limit) for _ in range(size)]

max_ind = 0
min_ind = 0

for i in range(len(input_list)):
    if input_list[i] > input_list[max_ind]:
        max_ind = i
    elif input_list[i] < input_list[min_ind]:
        min_ind = i

print(f'Исходный массив: {input_list}')

input_list[max_ind], input_list[min_ind] = input_list[min_ind], input_list[max_ind]

print(f'Полученный массив: {input_list}')