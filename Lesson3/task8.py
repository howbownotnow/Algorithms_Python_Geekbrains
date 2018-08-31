'''
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.
'''

result_list = []

for i in range(5):
    row_sum = 0
    result_list.append([])
    for k in range(3):
        elem = int(input(f'Введите элемент {k + 1} строки {i + 1} '))
        result_list[i].append(elem)
        row_sum += elem
    result_list[i].append(row_sum)


for line in result_list:
    print(line)
