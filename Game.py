
class Game:
    EMPTY = " "
    DIM = 3
    P1 = "o"
    P2 = "x"
    
    def __init__(self):
        self._board = [[Game.EMPTY for _ in range(Game.DIM)] for _ in range(Game.DIM)]
        self._player = Game.P1

    def __repr__(self):
        return ''

    def play(self,row,col):
        row -= 1
        col -=1
        self._board[row][col] = self._player
        self._player = Game.P2 if self._player == Game.P1 else self._player = Game.P1
    
    @property
    def winner(self):
        pass

if __name__ == "__main__":
    pass
