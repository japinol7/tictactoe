"""Module actor types."""
__author__ = 'Joan A. Pinol  (japinol)'

from enum import Enum


class ActorBaseType(Enum):
    NONE = 0
    ITEM = 1


class ActorCategoryType(Enum):
    NONE = 0
    CELL = 1
    CLOCK = 11


class ActorType(Enum):
    CELL = 1
    CLOCK_A = 11
    CLOCK_TIMER_A = 12
    CLOCK_STOPWATCH_A = 21
