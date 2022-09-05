"""Module score_bars."""
__author__ = 'Joan A. Pinol  (japinol)'

from tictactoe.tools.utils.color import Color
from tictactoe.tools.utils import utils_graphics as libg_jp
from tictactoe.resources import Resource
from tictactoe.config.settings import Settings
from tictactoe.version import version


class ScoreBar:
    """Represents a score bar."""

    def __init__(self, game, screen):
        self.game = game
        self.game_cls = game.__class__
        self.player1 = self.game_cls.stats_gen['players'][0]
        self.player2 = self.game_cls.stats_gen['players'][1]
        self.screen = screen

    def draw_chars_render_text(self, text, x, y, color=Color.YELLOW):
        libg_jp.draw_text_rendered(text, x, y, self.screen, color)

    def render_stats_if_necessary(self, x, y, stats_name, color=Color.BLUE_VIOLET):
        libg_jp.draw_text_rendered(text=f'{self.game.stats[stats_name]}',
                                   x=x, y=y, screen=self.screen, color=color)
        if self.game.stats[stats_name] != self.game.stats_old[stats_name]:
            self.game.stats_old[stats_name] = self.game.stats[stats_name]

    def render_stats_gen_if_necessary(self, x, y, stats_name, color=Color.BLUE_VIOLET):
        libg_jp.draw_text_rendered(text=f'{self.game_cls.stats_gen[stats_name]}',
                                   x=x, y=y, screen=self.screen, color=color)
        if self.game_cls.stats_gen[stats_name] != self.game_cls.stats_gen_old[stats_name]:
            self.game_cls.stats_gen_old[stats_name] = self.game_cls.stats_gen[stats_name]

    def render_player_stats_if_necessary(self, x, y, player, stats_name, color=Color.BLUE_VIOLET):
        libg_jp.draw_text_rendered(text=f'{player.stats[stats_name]}',
                                   x=x, y=y, screen=self.screen, color=color)
        if player.stats[stats_name] != player.stats_old[stats_name]:
            player.stats_old[stats_name] = player.stats[stats_name]

    def render_player_attributes_if_necessary(self, x, y, player, stats_name, color=Color.BLUE_VIOLET):
        libg_jp.draw_text_rendered(text=f'{player.__dict__[stats_name]}',
                                   x=x, y=y, screen=self.screen, color=color)

    def draw_general_stats(self):
        # Draw score titles
        self.screen.blit(*Resource.txt_surfaces['sb_games_to_play'])
        self.screen.blit(*Resource.txt_surfaces['sb_current_game'])
        self.screen.blit(*Resource.txt_surfaces['sb_games_played'])
        self.screen.blit(*Resource.txt_surfaces['sb_turn_max_time_secs'])
        self.screen.blit(*Resource.txt_surfaces['sb_turn_token'])
        self.screen.blit(*Resource.txt_surfaces['sb_version'])
        self.screen.blit(*Resource.txt_surfaces['sb_player1'])
        self.screen.blit(*Resource.txt_surfaces['sb_player1_token'])
        self.screen.blit(*Resource.txt_surfaces['sb_player1_victories'])
        self.screen.blit(*Resource.txt_surfaces['sb_player1_defeats'])
        self.screen.blit(*Resource.txt_surfaces['sb_player1_draws'])
        self.screen.blit(*Resource.txt_surfaces['sb_player1_games_started'])
        self.screen.blit(*Resource.txt_surfaces['sb_player2'])
        self.screen.blit(*Resource.txt_surfaces['sb_player2_token'])
        self.screen.blit(*Resource.txt_surfaces['sb_player2_victories'])
        self.screen.blit(*Resource.txt_surfaces['sb_player2_defeats'])
        self.screen.blit(*Resource.txt_surfaces['sb_player2_draws'])
        self.screen.blit(*Resource.txt_surfaces['sb_player2_games_started'])
        self.screen.blit(*Resource.txt_surfaces['sb_current_tournament'])
        self.screen.blit(*Resource.txt_surfaces['sb_tournaments_winners'])

        # Draw score stats and render them if needed
        libg_jp.draw_text_rendered(text=f"{self.game_cls.stats_gen['turn_player'].token}",
                                   x=820, y=16, screen=self.screen, color=Color.BLUE_VIOLET)
        libg_jp.draw_text_rendered(text=f"{version.get_version()}",
                                   x=1194, y=16, screen=self.screen, color=Color.BLACK_SAFE,
                                   space_btw_chars=12, is_font_fixed=False)
        y = 0
        self.render_stats_gen_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y, 'current_tournament')
        y += Settings.text_y_distance * 2
        self.render_stats_gen_if_necessary(Settings.score_pos_label[0] + 15, Settings.score_pos_label[1] + y, 'tournaments_winners_tokens')

        y += Settings.text_y_distance * 2
        self.render_stats_gen_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y, 'games_to_play')
        y += Settings.text_y_distance
        self.render_stats_gen_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y, 'turn_max_time_secs')

        y += Settings.text_y_distance * 2
        self.render_stats_gen_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y, 'current_game')
        y += Settings.text_y_distance
        self.render_stats_gen_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y, 'games_played')

        y += Settings.text_y_distance * 3.5
        self.render_player_attributes_if_necessary(Settings.score_pos_x - 1.6, Settings.score_pos_label[1] + y,
                                                   self.player1, 'token', color=Color.BLACK_SAFE)
        y += Settings.text_y_distance
        self.render_player_stats_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y,
                                              self.player1, 'victories')
        y += Settings.text_y_distance
        self.render_player_stats_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y,
                                              self.player1, 'defeats', color=Color.RED)
        y += Settings.text_y_distance
        self.render_player_stats_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y,
                                              self.player1, 'draws')
        y += Settings.text_y_distance
        self.render_player_stats_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y,
                                              self.player1, 'games_started')

        y += Settings.text_y_distance * 3.5
        self.render_player_attributes_if_necessary(Settings.score_pos_x - 1.6, Settings.score_pos_label[1] + y,
                                                   self.player2, 'token', color=Color.BLACK_SAFE)
        y += Settings.text_y_distance
        self.render_player_stats_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y,
                                              self.player2, 'victories')
        y += Settings.text_y_distance
        self.render_player_stats_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y,
                                              self.player2, 'defeats', color=Color.RED)
        y += Settings.text_y_distance
        self.render_player_stats_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y,
                                              self.player2, 'draws')
        y += Settings.text_y_distance
        self.render_player_stats_if_necessary(Settings.score_pos_x, Settings.score_pos_label[1] + y,
                                              self.player2, 'games_started')

    def update(self):
        self.draw_general_stats()
