import re

text = ('Жирафы любят таскать различные __СУЩЕСТВИЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__ целый\n'
        'день напролет. Жирафы также славятся тем, что поедают прекрасные\n'
        '__СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕЕ__, но после этого у них часто болит\n'
        '__ЧАСТЬ ТЕЛА__. Если же жирафы находят __ЧИСЛО__ __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__,\n'
        'то у них моментально отваливается __ЧАСТЬ ТЕЛА__.')

def mad_words(info):
    """
    :param info: в строках пользовательский ввод
    должен быть окружен двойными подчеркиваниями.
    Подчеркивания нельзя вставлять в подсказку:
    __слово_слово__ (нельзя), __слово__ (можно)
    """
    matches = re.findall('__.*?__', info)

    if matches is not None:
        for word in matches:
            new_word = input(f'[INPUT] Введите {word}: ')
            info = info.replace(word, new_word, 1)
        print('\n')
        print(info)
    else:
        print('[ERROR] Ошибка в вводе')

mad_words(text)