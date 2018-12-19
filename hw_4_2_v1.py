from string import whitespace, punctuation, digits, ascii_letters
from hw_4_1_v1 import clear_word, my_print_error


def get_eng_words(text):
    result = list()
    j_list_1 = list()
    text1 = ''
    for i in text:
        if i not in (whitespace+punctuation):
            text1 += i
        else:
            text1 += ' '
    j_list = text1.split()
    for i in range(len(j_list)):
        j_list_1.append(clear_word(j_list[i], punctuation + digits))

    for i in range(len(j_list_1)):
        j_list_1[i] = j_list_1[i].lower()

    for i in j_list_1:
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


if __name__ == "__main__":
    # Ниже вместо ... можете вставить свой блок кода для демонстрации работы функции или отладки.
    # Этот код проверяться и оцениваться не будет
    s = '''["""he Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested."
    Sparse is better than dense.""",
            "Created by Guido van Rossum and first released in 1991.",
            "Сreated by Гвидо van Rossum and first released in 1991.",
            ]
        :param text: текст в виде списка строк.
        В строке допустимы любые символы в любом регистре, а также
        * знаки препинания (string.punctuation),
        * цифры (string.digits)
        * непечатаемые символы (string.whitespace)'''


    print(get_eng_words(s))