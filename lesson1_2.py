seconds = int(input('Введите время в секундах: '))
seconds = seconds % (24 * 3600)#остаток от деления - секунды
hours = seconds // 3600 # вычисляем часы
print('Часы',hours)
seconds %= 3600
minutes = seconds // 60 # вычисляем минуты
print('Минуты',minutes)
seconds %= 60
print('Секунды',seconds) # вычисляем минуты
print ('Время в формате чч:мм:сс '+ '{0}:{1}:{2}'. format (hours, minutes, seconds))
# не придумал как добавить 0 к формату когда часы, минуты, секунды составляют один знак