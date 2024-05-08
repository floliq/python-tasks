class Cell:

    def __init__(self, number):
        self.number = number
        self.value = '*'

    def set_value(self, value):
        if self.value != '*':
            return False
        self.value = value
        return True


class Board:

    def __init__(self):
        self.cells = [Cell(i) for i in range(1,10)]

    def print_board(self):
        for index, cell in enumerate(self.cells):
            if index == 2 or index == 5:
                print('{} '.format(cell.value))
            else:
                print('{} '.format(cell.value), end='')
        print("\n")

    def check_winner(self, symbol):
        winning_combinations = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)  
        )
        for combination in winning_combinations:
            if all(self.cells[i].value == symbol for i in combination):
                return symbol
        return '*'


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0


class Game:

    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.turn = 1  

    def get_symbol(self, turn):
        if turn % 2 != 0:
            return self.player1.symbol
        else:
            return self.player2.symbol

    def make_turn(self, symbol, number):
        if not self.board.cells[number].set_value(symbol):
            print('Невозможно сделать ход, ячейка занята')
        else:
            self.turn += 1
        self.board.print_board()

    def play_match(self):
        self.turn = 1
        self.board.cells = [Cell(i) for i in range(1,10)]
        self.board.print_board()
        while self.turn < 10:
            char = self.get_symbol(self.turn)
            print('Номер хода {}, ходит {}'.format(self.turn, char))
            number = int(input('Введите номер ячейки: ')) - 1
            self.make_turn(char, number)
            if self.board.check_winner(char) == player1.symbol:
                print('Победил {}'.format(player1.name))
                return player1.name
            if self.board.check_winner(char) == player2.symbol:
                print('Победил {}'.format(player2.name))
                return player2.name
            if self.turn == 10 and self.board.check_winner(char) == '*':
                print('Ничья')
                return False

    def run(self):
        while True:
            winner = self.play_match()
            if winner == player1.name:
                self.player1.score += 1
            elif winner == player2.name:
                self.player2.score += 1
            print('{} {} - {} {}'.format(
                self.player1.name,
                self.player1.score,
                self.player2.score,
                self.player2.name,
            ))
            question = input('Введите "нет", если хотите закончить игру, Enter чтобы продолжить: ').lower()
            if question == 'нет':
                print('игра завершена')
                break


name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя второго игрока: ')
player1 = Player(name1, 'X')
player2 = Player(name2, '0')
game = Game(player1, player2)
game.run()
