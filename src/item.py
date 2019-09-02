# -*- coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    Item module for the McGyver game
    It contain the class 'Item'
"""
import sys
import os

import pygame

from .maze_config import CELL_WIDTH, CELL_HEIGHT


class Item:
    """
        Define an item in the game
        And define a list of all items
    """

    # List of items
    items = list()

    def __init__(self, image, position):
        """
            Create each attributes for the object:
            - 'name'
            - 'image'
            - 'position'
        """
        image = os.path.join('ressources', image)
        try:
            self.image = pygame.image.load(image)
        except pygame.error:
            # If someone move or delete the file
            print(f'{image} was not found')
            sys.exit()

        # Create 'image' with transparency
        if 'ether' in image:
            self.name = 'ether'
            self.image.set_colorkey((1, 1, 1))
        elif 'plastic_tube' in image:
            self.name = 'plastic_tube'
            self.image.set_colorkey((255, 255, 255))
        else:
            self.name = 'needle'
            self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (CELL_WIDTH, CELL_HEIGHT))

        # Define item position
        self.position = self.image.get_rect().move(position)

        Item.items.append(self)

if __name__ == '__main__':
    print('Error, not the main file.')
