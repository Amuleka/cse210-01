import random

from game.terminal_service import TerminalService

class Puzzle:

    def __init__(self):
        self._terminal_service = TerminalService()
        self._words = ['mexico', 'usa', 'brazil', 'argentina', 'france', 'italy', 'germany', 'sweden']
        self._word_selected = random.choice(self._words)
        self._word_guess = ['_'] * len(self._word_selected)
        

    def draw_word_guess(self):
        for letter in self._word_guess:
            self._terminal_service.write_text(letter)

    def process_guess(self, guess_letter):
        correct_guess = False
        #Loop through _word_selected by index
        for i in range(0,len(self._word_selected)):
        #Check if guess_letter = _word_select[index]
            if guess_letter == self._word_selected[i]:
        #Set _word_guess[index] = guess_letter
                self._word_guess[i] = guess_letter

        return correct_guess

    def can_keep_guessing(self):
        return "_" in self._word_guess






