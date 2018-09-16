'''
Отсортировать по убыванию методом «пузырька» одномерный целочисленный
массив, заданный случайными числами на промежутке [-100; 100).
Вывести на экран исходный и отсортированный массивы.
'''

import random

n = int(input('Введите длину массива для сортировки '))

array = [random.randint(-100, 99) for _ in range(n)]

print(f'Исходный массив:\n{array}')

def bubble_sort(array):

    for i in range(1, len(array)):
        inversion_count = 0
        for j in range(len(array) - i):

            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                inversion_count += 1

        # Если счетчик перестановок после прохода по массиву равен нулю,
        # Значит на этом этапе массив уже отсортирован, и можно прекращать
        if inversion_count == 0:
            return

        # Раскомменитровать для визуализации массива после каждого прохода
        # print(array)

bubble_sort(array)

print(f'Отсортированный по убыванию массив:\n{array}')
