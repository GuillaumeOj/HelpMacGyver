"""
    Maze module for the MacGyver game
    It contain the class 'Maze' for creating a maze depends on a level file
"""
import os

import pygame

from .util import load_image
from .game_config import CELL_WIDTH, CELL_HEIGHT, MAZE_WIDTH, MAZE_HEIGHT


class Maze:
    """
        Define the maze for the game
    """

    def __init__(self, level):
        """
            Create each attributes for the maze:
                - 'maze' contain all the maze's structure
                - 'background'
                - 'rect'
                - 'textures' contain all the textures used for the background
                - 'cells' a list of cells composed by a name, a texture and a rect
                - 'start_rect' is the maze's start
                - 'end_rect' is the maze's end
        """

        # Create the maze structure
        self.maze = list()

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

        self.background = pygame.Surface((MAZE_WIDTH * CELL_WIDTH, MAZE_HEIGHT * CELL_HEIGHT))
        self.rect = self.background.get_rect()

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


    def _create_texture(self, texture_name, texture_position):
        """
            Create a texture with a name
        """
        # Load the 'background.png' ressource
        source = load_image('background.png')

        # Define a texture based on 'source'
        texture = pygame.Surface((20, 20))
        texture.blit(source, (texture_position))

        # Transform the surface to fit cells width and height
        texture = pygame.transform.scale(texture, (CELL_WIDTH, CELL_HEIGHT))

        # Add the texture to 'textures'
        self.textures[texture_name] = texture

    def _generate_cells(self):
        """
            Generate all the maze's cells based on 'maze'
        """
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                # Define the texture name depend on cell content
                if cell == '#':
                    texture = 'wall'
                elif cell == ' ':
                    texture = 'floor'
                elif cell == 'S':
                    texture = 'start'
                else:
                    texture = 'end'

                # Define a cell's rect depend on cell position in 'maze'
                cell_rect = pygame.Rect(j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)

                # Add the cell to 'cells'
                # Each cell is define by a name, a texture and a rect
                self.cells.append({'name': texture,
                                   'texture': self.textures[texture],
                                   'rect': cell_rect})

                # Blit the cell to the background
                self.background.blit(self.textures[texture], cell_rect.topleft)

    def detect_collision(self, old_rect, next_rect):
        """
            Detect collisions from a defined object with walls
        """

        # Detect if 'next_rect' collide with a wall
        for cell in self.cells:
            if cell['rect'].colliderect(next_rect) and cell['name'] == 'wall':
                # If there is a collision, the 'next_rect' get 'old_rect' values
                next_rect = old_rect

        return next_rect

    def clean_cell(self, old_rect):
        """
            Clean a cell at a specific position
        """
        cells_to_erase = list()

        for cell in self.cells:
            if cell['rect'].colliderect(old_rect):
                cells_to_erase.append(cell)

        return cells_to_erase


if __name__ == '__main__':
    print('Error, not the main file.')
