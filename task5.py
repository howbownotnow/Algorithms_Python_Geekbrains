a, b = input('Введите две буквы ').split()

ord_a = ord(a) - 96
ord_b = ord(b) - 96

delta = abs(ord_b - ord_a) - 1

print(f'Номер буквы {a} - {ord_a}; {b} - {ord_b}, между ними {delta} букв(ы)')