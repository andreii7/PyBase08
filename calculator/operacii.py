import math
def control_zero(a):
#Контроль 0 после запятой
    if int(a) == 0:
        return int(a)
    elif a%int(a) > 0:
        return a
    else:
        return int(a)

def proverka_vvoda_number(text):
#Проверка ввода чисел
    while True:
        try:
            a = float(input(text))
            return a
        except:
            print('Вас просили ввести число')


def my_sum(a,b):
    return a + b

def my_razn(a,b):
    return a - b

def my_del(a,b):
    try:
        return a / b
    except:
        print('Деление на 0')
        return None

def my_stepen(a,b):
    return a**b

def my_ostatok(a,b):
    return a % b

def my_bez_ostatka(a,b):
    return a // b

def my_umnoj(a,b):
    return a*b

KEY_OPERATIONS = {
    '+': my_sum,
    '-': my_razn,
    '*': my_umnoj,
    '**': my_stepen,
    '/': my_del,
    '//': my_bez_ostatka,
    '%': my_ostatok
                 }