'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Первый - использовать алгоритм решето Эратосфена. Второй -
без использования "решета".
Проанализировать скорость и сложность алгоритмов.
'''
import cProfile


def prime_number_Er(n):
    '''
    Нахождения простого числа под номером n
    по алгоритму "решето Эратосфена"
    '''
    primes = [2, 3]

    while len(primes) < n:
        candidate = primes[-1] + 1 # для оптимизации можно сделать +2: сразу отсекаем все четные числа
        i = 0

        while i < len(primes):
            if candidate % primes[i] == 0:
                candidate += 1
                i = 0
            else:
                i += 1
        else:
            primes.append(candidate)
    return primes

# "Task2.prime_number_Er(10)"
# 100 loops, best of 3: 19.5 usec per loop

# c проходом только по нечетным числам
# "Task2.prime_number_Er(10)"
# 100 loops, best of 3: 16.8 usec per loop


# "Task2.prime_number_Er(20)"
# 100 loops, best of 3: 72.7 usec per loop

# c проходом только по нечетным числам
# "Task2.prime_number_Er(20)"
# 100 loops, best of 3: 59.8 usec per loop


# "Task2.prime_number_Er(100)"
# 100 loops, best of 3: 1.41 msec per loop

# c проходом только по нечетным числам
# "Task2.prime_number_Er(100)"
# 100 loops, best of 3: 1.32 msec per loop


# "Task2.prime_number_Er(1000)"
# 100 loops, best of 3: 139 msec per loop

# c проходом только по нечетным числам
# "Task2.prime_number_Er(1000)"
# 100 loops, best of 3: 137 msec per loop

cProfile.run("prime_number_Er(10)")
#  1    0.000    0.000    0.000    0.000 Task2.py:10(prime_number_Er)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 85    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#  8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('prime_number_Er(20)')
#   1    0.000    0.000    0.000    0.000 Task2.py:10(prime_number_Er)
#   1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 298    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#  18    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('prime_number_Er(100)')
#    1    0.002    0.002    0.002    0.002 Task2.py:10(prime_number_Er)
#    1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
# 5941    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#   98    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('prime_number_Er(1000)')
#      1    0.169    0.169    0.221    0.221 Task2.py:10(prime_number_Er)
#      1    0.000    0.000    0.221    0.221 {built-in method builtins.exec}
# 518379    0.051    0.000    0.051    0.000 {built-in method builtins.len}
#    998    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}



def prime_number(n):
    '''
    нахождение простого числа под номером n
    прямой проверкой делимости
    '''
    primes = []
    i = 1
    while len(primes) < n:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)

    return primes


# "Task2.prime_number(10)"
# 100 loops, best of 3: 27.2 usec per loop

# "Task2.prime_number(20)"
# 100 loops, best of 3: 88.1 usec per loop

# "Task2.prime_number(100)"
# 100 loops, best of 3: 2.12 msec per loop

# "Task2.prime_number(1000)"
# 100 loops, best of 3: 345 msec per loop

cProfile.run("prime_number(10)")
#  1    0.000    0.000    0.000    0.000 Task2.py:72(prime_number)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 29    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('prime_number(20)')
#  1    0.000    0.000    0.000    0.000 Task2.py:72(prime_number)
#  1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 71    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('prime_number(100)')
#   1    0.002    0.002    0.002    0.002 Task2.py:72(prime_number)
#   1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
# 541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run('prime_number(1000)')
 #    1    0.346    0.346    0.347    0.347 Task2.py:72(prime_number)
 #    1    0.000    0.000    0.347    0.347 {built-in method builtins.exec}
 # 7919    0.001    0.000    0.001    0.000 {built-in method builtins.len}
 # 1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
