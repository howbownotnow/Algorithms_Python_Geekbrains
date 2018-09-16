'''
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найти в массиве медиану. Медианой называется элемент ряда, делящий его
на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше ее.
'''

import random

m = int(input('Длина массива составит 2m+1. Введите m '))

n = 2 * m + 1

array = [random.randint(0, 100) for _ in range(n)]

print(f'Исходный массив:\n{array}')

for i in range(len(array)):
    median = array[i]
    counter_left = 0
    equals_num = 0

    for j in range(len(array)):
        # Предотвращаем сравнение с самим собой
        if i != j:
            if median > array[j]:
                counter_left += 1
            elif median == array[j]:
                equals_num += 1

    # Цикл работает до тех пор, пока не найдется элемент, для которого
    # Количество элементов меньше него будет равно половине списка
    if equals_num != 0:
        if counter_left < len(array) // 2 and counter_left + equals_num >= len(array) // 2:
            # Если есть равные элементы, и суммарное количество меньших
            # и равных больше половины длины массива, то медианой будет
            # один из равных элементов
            break
    else:
        if counter_left == len(array) // 2:
            break

# Раскомментировать для наглядной проверки медианы:
# print(f'Отсортированный массив:\n{sorted(array)}')

print(f'Медиана массива: {median}')
