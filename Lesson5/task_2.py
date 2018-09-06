'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это
цифры числа.
'''

a = input('Введите первое шестнадцатеричное число ')
b = input('Введите второе шестнадцатеричное число ')

####################################################################
# Первый пришедший в голову способ

# PREFIX = '0X'


# def add_hex_list(a, b):
#     x = y = PREFIX
#     for digit in a:
#         x += digit
#     for digit in b:
#         y += digit
#     return list(str(hex(int(x, 16) + int(y, 16)))[2:])


# def mul_hex_list(a, b):
#     x = y = PREFIX
#     for digit in a:
#         x += digit
#     for digit in b:
#         y += digit
#     return list(str(hex(int(x, 16) * int(y, 16)))[2:])


# a = list(a)
# b = list(b)

# print(f'Их сумма равна {add_hex_list(a, b)}')
# print(f'Их произведение равно {mul_hex_list(a, b)}')

######################################################################
# Способ более изощренный:

class HexList:

    def __init__(self, num):
        self.num = list(num)
        self.prefix = '0x'

    def __repr__(self):
        return str(self.num)

    def __add__(self, other):
        x = y = self.prefix
        for digit in self.num:
            x += digit
        for digit in other.num:
            y += digit
        return HexList(str(hex(int(x, 16) + int(y, 16)))[2:])

    def __mul__(self, other):
        x = y = self.prefix
        for digit in self.num:
            x += digit
        for digit in other.num:
            y += digit
        return HexList(str(hex(int(x, 16) * int(y, 16)))[2:])


a = HexList(a)
b = HexList(b)

print(f'Числа сохранены в следующем виде:\n{a}\n{b}')

print(f'Их сумма равна {a + b},\nИх произведение равно {a * b}')
