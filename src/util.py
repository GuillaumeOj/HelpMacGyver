"""
    This module regroup all helper functions for the game
"""
import os

import pygame

def load_image(image_name):
    """
        This function load an image as a Pygame Surface
    """

    image_path = os.path.join('ressources', image_name)
    try:
        image = pygame.image.load(image_path)
    except pygame.error:
        # If someone move or delete the file
        print(f'{image_path} was not found')

    return image
