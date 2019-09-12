"""
    Panel module for the McGyver game
    It contain the class 'Panel' for manage the panel on the right side
"""
import pygame

from .util import create_text
from .maze_config import * # pylint: disable=wildcard-import, unused-wildcard-import

class Panel: # pylint: disable=too-few-public-methods
    """
        Configure and manage the right panel on the screen
    """

    # List of slots
    slots = list()

    def __init__(self, screen):
        """
            Create each attributes for the panel:
                - 'background'
                - 'rect'
                - 'stuff' an area to store character's items
                - 'stuff_rect'
                - 'yep' a yes button for the end menu
                - 'nope' a no button for the end menu
        """

        # Create a background with a specific color
        self.background = screen.subsurface(PANEL_X, 0, PANEL_WIDTH, CELL_HEIGHT * MAZE_HEIGHT)
        self.background.fill((159, 112, 76))

        self.rect = self.background.get_rect()

        # Draw a border to the rect
        pygame.draw.rect(self.background, (100, 47, 35), self.rect, 10)

        create_text('Stuffs', 20, (self.rect.width / 2, 20), self.background)

        # Create a surface to stock all picked up items
        self.residue = (PANEL_WIDTH - STUFF_COLUMN * CELL_WIDTH) / (STUFF_COLUMN + 1)
        stuff_width = STUFF_COLUMN * CELL_WIDTH + self.residue * (STUFF_COLUMN - 1)
        stuff_height = STUFF_ROW * CELL_HEIGHT + self.residue * (STUFF_ROW - 1)

        # Define the stuff surface
        self.stuff = self.background.subsurface(self.residue, 50, stuff_width, stuff_height)
        self.stuff.fill((159, 112, 76))

        self.stuff_rect = self.stuff.get_rect()

        # Create the stuff's slots
        self._stuff_slots()

    def _stuff_slots(self):
        """
            Create stuff slot for a  given 'position'
        """
        # Create each slot
        for row in range(STUFF_ROW):
            for column in range(STUFF_COLUMN):
                position = ((column * (CELL_WIDTH + self.residue),
                             row * (CELL_HEIGHT + self.residue)))

                # Create a rect for the slot
                slot = self.stuff.subsurface(position, (CELL_WIDTH, CELL_HEIGHT))
                slot.fill((63, 45, 42))

                # Store the slot in a list
                Panel.slots.append(slot)

    def store_items(self, items):
        """
            Store character's items in the stuff slots
        """
        if items:
            # Erase the slots
            self._stuff_slots()

            for i, item in enumerate(items):
                slot = Panel.slots[i]
                slot_dimension = slot.get_size()
                slot_position = slot.get_offset()
                slot_surface = self.stuff.subsurface(slot_position, slot_dimension)

                slot_surface.blit(item.image, (0, 0))

if __name__ == '__main__':
    print('Error, not the main file.')
