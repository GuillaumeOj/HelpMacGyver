# -*- coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    This is a maze game based on Python and using 'Pygame'

    The aim is to help MacGyver to escape from a maze. The exit is kept by an evil bodyguard.
    To neutralize the guard, the player must pick up some items in the maze.
    If MacGyver meet the guardian without those items, he dies. Else, he completes the level.
    For moving MacGyver in the maze, the player use the arrows on her/his keyboard.

    This game is a project from OpenClassrooms:
    - https://openclassrooms.com/fr/projects/156/assignment
"""
import sys

import pygame

# pylint: disable=wildcard-import
from src import *

# Define the size of the screen
SCREEN_SIZE = ((MAZE_WIDTH * CELL_WIDTH + PANEL_WIDTH),
               (MAZE_HEIGHT * CELL_HEIGHT))

def main():
    """
    Main part of the game is handle in this main function
    """

    pygame.init()
    # Hide the mouse because it's useless
    pygame.mouse.set_visible(False)

    # Set the window caption better than default
    pygame.display.set_caption('== Help Mc gyver == V 0.0.1 ==')

    screen = pygame.display.set_mode(SCREEN_SIZE)

    # =========================
    # ==== CREATE THE MAZE ====
    maze = Maze('level_1-1.txt')
    for cells in maze.cells:
        screen.blit(cells[0], cells[1])

    # =========================
    # === CREATE THE PANEL ====
    panel = Panel()
    screen.blit(panel.background, panel.position)

    # =========================
    # = CREATE THE CHARACTERS =
    # Create the guardian
    guardian = Character('guardian.png', maze.end_position)
    screen.blit(guardian.image, guardian.position)

    # Create Mc Gyver
    macgyver = Character('macgyver.png', maze.start_position)
    screen.blit(macgyver.image, macgyver.position)

    # =========================
    # ===== CREATE ITEMS ======
    Item('needle.png', maze.cells)
    Item('ether.png', maze.cells)
    Item('plastic_tube.png', maze.cells)

    # Blit each item on the screen
    for item in Item.items:
        screen.blit(item.image, item.position)

    # Update the screen
    pygame.display.update()

    while True:
        # Handle events
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            # If the player used the 'cross' or 'escape', the game closed
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                sys.exit()

        # If player press an arrow on keyboard, we move 'macgyver'
        if key[pygame.K_DOWN] or key[pygame.K_UP] or key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
            # Erase 'macgyver's
            for cell in maze.cells:
                if cell[1] == (macgyver.position.left, macgyver.position.top):
                    screen.blit(cell[0], cell[1])

            # Move macgyver's position
            macgyver.move(key)
            macgyver.position = maze.detect_collision(macgyver.position, macgyver.next_position)

            # Check if macgyver is on an item
            Item.items = macgyver.pick_item(Item.items)

            # Store macgyver items in the stuff
            if macgyver.items != []:
                panel.store_items(macgyver.items)
            screen.blit(panel.background, panel.position)

            # Blit the screen with the new position
            screen.blit(macgyver.image, macgyver.position)

        # If the player reach the end of the maze he win
        if macgyver.position == guardian.position and Item.items == []:
            print('You win !')
            sys.exit()
        elif macgyver.position == guardian.position and Item.items != []:
            print('You loose !')
            sys.exit()

        pygame.display.update()

        # Used for macgyver don't run in the maze
        pygame.time.delay(UPDATE_DELAY)

if __name__ == '__main__':
    main()
