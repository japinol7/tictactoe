from tictactoe.config.constants import (
    GAMES_TO_PLAY_MAX, TOURNAMENTS_MAX,
    TURN_MAX_TIME_SECS_MIN, TURN_MAX_TIME_SECS_MAX,
    LOG_INPUT_ERROR_PREFIX_MSG,
    )


class InputValidator:

    def __init__(self, tournaments, games_to_play, turn_max_secs):
        self.tournaments = tournaments
        self.games_to_play = games_to_play
        self.turn_max_secs = turn_max_secs
        self.input_errors = []

    def validate_input(self):
        self.validate_tournaments()
        self.validate_games_to_play()
        self.validate_turn_max_secs()
        return self.input_errors

    def validate_tournaments(self):
        if self.tournaments is None:
            return
        if not (1 <= self.tournaments <= TOURNAMENTS_MAX):
            self.input_errors += [
                    f"{LOG_INPUT_ERROR_PREFIX_MSG}"
                    f"Tournaments to play must be between 1 and {TOURNAMENTS_MAX}."]

    def validate_games_to_play(self):
        if self.games_to_play is None:
            return
        if not (2 <= self.games_to_play <= GAMES_TO_PLAY_MAX):
            self.input_errors += [
                    f"{LOG_INPUT_ERROR_PREFIX_MSG}"
                    f"Games to play on each tournament must be between 2 and {GAMES_TO_PLAY_MAX}"]

    def validate_turn_max_secs(self):
        if self.turn_max_secs is None:
            return
        if not (TURN_MAX_TIME_SECS_MIN <= self.turn_max_secs <= TURN_MAX_TIME_SECS_MAX):
            self.input_errors += [
                    f"{LOG_INPUT_ERROR_PREFIX_MSG}"
                    f"Turn max seconds for game must be between {TURN_MAX_TIME_SECS_MIN} and {TURN_MAX_TIME_SECS_MAX}."]
