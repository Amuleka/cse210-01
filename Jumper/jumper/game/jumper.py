from game.terminal_service import TerminalService

class Jumper:
    '''Creates and returns the main character
    '''
    def __init__(self):
        self._terminal_service = TerminalService()
        self._parachute = [ " ___",
                          "/___\\",
                            "\   /",
                            " \ /",
                             "  O",
                             " /|\\",
                             " / \\",
                             "",
                            "^^^^^"]

    def draw_jumper(self):
        for line in self._parachute:
            self._terminal_service.write_text(line)
            

    def remove_parachute_piece(self):
        self._parachute.pop(0)
        
    def has_parachute(self):
        return len(self._parachute) >= 6

    def parachute_gone(self):
        self._parachute[0].replace('O', 'x')
        
        

