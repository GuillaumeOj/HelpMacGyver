# -*- coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    Item module for the McGyver game
    It contain the class 'Item'
"""
import sys

import pygame

from .maze_config import CELL_WIDTH, CELL_HEIGHT


class Item:
    """
        Define an item in the game
        Attributes:
            - self.image
            - self.position
    """

    def __init__(self, item_src, position):
        """
            Create each attributes for the object:
            - 'image'
            - 'position'
        """
        try:
            image_src = pygame.image.load(item_src)
        except pygame.error:
            # If someone move or delete the file
            print(f'{image_src} was not found')
            sys.exit()
        image_dim = image_src.get_rect()

        # Create 'image' with transparency
        self.image = pygame.Surface((image_dim.width, image_dim.height), pygame.SRCALPHA, 32)
        self.image.blit(image_src, (0, 0))
        self.image = self.transform_scale(self.image, CELL_WIDTH, CELL_HEIGHT)

        # Define item position
        self.position = self.image.get_rect().move(position)

    @staticmethod
    def transform_scale(surface, width, height):
        """
            Just transform with 'scale' a 'surface'
            to a new 'width' and a new 'height'
        """
        return pygame.transform.scale(surface, (width, height))

if __name__ == '__main__':
    print('Error, not the main file.')
