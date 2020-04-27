from itertools import product
class GameError(Exception):
    pass

class Game:
    EMPTY = " "
    DIM = 3
    P1 = "o"
    P2 = "x"
    
    def __init__(self):
        self._board = [[Game.EMPTY for _ in range(Game.DIM)] for _ in range(Game.DIM)]
        self._player = Game.P1

    def __repr__(self):
        output = '''  '''
        output += ''.join([str(j+1)+' ' for j in range(Game.DIM)]) + '\n'
        for i in range(Game.DIM):
            output += str(i+1) + ' ' + '|'.join([self._board[i][j] for j in range(Game.DIM)]) + '\n'
        return output



    def play(self,row,col):
        if not (0<row<=Game.DIM):
            raise GameError(f'Row {row} out of range')
        if not(0<col<=Game.DIM):
            raise GameError(f'Column{col} out of range')
        
        row -= 1
        col -=1
        
        if self._board[row][col]!= Game.EMPTY:
            raise GameError(f'Board not empty in {row},{col}')
        
        self._board[row][col] = self._player
        if self._player == Game.P1: self._player = Game.P2
        else: self._player = Game.P1
    
    @property
    def winner(self):
        for p in [Game.P1,Game.P2]:
            for row in range(Game.DIM):
                if all(self._board[row][col] is p for col in range(Game.DIM)):
                    return p
            for col in range(Game.DIM):
                if all(self._board[row][col] is p for row in range(Game.DIM)):
                    return p
            #Diagonals
            if all(self._board[i][i] is p for i in range(Game.DIM)):
                return p
            if all(self._board[i][2-i] is p for i in range(Game.DIM)):
                return p
        #No winner
        return None
    
    
    
    @property
    def drawer(self):
        if all(self._board[row][col] is not Game.EMPTY for (row,col) in product(range(Game.DIM),range(Game.DIM))):
            return True
        return None
    
    def at(self,row,col):
        row-=1
        col-=1
        return self._board[row][col]
if __name__ == "__main__":
    game = Game()
    print(game)