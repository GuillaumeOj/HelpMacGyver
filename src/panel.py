"""
    Panel module for the McGyver game
    It contain the class 'Panel' for manage the panel on the right side
"""
import pygame

from .util import create_text
from .game_config import *  # pylint: disable=wildcard-import, unused-wildcard-import


class Panel:
    """
        Configure and manage the right panel on the screen
    """

    # List of slots
    slots = list()

    def __init__(self, screen, font):
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
        self.background = screen.subsurface(
            PANEL_X, 0, PANEL_WIDTH, CELL_HEIGHT * MAZE_HEIGHT
        )
        self.background.fill(LIGHT_BROWN)

        self.rect = self.background.get_rect()

        # Draw a border to the rect
        pygame.draw.rect(self.background, BROWN, self.rect, 10)

        create_text(
            "Stuffs", font, BROWN, (self.rect.width / 2, 20), self.background,
        )

        # Create a surface to stock all picked up items
        self.residue = (PANEL_WIDTH - STUFF_COLUMN * CELL_WIDTH) / (STUFF_COLUMN + 1)
        stuff_width = STUFF_COLUMN * CELL_WIDTH + self.residue * (STUFF_COLUMN - 1)
        stuff_height = STUFF_ROW * CELL_HEIGHT + self.residue * (STUFF_ROW - 1)

        # Define the stuff surface
        self.stuff = self.background.subsurface(
            self.residue, 50, stuff_width, stuff_height
        )
        self.stuff_rect = self.stuff.get_rect()

        # Create the stuff's slots
        self._stuff_slots()

        self.yep = False
        self.nope = False

    def _stuff_slots(self):
        """
            Create stuff slot for a  given 'position'
        """
        # Create each slot
        for row in range(STUFF_ROW):
            for column in range(STUFF_COLUMN):
                position = (
                    column * (CELL_WIDTH + self.residue),
                    row * (CELL_HEIGHT + self.residue),
                )

                # Create a rect for the slot
                slot = self.stuff.subsurface(position, (CELL_WIDTH, CELL_HEIGHT))
                slot.fill(DARK_BROWN)

                # Store the slot in a list
                Panel.slots.append(slot)

    def _create_button(self, position, size):
        """
            Create a button to interact with the player
        """
        button = self.background.subsurface(position, size)

        return button

    @staticmethod
    def _hover_button(button, rect):
        """
            Create an hover effect for buttons
        """
        cursor_position = pygame.mouse.get_pos()
        if rect.collidepoint(cursor_position):
            button.fill(DARK_BROWN)
        else:
            button.fill(BROWN)

    @property
    def yep_abs_rect(self):
        """
            Return the absolute rectangle for the button 'Yes'
        """
        yep_rect = self.yep.get_rect()
        yep_abs_rect = yep_rect.move(self.yep.get_abs_offset())

        return yep_abs_rect

    @property
    def nope_abs_rect(self):
        """
            Return the absolute rectangle for the button 'No'
        """
        nope_rect = self.nope.get_rect()
        nope_abs_rect = nope_rect.move(self.nope.get_abs_offset())

        return nope_abs_rect

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

    def end_message(self, items, font):
        """
            Show a text to say the player she/he win or lose
        """
        # Show a Win or Lose text
        if items == []:
            end_text = "You win !"
        else:
            end_text = "You lose !"

        create_text(
            end_text,
            font,
            BROWN,
            (self.rect.width / 2, self.rect.height / 2),
            self.background,
        )

    def end_menu(self, font):
        """
            Create a menu for asking the player if she/he wants continue to play
        """
        create_text(
            "Continue ?",
            font,
            BROWN,
            (self.rect.width / 2, self.rect.height - 150),
            self.background,
        )

        # Create yes button
        self.yep = self._create_button((10, 350), (180, 30))

        # Create no button
        self.nope = self._create_button((10, 400), (180, 30))

        # Create an hover effect on buttons
        self._hover_button(self.yep, self.yep_abs_rect)
        self._hover_button(self.nope, self.nope_abs_rect)

        # Create button's text after the hover effect
        create_text("Yes", font, LIGHT_BROWN, self.yep_abs_rect.topleft, self.yep, True)
        create_text("No", font, LIGHT_BROWN, self.nope_abs_rect.topleft, self.nope, True)


if __name__ == "__main__":
    print("Error, not the main file.")

