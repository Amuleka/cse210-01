import random

class Puzzle:

    def __init__(self):
        _words = ['car', 'truck', 'van', 'bike', 'scooter']
        self._word = random.choice(_words)

    def _create_word(self):
        #picks the word for the game ['cart','tank','bowl','door','cake','part']
        self._words = ['cart', 'cart', 'cart',]

    def _check_guess(self, guess):
        # adds letters to a list if correct
        self._correct_letters = []
        for x in self._word:
            if guess == x:
                self._correct_letters.append(x)

        if guess in self._correct_letters:
            return True
        else:
            return False

    def _completed_word(self):
        #checks to see if user has completed the word

        self._correct_letters = []
        _correct_word = []

        #convert word into list
        for x in self._word:
            _correct_word.append(x)
        
        #sort lists so we can check
        _checker = self._correct_letters.sort()
        _correct_check = _correct_word.sort()

        #checks the word
        if _checker != _correct_check:
            return False
        elif _checker == _correct_check:
            return self._word
