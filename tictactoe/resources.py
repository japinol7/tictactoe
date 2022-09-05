"""Module resources."""
__author__ = 'Joan A. Pinol  (japinol)'

import os

import pygame as pg

from tictactoe.tools.utils.color import Color
from tictactoe.config import constants as consts
from tictactoe.tools.utils import utils_graphics as libg_jp
from tictactoe.config.settings import Settings


def file_name_get(name, subname='', folder=consts.BITMAPS_FOLDER):
    return os.path.join(
        folder,
        f"{consts.FILE_NAMES['%s%s' % (name, subname)][0]}"
        f".{consts.FILE_NAMES['%s%s' % (name, subname)][1]}")


class Resource:
    """Some resources used in the game that do not have their own class."""
    apple_hit_sound = None
    images = {}
    txt_surfaces = {'game_paused': None, 'player_wins': None,
                    'game_turn_time_out': None, 'game_turn_time_out_2': None,
                    'press_intro_to_continue_center': None,
                    'press_intro_to_continue': None, 'press_intro_to_continue_2': None,
                    'tournament_start': None, 'tournament_start_2': None,
                    'game_start': None, 'game_start_2': None,
                    'level_no': None,
                    'congrats': None, 'congrats_2': None,
                    'token_O_wins': None, 'token_O_wins_2': None,
                    'token_X_wins': None, 'token_X_wins_2': None,
                    'it_is_a_draw': None, 'it_is_a_draw_2': None,
                    }

    @classmethod
    def load_sound_resources(cls):
        cls.apple_hit_sound = pg.mixer.Sound(file_name_get(name='snd_apple_hit', folder=consts.SOUNDS_FOLDER))

    @classmethod
    def render_text_frequently_used(cls, game):
        libg_jp.render_text('– PAUSED –',*Settings.board_base_center,
                            cls.txt_surfaces, 'game_paused', color=Color.CYAN,
                            size=int(148*Settings.font_pos_factor), align="center")

        libg_jp.render_text('– Press Escape to Exit this Game  –', Settings.screen_width // 2,
                            (Settings.screen_height // 2.6) - int(6 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'exit_current_game_confirm', color=Color.CYAN,
                            size=int(78*Settings.font_pos_factor_t2), align="center")

        libg_jp.render_text('– Press Enter to Continue –', Settings.screen_width // 2,
                            (Settings.screen_height // 1.764) + int(82 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'press_intro_to_continue_center', color=Color.CYAN,
                            size=int(82*Settings.font_pos_factor_t2), align="center")

        libg_jp.render_text("TIME OUT", Settings.screen_width // 1.99,
                            Settings.screen_height // 2.484,
                            cls.txt_surfaces, 'game_turn_time_out', color=Color.BLUE,
                            size=int(120*Settings.font_pos_factor), align="center")
        libg_jp.render_text("TIME OUT", Settings.screen_width // 2,
                            Settings.screen_height // 2.5,
                            cls.txt_surfaces, 'game_turn_time_out_2', color=Color.CYAN,
                            size=int(120*Settings.font_pos_factor), align="center")

        libg_jp.render_text('Press Enter to Continue', Settings.board_base_center[0],
                            (Settings.screen_height // 1.88) + int(82 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'press_intro_to_continue', color=Color.BLUE,
                            size=int(82*Settings.font_pos_factor_t2), align="center")
        libg_jp.render_text('Press Enter to Continue', Settings.board_base_center[0] / 1.002,
                            (Settings.screen_height // 1.896) + int(82 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'press_intro_to_continue_2', color=Color.CYAN,
                            size=int(82*Settings.font_pos_factor_t2), align="center")

        libg_jp.render_text('Token O Wins', Settings.board_base_center[0],
                            (Settings.screen_height // 1.22) + int(82 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'token_O_wins', color=Color.BLUE,
                            size=int(82*Settings.font_pos_factor_t2), align="center")
        libg_jp.render_text('Token O Wins', Settings.board_base_center[0] / 1.002,
                            (Settings.screen_height // 1.226) + int(82 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'token_O_wins_2', color=Color.CYAN,
                            size=int(82*Settings.font_pos_factor_t2), align="center")

        libg_jp.render_text('Token X Wins', Settings.board_base_center[0],
                            (Settings.screen_height // 1.22) + int(82 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'token_X_wins', color=Color.BLUE,
                            size=int(82*Settings.font_pos_factor_t2), align="center")
        libg_jp.render_text('Token X Wins', Settings.board_base_center[0] / 1.002,
                            (Settings.screen_height // 1.226) + int(82 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'token_X_wins_2', color=Color.CYAN,
                            size=int(82*Settings.font_pos_factor_t2), align="center")

        libg_jp.render_text("It's a draw", Settings.board_base_center[0],
                            (Settings.screen_height // 1.22) + int(82 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'it_is_a_draw', color=Color.BLUE,
                            size=int(82*Settings.font_pos_factor_t2), align="center")
        libg_jp.render_text("It's a draw", Settings.board_base_center[0] / 1.002,
                            (Settings.screen_height // 1.226) + int(82 * Settings.font_pos_factor_t2),
                            cls.txt_surfaces, 'it_is_a_draw_2', color=Color.CYAN,
                            size=int(82*Settings.font_pos_factor_t2), align="center")

    @classmethod
    def load_and_render_background_images(cls):
        """Load and render background images and effects."""
        img = pg.Surface((Settings.screen_width, Settings.screen_height)).convert_alpha()
        img.fill((0, 0, 0, 55))
        cls.images['dim_screen'] = img

        img = pg.image.load(file_name_get(folder=consts.BM_BACKGROUNDS_FOLDER,
                                          name='im_background', subname='')).convert()
        img = pg.transform.smoothscale(img, (Settings.screen_width, Settings.screen_height))
        cls.images['background'] = img

        img = pg.image.load(file_name_get(folder=consts.BM_BACKGROUNDS_FOLDER,
                                          name='bg_blue_t1_big_logo', subname='')).convert()
        img = pg.transform.smoothscale(img, (Settings.screen_width, Settings.screen_height))
        cls.images['bg_blue_t1'] = img

        img = pg.image.load(file_name_get(folder=consts.BM_BACKGROUNDS_FOLDER,
                                          name=Settings.im_screen_help)).convert()
        cls.images['screen_help'] = img

        img = pg.image.load(file_name_get(folder=consts.BM_BACKGROUNDS_FOLDER,
                                          name=Settings.im_bg_start_game)).convert()
        img = pg.transform.smoothscale(img, (Settings.screen_width_adjusted,
                                             Settings.screen_height_adjusted))
        cls.images['screen_start'] = img

        img = pg.image.load(file_name_get(name='im_help_key')).convert()
        img = pg.transform.smoothscale(img, (int((Settings.help_key_size.w)
                                                 * Settings.font_pos_factor_t2),
                                             int(Settings.help_key_size.h
                                                 * Settings.font_pos_factor_t2)))
        cls.images['help_key'] = img

        img = pg.image.load(file_name_get(folder=consts.BM_LOGOS_FOLDER,
                                          name='im_logo_japinol')).convert()
        img = pg.transform.smoothscale(img, (173, 39))
        cls.images['logo_jp'] = img

        img = pg.image.load(file_name_get(name='im_board')).convert()
        cls.images['board'] = img
        Settings.board_width = Resource.images['board'].get_width()
        Settings.board_height = Resource.images['board'].get_height()
        Settings.board_x = Settings.board_base_x - Settings.board_width // 2 + Settings.board_base_width // 2
        Settings.board_y = Settings.board_base_y - Settings.board_height // 2 + Settings.board_base_height // 2

    @classmethod
    def load_and_render_scorebar_images_and_txt(cls):
        libg_jp.render_text('Turn:', 760, 16,
                            cls.txt_surfaces, 'sb_turn_token', color=Color.BLUE_VIOLET)

        libg_jp.render_text('v.', 1170, 16,
                            cls.txt_surfaces, 'sb_version', color=Color.BLACK_SAFE)

        y = Settings.score_pos_label[1]
        libg_jp.render_text('Current Tournament:', Settings.score_pos_label[0], y,
                            cls.txt_surfaces, 'sb_current_tournament', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Tournaments Winners:', Settings.score_pos_label[0], y,
                            cls.txt_surfaces, 'sb_tournaments_winners', color=Color.GREEN_DARK)

        y += Settings.text_y_distance * 3
        libg_jp.render_text('Games to Play:', Settings.score_pos_label[0], y,
                            cls.txt_surfaces, 'sb_games_to_play', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Turn Max Seconds:', Settings.score_pos_label[0], y,
                            cls.txt_surfaces, 'sb_turn_max_time_secs', color=Color.GREEN_DARK)

        y += Settings.text_y_distance * 2
        libg_jp.render_text('Current Game:', Settings.score_pos_label[0], y,
                            cls.txt_surfaces, 'sb_current_game', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Games Played:', Settings.score_pos_label[0], y,
                            cls.txt_surfaces, 'sb_games_played', color=Color.GREEN_DARK)

        y += Settings.text_y_distance * 2.5
        libg_jp.render_text('Player 1', Settings.score_pos_label[0], y,
                            cls.txt_surfaces, 'sb_player1', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Token:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player1_token', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Victories:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player1_victories', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Defeats:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player1_defeats', color=Color.RED)
        y += Settings.text_y_distance
        libg_jp.render_text('Draws:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player1_draws', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Games Started:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player1_games_started', color=Color.GREEN_DARK)

        y += Settings.text_y_distance * 2.5
        libg_jp.render_text('Player 2', Settings.score_pos_label[0], y,
                            cls.txt_surfaces, 'sb_player2', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Token:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player2_token', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Victories:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player2_victories', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Defeats:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player2_defeats', color=Color.RED)
        y += Settings.text_y_distance
        libg_jp.render_text('Draws:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player2_draws', color=Color.GREEN_DARK)
        y += Settings.text_y_distance
        libg_jp.render_text('Games Started:', Settings.score_pos_label[0] + 30, y,
                            cls.txt_surfaces, 'sb_player2_games_started', color=Color.GREEN_DARK)

    @staticmethod
    def load_music_song(current_song):
        pg.mixer.music.load(os.path.join(consts.MUSIC_FOLDER, consts.MUSIC_BOX[current_song]))
