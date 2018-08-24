y = int(input('Введите год '))

if y % 400 == 0:
	print('Високосный')

elif y % 100 == 0:
	print('Невисокосный')

elif y % 4 == 0:
	print('Високосный')

else:
	print('Невисокосный')