"""
    This is a maze game based on Python and using 'Pygame'

    The aim is to help MacGyver to escape from a maze. The exit is kept by an evil bodyguard.
    To neutralize the guard, the player must pick up some items in the maze.
    If MacGyver meet the guardian without those items, he dies. Else, he completes the level.
    For moving MacGyver in the maze, the player use the arrows on her/his keyboard.

    This game is a project from OpenClassrooms:
    - https://openclassrooms.com/fr/projects/156/assignment
"""

import pygame

from src import * # pylint: disable=wildcard-import, unused-wildcard-import

def start_game():
    """
        This function allow to start the game at the begining
    """

    pygame.init()
    clock = pygame.time.Clock()
    # Hide the mouse because it's useless
    pygame.mouse.set_visible(False)
    mouse_position = False

    # Set the window caption better than default
    pygame.display.set_caption('== Help Mc gyver == V 0.0.1 ==')

    screen = pygame.display.set_mode(SCREEN_SIZE)

    # =========================
    # ==== CREATE THE MAZE ====
    maze = Maze('level_1-1.txt')
    screen.blit(maze.background, maze.rect.topleft)

    # =========================
    # === CREATE THE PANEL ====
    panel = Panel()
    screen.blit(panel.background, panel.rect.topleft)

    # =========================
    # = CREATE THE CHARACTERS =
    # Create the guardian
    guardian = Character('guardian.png', maze.end_rect)
    screen.blit(guardian.image, guardian.rect.topleft)

    # Create Mc Gyver
    macgyver = Character('macgyver.png', maze.start_rect)
    macgyver.move_auth = True
    screen.blit(macgyver.image, macgyver.rect.topleft)

    # =========================
    # ===== CREATE ITEMS ======
    # Delete former items (when reinit the game)
    if Item.items:
        Item.items = list()

    # Create three items
    Item('needle.png', maze.cells)
    Item('ether.png', maze.cells)
    Item('plastic_tube.png', maze.cells)

    # Blit each item on the screen
    for item in Item.items:
        screen.blit(item.image, item.rect.topleft)

    # Update the screen
    pygame.display.update()

    return clock, mouse_position, screen, maze, panel, guardian, macgyver

def clean_cells(screen, maze, character):
    """
        Little function for cleaning the maze when the character move
    """

    cells = maze.clean_cell(character)
    for cell in cells:
        screen.blit(cell['texture'], cell['rect'].topleft)

def main(): # pylint: disable=too-many-branches
    """
    Main part of the game is in this main function
    """

    game_new = True

    while True:
        if game_new:
            clock, mouse_position, screen, maze, panel, guardian, macgyver = start_game()
            game_new = False

        # Keep the key pressed
        key = pygame.key.get_pressed()

        # Look for events
        for event in pygame.event.get():
            # If the player used the 'cross' or 'escape', the game closed
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                return False
            if panel.yep and panel.nope and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos

        # If player press an arrow on keyboard, we move 'macgyver'
        if key[pygame.K_DOWN] or key[pygame.K_UP] or key[pygame.K_LEFT] or key[pygame.K_RIGHT]:

            # Clean the old cell
            clean_cells(screen, maze, macgyver)

            # Move macgyver's position
            if macgyver.move_auth:
                macgyver.move(key, maze)

            # Check if macgyver is on an item
            macgyver.pick_item(Item.items)

            # Clean the new cell (remove item when macgyver is ON the cell)
            clean_cells(screen, maze, macgyver)

            screen.blit(macgyver.image, macgyver.rect.topleft)

        # Show macgyver items in the stuff
        if macgyver.items != []:
            panel.store_items(macgyver.items)
            screen.blit(panel.background, panel.rect.topleft)

        # If the player reach the end of the maze he win
        if macgyver.rect.collidepoint(guardian.rect.center):
            macgyver.move_auth = False
            screen.blit(panel.background, panel.rect.topleft)
            panel.end_menu(screen, Item.items)

            pygame.mouse.set_visible(True)

        if mouse_position and panel.yep.collidepoint(mouse_position):
            game_new = True
        if mouse_position and panel.nope.collidepoint(mouse_position):
            return False

        pygame.display.update()

        # Used for macgyver don't run in the maze
        clock.tick(FPS)

if __name__ == '__main__':
    main()
