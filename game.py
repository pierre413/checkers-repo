import pygame
from const import *
from board import Board
from dragger import Dragger

#
# img = Image.open("black_normal_piece.png")
# img.show()

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.switch_player = "black"


    def new_game(self):
        self.__init__()


    def next_turn(self):
        self.switch_player = 'red' if self.switch_player == 'black' else 'black'


    def score(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 12)
        color2 = (119, 154, 88)
        text = font.render(f'R: {self.board.red_score}', True, color2)
        text_rect = text.get_rect()
        text_rect.center = (15, 36)
        screen.blit(text, text_rect)

        text2 = font.render(f'B: {self.board.black_score}', True, color2)
        text_rect2 = text2.get_rect()
        text_rect2.center = (15, 24)
        screen.blit(text2, text_rect2)

        text3 = font.render('SCORE:', True, color2)
        text_rect3 = text3.get_rect()
        text_rect3.center = (26, 12)
        screen.blit(text3, text_rect3)

    def show_bg(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) # light green
                else:
                    color = (119, 154, 88) # dark green

                rectangle = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(screen, color, rectangle)
        self.score(screen)




    def show_piece(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_circle():
                    circle = self.board.squares[row][col].circle
                    if circle is not self.dragger.circle:
                        img = pygame.image.load(circle.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        circle.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, circle.texture_rect)
                        if circle.king:
                            img = pygame.transform.scale(pygame.image.load(circle.king_text), (50, 25))
                            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                            circle.texture_rect = img.get_rect(center=img_center)
                            surface.blit(img, circle.texture_rect)


    def show_moves(self, surface): #shows possible move
        if self.dragger.dragging:
            circle = self.dragger.circle

            for move in circle.moves:
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)











