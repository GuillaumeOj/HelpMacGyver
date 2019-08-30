# -*- coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    Character module for the McGyver game
    It contain the class 'Character'
"""
import sys

import pygame

from .maze_config import CELL_WIDTH, CELL_HEIGHT, MAZE_WIDTH, MAZE_HEIGHT


class Character:
    """
        Define a character in the game
        Attributes:
            - self.image
            - self.position
    """

    def __init__(self, character_src, role, maze):
        """
            Create the character image
            Place the character in the maze
        """

        # Load the image
        try:
            image_src = pygame.image.load(character_src)
        except pygame.error:
            # If someone move or delete the file
            print(f'{character_src} was not found')
            sys.exit()
        image_dim = image_src.get_rect()

        # Create 'image' with transparency
        self.image = pygame.Surface((image_dim.width, image_dim.height), pygame.SRCALPHA, 32)
        self.image.blit(image_src, (0, 0))
        self.image = self.transform_scale(self.image, CELL_WIDTH, CELL_HEIGHT)

        # Find character position in the maze
        self.position = self.image.get_rect().move(0, 0)
        for row in maze:
            for column in row:
                if role == 'guardian' and column == 'E':
                    self.position = self.position.move(row.index(column) * CELL_WIDTH,
                                                       maze.index(row) * CELL_HEIGHT)
                elif role == 'mc_gyver' and column == 'S':
                    self.position = self.position.move(row.index(column) * CELL_WIDTH,
                                                       maze.index(row) * CELL_HEIGHT)

    @staticmethod
    def transform_scale(surface, width, height):
        """
            Just transform with 'scale' a 'surface'
            to a new 'width' and a new 'height'
        """
        return pygame.transform.scale(surface, (width, height))

    def  move(self, key):
        """
            Method for moving mc_gyver
        """
        if key[pygame.K_DOWN] and self.position.bottom < (MAZE_HEIGHT * CELL_HEIGHT):
            self.position = self.position.move(0, CELL_HEIGHT)
        elif key[pygame.K_UP] and self.position.top > 0:
            self.position = self.position.move(0, -CELL_HEIGHT)
        elif key[pygame.K_RIGHT] and self.position.right < (MAZE_WIDTH * CELL_WIDTH):
            self.position = self.position.move(CELL_WIDTH, 0)
        elif key[pygame.K_LEFT] and self.position.left > 0:
            self.position = self.position.move(-CELL_WIDTH, 0)

if __name__ == '__main__':
    print('Error, not the main file.')
