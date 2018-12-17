import msvcrt
import re
from sys import stdout
from operacii import *

#------------------------------------Ввод и проверка символов
x = 1 # значения для цикла ввода и проверки символов
a = 0 # индекс для списка
d = ''
number_sum = 0
split_number = []
split_operac = []
first_numbers = ''
str1 = '+-%/*'
str2 = '/*+-%'
str3 = '0123456789.='
str7 = ''
print('''Введите первое число, знак операции( +, -, *, **, /, //, % ), второе число и поставте знак = 
      можно и так 1+2+3+4+5+6+7+8+9= 
      : ''')
while x == 1:

    if msvcrt.kbhit():
        str4 = msvcrt.getch()
        str5 = str(str4)
        str5 = re.sub(r"[@\'b]", '', str5)
        if str5 in str3:
            first_numbers = first_numbers + str5
            stdout.write(str5)
            stdout.flush()
        if str5 in str1:
            first_numbers = first_numbers + str5
            stdout.write(str5)
            stdout.flush()
        if str4 == b'=':
            x = 0

# Анализ операндов, операций и их веса
str6 = ''
for i in first_numbers:
    if i == '=':
        split_number.append(str6)
        str6 = ''
        break
    elif i not in str2:
        str6 = str6 + i
        if d != '':
            split_operac.append(d)
            d = ''
    else:
        if str6 == '' and d != '':
            if d == '+' and i == '+':
                split_operac.append('+')
            elif d == '-' and i == '-':
                split_operac.append('+')
            elif d == '-' and i == '+':
                split_operac.append('-')
            elif d == '+' and i == '-':
                split_operac.append('-')
            else:
                split_operac.append(d*2)
            d = ''
        if str6 != '' and d == '':
            split_number.append(str6)
            d = i
            str6 = ''


list_operat =['**','*','/','//','%','+','-']

if len(split_operac) == 0:
    print((split_number[0]))
else:
    while len(split_operac):
        i = 0
        j = 0
        while i < len(list_operat):
            while j < len(split_operac):
                if list_operat[i] == split_operac[j]:
                    a = j
                    j = len(split_operac)
                    i = len(list_operat)
                else:
                    j += 1
            i += 1
            j = 0
        i = 0
        if split_operac[a] == '*':
            number_sum = my_umnoj(float(split_number[a]),float(split_number[a+1]))
            del split_operac[a]
            del split_number[a+1]
            split_number[a] = str(number_sum)

        elif split_operac[a] == '**':
            number_sum = my_stepen(float(split_number[a]),float(split_number[a+1]))
            del split_operac[a]
            del split_number[a+1]
            split_number[a] = str(number_sum)

        elif split_operac[a] == '%':
            number_sum = my_ostatok(float(split_number[a]),float(split_number[a+1]))
            del split_operac[a]
            del split_number[a+1]
            split_number[a] = str(number_sum)

        elif split_operac[a] == '//':
            number_sum = my_bez_ostatka(float(split_number[a]),float(split_number[a+1]))
            del split_operac[a]
            del split_number[a+1]
            split_number[a] = str(number_sum)

        elif split_operac[a] == '/':
            try:
                number_sum = my_del(float(split_number[a]),float(split_number[a+1]))
                del split_operac[a]
                del split_number[a+1]
                split_number[a] = str(number_sum)
            except ZeroDivisionError as e:
                split_number[0] = e
                break
        elif split_operac[a] == '+':
            number_sum = my_sum(float(split_number[a]),float(split_number[a+1]))
            del split_operac[a]
            del split_number[a+1]
            split_number[a] = str(number_sum)

        elif split_operac[a] == '-':
            number_sum = my_razn(float(split_number[a]),float(split_number[a+1]))
            del split_operac[a]
            del split_number[a+1]
            split_number[a] = str(number_sum)

    print(split_number[0])


