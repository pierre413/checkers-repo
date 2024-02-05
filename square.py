class Square:
    def __init__(self, row, col, circle=None):
        self.row = row
        self.col = col
        self.circle = circle

    def has_circle(self):
        return self.circle is not None


    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def enemy(self, color):
        return self.has_circle() and self.circle.color != color

    def has_team(self, color):
        return self.has_circle() and self.circle.color == color

    def enemy_edge(self, color, col):
        if self.enemy(color) and col in (0, 7):
            return True

    def next_square(self, row, col):
        if Square.in_range(row, col):
            if not self.has_circle():
                return True
            else:
                return False
        else:
            return False











    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True

