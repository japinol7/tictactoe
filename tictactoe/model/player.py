"""Module player."""
__author__ = 'Joan A. Pinol  (japinol)'

from abc import ABC, abstractmethod

from tictactoe.tools.logger.logger import log


class PlayerBase(ABC):
    players = []

    def __init__(self, token, name, is_computer_player):
        self.name = name
        self.token = token
        self.is_computer_player = is_computer_player
        self.turn_played = False
        self.stats = {
            'tournament_victories': 0,
            'victories': 0,
            'defeats': 0,
            'draws': 0,
            'games_started': 0,
            'total_draws': 0,
            'total_games_played': 0,
            }
        self.stats_old = {key: None for key in self.stats}
        self.__class__.players.append(self)
        log.info(f"Create {self}")

    @abstractmethod
    def update(self, board):
        pass

    def move_token(self, board, x, y):
        board.set_token(self, x, y)
        log.info(f"Player {self.token} sets token in pos: x: {x}, y: {y}")

    @staticmethod
    def move_token_sim(board, x, y, player_token):
        board.set_token_sim(player_token, x, y)

    def update_stats_for_new_tournament(self):
        self.stats['victories'] = 0
        self.stats['defeats'] = 0
        self.stats['draws'] = 0
        self.stats['games_started'] = 0

    def __str__(self):
        return f"Player: {self.name} with Token: {self.token.value}. Class: {self.__class__.__name__}"

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"({self.token.__class__.__name__}.{self.token.value}, {self.name})"


class Player(PlayerBase):

    def __init__(self, token, name):
        super().__init__(token, name, is_computer_player=False)

    def update(self, board):
        super().update(board)
