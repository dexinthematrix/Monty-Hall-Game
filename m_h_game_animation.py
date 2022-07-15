import sys
import time

import pygame
from random import randint
from time import sleep

import pygame.display

from settings import Settings
from button import Button, Banner
from game_stats import GameStats, Scoreboard
from host import Host
from images import Doors, Goat, Car, Star


class MontyHallGame:
    """Overall class to manage the game assets and behaviour"""

    def __init__(self):
        """Initialise the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen_bottom = self.screen.get_rect().bottom
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Monty Hall Game")

        # Make an instance of the host
        self.host = Host(self)
        self.my_group = pygame.sprite.Group(self.host)

        # Make the doors
        self.doors = Doors(self, False, False, False)
        # Make the goat
        self.goat = Goat(self, False, False, False)
        # Make the car
        self.car = Car(self, False, False, False)
        # Initialise a change door decision
        self.change_door = False
        self.open = 0
        # Make an instance of the star
        self.star = Star(self, 0)

        # Make an instance of pygame clock
        self.clock = pygame.time.Clock()

        # Initialise the prize
        self.prize_door = randint(1, 3)

        # Create and instance to store game stats
        self.stats = GameStats(self)

        # Make an instance of the scoreboard
        self.sb = Scoreboard(self)

        # Initialise the door_selected
        self.door_selected = self.settings.door_selected
        # Make a play button
        self.play_button = Button(self, "Start", 500, 400)

        # Initialise the play loop
        self.x = True

        # Make a banner of instructions
        self.banner = Banner(self, "Hi! This is the Monty Hall Game", 250, 100)
        self.banner2 = Banner(self, "Pick the door you think the prize is behind,", 250, 600)
        self.banner3 = Banner(self, "You'll then be shown a losing door and offered a swap.", 250, 700)

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._update_screen()
            self._check_events()
            if self.stats.game_active:
                while self.x:
                    self._game_loop()

    def _check_events(self):
        """ Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game if player clicks Start"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Set the game to active
            self.stats.game_active = True

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

    def _game_loop(self):
        """The loop that does the game and responds to Y/N etc"""
        self.stats.number_plays += 1


        # Display the option banner
        self.banner2 = Banner(self, "Pick door A, B or C  - (Q to quit)", 350, 200)
        # Hide banner 3 until needed
        self.banner3 = Banner(self, "", 0, -200)
        self._update_screen()
        # Get the door selection
        self._door_select()
        if self.door_selected == 1:
            self.text = "You selected Door A"
            self.star = Star(self, 1)
            self._door_select_banners(self.text)

            if self.prize_door == 2:
                print("Door C has a goat")
                self._doors(False, False, True, False, False, True, False, False, False)
                self.banner3 = Banner(self, "Door C has a goat.  Would you like to swap to door B - Y/N", 350, 400)
                self._update_screen()
                self._wait_events(2)
                self._doors(False, True, False, False, False, False, False, True, False)
                self._true_winner(self.change_door)
                self._play_again()

            elif self.prize_door == 3:
                print("Door B has a goat")
                self._doors(False, True, False, False, True, False, False, False, False)
                self.banner3 = Banner(self, "Door B has a goat.  Would you like to swap to door C - Y/N", 350, 400)
                self._update_screen()
                self._wait_events(3)
                self._doors(False, False, True, False, False, False, False, False, True)
                self._true_winner(self.change_door)
                self._play_again()

            else:
                self.open = randint(1, 2)
                if self.open == 1:
                    print("Door B has a goat")
                    self._doors(False, True, False, False, True, False, False, False, False)
                    self.banner3 = Banner(self, "Door B has a goat.  Would you like to swap to door C - Y/N",
                                          350, 400)
                    self._update_screen()
                    self._wait_events(3)
                    self._doors(True, False, False, False, False, False, True, False, False)
                    self._true_loser(self.change_door)
                    self._play_again()

                else:
                    print("Door C has a goat")
                    self._doors(False, False, True, False, False, True, False, False, False)
                    self.banner3 = Banner(self, "Door C has a goat.  Would you like to swap to door B - Y/N", 350, 400)
                    self._update_screen()
                    self._wait_events(2)
                    self._doors(True, False, False, False, False, False, True, False, False)
                    self._true_loser(self.change_door)
                    self._play_again()

        elif self.door_selected == 2:
            self.text = "You selected Door B"
            self.star = Star(self, 2)
            self._door_select_banners(self.text)
            if self.prize_door == 3:
                print("Door A has a goat")
                self._doors(True, False, False, True, False, False, False, False, False)
                self.banner3 = Banner(self, "Door A has a goat.  Would you like to swap to door C - Y/N", 350, 400)
                self._update_screen()
                self._wait_events(3)
                self._doors(False, False, True, False, False, False, False, False, True)
                self._true_winner(self.change_door)
                self._play_again()

            elif self.prize_door == 1:
                print("Door C has a goat")
                self._doors(False, False, True, False, False, True, False, False, False)
                self.banner3 = Banner(self, "Door C has a goat.  Would you like to swap to door A - Y/N", 350, 400)
                self._update_screen()
                self._wait_events(1)
                self._doors(True, False, False, False, False, False, True, False, False)
                self._true_winner(self.change_door)
                self._play_again()

            else:
                self.open = randint(1, 2)
                if self.open == 1:
                    print("Door A has a goat")
                    self._doors(True, False, False, True, False, False, False, False, False)
                    self.banner3 = Banner(self, "Door A has a goat.  Would you like to swap to door C - Y/N", 350, 400)
                    self._update_screen()
                    self._wait_events(3)
                    self._doors(False, True, False, False, False, False, False, True, False)
                    self._true_loser(self.change_door)
                    self._play_again()

                else:
                    print("Door C has a goat")
                    self._doors(False, False, True, False, False, True, False, False, False)
                    self.banner3 = Banner(self, "Door C has a goat.  Would you like to swap to door A - Y/N", 350, 400)
                    self._update_screen()
                    self._wait_events(1)
                    self._doors(False, True, False, False, False, False, False, True, False)
                    self._true_loser(self.change_door)
                    self._play_again()

        elif self.door_selected == 3:
            self.text = "You selected Door C"
            self.star = Star(self, 3)
            self._door_select_banners(self.text)
            if self.prize_door == 1:
                print("Door B has a goat")
                self._doors(False, True, False, False, True, False, False, False, False)
                self.banner3 = Banner(self, "Door B has a goat.  Would you like to swap to door A - Y/N", 350, 400)
                self._update_screen()
                self._wait_events(1)
                self._doors(True, False, False, False, False, False, True, False, False)
                self._true_winner(self.change_door)
                self._play_again()

            elif self.prize_door == 2:
                print("Door A has a goat")
                self._doors(True, False, False, True, False, False, False, False, False)
                self.doors = Doors(self, True, False, False)
                self.goat = Goat(self, True, False, False)
                self.banner3 = Banner(self, "Door A has a goat.  Would you like to swap to door B - Y/N", 350, 400)
                self._update_screen()
                self._wait_events(2)
                self._doors(False, True, False, False, False, False, False, True, False)
                self._true_winner(self.change_door)
                self._play_again()

            else:
                self.open = randint(1, 2)
                if self.open == 1:
                    print("Door A has a goat")
                    self._doors(True, False, False, True, False, False, False, False, False)
                    self.banner3 = Banner(self, "Door A has a goat.  Would you like to swap to door B - Y/N", 350, 400)
                    self._update_screen()
                    self._wait_events(2)
                    self._doors(False, False, True, False, False, False, False, False, True)
                    self._true_loser(self.change_door)
                    self._play_again()

                else:
                    print("Door B has a goat")
                    self._doors(False, True, False, False, True, False, False, False, False)
                    self.banner3 = Banner(self, "Door B has a goat.  Would you like to swap to door A - Y/N", 350, 400)
                    self._update_screen()
                    self._wait_events(1)
                    self._doors(False, False, True, False, False, False, False, False, True)
                    self._true_loser(self.change_door)
                    self._play_again()

    def _door_select(self):
        """Stops the running while awaiting door selection"""
        # First check that the window cross hasn't been used to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Await a key input and loop back around if it's not A, B or C.
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and self.stats.game_active:
                self.door_selected = 1
                print("Door selected is A")
            elif event.key == pygame.K_b and self.stats.game_active:
                self.door_selected = 2
                print("Door selected is B")
            elif event.key == pygame.K_c and self.stats.game_active:
                self.door_selected = 3
                print("Door selected is C")
            elif event.key == pygame.K_q:
                sys.exit()
            else:
                # Covers the case of any other key being selected
                self._door_select()
        else:
            #  Covers case of any other key selected or mouse movement being detected.
            self._door_select()

    def _wait_events(self, door):
        """Stops the running while awaiting a yes or no answer for the door change"""
        # First check that the window cross hasn't been used to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Await a key input and loop back around if it's not yes or no.
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_y:
                self.change_door = True
                print("You chose Y")
                self.stats.change_plays += 1
                self.star = Star(self, door)
                self.text = "You swapped doors"
                self._door_select_banners2(self.text)

                print("Change Plays = ", self.stats.change_plays)
                return
            elif event.key == pygame.K_n:
                self.change_door = False
                print("You chose N")
                self.stats.no_change_plays += 1
                print("No change Plays = ", self.stats.no_change_plays)
                if self.door_selected == 1:
                    self.text = "You stuck with A"
                elif self.door_selected == 2:
                    self.text = "You stuck with B"
                elif self.door_selected == 3:
                    self.text = "You stuck with C"
                self._door_select_banners2(self.text)
                return
            else:
                self._wait_events(door)

        else:
            self._wait_events(door)

    def _play_again(self):
        self.banner2 = Banner(self, "", 350, 400)
        self.banner3 = Banner(self, "Would you like to play again?   Y/N", 350, 400)
        self._update_screen()
        self.another_game = False
        # First check that the window cross hasn't been used to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Await a key input and loop back around if it's not yes or no.
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_y:
                self.another_game = True
                self.door_selected = 0
                # Re-initialise the prize
                self.prize_door = randint(1, 3)
                print("Prize is behind door ", self.prize_door)
                # Ensure doors are closed and no goats or cars present and the star is removed
                self._doors(False, False, False,  False, False, False,  False, False, False)
                self.star = Star(self, 0)
                # Re-enter the game loop
                self._game_loop()
                print("You chose Y")
            elif event.key == pygame.K_n:
                self.another_game = False
                print("You chose N")
                sys.exit()
            else:
                self._play_again()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            self._play_again()

    def _door_select_banners(self, text):
        self.banner2 = Banner(self, text, 350, 200)
        self.banner3 = Banner(self, "I'm going to show you a losing door now", 350, 400)
        self._update_screen()
        sleep(2.5)

    def _door_select_banners2(self, text):
        self.banner2 = Banner(self, text, 350, 200)
        self.banner3 = Banner(self, "Did you get the prize???", 350, 400)
        self._update_screen()
        sleep(2.5)

    def _true_winner(self, choice):
        if choice:
            self.banner3 = Banner(self, "You are a winner", 350, 400)
            self.stats.change_wins += 1
            print("Change wins = ", self.stats.change_wins)
        else:
            self.banner3 = Banner(self, "Sorry - You just lost", 350, 400)
        self._update_screen()
        time.sleep(2.5)

    def _true_loser(self, choice):
        if choice:
            self.banner3 = Banner(self, "Sorry - You just lost", 350, 400)
        else:
            self.banner3 = Banner(self, "You are a winner", 350, 400)
            self.stats.no_change_wins += 1
            print("No change wins = ", self.stats.no_change_wins)
        self._update_screen()
        time.sleep(2.5)

    def _doors(self, d1, d2, d3, g1, g2, g3, c1, c2, c3):
        self.doors = Doors(self, d1, d2, d3)
        self.goat = Goat(self, g1, g2, g3)
        self.car = Car(self, c1, c2, c3)

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        self.doors.blitme()
        self.goat.blitme()
        self.car.blitme()
        self.star.blitme()
        self.sb.show_score()

        # Draw the Start button if the game is inactive
        while not self.stats.game_active:
            self.screen.fill(self.bg_color)  # Makes sure the animation files are blanked down for each frame
            self.play_button.draw_button()
            self.banner.draw_button()
            self.banner2.draw_button()
            self.banner3.draw_button()
            self.my_group.update()
            self.my_group.draw(self.screen)
            pygame.display.update()
            self.clock.tick(self.settings.fps)
            self._check_events()
        if self.stats.game_active:
            self.banner2.draw_button()
            self.banner3.draw_button()

        # Make the most recently drawn screen visible. What's the difference between display.flip and display.update?
        pygame.display.update()


if __name__ == '__main__':
    # Make a game instance and run game.
    r = MontyHallGame()
    r.run_game()
    