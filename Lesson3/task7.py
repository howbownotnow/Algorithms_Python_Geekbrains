'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
так и различаться.
'''

import random

size = int(input('Введите размер массива '))
limit = int(input('Введите лимит значений '))
l = [random.randint((-1)*limit, limit) for _ in range(size)]

min_ind = 0
second_min_ind = 0

for i in range(len(l)):
    if l[i] <= l[min_ind]:
        second_min_ind = min_ind
        min_ind = i
    elif l[i] <= l[second_min_ind]:
        second_min_ind = i

print(f'Для массива {l} сумма двух минимальных элементов равна {l[min_ind] + l[second_min_ind]}')