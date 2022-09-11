"""Module __main__. Entry point."""
__author__ = 'Joan A. Pinol  (japinol)'

from argparse import ArgumentParser
import gc
import traceback
import sys

import pygame as pg

from tictactoe.config.constants import (
    TOURNAMENTS_MAX, GAMES_TO_PLAY_MAX,
    GAMES_TO_PLAY, TOURNAMENTS_TO_PLAY,
    TOURNAMENTS_WARGAME, GAMES_TO_PLAY_WARGAME,
    TURN_MAX_TIME_SECS, TURN_MAX_TIME_SECS_MAX,
    TURN_MAX_TIME_SECS_MIN,
    LOG_START_APP_MSG, LOG_END_APP_MSG,
    )
from tictactoe.game_entry_point import Game
from tictactoe.validator.validator import InputValidator
from tictactoe.tools.logger import logger
from tictactoe.tools.logger.logger import log, LOGGER_FORMAT, LOGGER_FORMAT_NO_DATE
from tictactoe import screen


def main():
    """Entry point of The Tic Tac Toe program."""
    # Parse optional arguments from the command line
    parser = ArgumentParser(description="Tic Tac Toe",
                            prog="tictactoe",
                            usage="%(prog)s usage: tictactoe [-h] [-a] [-g GAMESTOPLAY] [-u TOURNAMENTS] "
                                  "[-l] [-m] [-n] [-o] [-p] [-s TURNMAXSECS] [-w] [-d] [-t]")
    parser.add_argument('-a', '--auto', default=False, action='store_true',
                        help='Auto mode. It does not stop between games or tournaments. '
                             'Only when it needs a user input')
    parser.add_argument('-g', '--gamestoplay', default=GAMES_TO_PLAY,
                        help=f"Games to play on each tournament. Must be between 2 and {GAMES_TO_PLAY_MAX}")
    parser.add_argument('-u', '--tournaments', default=TOURNAMENTS_TO_PLAY,
                        help=f"Tournaments to play. Must be between 1 and {TOURNAMENTS_MAX}")
    parser.add_argument('-l', '--multiplelogfiles', default=False, action='store_true',
                        help='A log file by app execution, instead of one unique log file')
    parser.add_argument('-m', '--stdoutlog', default=False, action='store_true',
                        help='Print logs to the console along with writing them to the log file')
    parser.add_argument('-n', '--nologdatetime', default=False, action='store_true',
                        help='Logs will not print a datetime')
    parser.add_argument('-o', '--player1ai', default=False, action='store_true',
                        help='Player 1 will be controlled by the computer')
    parser.add_argument('-p', '--player2human', default=False, action='store_true',
                        help='Player 2 will be controlled by a human player')
    parser.add_argument('-s', '--turnmaxsecs', default=TURN_MAX_TIME_SECS,
                        help=f"Turn max seconds before the player who holds the turn loses the current game. "
                             f"Must be between {TURN_MAX_TIME_SECS_MIN} and {TURN_MAX_TIME_SECS_MAX}")
    parser.add_argument('-w', '--wargametraining', default=False, action='store_true',
                        help='War game training speculating on playing Tic Tac Toc. '
                             'It activates the following flags: player1ai, '
                             f'auto, tournaments {TOURNAMENTS_WARGAME}, gamestoplay {GAMES_TO_PLAY_WARGAME}')
    parser.add_argument('-d', '--debug', default=None, action='store_true',
                        help='Debug actions when pressing the right key, information and traces')
    parser.add_argument('-t', '--debugtraces', default=None, action='store_true',
                        help='Show debug back traces information when something goes wrong')
    args = parser.parse_args()

    logger_format = LOGGER_FORMAT_NO_DATE if args.nologdatetime else LOGGER_FORMAT
    args.stdoutlog and logger.add_stdout_handler(logger_format)
    logger.add_file_handler(args.multiplelogfiles, logger_format)

    tournaments = args.tournaments and int(args.tournaments) or 0
    games_to_play = args.gamestoplay and int(args.gamestoplay) or 0
    turn_max_secs = args.turnmaxsecs and int(args.turnmaxsecs) or 0
    auto = True if args.wargametraining else args.auto
    input_validator = InputValidator(tournaments, games_to_play, turn_max_secs)
    validate_input_errors = input_validator.validate_input()
    if validate_input_errors:
        for input_error in validate_input_errors:
            log.error(input_error)
        return

    pg.init()
    pg.mouse.set_visible(True)
    is_music_paused = False
    log.info(LOG_START_APP_MSG)
    not args.stdoutlog and print(LOG_START_APP_MSG)
    log.info(f"App arguments: {' '.join(sys.argv[1:])}")
    # Multiple games loop
    while not Game.is_exit_game:
        try:
            game = Game(is_debug=args.debug, is_player1_ai=args.player1ai, is_player2_ai=not args.player2human,
                        tournaments=tournaments, games_to_play=games_to_play,
                        turn_max_secs=turn_max_secs, wargame_training=args.wargametraining,
                        auto=auto, no_log_datetime=args.nologdatetime, stdout_log=args.stdoutlog)
            Game.stats_gen.update({'games_played': Game.current_game})
            game.is_music_paused = is_music_paused
            screen_start_game = screen.StartGame(game)
            if Game.stats_gen['current_tournament'] >= Game.stats_gen['tournaments_to_play'] \
                    and Game.current_game >= Game.stats_gen['games_to_play']:
                game.set_is_exit_game(True)
                break
            while not auto and game.is_start_screen:
                screen_start_game.start_up()
            if not Game.is_exit_game:
                game.start()
                is_music_paused = game.is_music_paused
                del screen_start_game
                del game
                gc.collect()
        except FileNotFoundError as e:
            if args.debugtraces or args.debug:
                traceback.print_tb(e.__traceback__)
            log.critical(f'File not found error: {e}')
            break
        except Exception as e:
            if args.debugtraces or args.debug:
                traceback.print_tb(e.__traceback__)
            log.critical(f'ERROR. Abort execution: {e}')
            not args.stdoutlog and print(f'CRITICAL ERROR. Abort execution: {e}')
            break
    log.info(LOG_END_APP_MSG)
    not args.stdoutlog and print(LOG_END_APP_MSG)
    pg.quit()


if __name__ == '__main__':
    main()
