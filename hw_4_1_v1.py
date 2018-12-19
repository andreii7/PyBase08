from string import whitespace, punctuation, digits, ascii_letters

class MyError(ValueError):
    pass
def my_print_error(i,x):
    print('Valueerror : символ {} в позиции {}'.format(i, x))

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
            word = ''
            my_print_error(i,x)
    result = word.translate({ord(i): '' for i in filterstr})

    return result


if __name__ == "__main__":
    # Ниже вместо ... можете вставить свой блок кода для демонстрации работы функции или отладки.
    # Этот код проверяться и оцениваться не будет

    word = input('Введите строку с которой надо будет работать:')
    filterstr = input('''Введите символы которые надо убрать из строки выше, 
    не забывайте, что пробел - это тоже символ:''')
    j_list = []
    filterstr_true = False
    j = 0
    i = 0
    while i < len(filterstr):
        while j < len(word):
            if filterstr[i] == word[j]:
                j_list.append(j)
            j += 1
        if len(j_list) != 0:
            filterstr_true = True
            print('Символ {} встречается в строке в позициях {}'.format(filterstr[i],j_list))
            j_list.clear()
        j = 0
        i += 1

    if filterstr_true == False:
        print('В данной строке нет символов которые Вы хотели бы убрать.')
    j_list = word.split()
    for i in range(len(j_list)):
        print(clear_word(j_list[i],filterstr))