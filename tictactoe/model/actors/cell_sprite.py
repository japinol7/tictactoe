"""Module sprite_cell."""
__author__ = 'Joan A. Pinol  (japinol)'

from tictactoe.config.constants import BITMAPS_FOLDER
from tictactoe.model.actors.actor import ActorItem, ActorType, Actor
from tictactoe.model.actor_type import ActorCategoryType
from tictactoe.model.cell import Cell


class CellBase(ActorItem):
    """Represents a Sprite Cell.
    It is not intended to be instantiated.
    """
    def __init__(self, x, y, game, name=None):
        self.file_folder = BITMAPS_FOLDER
        self.file_name_key = 'im_piece'
        self.images_sprite_no = 3
        self.category_type = ActorCategoryType.CELL
        super().__init__(x, y, game, name=name)

    def update(self):
        self.update_sprite_image()


class CellSprite(CellBase):
    """Represents a Sprite Cell."""

    def __init__(self, x, y, game):
        self.name = Cell.EMPTY.value
        self.file_mid_prefix = ''
        self.type = ActorType.CELL
        super().__init__(x, y, game, name=self.name)
