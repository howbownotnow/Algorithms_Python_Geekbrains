'''
Среди натуральных чисел, которые были введены, найти наибольшее
по сумме цифр. Вывести на экран это число и сумму его цифр.
'''

def digit_sum(num):
    summ = 0
    while num != 0:
        summ += num % 10
        num //= 10

    return summ

ans = 0
ans_digit = 0

while True:
    num = int(input('Введите число (0, чтобы закончить): '))

    if num == 0:
        break

    digit_sum_for_num = digit_sum(num)
    if digit_sum_for_num > ans_digit:
        ans_digit = digit_sum_for_num
        ans = num

print(f'Наибольшей суммой цифр обладает число {ans}: {ans_digit}')
