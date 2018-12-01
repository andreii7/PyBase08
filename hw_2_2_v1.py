# -------программа для вичисления сумм всех натуральных чисел от меньшего до большего (включительно).
import math
print('''Здравствуйте.
Данная программа вичисляет сумму всех натуральных чисел от меньшего до большего (включительно).''')

while True:
    summa_natur_number = 0
    napravlenie_natur_number = 0
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
                first_number = float(input('Введите первое число:'))
            except:
                print('Вы ввели не число')
                continue
            if first_number < 1:
                print('Натуральное число не может быть меньше 1')
                continue
            break
        while True:
            try:
                second_number = float(input('Введите второе число:'))
            except:
                print('Вы ввели не число')
                continue
            if second_number < 1:
                print('Натуральное число не может быть меньше 1')
                continue
            break
        if second_number < first_number:
            second_number,first_number = first_number,second_number
            napravlenie_natur_number = 1
        for i in range(int(math.ceil(first_number)),int(math.floor(second_number))+1,1):
            summa_natur_number = summa_natur_number + i
        if napravlenie_natur_number == 1:
            second_number,first_number = first_number,second_number
            napravlenie_natur_number = 2
        if first_number % int(first_number) == 0:
            first_number = int(first_number)
        if second_number % int(second_number) == 0:
            second_number = int(second_number)
        print('Сумма натуральных чисел от {} до {} равна {}'.format(first_number,second_number,summa_natur_number))
print('''
Вы вышли из программы
''')