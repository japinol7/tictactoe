"""Module board."""
__author__ = 'Joan A. Pinol  (japinol)'

from tictactoe.config.constants import CELL_SEPARATOR, CELL_SPRITE_CELL_MAP
from tictactoe.tools.logger.logger import log
from tictactoe.config.settings import Settings
from tictactoe.model.cell import Cell
from tictactoe.model.actors.cell_sprite import CellSprite


class Board:
    def __init__(self, current_game, current_tournament):
        self.rows = 3
        self.columns = 3
        self.empty_cells = 9
        self.grid = None
        self.sprite_grid = None
        self.sprite_cells_grid = None
        self.current_turn_token = None
        self._create()
        log.info(f"Create board for game: {current_game} of tournament: {current_tournament}\n{self}")

    def set_token(self, player, x, y):
        log.debug(f"{x=}, {y=}, {self.grid[x][y]=}")
        if self.grid[x][y] == Cell.EMPTY.value:
            self.grid[x][y] = player.token.value
            self.empty_cells -= 1
            player.turn_played = True
            self.sprite_cells_grid[x][y].frame_index = CELL_SPRITE_CELL_MAP[player.token.value]
            return
        log.warning(f"Warning: Illegal move for player {player.name}. "
                    f"Cell not empty at {x}, {y}. Current value: {self.grid[x][y]}")

    def set_token_sim(self, player_token, x, y):
        if self.grid[x][y] == Cell.EMPTY.value:
            self.grid[x][y] = player_token

    def available_moves(self):
        return [(x, y) for x, column in enumerate(self.grid) for y, cell in enumerate(column) if cell == Cell.EMPTY.value]

    def count_empty_cells(self):
        return len(self.available_moves())

    def is_win(self):
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] != Cell.EMPTY.value:
            return True
        if self.grid[1][0] == self.grid[1][1] == self.grid[1][2] != Cell.EMPTY.value:
            return True
        if self.grid[2][0] == self.grid[2][1] == self.grid[2][2] != Cell.EMPTY.value:
            return True
        if self.grid[0][0] == self.grid[1][0] == self.grid[2][0] != Cell.EMPTY.value:
            return True
        if self.grid[0][1] == self.grid[1][1] == self.grid[2][1] != Cell.EMPTY.value:
            return True
        if self.grid[0][2] == self.grid[1][2] == self.grid[2][2] != Cell.EMPTY.value:
            return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != Cell.EMPTY.value:
            return True
        if self.grid[2][0] == self.grid[1][1] == self.grid[0][2] != Cell.EMPTY.value:
            return True
        return False

    def is_draw(self):
        return len(self.available_moves()) < 1

    def clean_cell(self, x, y):
        self.grid[x][y] = Cell.EMPTY.value

    def _create(self):
        self._clean_grid()

    def _clean_grid(self):
        self.empty_cells = 9
        self.grid = [[Cell.EMPTY.value for _ in range(self.columns)]
                     for r in range(self.rows)]

    def init_graphic_board(self, game):
        self.sprite_cells_grid = [
            [
                CellSprite(*Settings.cells_pos_board[0, 0], game),
                CellSprite(*Settings.cells_pos_board[1, 0], game),
                CellSprite(*Settings.cells_pos_board[2, 0], game)
             ],
            [
                CellSprite(*Settings.cells_pos_board[0, 1], game),
                CellSprite(*Settings.cells_pos_board[1, 1], game),
                CellSprite(*Settings.cells_pos_board[2, 1], game)
            ],
            [
                CellSprite(*Settings.cells_pos_board[0, 2], game),
                CellSprite(*Settings.cells_pos_board[1, 2], game),
                CellSprite(*Settings.cells_pos_board[2, 2], game)
            ],
        ]

    def __str__(self):
        res = ''
        for row in self.grid:
            res += CELL_SEPARATOR.join([cell for cell in row]) + '\n'
        return res[:-1]

    def __repr__(self):
        return self.__str__()
