"""
    Character module for the McGyver game
    It contain the class 'Character'
"""
import pygame

from .util import load_image
from .maze_config import * # pylint: disable=wildcard-import, unused-wildcard-import


class Character:
    """
        Define a character in the game
    """

    def __init__(self, image_name, insert_rect):
        """
            Create each Attributes for the object:
            - 'image'
            - 'position'
            - 'next_position' => usefull only for moving
            - 'items' for all items picked up
            - 'speed'
        """

        # Load the image
        self.image = load_image(image_name)

        # Create 'image' with transparency
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, CHARACTER_SIZE)

        # Declare position (centered)
        self.rect = self.image.get_rect()
        move = ((insert_rect.w - self.rect.w) / 2 + insert_rect.left,
                (insert_rect.h - self.rect.h) / 2 + insert_rect.top)
        self.rect = self.image.get_rect().move(move)

        self.items = list()

        # Authorize the character to move
        self.move_auth = False

    def  move(self, key, maze):
        """
            Method for moving the character in the maze
        """
        next_rect = False

        if key[pygame.K_DOWN] and self.rect.bottom < (MAZE_HEIGHT * CELL_HEIGHT):
            next_rect = self.rect.move(0, MOVE_SPEED_Y)
        elif key[pygame.K_UP] and self.rect.top > 0:
            next_rect = self.rect.move(0, -MOVE_SPEED_Y)
        elif key[pygame.K_RIGHT] and self.rect.right < (MAZE_WIDTH * CELL_WIDTH):
            next_rect = self.rect.move(MOVE_SPEED_X, 0)
        elif key[pygame.K_LEFT] and self.rect.left > 0:
            next_rect = self.rect.move(-MOVE_SPEED_X, 0)

        if next_rect:
            self.rect = maze.detect_collision(self.rect, next_rect)

    def pick_item(self, items):
        """
            This method pick up items in the maze when the character is in the same cell
        """
        for i, item in enumerate(items):
            if item.rect.colliderect(self.rect):
                self.items.append(items.pop(i))

        return items

if __name__ == '__main__':
    print('Error, not the main file.')
