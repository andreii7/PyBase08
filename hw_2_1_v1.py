# ----программа для решения квадратного уравнение
print('''Здравствуйте.
Сегодня мы с Вами будем решать квадратное уравнение вида

           a*x*x + b*x + c = 0
           ''')
while True:
    print('''Для продолжения нажмите: 1
Для выхода нажмите: 2''')
    try:
        vubor_menu = int(input())
    except:
        continue
    if vubor_menu == 2:
        break
    elif vubor_menu == 1:
        while True:
            try:
                a= float(input('Введите коэффициент а:'))
            except:
                print('Вы ввели не число')
                continue
            if a == 0:
                print('Вы решаете квадратное уравнение, необходимо ввести не нулевой коэфициент а')
                continue
            break
        while True:
            try:
                b = float(input('Введите коэффициент b:'))
            except:
                print('Вы ввели не число')
                continue
            break
        while True:
            try:
                c = float(input('Введите свободный член c:'))
            except:
                print('Вы ввели не число')
                continue
            break
        try:
            D = b**2-4*a*c
            if D > 0:
                print('''
            Дискриминант квадратного уравнения D > 0,
            тогда корни урвнения Х1 = {} и X2 = {}
            '''.format(round((-b+(D**0.5))/(2*a),3),round((-b-(D**0.5))/(2*a),3)))
            elif D == 0:
                print('''
            Дискриминант квадратного уравнения D > 0,
            тогда корни урвнения Х1 =  X2 = {}
            '''.format(round(-b/(2*a)),3))
            else:
                if b == 0:
                    print('''
            Дискриминант квадратного уравнения D < 0,
            в этом случае корни уравнение содержат комплексные числа
            X1 = {0.imag:+.3f}j и X2 = {1.imag:+.3f}j
            '''.format(((abs(D) ** 0.5) / (2 * a)) * 1j,- 1j * ((abs(D) ** 0.5) / (2 * a))))
                else:
                    print('''
            Дискриминант квадратного уравнения D < 0,
            в этом случае корни уравнение содержат комплексные числа
            X1 = {0.real:.3f}{0.imag:+.3f}j и X2 = {1.real:.3f}{1.imag:+.3f}j
            '''.format(-b/(2*a)+((abs(D)**0.5)/(2*a))*1j,-b/(2*a)-1j*((abs(D)**0.5)/(2*a))))

        except:
            print('Деление на ноль')

print('Вы вышли из программы по решению квадратного уравнения')