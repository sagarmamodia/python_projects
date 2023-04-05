import pygame as pg
from pygame.math import Vector2 as vec2
from settings import *
from random import randrange

class Snake():
    def __init__(self, game):
        self.game = game
        self.rect = pg.Rect(0, 0, TILE_SIZE, TILE_SIZE)
        self.rect.center = self.get_random_pos()
        self.direction = vec2(TILE_SIZE, 0)
        self.length = 1
        self.segments = []
        self.time = 0
        self.delay_step = 150 #milliseconds
        self.food = Food(self)
        self.directions = {'up': 1, 'down': 1, 'right': 1, 'left': 0}

    def get_random_pos(self):
        return randrange(TILE_SIZE//2, SCREEN_WIDTH, TILE_SIZE), randrange(TILE_SIZE//2, SCREEN_HEIGHT, TILE_SIZE)

    def check_food(self):
        self.food.update()
        if self.food.rect.center == self.rect.center:
            self.length += 1
            self.food = Food(self)

    def control(self, event):
        if event.key == pg.K_w and self.directions['up']:
            self.direction = vec2(0, -TILE_SIZE)
            self.directions = {'up': 1, 'down': 0, 'right': 1, 'left': 1}
        elif event.key == pg.K_s and self.directions['down']:
            self.direction = vec2(0, TILE_SIZE)
            self.directions = {'up': 0, 'down': 1, 'right': 1, 'left': 1}
        elif event.key == pg.K_d and self.directions['right']:
            self.direction = vec2(TILE_SIZE, 0)
            self.directions = {'up': 1, 'down': 1, 'right': 1, 'left': 0}
        elif event.key == pg.K_a:
            self.direction = vec2(-TILE_SIZE, 0)
            self.directions = {'up': 1, 'down': 1, 'right': 0, 'left': 1}

    def delta_time(self):
        current_time = pg.time.get_ticks()
        delta_time = current_time - self.time
        if delta_time > self.delay_step:
            self.time = current_time
            return True
        return False

    def check_self_eating(self):
        if len(set([segment.center for segment in self.segments])) != len(self.segments):
            self.game.new_game()

    def check_borders(self):
        if self.rect.center[0] < 0 or self.rect.center[0] > SCREEN_WIDTH or self.rect.center[1] < 0 or self.rect.center[1] > SCREEN_HEIGHT:
            self.game.new_game()

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
    
    def draw(self):
        for segment in self.segments:
            pg.draw.rect(self.game.display, GREEN, segment)
        self.segments = self.segments[-self.length:]

    def update(self):
        self.check_food()
        self.check_borders()
        self.check_self_eating()
        self.move()
        self.draw()

class Food:
    def __init__(self, snake):
        self.snake = snake
        self.rect = pg.Rect(0, 0, TILE_SIZE, TILE_SIZE )
        self.rect.center = (self.snake.get_random_pos()[0], self.snake.get_random_pos()[1])

    def draw(self):
        pg.draw.rect(self.snake.game.display, RED, self.rect)
    
    def update(self):
        self.draw()