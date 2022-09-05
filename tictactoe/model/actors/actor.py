"""Module actor."""
__author__ = 'Joan A. Pinol  (japinol)'

from collections import Counter
from os import path

import pygame as pg

from tictactoe.tools.logger.logger import log
from tictactoe.config.constants import FILE_NAMES
from tictactoe.model.actor_type import ActorBaseType, ActorCategoryType, ActorType
from tictactoe.tools.utils.color import Color


class Actor(pg.sprite.Sprite):
    """Represents an actor.
    It is not intended to be instantiated.
    """
    type_id_count = Counter()
    # key: sprite_sheet_data_id, value: (image, frames)
    sprite_images = {}
    # Security size so the sprite will not be too close to the border of the screen.
    CELL_SCREEN_SECURITY_SIZE = 1

    def __init__(self, x, y, game, name=None, change_x=0, change_y=0, items_to_drop=None):
        super().__init__()
        Actor.type_id_count[self.type] += 1
        self.id = f"{self.type.name}_{Actor.type_id_count[self.type]:05d}"
        self.game = game
        self.last_shot_time = 0
        self.time_between_shots_base = 1200
        self.target_of_spells_count = Counter()
        self.direction = 1

        if not getattr(self, 'base_type', None):
            self.base_type = ActorBaseType.NONE
        if not getattr(self, 'category_type', None):
            self.category_type = ActorCategoryType.NONE
        if not getattr(self, 'type', None):
            self.type = ActorType.CELL_EMPTY

        if not getattr(self, 'file_folder', None):
            self.file_folder = None
        if not getattr(self, 'file_mid_prefix', None):
            self.file_mid_prefix = None
        if not getattr(self, 'file_prefix', None):
            self.file_prefix = None
        if not getattr(self, 'file_name_key', None):
            self.file_name_key = None

        if not getattr(self, 'images_sprite_no', None):
            self.images_sprite_no = 1
        if not getattr(self, 'animation_speed', None):
            self.animation_speed = 0.1
        if not getattr(self, 'frame_index', None):
            self.frame_index = 0

        if not getattr(self, 'is_item', None):
            self.is_item = False

        if not getattr(self, 'transparency_alpha', None):
            self.transparency_alpha = False

        self.name = name or 'unnamed'

        self.init_before_load_sprites_hook()
        self._load_sprites()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.init_after_load_sprites_hook()
        log.info(f"Create actor of type: {self.type}")

    def _load_sprites(self):
        if not Actor.sprite_images.get(self.type.name):
            frames = []
            image = None
            for i in range(self.images_sprite_no):
                if self.transparency_alpha:
                    image = pg.image.load(self.file_name_im_get(
                                self.file_folder, self.file_name_key,
                                self.file_mid_prefix, suffix_index=i+1
                                )).convert_alpha()
                else:
                    image = pg.image.load(self.file_name_im_get(
                        self.file_folder, self.file_name_key,
                        self.file_mid_prefix, suffix_index=i+1
                    )).convert()
                    image.set_colorkey(Color.BLACK)
                frames.append(image)
            Actor.sprite_images[self.type.name] = (image, frames)
            self.image = frames[0]
        else:
            self.image = Actor.sprite_images[self.type.name][0]

    def init_before_load_sprites_hook(self):
        pass

    def init_after_load_sprites_hook(self):
        pass

    def update(self):
        self.frame_index += self.animation_speed
        self.update_after_inc_index_hook()
        if self.frame_index >= self.images_sprite_no:
            self.frame_index = 0

        self.update_sprite_image()
        self.update_when_hit()

    def update_sprite_image(self):
        self.image = Actor.sprite_images[self.type.name][self.direction][int(self.frame_index)]

    def update_after_inc_index_hook(self):
        pass

    def update_when_hit(self):
        bullet_hit_list = pg.sprite.spritecollide(self, self.game.level.bullets, False)
        if not bullet_hit_list:
            return

    def kill_hook(self):
        self.kill()

    @staticmethod
    def file_name_im_get(folder, file_name_key, mid_prefix, suffix_index):
        return path.join(folder, f"{FILE_NAMES[file_name_key][0]}"
                         f"{'_' if mid_prefix else ''}"
                         f"{mid_prefix or ''}"
                         f"_{suffix_index:02d}.{FILE_NAMES[file_name_key][1]}")


class ActorItem(Actor):
    """Represents an item actor.
    It is not intended to be instantiated.
    """
    def __init__(self, x, y, game, name=None):
        super().__init__(x, y, game, name=name)
        self.base_type = ActorBaseType.ITEM
