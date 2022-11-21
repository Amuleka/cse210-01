
class Jumper:
    '''Creates and returns the main character
    '''
    def __init__(self):
        self._parachute = ['''
                         __
                        |  |
                        \  /
                        \ /
                         O
                        /|\|
                        / \|
                        ''', 
                        '''
                        |  |
                        \  /
                        \ /
                         O
                        /|\|
                        / \|
                        ''', 
                        '''
                        \  /
                        \ /
                         O
                        /|\|
                        / \|
                        ''',
                        '''
                        \ /
                         O
                        /|\|
                        / \|
                        ''',
                        '''
                         X
                        /|\|
                        / \|
                        '''
        ]

    def set_parachute(self):
        self._parachute.pop(0)
        
    def get_parachute(self):
        return self._parachute[0]

