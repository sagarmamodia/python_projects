import pygame as pg
import random
from sys import exit  
from settings import *
from board import *
from solve import *

class Game:
    def __init__(self):
        pg.init()
        self.WIN = pg.display.set_mode(WIN_DIM)
        self.board = Board(self)
        self.font = pg.font.SysFont('opensans', 34, True)
        self.solver = Solve(self.board)
        self.solved = False
        
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()


    def run(self):
        while True:
            self.WIN.fill(BG_COLOR)
            self.check_events()
            self.board.update()
            pg.display.update()

game = Game()
game.run()
