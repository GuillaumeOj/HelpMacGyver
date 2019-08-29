# -*- coding: utf-8 -*-
"""
    Author: GuillaumeOj
    Version: 0.0.1

    Maze module for the McGyver game
    It contain the classe 'Maze'
"""
import sys
import os


class Maze:
    """
        Maze class for create a maze
        Attributes:
            - background
            - structure
    """

    def __init__(self, level, background_src):
        """
            Read the level's file
            Create the maze structure
            Create the maze background
        """
        self.background_src = background_src

        try:
            with open(os.path.join(os.getcwd(), level), mode='r') as file:
                # Read the file
                data = file.read()

                # Store the maze in a double list
                self.maze = [list(row) for row in data.split('\n')]
        except FileNotFoundError:
            print(f'{os.path.join(os.getcwd(), level)} was not found')
            sys.exit()

if __name__ == '__main__':
    print('Error, not the main file.')
