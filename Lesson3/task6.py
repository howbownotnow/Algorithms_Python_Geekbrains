'''
В одномерном массиве найти сумму элементов, находящихся между минимальным
и максимальным элементами. Сами минимальный и максимальный элементы
в сумму не включать.
'''
import random

size = int(input('Введите размер массива '))
limit = int(input('Введите лимит значений '))
l = [random.randint((-1)*limit, limit) for _ in range(size)]

max_ind = 0
min_ind = 0

for i in range(len(l)):
    if l[i] > l[max_ind]:
        max_ind = i
    elif l[i] < l[min_ind]:
        min_ind = i

ans = 0

for k in range(min_ind + 1, max_ind):
    ans += l[k]

print(f'Сумма элементов между максимальным и минимальным для массива {l} равна {ans}')