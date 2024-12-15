
class Table:
    def __init__(self):
        self.board = [1, 2, 3,
                      4, 5, 6,
                      7, 8, 9]

    def show_table(self):
        print('-' * 13)
        for i in range(3):
            print('|', self.board[0 + i * 3],
                  '|', self.board[1 + i * 3],
                  '|', self.board[2 + i * 3],
                  '|')
            print('-' * 13)

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Game:
    def __init__(self):
        name1 = input('[NAME] Введите имя 1 игрока: ')
        name2 = input('[NAME] Введите имя 2 игрока: ')
        self.p1 = Player(name1, 'X')
        self.p2 = Player(name2, 'O')

    def make_move(self, board, table, msg, symbol, player):
        if msg == 'EXIT':
            exit()

        if msg in board:
            ind = int(board.index(msg))
            board[ind] = symbol
            table.show_table()
        else:
            if msg > 9:
                while msg > 9:
                    print(f'[ERROR] Клетка {msg} не существует.')
                    table.show_table()
                    msg = int(input(f'[{symbol}] {player} снова ходит\n'))
                    if msg <= 9:
                        ind = board.index(msg)
                        board[ind] = symbol
                        table.show_table()
            else:
                while not (msg in board):
                    print(f'[ERROR] Клетка {msg} уже занята!')
                    table.show_table()
                    msg = int(input(f'[{symbol}] {player} снова ходит\n'))
                    if msg in board:
                        ind1 = board.index(msg)
                        board[ind1] = symbol
                        table.show_table()
                        break

    def check_win(self, board, symbol, player):
        if (board[0] == board[1] == board[2] or  # 3 по горизонтали
            board[3] == board[4] == board[5] or
            board[5] == board[7] == board[8] or
            board[0] == board[4] == board[8] or  # 2 по диагонали
            board[2] == board[4] == board[6] or
            board[0] == board[3] == board[6] or  # 3 по вертикали
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8]):
            print(f'[WIN] [{symbol}] {player} победил.\n'
                  f'[END] Игра окончена!')
            exit()

    def play(self):
        table = Table()
        board = table.board
        free_cells = 9

        print('[INFO] Пишите цифру от 1 до 9 и ваш знак поставится сам.\n'
              '[EXIT] Любой игрок может написать EXIT для выхода.\n'
              '[START] Игра началась!')
        table.show_table()

        while True:
            msg1 = int(input(f'[{self.p1.symbol}] {self.p1.name} ходит\n')) # действия первого игрока

            game.make_move(board, table, msg1, self.p1.symbol, self.p1.name)
            game.check_win(board, self.p1.symbol, self.p1.name)
            free_cells -= 1
            if free_cells == 0:
                print('[TIE] Ничья!\n'
                      '[END] Игра окончена!')
                break

            msg2 = int(input(f'[{self.p2.symbol}] {self.p2.name} ходит\n')) # действия второго игрока

            game.make_move(board, table, msg2, self.p2.symbol, self.p2.name)
            game.check_win(board, self.p2.symbol, self.p2.name)
            free_cells -= 1
            if free_cells == 0:
                print('[TIE] Ничья!\n'
                      '[END] Игра окончена!')
                break

game = Game()
game.play()