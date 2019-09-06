"""
    Panel module for the McGyver game
    It contain the class 'Panel' for manage the panel on the right side
"""
import os

import pygame

# pylint: disable=wildcard-import
from .maze_config import * # pylint: disable=unused-wildcard-import

class Panel:
    """
        Configure and manage the right panel on th screen
    """

    # List of slots
    slots = list()

    def __init__(self):
        """
            Create each attributes for the object:
            - 'image'
            - 'position'
        """

        self.background = pygame.Surface((PANEL_WIDTH, CELL_HEIGHT * MAZE_HEIGHT))
        self.background.fill((159, 112, 76))

        self.rect = self.background.get_rect()
        pygame.draw.rect(self.background, (100, 47, 35), self.rect, 10)
        self.rect = self.rect.move(MAZE_WIDTH * CELL_WIDTH, 0)

        self._create_font('Stuffs', 20, (self.rect.width / 2, 20), True)

        # Create a surface to stock all picked up items
        residue = (PANEL_WIDTH - STUFF_COLUMN * CELL_WIDTH) / (STUFF_COLUMN + 1)
        self.stuff = pygame.Surface((STUFF_COLUMN * CELL_WIDTH + residue * (STUFF_COLUMN - 1),
                                     STUFF_ROW * CELL_HEIGHT + residue * (STUFF_ROW - 1)))
        self.stuff.fill((159, 112, 76))

        self.stuff_rect = self.stuff.get_rect().move(residue, 50)

        # Create each slot
        for row in range(STUFF_ROW):
            for column in range(STUFF_COLUMN):
                self._stuff_slot((column * (CELL_WIDTH + residue),
                                  row * (CELL_HEIGHT + residue)))

        self.background.blit(self.stuff, self.stuff_rect.topleft)

    def _stuff_slot(self, position):
        """
            This method create stuff slot for a  given 'position'
        """

        # Create a surface for the slot
        slot = pygame.Surface((CELL_WIDTH, CELL_HEIGHT))
        slot.fill((63, 45, 42))

        slot_rect = slot.get_rect().move(position)
        slot = pygame.Rect(position, (CELL_WIDTH, CELL_HEIGHT))

        # Store the slot in a list
        Panel.slots.append({'texture': slot, 'rect': slot_rect})
        Panel.slots.append(slot)

        # Blit the 'slot' with the 'background'
        self.stuff.blit(slot, slot_rect.topleft)
        pygame.draw.rect(self.stuff, (63, 45, 42), slot)


    def _create_font(self, text, size, position, center=False):
        """
            This function create a text:
                - Font type
                - Font size
                - Text
                - Position
        """
        pygame.font.init()

        # Find the font in 'ressources/'
        font_src = os.path.join('ressources', 'ka1.ttf')

        # Load the font
        try:
            font = pygame.font.Font(font_src, size)
        except FileNotFoundError:
            # If someone move or delete the file
            print(f'{font_src} was not found')

        # Render the font
        font = font.render(text, True, (100, 47, 35))
        if center:
            font_rect = font.get_rect(center=position)
        else:
            font_rect = font.get_rect(position)

        self.background.blit(font, font_rect)

        pygame.font.quit()

    def store_items(self, items):
        """
            Method called for store Mc Gyver items in the stuff
        """
        for i, item in enumerate(items):
            slot_rect = Panel.slots[i]['rect']
            slot = Panel.slots[i]

            position = (slot_rect.x + self.stuff_rect.x, slot_rect.y + self.stuff_rect.y)
            position = (slot.x + self.stuff_rect.x, slot.y + self.stuff_rect.y)

            self.background.blit(item.image, position)

    def end_text(self, text):
        """
            Print a text in the panel
        """

        self._create_font(text, 20, (self.rect.width / 2, self.rect.height / 2), True)

    def end_menu(self):
        """
            Show a menu a the end of the game for asking the player
            if she/he wants to continue to play
        """



if __name__ == '__main__':
    print('Error, not the main file.')
