numb_1 = float(input("Введите первое число: "))
numb_2 = float(input("Введите второе число: "))

if numb_1 >= numb_2:
    print('Первая ветка')
    if numb_1 > numb_2:
        print('Первое число больше второго')
    else:
        print('Числа равны')
elif numb_1 <= numb_2:
    print('Вторая ветка')
    if numb_1 < numb_2:
        print('Первое число меньше второго')
    else:
        print('Числа равны')
