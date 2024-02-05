import os
class Circle:
    def __init__(self, color, texture=None, texture_rect=None):
        self.color = color
        self.value = 1 if color == "red" else -1
        self.moves = []
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        self.piece_type = 'normal'
        self.king = False
        self.king_text = None
        self.double_move = False
        self.king_texture()
        self.piece_move = False

    def set_texture(self):
        self.texture = os.path.join(f'{self.color}_normal_piece.png')

    def king_texture(self):
        self.king_text = os.path.join(f'crown.png')

    def add_move(self, move):
        self.moves.append(move)