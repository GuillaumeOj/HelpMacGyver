# -*-coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    Configuration file for the maze's constants
"""

# Configue the updating delay
UPDATE_DELAY = 100

# Configure the maze's cells dimensions
CELL_WIDTH = 30
CELL_HEIGHT = 30

# Configure the maze's rows and column number
MAZE_WIDTH = 15
MAZE_HEIGHT = 15

# Configure the right panel width
PANEL_WIDTH = 200

# Define the size of the screen
SCREEN_SIZE = ((MAZE_WIDTH * CELL_WIDTH + PANEL_WIDTH),
               (MAZE_HEIGHT * CELL_HEIGHT))

# Configure the stuff size
STUFF_ROW = 2
STUFF_COLUMN = 3

if __name__ == '__main__':
    print('Error, not the main file.')
