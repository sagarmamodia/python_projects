import pygame as pg
from settings import *

class Block:
    def __init__(self, row, col, section, game):
        self.data = 0
        self.col = col
        self.row = row
        self.section = section
        self.game = game
        self.color = DEFAULT_COLOR
        self.selected = False
        self.hovered = False
        self.border = False
        self.permanent = False
        
    def draw(self):
        x_pos = BLOCK_DIM * self.col + BLOCK_MARGIN *(self.col+1)
        y_pos = BLOCK_DIM * self.row + BLOCK_MARGIN * (self.row+1)
        block_rect = pg.Rect(x_pos, y_pos, BLOCK_DIM, BLOCK_DIM)
        if self.border == False:
            pg.draw.rect(self.game.WIN, self.color, block_rect)
        else:
            pg.draw.rect(self.game.WIN, self.color, block_rect)
            x_pos = BLOCK_DIM * self.col + BLOCK_MARGIN *(self.col+1-1)
            y_pos = BLOCK_DIM * self.row + BLOCK_MARGIN * (self.row+1-1)
            NEW_DIM = BLOCK_DIM + 2*BLOCK_MARGIN
            pg.draw.rect(self.game.WIN, BORDER_COLOR, pg.Rect(x_pos, y_pos, NEW_DIM, NEW_DIM), BLOCK_MARGIN)
        
        if self.data != 0:
            self.draw_data(block_rect.center)
    
    def draw_data(self, center):
        if self.permanent:
            text_color = BLUE
        else:
            text_color = BLOCK_TEXT_COLOR
        text_img = self.game.font.render(str(self.data), True, text_color)
        text_rect = text_img.get_rect(center = center)
        self.game.WIN.blit(text_img, text_rect)
    
    def set_data(self, data):
        self.data = data
        if data != 0:
            self.permanent = True
        elif data==0:
            self.permanent = False

    def remove_data(self):
        self.data = 0
        self.permanent = False

    def put_data(self, data):
        self.data = data
        self.permanent = False

    def select(self):
        self.selected = True
        self.color = SELECT_COLOR
        self.border = True
    
    def deselect(self):
        self.selected = False
        self.color = DEFAULT_COLOR
        self.border = False
    
    def hover(self):
        self.hovered = True
        self.color = HOVER_COLOR
    
    def dehover(self):
        self.hovered = False
        self.color = DEFAULT_COLOR