'''
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''


a, b, c = map(int, input('Введите три числа ').split())

if a > b:
    if b > c:
        print(f'Среднее {b}')
    elif a > c:
        print(f'Среднее {c}')
    else:
        print(f'Среднее {a}')
elif b > c:
    if a > c:
        print(f'Среднее {a}')
    else:
        print(f'Среднее {c}')
else:
    print(f'Среднее {b}')
