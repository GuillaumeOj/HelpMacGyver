# -*- coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    Maze module for the McGyver game
    It contain the classe 'Maze'
"""
import sys

import pygame

from main import CELL_WIDTH, CELL_HEIGHT


class Maze:
    """
        Maze class for create a maze
        Attributes:
            - background
            - structure
    """

    def __init__(self, level, backgrounds):
        """
            Read the level's file
            Create the maze structure
            Create the maze background
        """
        # Load the 'backgrounds' ressource
        try:
            backgrounds = pygame.image.load(backgrounds)
        except pygame.error:
            # If someone move or delete the file
            print(f'{backgrounds} was not found')
            sys.exit()

        # Define texture for the walls
        wall = pygame.Surface((20, 20))
        wall.blit(backgrounds, (-20 * 9, 0))
        wall = self.transform_scale(wall, CELL_WIDTH, CELL_HEIGHT)

        # Define texture for the floor
        floor = pygame.Surface((20, 20))
        floor.blit(backgrounds, (0, -20 * 4))
        floor = self.transform_scale(floor, CELL_WIDTH, CELL_HEIGHT)

        # Define texture for the start
        start = pygame.Surface((20, 20))
        start.blit(backgrounds, (-20 * 4, -20 * 5))
        start = self.transform_scale(start, CELL_WIDTH, CELL_HEIGHT)

        # Define texture for the end
        end = pygame.Surface((20, 20))
        end.blit(backgrounds, (-20 * 4, -20 * 5))
        end = self.transform_scale(end, CELL_WIDTH, CELL_HEIGHT)

        # Load the level '.txt' file and store it in a double list
        try:
            with open(level, mode='r') as file:
                # Read the file
                data = file.read()

                # Store the maze in a double list
                self.maze = [list(row) for row in data.split('\n')]
        except FileNotFoundError:
            # If someone move or delete the file
            print(f'{level} was not found')
            sys.exit()

    @staticmethod
    def transform_scale(surface, width, height):
        """
            Just transform with 'scale' a 'surface'
            to a new 'width' and a new 'height'
        """
        return pygame.transform.scale(surface, (width, height))

if __name__ == '__main__':
    print('Error, not the main file.')
