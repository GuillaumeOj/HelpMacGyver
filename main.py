# -*- coding: utf-8 -*-
"""
Author: GuillaumeOj
Version: 0.0.1

This is a maze game based on Python and using 'Pygame'

The aim is to help McGyver to escape from a maze. The exit is kept by an evil bodyguard.
To neutralize the guard, the player must pick up some items in the maze.
If MacGyver meet the guardian without those items, he dies. Else, he completes the level.
For moving MacGyver in the maze, the player use the arrows on her/his keyboard.

This game is a project from OpenClassrooms: https://openclassrooms.com/fr/projects/156/assignment
"""
import sys
import pygame

# Define the size of the screen
SIZE = (350, 300) # 300*300 for the maze and 50*300 for the right side


def main():
    """
    Main part of the game is handle in this main function
    """
    pygame.init()
    # Hide the mouse because it's useless
    pygame.mouse.set_visible(False)

    pygame.display.set_mode(SIZE)
    pygame.display.update()

    while 1:
        # Handle events
        for event in pygame.event.get():
            # If the player used the 'cross', the game closed
            if event.type == pygame.QUIT:
                sys.exit()
            # If the player used the 'escape' key, the game closed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

if __name__ == '__main__':
    main()
