'''
В одномерном массиве найти сумму элементов, находящихся между минимальным
и максимальным элементами. Сами минимальный и максимальный элементы
в сумму не включать.
'''
import random

size = int(input('Введите размер массива '))
limit = int(input('Введите лимит значений '))
input_list = [random.randint((-1)*limit, limit) for _ in range(size)]

max_ind = 0
min_ind = 0

for i in range(len(input_list)):
    if input_list[i] > input_list[max_ind]:
        max_ind = i
    elif input_list[i] < input_list[min_ind]:
        min_ind = i

ans = 0

if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind

for k in range(min_ind + 1, max_ind):
    ans += input_list[k]

print(f'Сумма элементов между максимальным и минимальным для массива {input_list} равна {ans}')