# -*- coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    Maze module for the McGyver game
    It contain the class 'Maze'
"""
import sys
import os

import pygame

from .maze_config import CELL_WIDTH, CELL_HEIGHT


class Maze:
    """
        Maze class for create a maze
        Attributes:
            - self.maze
            - self.maze_texture
    """

# pylint: disable=too-many-locals
    def __init__(self, level):
        """
            Read the level's file
            Create the maze structure
            Create the maze textures
            Create the maze background
            Create a surface for erase a character
        """

        level = os.path.join('maps', level)

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

        # Load the 'background' ressource
        background = os.path.join('ressources', 'background.png')
        try:
            background = pygame.image.load(background)
        except pygame.error:
            # If someone move or delete the file
            print(f'{background} was not found')
            sys.exit()

        # Define texture for the walls
        wall = pygame.Surface((20, 20))
        wall.blit(background, (-20 * 9, 0))
        wall = pygame.transform.scale(wall, (CELL_WIDTH, CELL_HEIGHT))

        # Define texture for the floor
        floor = pygame.Surface((20, 20))
        floor.blit(background, (0, -20 * 4))
        floor = pygame.transform.scale(floor, (CELL_WIDTH, CELL_HEIGHT))

        # Define texture for the start
        start = pygame.Surface((20, 20))
        start.blit(background, (-20 * 4, -20 * 5))
        start = pygame.transform.scale(start, (CELL_WIDTH, CELL_HEIGHT))

        # Define texture for the end
        end = pygame.Surface((20, 20))
        end.blit(background, (-20 * 8, -20 * 1))
        end = pygame.transform.scale(end, (CELL_WIDTH, CELL_HEIGHT))

        # Initialize a list of maze cells
        self.cells = list()

        # pylint: disable=invalid-name
        for y, row in enumerate(self.maze):
            for x, column in enumerate(row):
                # Which type of texture ?
                if column == '#':
                    texture = wall
                    name = 'wall'
                elif column == ' ':
                    texture = floor
                    name = 'floor'
                elif column == 'S':
                    texture = start
                    name = 'start'
                else:
                    texture = end
                    name = 'end'

                # Which position in the maze ?
                position = (x * CELL_WIDTH, y * CELL_HEIGHT)

                if texture == start:
                    self.start_position = position
                elif texture == end:
                    self.end_position = position

                self.cells.append((texture, position, name))

    def detect_collision(self, old_cell, next_cell):
        """
            Method for detecting collision
        """

        # Get next X and Y position in the maze to determine the nature (wall or floor ?)
        next_position = [cell for cell in self.cells if cell[1] == (next_cell.left, next_cell.top)]
        next_position = next_position[0]

        # Determine if the character can go to the next position
        if next_position[2] == 'wall':
            next_cell = old_cell

        return next_cell

if __name__ == '__main__':
    print('Error, not the main file.')
