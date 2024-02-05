from const import *
from square import Square
from circle import *
from move import Move

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._add_piece('red')
        self._add_piece('black')
        self.initial = None
        self.final = None
        self.move_loc = None
        self.d_moves = []
        self.two_move = False
        self.red_score = 0
        self.black_score = 0






    def clear_move(self, circle):
        circle.moves = []

    def move(self, circle, move):
        x, y = 0, 0
        initial = move.initial
        final = move.final
        self.two_move = False
        z =[0, 7]

        self.squares[initial.row][initial.col].circle = None
        self.squares[final.row][final.col].circle = circle
        x = (final.row - initial.row) / 2
        y = (final.col - initial.col) / 2

        if abs(x) >= 1:
            self.squares[int(initial.row + x)][int(initial.col + y)].circle = None
            if circle.color == 'red':
                self.red_score += 1
            else:
                self.black_score += 1
            print(f"this was deleted {initial.row + x, initial.col + y}")

        circle.piece_move = True
        if circle.piece_move and int(final.row) in z:
            circle.king = True


        self.clear_move(circle)

        if abs(x) >= 1:
            self.another_move(circle, final.row, final.col)
            print(f'final.col, final.col {final.row, final.col}')
            # if not circle.moves:
            #     self.two_move = False

        else:
            print('2 move = false')
            self.two_move = False

        self.clear_move(circle)


    def valid_moves(self, circle, move):

        return move in circle.moves






    def another_move(self, circle, row, col):

        self.two_move = False
        normal_moves = [(circle.value, + 1),
                        (circle.value, - 1)]
        king_moves = [(+ 1, + 1),
                      (- 1, + 1),
                      (+ 1, - 1),
                      (- 1, - 1)]

        mov = king_moves if circle.king else normal_moves

        for possible_move in mov:
            x, y = possible_move
            print(x, y)
            poss_x = row + x
            poss_y = col + y
            if Square.in_range(poss_x, poss_y, int(poss_x + x), int(poss_y + y)):
                # print(f'board,another_move, row:{row, col} row:{poss_x, poss_y} and test: {self.squares[poss_x][poss_y].has_circle()}')
                if self.squares[poss_x][poss_y].enemy(circle.color) and not self.squares[poss_x + x][poss_y + y].has_circle():
                    # print('board,another_move, test: layer 2')
                    initial = Square(row, col)
                    final = Square(poss_x + x, poss_y + y)
                    # circle.double_move = False
                    move = Move(initial, final)
                    # print(f"z = {z}")
                    circle.add_move(move)
                    self.two_move = True


    def game_moves(self, circle, row, col):
        self.clear_move(circle)
        self.calc_moves3_1(circle, row, col)
        # while self.d_moves:
        #     self.calc_moves3_1(circle, self.move_loc[0], self.move_loc[1])
        #     self.move_loc = []



    def calc_moves3_1(self, circle, row, col):  #TODO move double outside of the function and call it outside of the fuction

        d_moves = []

        normal_moves = [(circle.value, + 1),
                        (circle.value, - 1)]
        king_moves = [(+ 1, + 1),
                      (- 1, + 1),
                      (+ 1, - 1),
                      (- 1, - 1)]

        mov = king_moves if circle.king else normal_moves

        for possible_move in mov:
            gen_z = self.move_gen2(circle, row, col, possible_move)
            if gen_z is not None:
                move = Move(gen_z[0], gen_z[1])
                circle.add_move(move)
                self.move_loc = gen_z[1].row, gen_z[1].col


    def move_gen2(self, circle, row, col, possible_move):
        x, y = possible_move
        poss_x = row + x
        poss_y = col + y
        if Square.in_range(poss_x, poss_y):
            if not self.squares[poss_x][poss_y].has_circle() and not self.two_move:
                initial = Square(row, col)
                final = Square(poss_x, poss_y)
                # circle.double_move = False
                return (initial, final)
                # move = Move(initial, final)
                # circle.add_move(move)

            elif self.squares[poss_x][poss_y].enemy(circle.color) and Square.in_range(poss_x + x, poss_y + y) and \
                    not self.squares[poss_x + x][poss_y + y].has_circle():
                initial = Square(row, col)
                final = Square(poss_x + x, poss_y + y)
                # self.calc_moves3(circle, poss_x + x, poss_y )
                # if Square.in_range(poss_x + 2 * x, poss_y + 2 * y):
                circle.double_move = True



                return (initial, final)

    def _create(self):
        """
        turn each square into an array
        :return:
        """
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_piece(self, color):
        rows_ = [0, 1, 2] if color == 'red' else [5, 6, 7]
        for loc in rows_:
            for col in range(COLS):
                if (loc + col) % 2 != 0:
                    self.squares[loc][col] = Square(loc, col, Circle(color))

