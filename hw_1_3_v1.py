number_int_1 = int(input('Введите целое число: '))
print('Число в представлении целого числа:',number_int_1)
print('Число в представлении вещественного числа:',float(number_int_1))
print('Число в представлении логического значения : {}'.format(bool(number_int_1)))
print('''Число в представлении строки: '{}' '''.format(number_int_1))
number_int_2 = int(input('Введите еще целое число: '))
print('''Умножение целого представления первого числа на целое представление второго числа
    {} * {} = {}'''.format(number_int_1,number_int_2,number_int_1 * number_int_2))
print('''Сложение целого представления первого числа и целого представления второго числа
    {} + {} = {}'''.format(number_int_1,number_int_2,number_int_1 + number_int_2))
print('''Умножение вещественного представления первого числа на вещественное представление второго числа
    {} * {} = {}'''.format(float(number_int_1),float(number_int_2),float(number_int_1) * float(number_int_2)))
print('''Сложение вещественного представления первого числа и вещественного представления второго числа
    {} + {} = {}'''.format(float(number_int_1),float(number_int_2),float(number_int_1) + float(number_int_2)))
print('''Умножение вещественного представления первого числа на целое представление второго числа
    {} * {} = {}'''.format(float(number_int_1),number_int_2,float(number_int_1) * number_int_2))
print('''Сложение вещественного представления первого числа и целого представления второго числа
    {} + {} = {}'''.format(float(number_int_1),number_int_2,float(number_int_1) + number_int_2))
print('''Умножение строкового представления первого числа на целое представление второго числа
    '{}' * {} = '{}' '''.format(str(number_int_1),number_int_2,str(number_int_1) * number_int_2))
print('''Сложение строкового представления первого числа и строкового представления второго числа
    '{}' + '{}' = '{}' '''.format(str(number_int_1),str(number_int_2),str(number_int_1) + str(number_int_2)))

