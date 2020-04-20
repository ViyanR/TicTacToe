
class Game:
    EMPTY = " "
    DIM = 3
    P1 = "o"
    P2 = "x"
    
    def __init__(self):
        self._board = [[Game.EMPTY for _ in range(Game.DIM)] for _ in range(Game.DIM)]
        self._player = Game.P1

    def __repr__(self):
        #output = '''  '''
        #output.join([str(j)+ '' for j in range(1,Game.DIM+1)])
        #for i in range(Game.DIM):
        #    output.join(str(i)+' ')
          
        return f'''  1 2 3
1 {self._board[0][0]}|{self._board[0][1]}|{self._board[0][2]}
  _____
2 {self._board[1][0]}|{self._board[1][1]}|{self._board[1][2]}
  _____
3 {self._board[2][0]}|{self._board[2][1]}|{self._board[2][2]}
'''


        
        

    def play(self,row,col):
        row -= 1
        col -=1
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

if __name__ == "__main__":
    game = Game()
    print(game)
