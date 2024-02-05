import pygame
from const import *
import sys
from game import Game
from square import Square
from move import Move

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Checkers")
        self.game = Game()



    def mainloop(self):
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board

        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_piece(screen)
            if dragger.dragging:
                dragger.update_blit(screen)
            for event in pygame.event.get():

                # clicking pieces
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_col = dragger.mousex // SQSIZE
                    clicked_row = dragger.mousey // SQSIZE


                    if board.squares[clicked_row][clicked_col].has_circle():
                        circle = board.squares[clicked_row][clicked_col].circle
                        if circle.color == game.switch_player:
                            # if not board.two_move:
                            board.game_moves(circle, clicked_row, clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_(circle)
                            game.show_bg(screen)
                            game.show_moves(screen)
                            game.show_piece(screen)

                # moving pieces
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_piece(screen)
                        dragger.update_blit(screen)

                # releasing piece
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        release_row = dragger.mousey // SQSIZE
                        release_col = dragger.mousex // SQSIZE


                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(release_row, release_col)
                        move = Move(initial, final)
                        if board.valid_moves(dragger.circle, move):
                            board.move(dragger.circle, move)
                            game.show_bg(screen)
                            game.show_piece(screen)
                            if not board.two_move:
                                game.next_turn()
                                board.two_move = False

                    dragger.undrag()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game.next_turn()
                    if event.key == pygame.K_r:
                        print('it prints something')
                        game.new_game()
                        game = self.game
                        dragger = self.game.dragger
                        board = self.game.board


                #quiting
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()