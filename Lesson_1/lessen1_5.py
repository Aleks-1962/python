revenue = float(input('Введите величину выручки в тыс.руб. '))
costs = float(input('Введите величину издержек тыс.руб '))
if revenue >= costs:
    print('Фирма работает без убытков')
    if revenue > costs:
        print('Финансовый результат в тыс.руб. =  %s' % (revenue-costs))
        fin_result = revenue-costs
        profitability = fin_result/revenue*100
        print('Рентабельность в процентах =  %s' % profitability)
        personal = int(input('Введите количество сотрудников '))
        if personal > 0:
            print('Прибыль на одного сотрудника составляет = %s' % (fin_result / personal))
        else:
            print('Количество сотрудников должно быть больше нуля')
    else:
        print('Финансовый результат = 0')
else:
    print('Фирма работает c убытками')
    print('Финансовый результат =  %s' % (revenue - costs))
