number = int(input('Введите целое число: '))
if number > 0:
    tmp = str(number)
    tmp1 = tmp + tmp
    tmp2 = tmp + tmp + tmp
    summa_number = number + int(tmp1) + int(tmp2)
    print("Результат равен:", summa_number)
else:
    print("Число должно быть больше 0, вы ввели:", number)
