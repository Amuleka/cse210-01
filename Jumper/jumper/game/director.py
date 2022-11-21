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
        self.jumper = Jumper()
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
        """Asks the user for a guess.

        Args:
            self (Director): An instance of Director.
        """
        letter_guessed = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")
        self._puzzle._check_guess(letter_guessed)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        if self._puzzle._check_guess is False:
            self.jumper.set_parachute()
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        if self._puzzle is True:
            self._terminal_service.write_text('That letter is correct ')
        else:
            self._terminal_service.write_text('Sorry, that letter is not part of this word')
        self._terminal_service.write_text(self.jumper.get_parachute())

        if self._puzzle._completed_word():
            self._terminal_service.write_text('You got it! ')
        self._terminal_service.write_text(self._puzzle._completed_word())
        self._is_playing = False
