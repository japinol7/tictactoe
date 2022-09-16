import pytest

from tictactoe.model.board import Board
from tictactoe.model.computer_player import ComputerPlayer
from tictactoe.model.cell import Cell


def create_players_and_board(cell_sprite):
    """Helper function to initialize the players and the board."""
    player1 = ComputerPlayer(Cell.X, 'player1')
    player2 = ComputerPlayer(Cell.O, 'player2')
    board = Board(1, 1)
    board.sprite_cells_grid = [[cell_sprite for _ in range(board.columns)] for r in range(board.rows)]
    return player1, player2, board


@pytest.mark.parametrize("player1_moves, player2_moves", [
    (((1, 1), (0, 2), (1, 0), (2, 2)), ((0, 0), (2, 0), (1, 2), (0, 1))),
    (((0, 0), (2, 0), (1, 2), (0, 1)), ((1, 1), (0, 2), (1, 0), (2, 2))), ])
def test_computer_player_move__one_cell_left(cell_sprite_mock, player1_moves, player2_moves):
    """Gets the correct move when there is only one cell left to move to."""
    player1, player2, board = create_players_and_board(cell_sprite_mock)
    for player1_move, player2_move in zip(player1_moves, player2_moves):
        board.set_token(player1, *player1_move)
        board.set_token(player2, *player2_move)
    board.current_turn_token = 'O'

    result_expected = (2, 1)
    result = player2.minimax(board, player2.token.value)['location']
    assert result == result_expected


@pytest.mark.parametrize("player1_moves, player2_moves", [
    (((1, 1), (2, 0), (0, 1)), ((0, 2), (2, 2))),
    (((1, 0), (2, 0), (0, 1)), ((0, 2), (2, 2))), ],
    ids=lambda x: f"{x}")
def test_computer_player_move__win(cell_sprite_mock, player1_moves, player2_moves):
    """Gets the correct move to win after the opponent player makes a mistake."""
    player1, player2, board = create_players_and_board(cell_sprite_mock)
    for player1_move, player2_move in zip(player1_moves[:2], player2_moves):
        board.set_token(player1, *player1_move)
        board.set_token(player2, *player2_move)
    board.set_token(player1, *player1_moves[2])
    board.current_turn_token = 'O'

    result_expected = (1, 2)
    result = player2.minimax(board, player2.token.value)['location']
    assert result == result_expected


def test_computer_player_move__win_2_moves(cell_sprite_mock):
    """Gets the best move to have two winning next moves."""
    player1, player2, board = create_players_and_board(cell_sprite_mock)

    player1_moves = ((2, 1), (0, 0))
    player2_moves = ((2, 0), (1, 2))
    for player1_move, player2_move in zip(player1_moves, player2_moves):
        board.set_token(player1, *player1_move)
        board.set_token(player2, *player2_move)
    board.current_turn_token = 'X'

    result_expected = (0, 1)
    result = player1.minimax(board, player1.token.value)['location']
    assert result == result_expected


def test_computer_player_move__block(cell_sprite_mock):
    """Gets the correct move to block the opponent player from winning."""
    player1, player2, board = create_players_and_board(cell_sprite_mock)

    player1_moves = ((1, 1), (2, 1))
    player2_moves = ((0, 0), (0, 1))
    for player1_move, player2_move in zip(player1_moves, player2_moves):
        board.set_token(player1, *player1_move)
        board.set_token(player2, *player2_move)
    board.set_token(player1, 0, 2)
    board.current_turn_token = 'O'

    result_expected = (2, 0)
    result = player2.minimax(board, player2.token.value)['location']
    assert result == result_expected


def test_computer_player_move__block_2(cell_sprite_mock):
    """Gets the correct move to block the opponent player from winning. Case two."""
    player1, player2, board = create_players_and_board(cell_sprite_mock)

    player1_moves = ((1, 1), (0, 0))
    player2_moves = ((0, 2), (2, 2))
    for player1_move, player2_move in zip(player1_moves, player2_moves):
        board.set_token(player1, *player1_move)
        board.set_token(player2, *player2_move)
    board.set_token(player1, 1, 2)
    board.current_turn_token = 'O'

    result_expected = (1, 0)
    result = player2.minimax(board, player2.token.value)['location']
    assert result == result_expected
