"""
    Character module for the McGyver game
    It contain the class 'Character'
"""
import os

import pygame

from .maze_config import CELL_WIDTH, CELL_HEIGHT, MAZE_WIDTH, MAZE_HEIGHT


class Character:
    """
        Define a character in the game
    """

    def __init__(self, image, start_position):
        """
            Create each Attributes for the object:
            - 'image'
            - 'position'
            - 'next_position' => usefull only for moving
            - 'items' for all items picked up
        """

        # Load the image
        image = os.path.join('ressources', image)
        try:
            self.image = pygame.image.load(image)
        except pygame.error:
            # If someone move or delete the file
            print(f'{image} was not found')

        # Create 'image' with transparency
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (CELL_WIDTH, CELL_HEIGHT))

        # Declare position, first on top/left
        self.position = self.image.get_rect().move(start_position)
        # Declare 'next_position' for 'move'
        self.next_position = self.position

        self.items = list()

    def  move(self, key):
        """
            Method for moving the character in the maze
        """
        if key[pygame.K_DOWN] and self.position.bottom < (MAZE_HEIGHT * CELL_HEIGHT):
            self.next_position = self.position.move(0, CELL_HEIGHT)
        elif key[pygame.K_UP] and self.position.top > 0:
            self.next_position = self.position.move(0, -CELL_HEIGHT)
        elif key[pygame.K_RIGHT] and self.position.right < (MAZE_WIDTH * CELL_WIDTH):
            self.next_position = self.position.move(CELL_WIDTH, 0)
        elif key[pygame.K_LEFT] and self.position.left > 0:
            self.next_position = self.position.move(-CELL_WIDTH, 0)

    def pick_item(self, items_list):
        """
            This method pick up items in the maze when the character is in the same cell
        """
        for item in items_list:
            if item.position == self.position:
                self.items.append(items_list.pop(items_list.index(item)))

        return items_list

if __name__ == '__main__':
    print('Error, not the main file.')
