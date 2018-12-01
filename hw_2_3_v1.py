# -------программа для вичисления факториал введённого натурального числа
print('''Здравствуйте.
Данная программа вичисляет факториал введённого натурального числа.
Для напоминания - Факториал числа n называется число n! = 1*2*3* ...*n, при том, что 0! = 1! = 1.''')

while True:
    factor_natur_number = 0
    print('''
Для продолжения нажмите: 1
Для выхода нажмите: 2
''')
    try:
        vubor_menu = int(input())
    except:
        continue
    if vubor_menu == 2:
        break
    elif vubor_menu == 1:
        while True:
            try:
                natur_number = int(input('Введите натуральное число:'))
            except:
                print('Вы ввели не натуральное число')
                continue
            if natur_number < 1:
                print('Натуральное число не может быть меньше 1, хотя 0!=1.')
                continue
            break
        for i in range(0,natur_number+1,1):
            if i == 0 or i == 1:
                factor_natur_number = 1
            else:
                factor_natur_number = factor_natur_number * i
        print('Факториал введённого Вами числа {}! = {}'.format(natur_number,factor_natur_number))
print('''
Вы вышли из программы
''')