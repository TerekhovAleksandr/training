number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
if number_1 > number_2:
    print(f'{number_1} больше {number_2}')
elif number_2 > number_1:
    print(f'{number_2} больше {number_1}')
else:
    print('Числа равны')
