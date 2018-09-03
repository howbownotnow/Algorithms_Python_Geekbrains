'''
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны любому из чисел в диапазоне от 2 до 9.
'''

ans = {k: 0 for k in range(2, 10)}
for i in range(2, 100):
    for key in ans:
        if i % key == 0:
            ans[key] += 1

for key in ans.keys():
    print(f'числу {key} кратны {ans[key]} чисел в диапазоне от 2 до 99')
