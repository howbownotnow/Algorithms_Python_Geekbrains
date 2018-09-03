'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
так и различаться.
'''

import random

size = int(input('Введите размер массива '))
limit = int(input('Введите лимит значений '))
input_list = [random.randint((-1)*limit, limit) for _ in range(size)]

min_ind = 0
second_min_ind = 0

for i in range(len(input_list)):
    if input_list[i] <= input_list[min_ind]:
        second_min_ind = min_ind
        min_ind = i
    elif input_list[i] <= input_list[second_min_ind]:
        second_min_ind = i

print(f'Для массива {input_list} сумма двух минимальных элементов равна {input_list[min_ind] + input_list[second_min_ind]}')