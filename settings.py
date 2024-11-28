#!/usr/bin/env python3

# The settings for the Alien Invasion game
import pygame

class Settings:
    """A  class to store all settings for Alien  Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = pygame.Color("skyblue")
