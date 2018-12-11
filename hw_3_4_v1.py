# -------программа которая принимает в качестве параметра текст и
# возвращает словарь переводов слов из введённого пользователем текста
dict2 = {}
def get_vocabluary(text):
#функция выявления неизвестных слов, составления словаря
    result = ''
    dict1 = {}
    dict3 = {}
    transl_word = ''
    text1 = text
    punctuation_str = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'

    for i in punctuation_str:
        text = text.replace(i, ' '+i)
    for i in punctuation_str:
        text1 = text1.replace(i, ' ')
    dict1 = text1.lower().split()

    if len(dict2) == 0:
        for i in dict1:
            dict2[i] = None
#    print(dict2)
    for i in dict1:
        try:
            dict2[i]
        except:
            dict2[i] = None

    for i in dict1:
        if dict2[i] == None:
            x = 0
            while x < 1:
                print('Input translete for', i)
                transl_word = input()
                if transl_word == '':
                    x = 0
                else:
                    z = 0
                    for j in transl_word:
                        if j in punctuation_str:
                            z += 1
                    if z != 0:
                        x = 0
                    else:
                        z = 0
                        x =1

            dict2[i] = transl_word
    dict3 = text.lower().split()
    for i in dict3:
        if i in dict2:
            result = result + ' ' + dict2[i]
        else:
            result = result + i

    return result



def main():
    if __name__ == "__main__":
        TEXT = """Здесь определяется текст на котором будет продемонстрирована правильность работы программы.
    Текст должен быть многострочным.

    В тексте должны быть пустые строки
    и использоваться знаки из whitespace, например """ + "\t" + """табуляция"""

    vocabluary = get_vocabluary(TEXT)
    print(vocabluary)
    return
print('''Программа, которая принимает в качестве параметра текст и возвращает перевод слов из введённого пользователем текста.
Для демонстрации текст задаётся в программе как переменная TEXT, а дальше при вводе текста пользователем. 
Если введенного(уникального) слова нет в словаре, то программа запросит его перевод. В функции для каждого уникального 
слова (т.е. ранее не встречавшегося и для которого не был дан перевод) запрашивает перевод этого слова, например на английский.
Программа вызывает функцию, получает результат и выводит на экран переводов слов из текста.
В данной программе нельзя удалить слово из словоря (пока), и разные слова могут иметь один и тотже перевод. 
В самом начале программа выполнит операции с зашитым текстом, а потом предоставит Вам возможность ввести свой текст, если встретятся
неизвезтные слова, программа запросит их перевод и потом выведит переведенный текст.
''')
main()
Text = ''
while True:

    print('''Continue? 1 - yes
          2 - no
          3 - print vocabulary''')
    try:
        vubor_menu = int(input())
    except:
        continue
    if vubor_menu == 2:
        break
    elif vubor_menu == 1:
        while True:
            Text1 = ''
            Text1 = input('Enter word:')
            if Text1 == '':
                print(get_vocabluary(Text))
                Text = ''
                break
            else:
                Text = Text + ' ' + Text1
    elif vubor_menu == 3:
#можно сделать функцию по красивому выводу информации в ровной таблице
        dlinna_word = 0
        for i in dict2:
            if len(i) > dlinna_word:
                dlinna_word = len(i)
        dlinna_key = 0
        for i in dict2:
            if len(str(dict2[i])) > dlinna_key:
                dlinna_key = len(str(dict2[i]))
        print('-' * dlinna_word + '-' * dlinna_key + '-' * 9)
        for i in dict2:
            print('|', i, ' ' * (dlinna_word - len(i)), '|', dict2[i], ' ' * (dlinna_key - len(str(dict2[i]))), '|')
        print('-' * dlinna_word + '-' * dlinna_key + '-' * 9)
    else:
        continue
print('End')

