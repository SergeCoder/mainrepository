import random

def game(word):

    wrong = 0 # количество ошибок
    stages = ['               ',
              '---------      ',
              '|       |      ',
              '|       |      ',
              '|       O      ',
              '|      /|\\    ',
              '|      / \\    ',
              '|              ',
              '---------------'
              ]
    letters = list(word.lower())
    board = ['_'] * len(word) # создаем строку слова с пробелами
    win = False

    while wrong < len(stages) - 1:
        print('\n')
        msg = input('[INPUT] Введите букву: ').lower()
        if msg in letters:
            ind = letters.index(msg) # получаем номер индекса буквы, если она есть в строке
            board[ind] = msg # открываем одну букву в строке с пробелами
            letters[ind] = '#' # закрываем букву в строке, чтобы она не повторялась
        else:
            wrong += 1
        print(f'[WORD] Ваше слово: {' '.join(board)}') # выводим строку, которая отгадывается
        x = wrong + 1
        print('\n'.join(stages[0:x])) # выводим виселицу, если ответ неверный
        if '_' not in board:
            print(f'\n[WIN] Вы выиграли! Было загадано слово: {word}')
            win = True
            break

    if not win:
        print(f'\n[LOSE] Вы проиграли! Было загадано слово: {word}')

words = ['арбуз', 'кот', 'дверь',
         'человек', 'медведь', 'тарелка']

rdm_word = random.choice(words)
game(rdm_word)