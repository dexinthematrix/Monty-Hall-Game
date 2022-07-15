import pygame
from pygame.sprite import Sprite

SIZE = WIDTH, HEIGHT = 800, 600  # the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white')  # The background colod of our window
fps = 5  # Frames per second


class Host(Sprite):
    def __init__(self, m_h_game):
        super(Host, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('Images/monty.bmp'))
        self.images.append(pygame.image.load('Images/monty2.bmp'))
        self.images.append(pygame.image.load('Images/monty3.bmp'))
        self.images.append(pygame.image.load('Images/monty4.bmp'))
        self.images.append(pygame.image.load('Images/monty5.bmp'))

        self.screen = m_h_game.screen
        self.screen_rect = m_h_game.screen.get_rect()
        self.settings = m_h_game.settings

        self.index = 0
        self.count = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(1000, 150, 150, 198)

    def update(self):
        self.index += 1
        self.count += 1

        # Move the rect across the screen
        if self.count < 23:
            self.rect = pygame.Rect((1000 - (self.count * 20), 180, 150, 198))
        if self.index >= len(self.images):
            self.index = 1
        if self.count > 23:
            self.image = self.images[0]
        else:
            self.image = self.images[self.index]
