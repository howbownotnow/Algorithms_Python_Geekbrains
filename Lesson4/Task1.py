'''Проанализировать скорость и сложность одного - трёх любых алгоритмов,
разработанных в рамках домашнего задания первых трех уроков.'''
import cProfile


def digit_sum(num):
    '''подсчет всех цифр в числе'''
    summ = 0
    while num != 0:
        summ += num % 10
        num //= 10

    return summ

# "Task1.digit_sum(int('9'*10))"
# 100 loops, best of 3: 2.28 usec per loop
# :0: UserWarning: The test results are likely unreliable. The worst
# time (64.9 usec) was more than four times slower than the best time.

# "Task1.digit_sum(int('9'*100))"
# 100 loops, best of 3: 44.6 usec per loop

# "Task1.digit_sum(int('9'*900))"
# 100 loops, best of 3: 2.26 msec per loop

cProfile.run("digit_sum(int('9'*10))")
# 1    0.000    0.000    0.000    0.000 Task1.py:6(digit_sum)

cProfile.run("digit_sum(int('9'*100))")
# 1    0.000    0.000    0.000    0.000 Task1.py:6(digit_sum)

cProfile.run("digit_sum(int('9'*900))")
# 1    0.002    0.002    0.002    0.002 Task1.py:6(digit_sum)


def digit_sum_rec(num):
    '''подсчет всех цифр в числе с рекурсией'''
    if num == 0:
        return 0
    else:
        return num % 10 + digit_sum_rec(num // 10)

# "Task1.digit_sum_rec(int('9'*10))"       
# 100 loops, best of 3: 3.81 usec per loop
# :0: UserWarning: The test results are likely unreliable. The worst
# time (63.5 usec) was more than four times slower than the best time.

# "Task1.digit_sum_rec(int('9'*100))"
# 100 loops, best of 3: 60.7 usec per loop

# "Task1.digit_sum_rec(int('9'*900))"
# 100 loops, best of 3: 2.57 msec per loop

cProfile.run("digit_sum_rec(int('9'*10))")
# 11/1    0.000    0.000    0.000    0.000 Task1.py:31(digit_sum_rec)

cProfile.run("digit_sum_rec(int('9'*100))")
# 101/1    0.000    0.000    0.000    0.000 Task1.py:31(digit_sum_rec)

cProfile.run("digit_sum_rec(int('9'*900))")
# 901/1    0.003    0.000    0.003    0.003 Task1.py:31(digit_sum_rec)
