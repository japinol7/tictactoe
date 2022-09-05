"""Module clock."""
__author__ = 'Joan A. Pinol  (japinol)'

from tictactoe.config.constants import BM_CLOCKS_FOLDER
from tictactoe.model.actor_type import ActorCategoryType, ActorType
from tictactoe.model.actors.actor import ActorItem
from tictactoe.model.clock import ClockTimer, ClockStopwatch
from tictactoe.tools.utils.color import Color
from tictactoe.tools.utils import utils_graphics as libg_jp
from tictactoe.tools.logger.logger import log


class Clock(ActorItem):
    """Represents a clock.
    It is not intended to be instantiated.
    """
    def __init__(self, x, y, game, name=None):
        self.file_folder = BM_CLOCKS_FOLDER
        self.file_name_key = 'im_clocks'
        self.images_sprite_no = 1
        self.category_type = ActorCategoryType.CLOCK
        super().__init__(x, y, game, name=name)

    def update_when_hit(self):
        """Cannot be hit."""
        pass

    def set_on(self):
        pass


class ClockTimerA(Clock):
    """Represents a clock timer of type A."""

    def __init__(self, x, y, game, time_in_secs, name=None, trigger_method=None):
        self.file_mid_prefix = 'timer_01'
        self.type = ActorType.CLOCK_TIMER_A
        super().__init__(x, y, game, name=name)

        self.clock = ClockTimer(self.game, time_in_secs, trigger_method=trigger_method or self.die_hard)

    def update(self):
        super().update()
        self.clock.tick()

    def draw_text(self):
        libg_jp.draw_text_rendered(
            text=self.clock.get_time_formatted(),
            x=self.rect.x + 12, y=self.rect.y + 3,
            screen=self.game.screen, color=Color.BLUE_VIOLET)

    def die_hard(self):
        log.debug(f"{self.id} killed when {self.clock.id} ticked {self.clock.get_time()} secs.")
        self.kill()


class ClockStopwatchA(Clock):
    """Represents a clock stopwatch of type A."""

    def __init__(self, x, y, game, time_in_secs, name=None):
        self.file_mid_prefix = 'timer_01'
        self.type = ActorType.CLOCK_STOPWATCH_A
        super().__init__(x, y, game, name=name)

        self.clock = ClockStopwatch(self.game, time_in_secs)

    def update(self):
        super().update()
        self.clock.tick()

    def draw_text(self):
        libg_jp.draw_text_rendered(
            text=self.clock.get_time_formatted(),
            x=self.rect.x + 12, y=self.rect.y + 3,
            screen=self.game.screen, color=Color.BLUE_VIOLET)

    def die_hard(self):
        log.debug(f"{self.id} killed when {self.clock.id} ticked {self.clock.get_time()} secs.")
        self.kill()
