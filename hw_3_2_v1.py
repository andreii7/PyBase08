# -------программа для сортировки слов из текста
def obrabotka_stroki(enter_word_isodrabotka):
    enter_word_list_isobrabotka = []
    enter_word_list_1_isobrabotka = []
    digit_str = '1234567890'
    punctuation_str = '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'

    for i in punctuation_str:
        enter_word_isodrabotka = enter_word_isodrabotka.replace(i, ' ')
        enter_word_list_isobrabotka = enter_word_isodrabotka.split()
    for i in range(len(enter_word_list_isobrabotka)):
        y = 0
        for a in digit_str:
            if a in enter_word_list_isobrabotka[i]:
                y = 1
                break
        if y == 0:
            enter_word_list_1_isobrabotka.append(enter_word_list_isobrabotka[i])
    return enter_word_list_1_isobrabotka


print('''Здравствуйте.
Данная программа сортировки слов из текста. Пользователь вводит с клавиатуры строки, состоящие из слов.
Пустая строка означает прекратить ввод текста. Программа выводит на экран слова из текста, отсортированные по алфавиту.''')

while True:
    vubor_menu = 0
    print('''
Для продолжения нажмите: 1
Для выхода нажмите: 2
''')
    enter_word = ''
    enter_word_1 = ''
    enter_word_list = []
    enter_word_list_1 = []

    try:
        vubor_menu = int(input())
    except:
        continue
    if vubor_menu == 2:
        break
    elif vubor_menu == 1:
        while True:

                print('''Введите с клавиатуры строки, состоящие из слов. Вы можете нажимать Enter для ввода новой строки.
Пустая строка означает прекратить ввод текста.''')

                while True:
                    enter_word = ''
                    enter_word = input('Введите строку')
                    if enter_word == '':
                        break
                    else:
                        enter_word_1 = enter_word_1 + ' ' + enter_word
                enter_word_list_1 = obrabotka_stroki(enter_word_1)
                if len(enter_word_list_1) == 0:
                    print('Извините, нету слов')
                else:
                    print('Сортировка слов а алфавитном порядке (в данном варианте - вывод в столбик):')
                    enter_word_list_1 = sorted(enter_word_list_1)
                    for i in enter_word_list_1:
                        print(i)
                break
    else:
        continue
print('''
Вы вышли из программы
''')