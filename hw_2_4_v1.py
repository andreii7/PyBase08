# ----Программа вычисляет элемент ряда Фибоначчи и выводит его на экран
print('''Здравствуйте.
Данная программа вичисляет элемент ряда Фибоначчи.
Для напоминания - Ряд чисел Фибоначи состоит из натуральных чисел, начиная с первых двух 1 и 1.
                  Каждое следующее число определяется как сумма двух предыдущих.
                  Пример: 1, 1, 2, 3, 5, 8, ...''')

while True:
    fibonache_number = 0
    fibonache_number_n1 = 0
    fibonache_number_n2 = 0
    str_fibonache_number = ''
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
                natur_number = float(input('Введите число для которого необходимо расчитать ряд Фибоначчи:'))
            except:
                print('Вы не ввели число')
                continue
            if natur_number < 1:
                print('Число для которого необходимо расчитать ряд Фибоначчи не может быть меньше 1.')
                continue
            break
        print('Ряд Фибоначчи для числа {} представлен ниже'.format(int(natur_number)))
        for i in range(0,int(natur_number)+1,1):
            if i < 2:
                fibonache_number_n2 = 1
                fibonache_number_n1 = 1
                fibonache_number = 1
                str_fibonache_number = '1,1'

            else:
                fibonache_number = fibonache_number_n1 + fibonache_number_n2
                fibonache_number_n1 = fibonache_number_n2
                fibonache_number_n2 = fibonache_number
                str_fibonache_number = str_fibonache_number + ',' +str(fibonache_number)
        print(str_fibonache_number)
print('''
Вы вышли из программы
''')