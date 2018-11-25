import time
OPE = ('Сложение {} + {} = {}','Вычитание {} - {} = {}','Умножение {} * {} = {}','Деление {} / {} = {}',
       'Получение целой части от деления {} // {} = {}','Остаток от деления {} % {} = {}',
       'Смена знака числа {}  --  {}','Модуль числа abs({}) = {}','Пара (x // y, x % y) divmod({},{}) = {}',
       'Возведение в степень {} ** {} = {}','Побитовое или {} | {} = {}')
print('''Сейчас, Вы увидите какие операции можно провести над 
двумя числами. За основу возьмем два целых числа.''')
number_1 = int(input('Введите первое целое число :'))
number_2 = int(input('Введите второе целое число :'))
time.sleep(1)
print('''Числа в Python: целые, вещественные, комплексные. Числа в
Python ничем не отличаются от обычных чисел. Они поддерживают набор 
самых обычных математических операций:''')
time.sleep(1)
print(OPE[0].format(number_1,number_2,number_1+number_2))
time.sleep(1)
print(OPE[1].format(number_1,number_2,number_1-number_2))
time.sleep(1)
print(OPE[2].format(number_1,number_2,number_1*number_2))
time.sleep(1)
print(OPE[3].format(number_1,number_2,number_1/number_2))
time.sleep(1)
print(OPE[4].format(number_1,number_2,number_1//number_2))
time.sleep(1)
print(OPE[5].format(number_1,number_2,number_1%number_2))
time.sleep(1)
print(OPE[6].format(number_1,-number_1))
time.sleep(1)
print(OPE[7].format(-number_1,abs(number_1)))
time.sleep(1)
print(OPE[8].format(number_1,number_2,divmod(number_1,number_2)))
time.sleep(1)
print(OPE[9].format(number_1,number_2,number_1**number_2))
print('Над целыми числами также можно производить битовые операции:')
time.sleep(1)
print(OPE[10].format(number_1,number_2,number_1 | number_2),' и другие битовые операции.')
print('''Над целыми числами также можно производить операции сравнение:
 x строго меньше y : x < y
 x строго больше y : x > y
 x меньше или равно y : x <= y  
 x больше или равно y : x >= y
 x равно y : x == y  
 x не равно y : x != y  
 x и y – это один и тои же объект : x is y 
 x и y не является одним и тем же объектом в памяти : x is not y''')