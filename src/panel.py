"""
    Panel module for the McGyver game
    It contain the class 'Panel' for manage the panel on the right side
"""
import pygame

from .util import create_text
from .maze_config import * # pylint: disable=wildcard-import, unused-wildcard-import

class Panel:
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
        residue = (PANEL_WIDTH - STUFF_COLUMN * CELL_WIDTH) / (STUFF_COLUMN + 1)
        stuff_width = STUFF_COLUMN * CELL_WIDTH + residue * (STUFF_COLUMN - 1)
        stuff_height = STUFF_ROW * CELL_HEIGHT + residue * (STUFF_ROW - 1)
        self.stuff = self.background.subsurface(residue, 50, stuff_width, stuff_height)
        self.stuff.fill((159, 112, 76))

        self.stuff_rect = self.stuff.get_rect()

        # Create each slot
        for row in range(STUFF_ROW):
            for column in range(STUFF_COLUMN):
                self._stuff_slot((column * (CELL_WIDTH + residue),
                                  row * (CELL_HEIGHT + residue)))

        # Menu buttons
        self.yep = False
        self.nope = False

    def _stuff_slot(self, position):
        """
            Create stuff slot for a  given 'position'
        """

        # Create a rect for the slot
        slot = self.stuff.subsurface(position, (CELL_WIDTH, CELL_HEIGHT))
        slot.fill((63, 45, 42))

        # Store the slot in a list
        Panel.slots.append(slot)

    def _create_button(self, text, position, size):
        """
            Create a button to interact with the player
        """
        button = self.background.subsurface(position, size)
        button_rect = button.get_rect()

        create_text(text, 20, button_rect.topleft, button, True)

        pygame.draw.rect(button, (100, 47, 35), button_rect, 5)

        button_abs_rect = button_rect.move(button.get_abs_offset())
        return button_abs_rect


    def store_items(self, items):
        """
            Store character's items in the stuff slots
        """
        if items:
            for i, item in enumerate(items):
                slot = Panel.slots[i]
                slot_dimension = slot.get_size()
                slot_position = slot.get_offset()
                slot_surface = self.stuff.subsurface(slot_position, slot_dimension)

                slot_surface.blit(item.image, (0, 0))

    def end_menu(self, items):
        """
            Show a menu a the end of the game for asking the player
            if she/he wants to continue to play
        """
        # Show a Win or Lose text
        if items == []:
            end_text = 'You win !'
        else:
            end_text = 'You lose !'
        create_text(end_text,
                    20,
                    (self.rect.width / 2, self.rect.height / 2),
                    self.background)

        # Show a end menu
        create_text('Continue ?',
                    20,
                    (self.rect.width / 2, self.rect.height - 150),
                    self.background)

        # Create yes button
        self.yep = self._create_button('Yes', (10, 350), (180, 30))

        # Create no button
        self.nope = self._create_button('No', (10, 400), (180, 30))

if __name__ == '__main__':
    print('Error, not the main file.')
