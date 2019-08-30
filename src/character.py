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
            Create each Attributes for the object:
            - 'image'
            - 'position'
            - 'next_position' => usefull only for moving mcgyver
            - 'maze' => store the maze structure
        """

        self.maze = maze

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

        # Declare position, first on top/left
        self.position = self.image.get_rect().move(0, 0)
        # Declare 'next_position' for 'move'
        self.next_position = self.position

        # Place the character in the maze depend on his 'role'
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
            Method for moving mcgyver in the maze
            Actually it define only the 'next_position'
        """

        # Define 'next_position'
        if key[pygame.K_DOWN] and self.position.bottom < (MAZE_HEIGHT * CELL_HEIGHT):
            self.next_position = self.position.move(0, CELL_HEIGHT)
        elif key[pygame.K_UP] and self.position.top > 0:
            self.next_position = self.position.move(0, -CELL_HEIGHT)
        elif key[pygame.K_RIGHT] and self.position.right < (MAZE_WIDTH * CELL_WIDTH):
            self.next_position = self.position.move(CELL_WIDTH, 0)
        elif key[pygame.K_LEFT] and self.position.left > 0:
            self.next_position = self.position.move(-CELL_WIDTH, 0)

if __name__ == '__main__':
    print('Error, not the main file.')
