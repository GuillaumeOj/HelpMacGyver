"""
    Item module for the McGyver game
    It contain the class 'Item'
"""
import os
from random import randrange

import pygame

from .maze_config import CELL_WIDTH, CELL_HEIGHT

# For now, there is no public methods for 'Item' so we disable warnings for pylint
# pylint: disable=too-few-public-methods
class Item:
    """
        Define an item in the game
        And define a list of all items
    """

    # List of items
    items = list()

    def __init__(self, image, maze_cells):
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
        self.maze_cells = maze_cells

        self._find_position()

        Item.items.append(self)

    def _find_position(self):
        """
            Private method to find a position for each items
        """

        self.cell = False

        # Keep only cells with floor
        self.maze_cells = [cell for cell in self.maze_cells if cell['name'] == 'floor']
        while not self.cell:
            self.cell = self.maze_cells[randrange(len(self.maze_cells))]

            # If there already items stored we compare them
            if Item.items:
                for item in Item.items:
                    # If its the same cell, we rand choose another one
                    if self.cell == item.cell:
                        self.cell = False

        self.position = self.cell['position']



if __name__ == '__main__':
    print('Error, not the main file.')
