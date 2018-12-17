from string import whitespace, punctuation, digits, ascii_letters

class MyError(ValueError):
    pass
def my_print_error(i,x):
#    print('Valueerror : символ {} в позиции {}'.format(i, x))
    pass

def clear_word(word,filterstr):

    """
    Функция по очистке слова от заданных символов.
    * Если в слове есть символ не английского алфавита,
        то необходимо вызвать исключение ValueError
        и в сообщении передать сам неверный символ и его позицию.

    :param word: строка
    :param filter: строка из символов, которые надо убрать из строки, переданной в параметре word
    :return: result - строка из параметра word, очищенная от символов, содержащихся в параметре filterstr
    """

#Проверка введенного слова на отсутствие символов не английского алфавита
    x = 0

    for i in word:
        try:
            if i not in (ascii_letters + digits + punctuation + whitespace):
                raise MyError
            else:
                x += 1
        except MyError:
#            word = word[:x] + word[x+1:]
            word = ''
            my_print_error(i,x)

# Проверка введенного символа для очистки на отсутствие символов не английского алфавита
    x = 0
    for i in filterstr:
        try:
            if i not in (ascii_letters + digits + punctuation + whitespace):
                raise MyError
            else:
                x += 1
        except MyError:
#            word = word[:x] + word[x + 1:]
            word = ''
            my_print_error(i,x)
    result = word.translate({ord(i): '' for i in filterstr})

    return result

def get_eng_words(text):
    result = list()
    for i in range(len(text)):
        text[i] = text[i].lower()

    for i in text:
        if i not in result and i != '':
            result.append(i)

    """
    Функция из заданного текста формирует список слов, которые состоят исключительно из символов
    английского алфавита.

    :param text: текст в виде списка строк.
        В строке допустимы любые символы в любом регистре, а также
        * знаки препинания (string.punctuation),
        * цифры (string.digits)
        * непечатаемые символы (string.whitespace)

    :return: result - список строк, где каждая строка - это слово:
        * Слова состоят исключительно из символов английского алфавита в нижнем регистре.
        * Слова не должны повторяться.
    """

    return result

def main():
    if __name__ == "__main__":
    # Ниже вместо ... можете вставить свой блок кода для демонстрации работы функции или отладки.
    # Этот код проверяться и оцениваться не будет
        s = '''["What is world?", "World is peace!", "В Data Science язык программирования Python\tнашёл широкое применение.", 
        "непRавильные сл0ва сЦ1фрам - 123"]'''

        j_list_1 = list()
        j_list = s.split()
        for i in range(len(j_list)):
            j_list_1.append(clear_word(j_list[i], punctuation+digits))
#        st = get_eng_words(j_list_1)
#        for i in st:
#                print(i)
        print(get_eng_words(j_list_1))

main()