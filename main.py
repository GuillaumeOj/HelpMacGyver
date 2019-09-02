# -*- coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    This is a maze game based on Python and using 'Pygame'

    The aim is to help McGyver to escape from a maze. The exit is kept by an evil bodyguard.
    To neutralize the guard, the player must pick up some items in the maze.
    If MacGyver meet the guardian without those items, he dies. Else, he completes the level.
    For moving MacGyver in the maze, the player use the arrows on her/his keyboard.

    This game is a project from OpenClassrooms:
    - https://openclassrooms.com/fr/projects/156/assignment
"""
import sys
import os
from random import randrange

import pygame

# pylint: disable = wildcard-import
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

    # Create the maze
    maze = Maze('level_1-1.txt')
    screen.blit(maze.maze_texture, (0, 0))

    # =========================
    # = CREATE THE CHARACTERS =

    directory = os.path.dirname(__file__)

    # Create the guardian
    guardian = Character('guardian.png', maze.end_position)
    screen.blit(guardian.image, guardian.position)

    # Create Mc Gyver
    mc_gyver = Character('mc_gyver.png', maze.start_position)
    screen.blit(mc_gyver.image, mc_gyver.position)

    # =========================
    # ===== CREATE ITEMS ======

    # Define possibles positions for items
    items_positions = maze.floor_position

    # Path to the needle file
    needle_image = os.path.join(directory, 'ressources', 'needle.png')
    # Random needle position
    needle_position = items_positions.pop(randrange(len(items_positions)))
    # Create the needle
    needle = Item(needle_image, needle_position)

    # Path to the ether file
    ether_image = os.path.join(directory, 'ressources', 'ether.png')
    # Random ether position
    ether_position = items_positions.pop(randrange(len(items_positions)))
    # Create the tube
    ether = Item(ether_image, ether_position)

    # Path to the tube file
    tube_image = os.path.join(directory, 'ressources', 'plastic_tube.png')
    # Random tube position
    tube_position = items_positions.pop(randrange(len(items_positions)))
    # Create the tube
    tube = Item(tube_image, tube_position)

    # List items
    items = [needle, ether, tube]

    for item in items:
        screen.blit(item.image, item.position)

    pygame.display.update()

    while 1:
        # Handle events
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            # If the player used the 'cross', the game closed
            if event.type == pygame.QUIT:
                sys.exit()
            # If the player used the 'escape' key, the game closed
            if key[pygame.K_ESCAPE]:
                sys.exit()

        # If player press an arrow on keyboard, we move 'mc_gyver'
        if key[pygame.K_DOWN] or key[pygame.K_UP] or key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
            # Erase the 'mc_gyver' position
            maze.erase_character(mc_gyver.position)
            screen.blit(maze.eraser, mc_gyver.position)

            # Move 'mc_gyver's' position
            mc_gyver.move(key)
            mc_gyver.position = maze.detect_collision(mc_gyver.position, mc_gyver.next_position)

            # Check if mc_gyver is on an item
            items = mc_gyver.pick_item(items)

            # Blit the screen with the new position
            screen.blit(mc_gyver.image, mc_gyver.position)

        # If the player reach the end of the maze he win
        if mc_gyver.position == guardian.position and items == []:
            game_win = True
            print('You win !')
            sys.exit()
        elif mc_gyver.position == guardian.position and items != []:
            game_win = False
            print('You loose !')
            sys.exit()

        pygame.display.update()

        pygame.time.delay(75)

if __name__ == '__main__':
    main()
