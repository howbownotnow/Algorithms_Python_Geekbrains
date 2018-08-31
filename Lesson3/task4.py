'''
Определить, какое число в массиве встречается чаще всего.
'''

import random

size = int(input('Введите размер массива '))
limit = int(input('Введите лимит значений '))
l = [random.randint((1, limit) for _ in range(size)]

ans_dict = {}

for i, elem in enumerate(l):
    if elem not in ans_dict:
        ans_dict[elem] = 1
    else:
        ans_dict[elem] += 1

ans_index = 0
ans = 0
for key, val in ans_dict.items():
    if val >= ans_index:
        ans_index = val
        ans = key

print(f'В массиве {l} наиболее часто встречается элемент {ans}')
