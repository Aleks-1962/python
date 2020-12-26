original_password = 'first'  #
password = input('Введите пароль: ')  #
access = False  #
if password == original_password:  #
    print('Вход одобрен. Приятной работы!')
    access = True
if password != original_password:  #
    print('Пароль не принят, работать нельзя')
