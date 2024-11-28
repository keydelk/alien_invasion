#!/usr/bin/env python3

# The settings for the Alien Invasion game
import pygame

class Settings:
    """A  class to store all settings for Alien  Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.fullscreen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = pygame.Color("skyblue")

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = pygame.Color("darkslategrey")
        self.bullets_allowed = 5
