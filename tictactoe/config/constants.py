"""Module constants."""
__author__ = 'Joan A. Pinol  (japinol)'

from datetime import datetime
import os
import sys

from tictactoe.version import version

APP_NAME = 'tictactoe'

GAMES_TO_PLAY = 2
TOURNAMENTS_TO_PLAY = 10
TOURNAMENTS_MAX = 30
TURN_MAX_TIME_SECS = 15

GAMES_TO_PLAY_MAX = 5000
TURN_MAX_TIME_SECS_MIN = 5
TURN_MAX_TIME_SECS_MAX = 900

TOURNAMENTS_WARGAME = 1
GAMES_TO_PLAY_WARGAME = 500

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 900

SCROLL_NEAR_LEFT_SIDE = 380
SCROLL_NEAR_RIGHT_SIDE = SCREEN_WIDTH - SCROLL_NEAR_LEFT_SIDE
NEAR_LEFT_SIDE = 25

SCROLL_NEAR_TOP = 300
SCROLL_NEAR_BOTTOM = SCREEN_HEIGHT - SCROLL_NEAR_TOP

NEAR_TOP = 40
NEAR_BOTTOM = SCREEN_HEIGHT - NEAR_TOP
NEAR_EARTH = 40
SCREEN_NEAR_EARTH = SCREEN_HEIGHT - NEAR_EARTH
NEAR_BOTTOM_WHEN_PLATFORM = SCREEN_HEIGHT - NEAR_EARTH

NEAR_RIGHT_SIDE = SCREEN_WIDTH - NEAR_LEFT_SIDE

SCREEN_BAR_NEAR_TOP = 10
SCREEN_BAR_NEAR_BOTTOM = SCREEN_HEIGHT - 25

CELL_SEPARATOR = ' | '

LOG_START_APP_MSG = f"Start app {APP_NAME} version: {version.get_version()}"
LOG_END_APP_MSG = f"End app {APP_NAME}"

LOG_FILE = os.path.join('logs', f"log_{datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f')}.log")
LOG_FILE_UNIQUE = os.path.join('logs', "log.log")
SYS_STDOUT = sys.stdout
SCORES_FILE = os.path.join('files', 'scores.txt')

LOG_INPUT_ERROR_PREFIX_MSG = "User input error. "

SOUND_FORMAT = 'ogg'
MUSIC_FORMAT = 'ogg'

LOG_WARGAME_START_MSG = """Wargame Training mode ON. 
Playing 'Global Thermonuclear Warfare' alongside Tic Tac Toe. DEFCON 2."""
LOG_WARGAME_END_MSG = """Wargame Training mode OFF. 
- Greetings, Professor Falken.
- Hello, Joshua.
- Strange game [referring to Global Thermonuclear Warfare].
  The only winning move is not to play. 
  How about a nice game of chess?
- Colonel, take us to DEFCON 5.
  [(c) WarGames, 1983, an American science fiction techno-thriller film written 
  by L. Lasker and W. F. Parkes and directed by John Badham]."""

# If the code is frozen, use this path:
if getattr(sys, 'frozen', False):
    CURRENT_PATH = sys._MEIPASS
    BITMAPS_FOLDER = os.path.join(CURRENT_PATH, 'assets', 'img')
    SOUNDS_FOLDER = os.path.join(CURRENT_PATH, 'assets', 'snd', SOUND_FORMAT)
    MUSIC_FOLDER = os.path.join(CURRENT_PATH, 'assets', 'music')
    FONT_FOLDER = os.path.join(CURRENT_PATH, 'assets', 'data')
    FONT_DEFAULT_NAME = os.path.join(FONT_FOLDER, 'sans.ttf')
    FONT_FIXED_DEFAULT_NAME = os.path.join(FONT_FOLDER, 'fixed.ttf')
else:
    CURRENT_PATH = '.'
    # CURRENT_PATH = os.path.join(CURRENT_PATH, '..')
    BITMAPS_FOLDER = os.path.join(CURRENT_PATH, 'assets', 'img')
    SOUNDS_FOLDER = os.path.join(CURRENT_PATH, 'assets', 'snd', SOUND_FORMAT)
    MUSIC_FOLDER = os.path.join(CURRENT_PATH, 'assets', 'music')
    FONT_DEFAULT_NAME = os.path.join(CURRENT_PATH, 'assets', 'data', 'sans.ttf')
    FONT_FIXED_DEFAULT_NAME = os.path.join(CURRENT_PATH, 'assets', 'data', 'fixed.ttf')

BM_BACKGROUNDS_FOLDER = os.path.join(BITMAPS_FOLDER, 'backgrounds')
BM_LIVES_BASE_FOLDER = os.path.join(BITMAPS_FOLDER, 'lives')
BM_LOGOS_FOLDER = os.path.join(BITMAPS_FOLDER, 'logos')
BM_CLOCKS_FOLDER = os.path.join(BITMAPS_FOLDER, 'clocks')

INIT_OPTIONS_FOLDER = os.path.join(CURRENT_PATH, 'extra')
INIT_OPTIONS_FILE = os.path.join(INIT_OPTIONS_FOLDER, 'init_options.cfg')

MUSIC_BOX = (
    f'action_song__192b.{MUSIC_FORMAT}',
    )

FILE_NAMES = {
    'im_background': ('background', 'png'),
    'im_screen_help': ('screen_help', 'png'),
    'im_logo_japinol': ('logo_japinol_ld', 'png'),
    'im_help_key': ('help_key', 'png'),
    'bg_blue_t1_big_logo': ('bg_blue_t1_big_logo', 'png'),
    'im_bg_blue_t1': ('bg_blue_t1', 'png'),
    'im_bg_blue_t2': ('bg_blue_t2', 'png'),
    'im_bg_black_t1': ('bg_black_t1', 'png'),
    'im_board': ('board', 'png'),
    'im_piece': ('piece', 'png'),
    'life_heart': ('heart', 'png'),
    'im_clocks': ('clock', 'png'),
    'snd_apple_hit': ('move', SOUND_FORMAT),
    }

CELL_SPRITE_CELL_MAP = {
    '·': 0,
    'O': 1,
    'X': 2,
    }

CELL_SPRITE_POSITION_MAP = {
    7: (0, 0),
    8: (0, 1),
    9: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    1: (2, 0),
    2: (2, 1),
    3: (2, 2),
    }

