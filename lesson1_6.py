result_st = int(input("Введите начальный результат пробежки: "))
result_fn = int (input("Введите планируемый результат пробежки: "))
i = 1
print(i,'-й день',result_st)
while result_st < result_fn:
    step = 1.1
    i += 1
    result_st = result_st*step
    print("%s"%i,'- й день', "%.2f"% result_st)
if result_st > result_fn:
    print('На', i,'- й день спортсмен достиг результата - не менее',result_fn,'км')
