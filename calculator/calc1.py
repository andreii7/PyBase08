#Простой калькулятор
from operacii import *
print('''Здравствуйте.
Это простой калькулятор, который производит операцию над двумя числами.''')
VID_OPERATIONS = ['+','-','*','**','/','//','%']
number_1,number_2 =  0,0
result = None
prov_operacii = 0

while True:
    vubor_menu = 0
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
            number_1 = proverka_vvoda_number('Введите первое число >>')
            while True:
                operacii = (input('Введите вид операции из представленых [+ - * ** / // %] >>'))
                prov_operacii = 0
                for i in range(len(VID_OPERATIONS)):
                    if operacii == VID_OPERATIONS[i]:
                        prov_operacii = 1
                if prov_operacii != 0 :
                    break
            number_2 = proverka_vvoda_number('Введите второе число >>')
            result = KEY_OPERATIONS[operacii](number_1,number_2)
            print('{} {} {} = {}'.format(control_zero(number_1),operacii,control_zero(number_2),control_zero(result)))
            break
