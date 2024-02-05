import pygame
from const import *


class Dragger:
    def __init__(self):
        self.initial_row = 0
        self.initial_col = 0
        self.mousex = 0
        self.mousey = 0
        self.dragging = False
        self.circle = None
        self.x = 0
        self.y = 0

    def update_blit(self, surface):
        img = pygame.image.load(self.circle.texture)
        img_center = (self.mousex, self.mousey)
        self.circle.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.circle.texture_rect)
        if self.circle.king:
            img = pygame.transform.scale(pygame.image.load(self.circle.king_text), (50, 25))
            img_center = (self.mousex, self.mousey)
            self.circle.texture_rect = img.get_rect(center=img_center)
            surface.blit(img, self.circle.texture_rect)

    def update_mouse(self, pos):
        x, y = pos  # (x, y)

        self.mousex = x
        self.mousey = y


    def save_initial(self, pos):
        self.initial_col = pos[0] // SQSIZE
        self.initial_row = pos[1] // SQSIZE

    def drag_(self, circle):
        self.circle = circle
        self.dragging = True

    def undrag(self):
        self.circle = None
        self.dragging = False





    # def position(self, pos):
    #     x, y = pos
    #     self.mousex = x
    #     self.mousey = y


