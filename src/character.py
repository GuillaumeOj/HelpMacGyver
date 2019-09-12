"""
    Character module for the McGyver game
    It contain the class 'Character'
"""
import pygame

from .util import load_image
from .game_config import * # pylint: disable=wildcard-import, unused-wildcard-import


class Character:
    """
        Define a character in the game
    """

    def __init__(self, image_name, insert_rect):
        """
            Create each Attributes for the object:
                - 'image'
                - 'position'
                - 'items' for all items picked up
                - 'move_auth' to authorize the character to moves
        """

        # Load the image
        self.image = load_image(image_name)

        # Add transparency for 'image'
        self.image.set_colorkey((0, 0, 0))

        # Transform the image to fit cell's width and height
        self.image = pygame.transform.scale(self.image, CHARACTER_SIZE)

        # Declare position (centered)
        self.rect = self.image.get_rect().move(insert_rect.topleft)

        # Create a list to store each picked up items
        self.items = list()

        # Authorize the character to move or not
        self.move_auth = False

    def  move(self, key, maze):
        """
            Moving the character in the maze based on the keyboard's arrows
        """
        next_rect = False

        if self.move_auth:
            # Create a new 'rect' based on wich key was pressed
            if key[pygame.K_DOWN] and self.rect.bottom < (MAZE_HEIGHT * CELL_HEIGHT):
                next_rect = self.rect.move(0, MOVE_SPEED_Y)
            elif key[pygame.K_UP] and self.rect.top > 0:
                next_rect = self.rect.move(0, -MOVE_SPEED_Y)
            elif key[pygame.K_RIGHT] and self.rect.right < (MAZE_WIDTH * CELL_WIDTH):
                next_rect = self.rect.move(MOVE_SPEED_X, 0)
            elif key[pygame.K_LEFT] and self.rect.left > 0:
                next_rect = self.rect.move(-MOVE_SPEED_X, 0)

        # Detect if there any collision with maze's walls
        if next_rect:
            self.rect = maze.detect_collision(self.rect, next_rect)

    def pick_item(self, items):
        """
            Pick up items in the maze when the character is on the same cell
        """
        if items:
            for i, item in enumerate(items):
                if item.rect.colliderect(self.rect):
                    self.items.append(items.pop(i))

if __name__ == '__main__':
    print('Error, not the main file.')
