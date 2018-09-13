'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

import random

n = int(input('Введите длину массива для сортировки '))

array = [random.randint(0, 49) for _ in range(n)]

print(f'Исходный массив:\n{array}')

def merge_sort(array):

    if len(array) <= 1:
        return

    middle = len(array) // 2

    left = array[:middle]
    right = array[middle:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
            k += 1

        else:
            array[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

merge_sort(array)

print(f'Отсортированный массив:\n{array}')