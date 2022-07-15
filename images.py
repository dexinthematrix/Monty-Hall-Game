import pygame


class Doors:
    """Class to define the doors"""

    def __init__(self, m_h_game, door_A_status, door_B_status, door_C_status):
        """Initialise the doors"""
        self.screen = m_h_game.screen
        self.screen_rect = m_h_game.screen.get_rect()

        # Name the images
        door_A = 'Images/Door_A.bmp'
        door_A_open = 'Images/Door_A_open.bmp'
        door_B = 'Images/Door_B.bmp'
        door_B_open = 'Images/Door_B_open.bmp'
        door_C = 'Images/Door_C.bmp'
        door_C_open = 'Images/Door_C_open.bmp'

        # Load each image and get its rect
        if door_A_status == False:
            self.door_A_pic = door_A
        elif door_A_status:
            self.door_A_pic = door_A_open
        if door_B_status == False:
            self.door_B_pic = door_B
        elif door_B_status:
            self.door_B_pic = door_B_open
        if door_C_status == False:
            self.door_C_pic = door_C
        elif door_C_status:
            self.door_C_pic = door_C_open

        # Get rect for each image
        self.image_A = pygame.image.load(self.door_A_pic)
        self.image_B = pygame.image.load(self.door_B_pic)
        self.image_C = pygame.image.load(self.door_C_pic)
        self.rect_A = self.image_A.get_rect()
        self.rect_B = self.image_B.get_rect()
        self.rect_C = self.image_C.get_rect()

        # Draw the doors on the left side of the screen
        self.rect_A.right = self.screen_rect.left + 280
        self.rect_B.right = self.screen_rect.left + 280
        self.rect_C.right = self.screen_rect.left + 280

        self.rect_A.top = self.screen_rect.top + 40
        self.rect_B.top = self.screen_rect.top + 300
        self.rect_C.top = self.screen_rect.top + 560

    def blitme(self):
        self.screen.blit(self.image_A, self.rect_A)
        self.screen.blit(self.image_B, self.rect_B)
        self.screen.blit(self.image_C, self.rect_C)


class Goat:
    """Class to define the goat"""

    def __init__(self, m_h_game, door_A_status, door_B_status, door_C_status):
        """Initialise the goat"""
        self.screen = m_h_game.screen
        self.screen_rect = m_h_game.screen.get_rect()
        self.x, self.y = -100, -200
        # Name the images
        self.goat = 'Images/goat.bmp'

        # Load each image and get its rect
        if door_A_status and door_B_status and door_C_status == False:
            self.y = -100
        elif door_A_status:
            self.y = 60
        elif door_B_status:
            self.y = 320
        elif door_C_status:
            self.y = 580

        # Get rect for each image
        self.image = pygame.image.load(self.goat)
        self.rect = self.image.get_rect()

        # Draw the goat on the left side of the screen
        self.rect.right = self.screen_rect.left + 260
        self.rect.top = self.screen_rect.top + self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Car:
    """Class to define the car"""

    def __init__(self, m_h_game, door_A_status, door_B_status, door_C_status):
        """Initialise the goat"""
        self.screen = m_h_game.screen
        self.screen_rect = m_h_game.screen.get_rect()
        self.x, self.y = -100, -200
        # Name the images
        self.car = 'Images/car.bmp'

        # Load each image and get its rect
        if door_A_status and door_B_status and door_C_status == False:
            self.y = -200
        elif door_A_status:
            self.y = 60
        elif door_B_status:
            self.y = 320
        elif door_C_status:
            self.y = 580

        # Get rect for each image
        self.image = pygame.image.load(self.car)
        self.rect = self.image.get_rect()

        # Draw the car on the left side of the screen
        self.rect.right = self.screen_rect.left + 260
        self.rect.top = self.screen_rect.top + self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Star:
    """Class to define the highlighting star"""

    def __init__(self, m_h_game, door_selected):
        """Initialise the goat"""
        self.screen = m_h_game.screen
        self.screen_rect = m_h_game.screen.get_rect()
        self.x, self.y = -100, -200
        # Name the images
        self.star = 'Images/star.bmp'

        # Load each image and get its rect
        if door_selected == 0:
            self.y = -200
        elif door_selected == 1:
            self.y = 60
        elif door_selected == 2:
            self.y = 320
        elif door_selected == 3:
            self.y = 580

        # Get rect for each image
        self.image = pygame.image.load(self.star)
        self.rect = self.image.get_rect()

        # Draw the car on the left side of the screen
        self.rect.right = self.screen_rect.left + 370
        self.rect.top = self.screen_rect.top + self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)