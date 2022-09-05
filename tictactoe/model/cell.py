"""Module cell."""
__author__ = 'Joan A. Pinol  (japinol)'

from enum import Enum


class Cell(str, Enum):
    EMPTY = '·'
    X = 'X'
    O = 'O'
