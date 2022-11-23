from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        print(self._puzzle._word_selected)
        self._puzzle.draw_word_guess()
        self._jumper.draw_jumper()
        self._letter_guessed = self._terminal_service.read_guess("\nEnter a letter: [a-z] ").lower()
        self._puzzle.process_guess(self._letter_guessed)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        if self._letter_guessed in self._puzzle._word_selected:
            self._jumper.draw_jumper()
        else:
            self._jumper.remove_parachute_piece()

        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        if self._puzzle.can_keep_guessing() == False:
            print('Congrats, You won')
            self._is_playing = False
        elif self._jumper.has_parachute() == False:
            self._jumper.parachute_gone()
            self._is_playing = False
            
            
        # self._jumper.parachute_gone()
        #     # self._is_playing = False
            
            
