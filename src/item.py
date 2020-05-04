"""
    Item module for the McGyver game
    It contain the class 'Item'
"""
from random import randrange

import pygame

from .util import load_image
from .game_config import CELL_WIDTH, CELL_HEIGHT

# For now, there is no public methods for 'Item' so we disable warnings for pylint
class Item:  # pylint: disable=too-few-public-methods
    """
        Define an item in the game
        And define a list of all items
    """

    # List of items
    items = list()

    def __init__(self, image_name, maze_cells):
        """
            Create each attributes for the item:
            - 'image'
            - 'position'
        """

        self.image = load_image(image_name)

        # Create 'image' with transparency
        if "ether" in image_name:
            self.image.set_colorkey((1, 1, 1))
        elif "needle" in image_name:
            self.image.set_colorkey((0, 0, 0))
        else:
            self.image.set_colorkey((255, 255, 255))

        # Transform images to fit cell width and height
        self.image = pygame.transform.scale(self.image, (CELL_WIDTH, CELL_HEIGHT))

        # Define item position
        self.maze_cells = maze_cells

        self.cell = False

        self._find_position()

        Item.items.append(self)

    def _find_position(self):
        """
            Private method to find a position for each items
        """

        while not self.cell:
            self.cell = self.maze_cells[randrange(len(self.maze_cells))]

            # If the cell is'nt a floor
            if self.cell["name"] != "floor":
                self.cell = False

            # If there already items stored we compare them
            if Item.items:
                for item in Item.items:
                    # If its the same cell, we rand choose another one
                    if self.cell == item.cell:
                        self.cell = False

        self.rect = self.cell["rect"]


if __name__ == "__main__":
    print("Error, not the main file.")

