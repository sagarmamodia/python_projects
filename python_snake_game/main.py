import pygame as pg
from sys import exit
from pygame.math import Vector2 as vec2
from settings import *
from snake import *

class Game:
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.snake = Snake(self)

    def draw_grid(self):
        [pg.draw.line(self.display, GREY, (0, i), (SCREEN_WIDTH, i)) for i in range(0, SCREEN_WIDTH, TILE_SIZE)] 
        [pg.draw.line(self.display, GREY, (i, 0), (i, SCREEN_HEIGHT)) for i in range(0, SCREEN_HEIGHT, TILE_SIZE)]
    
    def run(self):  
        while True:
            self.display.fill(BLACK)
            self.update()
            pg.display.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                self.snake.control(event)
    
    def new_game(self):
        self.snake = Snake(self)

    def update(self):
        self.check_events()
        self.snake.update()
        self.draw_grid()


if __name__ == '__main__':

    game = Game()
    game.run()



