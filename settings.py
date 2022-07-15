

class Settings:
    """A class to store all settings for the Monty_Hall game"""

    def __init__(self):
        """Initialize the games settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.door_selected = 0
        self.fps = 5

    def initialize_dynamic_settings(self):
        self.door_selected = 0
