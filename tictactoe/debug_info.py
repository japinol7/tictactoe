"""Module debug info."""
__author__ = 'Joan A. Pinol  (japinol)'

from datetime import datetime
from collections import OrderedDict

from tictactoe.tools.logger.logger import log
from tictactoe.tools.utils.utils import pretty_dict_to_string


class DebugInfo:

    def __init__(self, game):
        self.game = game

    @staticmethod
    def print_help_keys():
        print('  ^ numpad_divide: \t interactive debug output\n'
              '  ^n: \t print a list of all NPCs in all levels, ordered by level\n'
              '  ^ Shift + n: \t print a list of all NPCs in all levels, ordered by NPC name\n'
              '  ^d: \t print debug information to console\n'
              '  ^l: \t write debug information to a log file\n'
              )

    def print_debug_info(self):
        debug_dict = OrderedDict([
            ('Time', str(datetime.now())),
            ('Full screen', self.game.is_full_screen_switch),
            ('------', '------'),
            ('Tournaments to play', self.game.stats_gen['tournaments_to_play']),
            ('Games for tournament', self.game.stats_gen['games_to_play']),
            ('Turn max time in secs', self.game.stats_gen['turn_max_time_secs']),
            ('-------', '------'),
            ('Current Tournament', self.game.stats_gen['current_tournament']),
            ('Current Game', self.game.stats_gen['current_game']),
            ('--------', '------------'),
            ('Player 1 Game stats for current tournament', ''),
            ('\t* Token', self.game.stats_gen['players'][0].token.value),
            ('\t* Computer Controlled', self.game.stats_gen['players'][0].is_computer_player),
            ('----', '------'),
            ('\t* Total Draws', self.game.stats_gen['players'][0].stats['total_draws']),
            ('\t* Total Games Played', self.game.stats_gen['players'][0].stats['total_games_played']),
            ('\t* Victories', self.game.stats_gen['players'][0].stats['victories']),
            ('\t* Defeats', self.game.stats_gen['players'][0].stats['defeats']),
            ('\t* Draws', self.game.stats_gen['players'][0].stats['draws']),
            ('\t* Tournament Victories', self.game.stats_gen['players'][0].stats['tournament_victories']),
            ('---------', '------------'),
            ('Player 2 Game stats for current tournament', ''),
            ('\t+ Token', self.game.stats_gen['players'][1].token.value),
            ('\t+ Computer Controlled', self.game.stats_gen['players'][1].is_computer_player),
            ('---', '------'),
            ('\t+ Total Draws', self.game.stats_gen['players'][1].stats['total_draws']),
            ('\t+ Total Games Played', self.game.stats_gen['players'][1].stats['total_games_played']),
            ('\t+ Victories', self.game.stats_gen['players'][1].stats['victories']),
            ('\t+ Defeats', self.game.stats_gen['players'][1].stats['defeats']),
            ('\t+ Draws', self.game.stats_gen['players'][1].stats['draws']),
            ('\t+ Tournament Victories', self.game.stats_gen['players'][1].stats['tournament_victories']),
            ('----------', '------------'),
            ('Tournament Winner', self.game.stats_gen['tournament_winner_text']),
            ('-----------', '------'),
            ('Tournaments Winners', self.game.stats_gen['tournaments_winners_tokens']),
        ])
        debug_info_title = 'Current game stats:'
        debug_info = f"{debug_info_title}\n"

        debug_info = f"{debug_info}{pretty_dict_to_string(debug_dict, with_last_new_line=True)}" \
                     f"{'-' * 62}"
        log.info(debug_info)
