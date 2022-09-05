"""Module computer_player."""
__author__ = 'Joan A. Pinol  (japinol)'

import math
import random

from tictactoe.model.player import PlayerBase


class ComputerPlayer(PlayerBase):

    def __init__(self, token, name):
        super().__init__(token, name, is_computer_player=True)

    def update(self, board):
        super().update(board)
        if len(board.available_moves()) > 8:
            location = random.choice(board.available_moves())
        else:
            location = self.minimax(board, self.token.value)['location']
        self.move_token(board, *location)

    def minimax(self, board_state, player_token):
        max_player = self.token.value
        opponent_player = 'O' if player_token == 'X' else 'X'
        if board_state.is_win() and board_state.current_turn_token == max_player:
            multiplier = 1 if opponent_player == max_player else -1
            return {'location': None,
                    'score': multiplier * (board_state.count_empty_cells() + 1),
                    }
        if board_state.is_draw():
            return {'location': None, 'score': 0}

        if player_token == max_player:
            best = {'location': None, 'score': -math.inf}
        else:
            best = {'location': None, 'score': math.inf}

        for possible_move in board_state.available_moves():
            self.move_token_sim(board_state, *possible_move, player_token)
            sim_score = self.minimax(board_state, opponent_player)
            # Rollback the board_state
            board_state.clean_cell(*possible_move)
            sim_score['location'] = possible_move
            # Maximize the max_player and minimize the opponent_player
            if player_token == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


class RandomComputerPlayer(PlayerBase):

    def __init__(self, token, name):
        super().__init__(token, name, is_computer_player=True)

    def update(self, board):
        super().update(board)
        self.move_token(board, *random.choice(board.available_moves()))
