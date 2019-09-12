"""
    Configuration file for the maze's constants
"""

# Configue the updating delay
FPS = 10

# Configure the maze's cells dimensions
CELL_WIDTH = 30
CELL_HEIGHT = 30

# Configure the maze's rows and column number
MAZE_WIDTH = 15
MAZE_HEIGHT = 15

# Configure the right panel width
PANEL_WIDTH = 200

# Define the panel position on the screen
PANEL_X = MAZE_WIDTH * CELL_WIDTH

# Define the size of the screen
SCREEN_SIZE = ((MAZE_WIDTH * CELL_WIDTH + PANEL_WIDTH),
               (MAZE_HEIGHT * CELL_HEIGHT))

# Configure the stuff size
STUFF_ROW = 2
STUFF_COLUMN = 3

# Manage the character size
CHARACTER_SIZE = (CELL_WIDTH, CELL_HEIGHT)

# Manage the moving speed for the character
MOVE_SPEED_X = CELL_WIDTH
MOVE_SPEED_Y = CELL_HEIGHT

# Colors
LIGHT_BROWN = (159, 112, 76)
BROWN = (100, 47, 35)
DARK_BROWN = (63, 45, 42)

if __name__ == '__main__':
    print('Error, not the main file.')
