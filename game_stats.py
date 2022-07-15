import pygame.font


class GameStats:
    """Track statistics for m_h_game"""
    def __init__(self, m_h_game):
        self.settings = m_h_game.settings
        # Reset all the stats
        self.number_plays = 0
        self.no_change_plays = 0
        self.change_plays = 0
        self.no_change_wins = 0
        self.change_wins = 0
        self.no_change_percent = 0
        self.change_percent = 0
        # Start RMonty Hall Game in an inactive state.
        self.game_active = False


class Scoreboard:
    """A class to report the stats"""
    def __init__(self, m_h_game):
        self.m_h_game = m_h_game
        self.screen = m_h_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = m_h_game.settings
        self.stats = m_h_game.stats

        # Font stettings for the scores.
        self.text_white = (255, 255, 255)
        self.text_red = (255, 10, 10)
        self.text_green = (10, 255, 10)
        self.font = pygame.font.SysFont(None, 40)

        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        self.prep_number_of_plays()
        self.prep_no_change_plays()
        self.prep_no_change_wins()
        self.prep_change_plays()
        self.prep_change_wins()

    def prep_number_of_plays(self):
        """Turn the number of plays into a rendered image."""
        plays = self.stats.number_plays
        plays_str = "Total number of plays:  {:,}".format(plays)

        self.plays_image = self.font.render(plays_str, True, self.text_white, self.settings.bg_color)
        self.plays_rect = self.plays_image.get_rect()
        self.plays_rect.right = self.screen_rect.right - 10
        self.plays_rect.top = self.screen_rect.top + 500

    def prep_no_change_plays(self):
        """Turn the number of  no change plays into a rendered image."""
        no_change_plays = self.stats.no_change_plays
        no_change_plays_str = "Total no change plays:  {:,}".format(no_change_plays)

        self.no_change_plays_image = self.font.render(no_change_plays_str, True, self.text_red, self.settings.bg_color)
        self.no_change_plays_rect = self.no_change_plays_image.get_rect()
        self.no_change_plays_rect.right = self.screen_rect.right - 400
        self.no_change_plays_rect.top = self.screen_rect.top + 550

    def prep_change_plays(self):
        """Turn the number of  no change plays into a rendered image."""
        change_plays = self.stats.change_plays
        change_plays_str = "Total change plays:  {:,}".format(change_plays)
        self.change_plays_image = self.font.render(change_plays_str, True, self.text_green, self.settings.bg_color)
        self.change_plays_rect = self.change_plays_image.get_rect()
        self.change_plays_rect.right = self.screen_rect.right - 400
        self.change_plays_rect.top = self.screen_rect.top + 600

    def prep_no_change_wins(self):
        """Turn the number of  no change plays into a rendered image."""
        no_change_wins = self.stats.no_change_wins
        no_change_wins_str = "Total no change wins:  {:,}".format(no_change_wins)
        self.no_change_wins_image = self.font.render(no_change_wins_str, True, self.text_red, self.settings.bg_color)
        self.no_change_wins_rect = self.no_change_wins_image.get_rect()
        self.no_change_wins_rect.right = self.screen_rect.right - 400
        self.no_change_wins_rect.top = self.screen_rect.top + 650

    def prep_change_wins(self):
        """Turn the number of  no change plays into a rendered image."""
        change_wins = self.stats.change_wins
        change_wins_str = "Total change wins:  {:,}".format(change_wins)
        self.change_wins_image = self.font.render(change_wins_str, True, self.text_green, self.settings.bg_color)
        self.change_wins_rect = self.change_wins_image.get_rect()
        self.change_wins_rect.right = self.screen_rect.right - 400
        self.change_wins_rect.top = self.screen_rect.top + 700

    def prep_no_change_percent(self):
        """Turn the number of no change wins into a percentage and a rendered image."""
        self.no_change_wins = self.stats.no_change_wins
        self.no_change_plays = self.stats.no_change_plays
        if self.no_change_plays == 0:
            self.no_change_percent = 0
        else:
            self.no_change_percent = self.no_change_wins * 100 / self.no_change_plays

        no_change_percent_str = "No change win %:  {:10.1f}".format(self.no_change_percent)

        self.no_change_percent_image = self.font.render(no_change_percent_str, True, self.text_red,
                                                     self.settings.bg_color)
        self.no_change_percent_rect = self.no_change_percent_image.get_rect()
        self.no_change_percent_rect.right = self.screen_rect.right - 10
        self.no_change_percent_rect.top = self.screen_rect.top + 650

    def prep_change_percent(self):
        """Turn the number of change wins into a percentage and a rendered image."""
        self.change_wins = self.stats.change_wins
        self.change_plays = self.stats.change_plays
        if self.change_plays == 0:
            self.change_percent = 0
        else:
            self.change_percent = self.change_wins * 100 / self.change_plays

        change_percent_str = "Change win %:  {:10.1f}".format(self.change_percent)

        self.change_percent_image = self.font.render(change_percent_str, True, self.text_green,
                                                     self.settings.bg_color)
        self.change_percent_rect = self.change_percent_image.get_rect()
        self.change_percent_rect.right = self.screen_rect.right - 10
        self.change_percent_rect.top = self.screen_rect.top + 700

    def show_score(self):
        """Draw the scores to the screen"""

        # Prep the scores
        self.prep_number_of_plays()
        self.prep_no_change_plays()
        self.prep_change_plays()
        self.prep_no_change_wins()
        self.prep_change_wins()
        self.prep_no_change_percent()
        self.prep_change_percent()
        self.screen.blit(self.plays_image, self.plays_rect)
        self.screen.blit(self.no_change_plays_image, self.no_change_plays_rect)
        self.screen.blit(self.change_plays_image, self.change_plays_rect)
        self.screen.blit(self.no_change_wins_image, self.no_change_wins_rect)
        self.screen.blit(self.change_wins_image, self.change_wins_rect)
        self.screen.blit(self.no_change_percent_image, self.no_change_percent_rect)
        self.screen.blit(self.change_percent_image, self.change_percent_rect)
