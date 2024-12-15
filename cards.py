from random import shuffle

class Card:
    suits = ['пикей', 'червей',
             'бубей', 'треф']

    values = [None, None, 2, 3, 4,
              5, 6, 7, 8, 9, 10,
              'валета', 'даму',
              'короля', 'туза']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        info = f'{self.values[self.value]} {self.suits[self.suit]}.'
        return info

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input('[NAME] Имя 1 игрока: ')
        name2 = input('[NAME] Имя 2 игрока: ')
        self.deck = Deck()
        self.p1 = Player(name=name1)
        self.p2 = Player(name=name2)

    def wins(self, winner):
        win = f'[WIN] {winner} забирает карты.'
        print(win)

    def draw(self, p1n, p1c, p2n, p2c):
        info = (f'\n[GAME] {p1n} кладет {p1c}\n'
                f'[GAME] {p2n} кладет {p2c}\n')
        print(info)

    def play_game(self):
        cards = self.deck.cards
        print('\n[START] Игра началась!')
        while len(cards) >= 2:
            msg = input('[INFO] Нажмите любую клавишу для начала игры.\n'
                        '[INFO] Нажмите Х для выхода.\n')
            if msg == 'Х':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print(f'[END] Игра окончена!\n'
              f'[WIN] {win} выиграл!')

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return f'[END] Ничья!'

game = Game()
game.play_game()