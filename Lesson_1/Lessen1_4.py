number = int(input('Введите целое положительное число, больше 0: '))
max_numb = number % 10 #если остаток от деления 0, то самая большая цифра
number = number // 10 # если остаток от деления не равен 0, то это не самая цифра, определяем остаток
while number > 0: # проверяем остаток, если 0, то самая большая цифра
    if number % 10 > max_numb: # сравниваем остаток с максимальной цифрой
        max_numb = number % 10 #  присваиваем мах цифру
        number = number // 10 # получаем  остаток и присваиваем значение и в начало цикла
print('Максимальная цифра в числе', max_numb)
