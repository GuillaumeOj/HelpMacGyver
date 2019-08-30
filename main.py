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

import pygame

import src

# Define the size of the screen
SCREEN_SIZE = ((src.MAZE_WIDTH * src.CELL_WIDTH + src.PANEL_WIDTH),
               (src.MAZE_HEIGHT * src.CELL_HEIGHT))

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

    directory = os.path.dirname(__file__)

    # Path to the level file
    maze_level = os.path.join(directory, 'maps', 'level_1-1.txt')
    # Path to the background file
    maze_background = os.path.join(directory, 'ressources', 'background.png')

    # Create the maze
    maze = src.Maze(maze_level, maze_background)

    screen.blit(maze.maze_texture, (0, 0))

    # =========================
    # = CREATE THE CHARACTERS =

    # Path to the guardian file
    guardian_image = os.path.join(directory, 'ressources', 'guardian.png')

    # Create the guardian
    guardian = src.Character(guardian_image, 'guardian', maze.maze)
    screen.blit(guardian.image, guardian.position)

    # Path to the guardian file
    mc_gyver_image = os.path.join(directory, 'ressources', 'mc_gyver.png')

    # Create the guardian
    mc_gyver = src.Character(mc_gyver_image, 'mc_gyver', maze.maze)
    screen.blit(mc_gyver.image, mc_gyver.position)

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

            # Blit the screen with the new position
            screen.blit(mc_gyver.image, mc_gyver.position)

        # If the player reach the end of the maze he win
        if mc_gyver.position == guardian.position:
            sys.exit()

        pygame.display.update()

        pygame.time.delay(75)

if __name__ == '__main__':
    main()
