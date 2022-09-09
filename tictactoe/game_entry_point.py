"""Module game entry point."""
__author__ = 'Joan A. Pinol  (japinol)'
__all__ = ['Game']

import pygame as pg

from tictactoe.model.actors.clock import ClockTimerA
from tictactoe.model.player import Player
from tictactoe.model.computer_player import ComputerPlayer
from tictactoe.score_bar import ScoreBar
from tictactoe.model.board import Board
from tictactoe.model.cell import Cell
from tictactoe.tools.utils.color import Color
from tictactoe.config.constants import (
    CELL_SPRITE_POSITION_MAP,
    FONT_DEFAULT_NAME,
    FONT_FIXED_DEFAULT_NAME,
    TOURNAMENTS_WARGAME, GAMES_TO_PLAY_WARGAME,
    LOG_WARGAME_START_MSG, LOG_WARGAME_END_MSG,
    LOG_START_APP_MSG,
    LOG_END_APP_MSG,
    )
from tictactoe.debug_info import DebugInfo
from tictactoe.help_info import HelpInfo
from tictactoe.tools.utils import utils_graphics as libg_jp
from tictactoe.resources import Resource
from tictactoe import screen
from tictactoe.tools.logger.logger import log
from tictactoe.config.settings import Settings


class Game:
    """Represents a 'Tic Tac Toe' game."""
    is_exit_game = False
    is_over = False
    is_first_game = True
    current_game = 0
    current_time = None
    turn_time_out = False
    K_b_keydown_seconds = False
    size = None
    screen = None
    screen_flags = None
    normal_screen_flags = None
    full_screen_flags = None
    wargame_training = False
    no_log_datetime = False
    stats_gen = {
        'current_game': 0,
        'games_played': 0,
        'turn_max_time_secs': 0,
        'tournaments_to_play': 0,
        'games_to_play': 0,
        'tournament_new': True,
        'current_tournament': 1,
        'tournament_winner': None,
        'tournament_winner_text': '',
        'tournaments_winners': [],
        'tournaments_winners_tokens': '',
        }
    stats_gen_old = {key: None for key in stats_gen}
    stats_gen.update({
        'turn_player': None,
        'turn_player_opponent': None,
        'players': [],
        })

    def __init__(self, is_debug=None, is_player1_ai=None, is_player2_ai=None,
                 tournaments=None, games_to_play=None, turn_max_secs=None,
                 speed_pct=None, wargame_training=None, no_log_datetime=None, auto=None):
        self.name = "Tic Tac Toe v 0.01"
        self.name_short = "Tic Tac Toe"
        self.name_long = "Tic Tac Toe"
        self.name_desc = "Tic Tac Toe  (c) 2012, 2022."
        Game.wargame_training = wargame_training
        if wargame_training:
            is_player1_ai = is_player2_ai = True
            tournaments = TOURNAMENTS_WARGAME
            games_to_play = GAMES_TO_PLAY_WARGAME
        self.is_player1_ai = is_player1_ai
        self.is_player2_ai = is_player2_ai
        self.auto = auto
        self.board = None
        self.stats = {}
        self.stats_old = {}
        self.start_time = None
        self.done = None
        self.players = None
        self.winner = None
        self.is_debug = is_debug
        self.is_paused = False
        self.is_start_screen = True
        self.is_full_screen_switch = False
        self.is_help_screen = False
        self.is_exit_curr_game_confirm = False
        self.is_music_paused = True
        self.sound_effects = True
        self.show_fps = False
        self.current_position = False
        self.clock = False
        self.active_sprites = None
        self.clock_in_game = None
        self.clock_sprites = None
        self.cell_sprites = None
        self.score_bars = None
        self.help_info = None
        self.debug_info = None
        self.current_song = 0
        self.writen_info_game_over_to_file = False
        self.screen_exit_current_game = None
        self.screen_game_over = None
        self.screen_pause = None
        self.screen_help = None
        self.mouse_pos = (0, 0)

        Game.is_exit_game = False
        if Game.current_game > 0:
            Game.is_first_game = False

        if Game.is_first_game:
            log.info(LOG_START_APP_MSG)
            Game.wargame_training and log.info(LOG_WARGAME_START_MSG)
            # Calculate settings
            Game.no_log_datetime = no_log_datetime
            Game.stats_gen['tournaments_to_play'] = tournaments
            Game.wargame_training = wargame_training
            pg_display_info = pg.display.Info()
            Settings.display_start_width = pg_display_info.current_w
            Settings.display_start_height = pg_display_info.current_h
            Settings.calculate_settings(tournaments=tournaments, games_to_play=games_to_play,
                                        turn_max_secs=turn_max_secs, speed_pct=speed_pct)
            Game.stats_gen.update({'turn_max_time_secs': Settings.turn_max_time_secs})
            Game.stats_gen.update({'games_to_play': Settings.games_to_play})
            # Set screen to the settings configuration
            Game.size = [Settings.screen_width, Settings.screen_height]
            Game.full_screen_flags = pg.FULLSCREEN | pg.DOUBLEBUF | pg.HWSURFACE | pg.SCALED
            Game.normal_screen_flags = pg.DOUBLEBUF | pg.HWSURFACE
            if Settings.is_full_screen:
                Game.screen_flags = Game.full_screen_flags
            else:
                Game.screen_flags = Game.normal_screen_flags
            Game.screen = pg.display.set_mode(Game.size, Game.screen_flags)
            # Load and render resources
            Resource.load_and_render_background_images()
            Resource.load_and_render_scorebar_images_and_txt()
            Resource.load_sound_resources()
            Resource.load_music_song(self.current_song)

            # Render characters in some colors to use it as a cache
            libg_jp.chars_render_text_tuple(font_name=FONT_DEFAULT_NAME)
            libg_jp.chars_render_text_tuple(font_name=FONT_FIXED_DEFAULT_NAME)

            # Create players
            player1_class = ComputerPlayer if self.is_player1_ai else Player
            player2_class = ComputerPlayer if self.is_player2_ai else Player
            Game.stats_gen['players'].extend([
                player1_class(Cell.X, name=1),
                player2_class(Cell.O, name=2),
                ])
            Game.stats_gen['turn_player'] = Game.stats_gen['players'][0]
            Game.stats_gen['turn_player_opponent'] = Game.stats_gen['players'][1]

            # Initialize music
            pg.mixer.music.set_volume(0.7)
            pg.mixer.music.play(loops=-1)
            if self.is_music_paused:
                pg.mixer.music.pause()
        else:
            if Game.stats_gen['turn_player'] == Game.stats_gen['players'][0]:
                Game.stats_gen['turn_player'] = Game.stats_gen['players'][1]
                Game.stats_gen['turn_player_opponent'] = Game.stats_gen['players'][0]
            else:
                Game.stats_gen['turn_player'] = Game.stats_gen['players'][0]
                Game.stats_gen['turn_player_opponent'] = Game.stats_gen['players'][1]

        self.turn_player = Game.stats_gen['turn_player']
        if self.board:
            self.board.current_turn_token = self.turn_player.token.value
        self.turn_player_opponent = Game.stats_gen['turn_player']
        self.score_bars = ScoreBar(self, Game.screen)
        # Initialize screens
        self.screen_exit_current_game = screen.ExitCurrentGame(self)
        self.screen_help = screen.Help(self)
        self.screen_pause = screen.Pause(self)
        self.screen_game_over = screen.GameOver(self)

    @staticmethod
    def campaign_winner():
        player1_tournament_victories = Game.stats_gen['players'][0].stats['tournament_victories']
        player2_tournament_victories = Game.stats_gen['players'][1].stats['tournament_victories']
        if player1_tournament_victories > player2_tournament_victories:
            return Game.stats_gen['players'][0], player1_tournament_victories, player2_tournament_victories
        elif player1_tournament_victories < player2_tournament_victories:
            return Game.stats_gen['players'][1], player1_tournament_victories, player2_tournament_victories
        return None, player1_tournament_victories, player2_tournament_victories

    @staticmethod
    def set_is_exit_game(is_exit_game):
        if is_exit_game:
            campaign_winner, player1_tournament_victories, player2_tournament_victories = Game.campaign_winner()
            if campaign_winner:
                log.info(f"Winner of this Tic Tac Toe campaign: "
                         f"Player {campaign_winner.name} with token {campaign_winner.token}. "
                         f"Score: {player1_tournament_victories} to {player2_tournament_victories}")
            elif Game.stats_gen['tournaments_winners_tokens']:
                log.info(f"Winner of this Tic Tac Toe campaign: It's a draw. "
                         f"Score: {player1_tournament_victories} to {player2_tournament_victories}")
                Game.wargame_training and log.info(LOG_WARGAME_END_MSG)
            else:
                log.info(f"Winner of this Tic Tac Toe campaign: None. No tournaments played to the end.")
            log.info(LOG_END_APP_MSG)
        Game.is_exit_game = is_exit_game

    def clock_in_game_trigger_method(self):
        Game.turn_time_out = True
        Game.is_over = True
        self.update_status_if_game_over()
        Game.stats_gen['turn_player'].stats['defeats'] += 1
        Game.stats_gen['turn_player_opponent'].stats['victories'] += 1
        log.info(f"Time out for player: {self.turn_player.token}")
        self.write_game_over_info_to_file()

    def write_game_over_info_to_file(self):
        self.debug_info.print_debug_info()
        # TODO: scores
        # Scores.write_scores_to_file(self)
        self.writen_info_game_over_to_file = True

    @staticmethod
    def draw_grid():
        for x in range(0, Settings.screen_width, Settings.cell_size):
            pg.draw.line(Game.screen, Color.GRAY10, (x, Settings.screen_near_top),
                         (x, Settings.screen_height))
        for y in range(Settings.screen_near_top, Settings.screen_height, Settings.cell_size):
            pg.draw.line(Game.screen, Color.GRAY10, (0, y), (Settings.screen_width, y))

    def put_initial_actors_on_the_board(self):
        self.active_sprites = pg.sprite.Group()
        self.clock_sprites = pg.sprite.Group()
        self.cell_sprites = pg.sprite.Group()

        self.board = Board(self.current_game, Game.stats_gen['current_tournament'])
        self.board.init_graphic_board(self)
        for sprites in self.board.sprite_cells_grid:
            self.cell_sprites.add(sprites)
        self.active_sprites.add(self.cell_sprites)

        log.info(f"Waiting input from player: {self.turn_player.token}")

        self.clock_in_game = ClockTimerA(990, Settings.board_base_y - 35, self, Settings.turn_max_time_secs,
                                         trigger_method=self.clock_in_game_trigger_method)
        self.active_sprites.add([self.clock_in_game])
        self.clock_sprites.add([self.clock_in_game])

    @staticmethod
    def update_tournament_stats():
        Game.stats_gen['current_tournament'] += 1
        Game.stats_gen['tournament_winner'] = None
        Game.stats_gen['tournament_winner_text'] = ''
        Game.current_game = Game.stats_gen['current_game'] = 0
        Game.stats_gen['games_played'] = 0
        Game.stats_gen['turn_player'].update_stats_for_new_tournament()
        Game.stats_gen['turn_player_opponent'].update_stats_for_new_tournament()

    def update_screen(self):
        # Handle game screens
        if self.is_paused or self.is_full_screen_switch:
            self.screen_pause.start_up(is_full_screen_switch=self.is_full_screen_switch)
        if self.is_help_screen:
            self.screen_help.start_up()
        elif self.is_exit_curr_game_confirm:
            self.screen_exit_current_game.start_up()
        elif Game.is_over and not self.auto:
            self.screen_game_over.start_up()
        else:
            if not Game.is_over:
                Game.screen.blit(Resource.images['background'], (0, 0))
                Game.screen.blit(Resource.images['board'], (Settings.board_x, Settings.board_y))
            elif not self.auto:
                Game.screen.blit(Resource.images['bg_blue_t2'], (0, 0))
            # Update score bars
            self.score_bars.update()

            if not Game.is_over:
                # Draw active sprites
                self.cell_sprites.update()
                self.active_sprites.draw(Game.screen)
                for clock in self.clock_sprites:
                    clock.draw_text()
                self.clock_sprites.update()

        self.show_fps and pg.display.set_caption(f"{self.clock.get_fps():.2f}")

    def change_turn_player(self):
        Game.stats_gen['turn_player'], Game.stats_gen['turn_player_opponent'] = Game.stats_gen['turn_player_opponent'], \
                                                                                Game.stats_gen['turn_player']
        self.turn_player = Game.stats_gen['turn_player']
        self.board.current_turn_token = self.turn_player.token.value
        self.turn_player_opponent = Game.stats_gen['turn_player_opponent']

    def update_status(self):
        is_game_over = False
        if self.board.is_win():
            is_game_over = True
            self.turn_player.stats['victories'] += 1
            self.turn_player_opponent.stats['defeats'] += 1
            self.winner = self.turn_player
            Game.is_over = True
            log.info(f"Player {self.turn_player.token} wins")
        elif self.board.empty_cells <= 0:
            is_game_over = True
            self.turn_player.stats['draws'] += 1
            self.turn_player.stats['total_draws'] += 1
            self.turn_player_opponent.stats['draws'] += 1
            self.turn_player_opponent.stats['total_draws'] += 1
            self.winner = None
            Game.is_over = True
            log.info("It's a draw")

        if is_game_over:
            self.turn_player.stats['total_games_played'] += 1
            self.turn_player_opponent.stats['total_games_played'] += 1
            self.update_status_if_game_over()

    def update_status_if_game_over(self):
        self.is_over = True
        self.done = True
        self.clock_in_game.clock.set_off()
        if Game.current_game >= Game.stats_gen['games_to_play']:
            if self.turn_player.stats['victories'] == self.turn_player_opponent.stats['victories']:
                tournament_winner = None
            elif self.turn_player.stats['victories'] > self.turn_player_opponent.stats['victories']:
                tournament_winner = self.turn_player
            else:
                tournament_winner = self.turn_player_opponent

            tournament_winner_token = tournament_winner and tournament_winner.token.value.lower() or '-'
            Game.stats_gen['tournament_winner'] = tournament_winner or None
            Game.stats_gen['tournament_winner_text'] = tournament_winner_token
            Game.stats_gen['tournaments_winners'] += [tournament_winner]
            Game.stats_gen['tournaments_winners_tokens'] = Game.stats_gen['tournaments_winners_tokens'] + tournament_winner_token
            Game.stats_gen['tournament_new'] = True
            if tournament_winner:
                tournament_winner.stats['tournament_victories'] += 1

    def start(self):
        Game.is_exit_game = False
        Game.is_over = False
        Game.stats_gen['tournament_new'] = False
        if Game.current_game >= Game.stats_gen['games_to_play']:
            self.update_tournament_stats()

        Game.current_game += 1
        Game.stats_gen.update({'current_game': Game.current_game})
        pg.display.set_caption(self.name_short)
        self.clock = pg.time.Clock()
        self.start_time = pg.time.get_ticks()

        self.put_initial_actors_on_the_board()

        self.help_info = HelpInfo()
        self.debug_info = DebugInfo(self)

        if Game.is_first_game:
            Resource.render_text_frequently_used(self)
            self.debug_info.print_debug_info()

        # Current game loop
        self.done = False
        while not self.done:
            self.current_time = pg.time.get_ticks()
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.is_exit_curr_game_confirm = True
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        if Settings.can_games_be_paused and not self.auto:
                            self.is_paused = True
                    elif event.key == pg.K_d and not self.auto:
                        if self.is_debug and pg.key.get_mods() & pg.KMOD_LCTRL:
                            self.debug_info.print_debug_info()
                    elif event.key == pg.K_s:
                        if pg.key.get_mods() & pg.KMOD_LCTRL:
                            self.sound_effects = not self.sound_effects
                    elif event.key == pg.K_m:
                        if pg.key.get_mods() & pg.KMOD_LCTRL:
                            self.is_music_paused = not self.is_music_paused
                            if self.is_music_paused:
                                pg.mixer.music.pause()
                            else:
                                pg.mixer.music.unpause()
                    elif event.key == pg.K_F1 and not self.turn_player.is_computer_player:
                        if not self.is_exit_curr_game_confirm:
                            self.is_help_screen = not self.is_help_screen
                    elif event.key in (pg.K_KP_ENTER, pg.K_RETURN) and not self.auto:
                        if pg.key.get_mods() & pg.KMOD_LALT and pg.key.get_mods() & pg.KMOD_RALT:
                            self.is_paused = True
                            self.is_full_screen_switch = True
                elif not self.turn_player.is_computer_player and event.type == pg.KEYUP:
                    if event.key in (pg.K_KP1, pg.K_1):
                        self.turn_player.move_token(self.board, 2, 0)
                    if event.key in (pg.K_KP2, pg.K_2):
                        self.turn_player.move_token(self.board, 2, 1)
                    if event.key in (pg.K_KP3, pg.K_3):
                        self.turn_player.move_token(self.board, 2, 2)
                    if event.key in (pg.K_KP4, pg.K_4):
                        self.turn_player.move_token(self.board, 1, 0)
                    if event.key in (pg.K_KP5, pg.K_5):
                        self.turn_player.move_token(self.board, 1, 1)
                    if event.key in (pg.K_KP6, pg.K_6):
                        self.turn_player.move_token(self.board, 1, 2)
                    if event.key in (pg.K_KP7, pg.K_7):
                        self.turn_player.move_token(self.board, 0, 0)
                    if event.key in (pg.K_KP8, pg.K_8):
                        self.turn_player.move_token(self.board, 0, 1)
                    if event.key in (pg.K_KP9, pg.K_9):
                        self.turn_player.move_token(self.board, 0, 2)
                    if event.key == pg.K_F5:
                        self.show_fps = not self.show_fps
                elif not self.turn_player.is_computer_player and event.type == pg.MOUSEBUTTONDOWN:
                    self.mouse_pos = pg.mouse.get_pos()
                    for sprite in self.cell_sprites:
                        if sprite.rect.collidepoint(self.mouse_pos):
                            self.turn_player.move_token(self.board, *CELL_SPRITE_POSITION_MAP[sprite.name])

            if not self.turn_player.turn_played and self.turn_player.is_computer_player:
                self.turn_player.update(self.board)

            if self.turn_player.turn_played and not self.is_over:
                self.clock_in_game.clock.restart()
                self.update_screen()
                self.update_status()
                self.turn_player.turn_played = False
                self.change_turn_player()
                log.info(f'Board:\n{self.board}')
                if not self.is_over:
                    log.info(f"Waiting input from player: {self.turn_player.token}")
                else:
                    self.write_game_over_info_to_file()

            self.update_screen()
            self.is_paused and self.clock.tick(Settings.fps_paused) or self.clock.tick(Settings.fps)
            pg.display.flip()
