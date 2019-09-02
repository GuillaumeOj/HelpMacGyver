# -*- coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    Panel module for the McGyver game
    It contain the class 'Panel' for manage the panel on the right side
"""

import pygame

# pylint: disable=wildcard-import
from .maze_config import *


class Panel:
    """
        Configure and manage the right panel on th screen
    """

    def __init__(self):
        """
            Create each attributes for the object:
            - 'image'
            - 'position'
        """

        self.background = pygame.Surface((PANEL_WIDTH, CELL_HEIGHT * MAZE_HEIGHT))
        self.background.fill((159, 112, 76))

        border_rect = self.background.get_rect()


        pygame.draw.rect(self.background, (100, 47, 35), border_rect, 10)

        self.position = (CELL_WIDTH * MAZE_WIDTH, 0)

if __name__ == '__main__':
    print('Error, not the main file.')
