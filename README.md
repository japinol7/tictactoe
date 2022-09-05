## Tic Tac Toe
    This version of the game is intended to be played in these three variations:
       > Two players using the same keyboard.
       > One player against the computer.
       > Two players controlled by the computer playing against each other.
    Note that: 
       > A player controlled by the computer will never lose.
       > If both players are controlled by the computer, the games will always end in a draw.


   * The program 

	program: Tic Tac Toe.
    name as a package: tictactoe 
	version: 0.0.1
	author: Joan A. Pinol
	author_nickname: japinol
	author_gitHub: japinol7
	author_twitter: @japinol
	requirements: pygame
	Python requires: 3.9 or greater.
	Python versions tested: 
        > 3.9.12 64bits under Windows 11


## Rules and user guide

	> Each app execution is considered a campaign, which consists in N tournaments.
    > The player who wins more tournaments wins the campaign. 
	    > A tournament consists of X games (2 by default)
    > Only the tournaments score count in the end.
    > Players always have the same tokens.
    > The two players alternate turns on a game.
    > Which player starts a game:
	    > Player 1 has the first turn on the first game.
	    > For next games, the two players alternate the first turns.
	    > So, to be fair, each tournament should consist in an even number of games.
    > To win this Tic Tac Toe game:
	    > You must have more tournament victories than the other player.


## Computer Controlled Players. Additional info

Computer Controlled Players use a simple version of the Minimax decision rule algorithm.

* You can find good info about Minimax here:
  [Wikipedia Minimax search](https://en.wikipedia.org/wiki/Minimax)


## Keyboard keys
       F1:    Show a help screen while playing the game
       1-9:   set a token to the board at the corresponding position:
                7 | 8 | 9
                4 | 5 | 6
                1 | 2 | 3
       ESC: exit game
       ^m:    pause/resume music
       ^s:    sound effects on/off
       L_Alt + R_Alt + Enter: change full screen / windowed screen mode
       ^h:    shows this help to the console

    > Additional keys for debug mode:
       ^d:    print debug information to the console and the log file


## Screenshots

<img src="screenshots/screenshot1.png"> <br />
<img src="screenshots/screenshot2.png"> <br />
<img src="screenshots/screenshot3.png"> <br />


## Usage

	tictactoe  usage: tictactoe [-h] [-a] [-g GAMESTOPLAY] [-u TOURNAMENTS] 
                                [-l] [-o] [-p] [-s TURNMAXSECS] [-w] [-d] [-t]
	
	optional arguments:
	  -h, --help            show this help message and exit.
	  -a, 			--auto
	                        Auto mode. It does not stop between games or tournaments.
	                        Only when it needs a user input
	  -g, 			--gamestoplay GAMESTOPLAY
	                        Games to play on each tournament. Must be between 2 and 5000.
	  -u, 			--tournaments TOURNAMENTS
	                        Tournaments to play.  Must be between 1 and 30.
	  -l, 			--multiplelogfiles
	                        A log file by app execution, instead of one unique log file.
	  -o, 			--player1ai
	                        Player 1 will be controlled by the computer.
	  -p, 			--player2ai
	                        Player 2 will be controlled by the computer.
	  -s, 			--turnmaxsecs TURNMAXSECS
	                        Turn max seconds before the player who holds the turn 
	                        loses the current game. Must be between 5 and 900.
	  -w, 			--wargametraining
	                        War game training speculating on playing Tic Tac Toc. It activates the following flags: 
	                        player1ai, player2ai, auto, tournaments 1, gamestoplay 500.
	  -d, 			--debug
	                        Debug actions when pressing the right key, information and traces.
	  -t, 			--debugtraces
	                        show debug back traces information when something goes wrong.


**Default optional arguments**

	auto                False
	gamestoplay         2
	tournaments         10
	player1ai           False
	player2ai           False
	turnmaxsecs         15
	multiplelogfiles    False
    debug               False
	debugtraces         False


**Examples of usage**

    > Modality two players using the same keyboard:
       $ python -m tictactoe
    > One player against the computer.
       $ python -m tictactoe --player2ai --tournaments 4
    > Two players controlled by the computer playing against each other without waiting between games.
       $ python -m tictactoe --player1ai --player2ai --auto


**To make Tic Tac Toe work**

	Do this:
	    1. Clone this repository in your local system.
	    2. Go to its folder in your system.
	    3. $ pip install -r requirements.txt
	    4. $ python -m tictactoe