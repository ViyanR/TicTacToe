from abc import ABC, abstractmethod
from Game import Game, GameError
from tkinter import Button, Tk, Toplevel, Frame, N,S,E,W,X,Y, LEFT,RIGHT, END, Scrollbar, Text, Message, Grid, StringVar
from ttkthemes import themed_tk as tk
from Game import Game, GameError
from sys import stderr
from itertools import product
from abc import ABC, abstractmethod

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = tk.ThemedTk()
        root.set_theme(theme_name='itft1')
        root.title('Tic Tac Toe')
        self._game_win = None
        frame = Frame(root)
        frame.pack(fill=X)
        Button(
            frame,
            text='Show Help',
            command=self.help_callback
        ).pack(fill=X)#Fill means expands in x-direction when window is resized

        Button(
            frame,
            text='Play Game',
            command=self.play_callback
        ).pack(fill=X)

        Button(
            frame,
            text='Quit',
            command=root.quit
        ).pack(fill=X)
        
        console = Text(frame,height=4,width=50)
        scroll= Scrollbar(frame)
        scroll.pack(side=RIGHT,fill=Y)
        console.pack(side=LEFT,fill=Y)
        
        #Use grid method rather than pack for more complexity
        
        scroll.config(command=console.yview)
        console.config(yscrollcommand=scroll.set)
        
        self._console = console
        self._root = root
      
    def help_callback(self):
        pass
    
    def _game_close(self):
        self._game_win.destroy()
        self._game_win = None
    
    def play_callback(self):
        if self._game_win:
            return
        
        self._game = Game()
        self._finished = False
        game_win = Toplevel(self._root)
        self._game_win = game_win
        
        game_win.title('Game')
        Grid.rowconfigure(game_win, 0, weight=1)
        Grid.columnconfigure(game_win, 0, weight=1)
        frame = Frame(game_win)
        frame.grid(row=0,column=0,sticky=N+S+E+W)
        
        self._buttons = [[None for _ in range(Game.DIM)] for _ in range(Game.DIM)]
        
        for row,col in product(range(Game.DIM),range(Game.DIM)):
            b = StringVar()
            b.set(self._game.at(row+1,col+1))
            
            cmd = lambda r=row,c=col : self.play_and_refresh(r,c)
            
            Button(
                frame,
                textvariable = b,
                command = cmd
            ).grid(row=row,column=col,sticky=N+S+E+W)
            
            self._buttons[row][col] = b
        
            for i in range(Game.DIM):
                Grid.rowconfigure(frame,i,weight=1)
                Grid.columnconfigure(frame, i, weight=1)
        Button(game_win,text='Dismiss',command=self._game.close).grid(row=1,column=0)
    
    def play_and_refresh(self,row,col):
        try:
            self._game.play(row+1,col+1)
        except GameError as ge:
            self._console.insert(END,f'{ge}\n')
            print(ge,file=stderr)

        text = self._game.at(row + 1, col + 1)
        self._buttons[row][col].set(text)
        #For a more complex game:
        '''
        for r,c in product(range(Game.DIM),range(Game.DIM)):
            text = self._game.at(r+1,c+1)
            self._buttons[r][c].set(text)
        '''
        w = self._game.winner
        if w is not None:
            self._console.insert(END, f'The winner was {w}\n')
        d = self._game.drawer
        if d is not None:
            self._console.insert(END, 'The game was a draw\n')
    
    def run(self):
        self._root.mainloop()

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while not (self._game.winner or self._game.drawer):
            print(self._game)
            try:
                row = int(input("Which row? "))
                col = int(input("Which column? "))
            except ValueError:
                print('Row and column need to be numbers')
                continue
            try:
                self._game.play(row,col)
            except GameError as g:
                print(f'Game error: {g}')
        print(self._game)
        if self._game.winner is not None:
            print(f'The winner was: {self._game.winner}')
        elif self._game.drawer is not None:
            print(f'The game was a draw')

if __name__=='__main__':
    ui = Terminal()
    ui.run()