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

def main():
    """
    Main part of the game is in this main function
    """

    pygame.init()
    clock = pygame.time.Clock()
    # Hide the mouse because it's useless
    pygame.mouse.set_visible(False)

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
    screen.blit(macgyver.image, macgyver.rect.topleft)

    # =========================
    # ===== CREATE ITEMS ======
    Item('needle.png', maze.cells)
    Item('ether.png', maze.cells)
    Item('plastic_tube.png', maze.cells)

    # Blit each item on the screen
    for item in Item.items:
        screen.blit(item.image, item.rect.topleft)

    # Update the screen
    pygame.display.update()

    while True:
        # Handle events
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            # If the player used the 'cross' or 'escape', the game closed
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                return False

        # If player press an arrow on keyboard, we move 'macgyver'
        if key[pygame.K_DOWN] or key[pygame.K_UP] or key[pygame.K_LEFT] or key[pygame.K_RIGHT]:

            # Clean the old cell
            clean_cells = maze.clean_cell(macgyver)
            for cell in clean_cells:
                screen.blit(cell['texture'], cell['rect'].topleft)

            # Move macgyver's position
            macgyver.move(key, maze)
            if macgyver.move_auth:
                macgyver.move(key, maze)

            # Check if macgyver is on an item
            macgyver.pick_item(Item.items)

            # Clean the new cell (remove item when macgyver is ON the cell)
            clean_cells = maze.clean_cell(macgyver)
            for cell in clean_cells:
                screen.blit(cell['texture'], cell['rect'].topleft)

            # Store macgyver items in the stuff
            if macgyver.items != []:
                panel.store_items(macgyver.items)
                screen.blit(panel.background, panel.rect.topleft)
            screen.blit(macgyver.image, macgyver.rect.topleft)

        # If the player reach the end of the maze he win
        if macgyver.rect.collidepoint(guardian.rect.center):
            if Item.items == []:
                panel.end_text('You win !')
            else:
                panel.end_text('You lose !')
            macgyver.move_auth = False
            screen.blit(panel.background, panel.rect.topleft)
            panel.end_menu(screen)

        pygame.display.update()

        # Used for macgyver don't run in the maze
        clock.tick(FPS)

if __name__ == '__main__':
    main()
