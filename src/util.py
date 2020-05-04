"""
    This module regroup all helper functions for the game
"""
import os

import pygame


def load_image(image_name):
    """
        This function load an image as a Pygame Surface
    """

    image_path = os.path.join("ressources", image_name)
    try:
        image = pygame.image.load(image_path)
    except pygame.error:
        # If someone move or delete the file
        print(f"{image_path} was not found")

    return image


# pylint: disable=too-many-arguments
def create_text(input_text, font, color, position, surface, button=False):
    """
        This function create a text a show it at a given position
    """

    # Render the font
    text = font.render(input_text, True, color)
    text_rect = text.get_rect(center=position)

    if button:
        text_rect.center = surface.get_rect().center

    surface.blit(text, text_rect)


# pylint: enable=too-many-arguments
