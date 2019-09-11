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


def create_text(input_text, size, position, surface, button=False):
    """
        This function create a text a show it at a given position
    """
    pygame.font.init()

    # Find the font in 'ressources/'
    font_src = os.path.join('ressources', 'ka1.ttf')

    # Load the font
    try:
        font = pygame.font.Font(font_src, size)
    except FileNotFoundError:
        # If someone move or delete the file
        print(f'{font_src} was not found')

    # Render the font
    text = font.render(input_text, True, (100, 47, 35))
    text_rect = text.get_rect(center=position)

    if button:
        text_rect.center = surface.get_rect().center

    surface.blit(text, text_rect)

    pygame.font.quit()
