"""
    Maze module for the MacGyver game
    It contain the class 'Maze' for creating a maze depends on a level file
"""
import os

import pygame

from .util import load_image
from .maze_config import CELL_WIDTH, CELL_HEIGHT, MAZE_WIDTH, MAZE_HEIGHT


class Maze:
    """
        Maze class for create a maze
        Attributes:
            - self.maze
            - self.maze_texture
    """

    def __init__(self, level):
        """
            Read the level's file
            Create the maze structure
            Create the maze background
            Create the maze position
            Create the maze textures
            Create a surface for erase a character
        """

        self.maze = list()
        self.background = pygame.Surface((MAZE_WIDTH * CELL_WIDTH, MAZE_HEIGHT * CELL_HEIGHT))
        self.rect = self.background.get_rect()

        # Path to the level file
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


        self.textures = dict()

        self._create_texture('wall', (-20 * 9, 0))
        self._create_texture('floor', (0, -20 * 4))
        self._create_texture('start', (-20 * 4, -20 * 5))
        self._create_texture('end', (-20 * 8, -20 * 1))

        # Initialize a list of maze cells
        self.cells = list()

        self._generate_cells()

        # Define start and end position
        for cell in self.cells:
            if cell['name'] == 'start':
                self.start_rect = (cell['rect'])
            elif cell['name'] == 'end':
                self.end_rect = (cell['rect'])


    def _create_texture(self, name, position):
        """
            Method for creating a texture for each part of the maze
            It use a generic file
            Each textures are stored in a dictionnary
        """
        # Load the 'background.png' ressource
        source = load_image('background.png')

        # Define a texture
        texture = pygame.Surface((20, 20))
        texture.blit(source, (position))
        texture = pygame.transform.scale(texture, (CELL_WIDTH, CELL_HEIGHT))

        self.textures[name] = texture

    def _generate_cells(self):
        """
            This method generate all the maze's cells
        """
        for i, row in enumerate(self.maze):
            for j, column in enumerate(row):
                # Which type of texture ?
                if column == '#':
                    texture = 'wall'
                elif column == ' ':
                    texture = 'floor'
                elif column == 'S':
                    texture = 'start'
                else:
                    texture = 'end'

                # Which position in the maze ?
                cell_rect = pygame.Rect(j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)

                self.cells.append({'name': texture,
                                   'texture': self.textures[texture],
                                   'rect': cell_rect})
                self.background.blit(self.textures[texture], cell_rect.topleft)

    def detect_collision(self, old_rect, next_rect):
        """
            Method for detecting collision
        """

        # Get next X and Y position in the maze to determine the nature (wall or floor ?)
        for cell in self.cells:
            if cell['rect'].colliderect(next_rect) and cell['name'] == 'wall':
                next_rect = old_rect

        return next_rect

    def clean_cell(self, character):
        """
            Method for clean a cell at a specific position
        """
        cells_to_erase = list()

        for cell in self.cells:
            if cell['rect'].colliderect(character.rect):
                cells_to_erase.append(cell)

        return cells_to_erase


if __name__ == '__main__':
    print('Error, not the main file.')
