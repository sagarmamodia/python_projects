import pygame as pg
from block import *

class Board:
    def __init__(self, game):
        self.game = game
        # [(rowStart, rowEnd), (colStart, colEnd)] all are inclusive
        # blocks are numbered from 0 to 8
        self.sections = [ [(0, 2), (0, 2)], [(0, 2), (3, 5)], [(0, 2), (6, 8)],
                        [(3, 5), (0, 2)], [(3, 5), (3, 5)], [(3, 5), (6, 8)],
                        [(6, 8), (0, 2)], [(6, 8), (3, 5)], [(6, 8), (6, 8)]] 
        
        self.board = [[Block(i, j, self.get_section(i, j), game) for j in range(9)] for i in range(9)]
        self.selected = None
        self.hovered_block = None
        self.iMTime = pg.time.get_ticks()
        self.fMTime = pg.time.get_ticks()
        self.iKTime = pg.time.get_ticks()
        self.fKTime = pg.time.get_ticks()


    def get_section(self, row, col):
        for i in range(len(self.sections)):
            if self.sections[i][0][0]<= row <= self.sections[i][0][1] and self.sections[i][1][0]<= col <= self.sections[i][1][1]:
                return i

    def draw_board(self):
        # draw section lines
        for i in [3, 6]:
            pos = BLOCK_DIM*i + BLOCK_MARGIN*i + BLOCK_MARGIN/2 - BLOCK_MARGIN/10
            pg.draw.line(self.game.WIN, LINE_COLOR, (pos, 0), (pos, WIN_HEIGHT), LINE_WIDTH)
            pg.draw.line(self.game.WIN, LINE_COLOR, (0, pos), (WIN_WIDTH, pos), LINE_WIDTH)
        


        for i in range(9):
            for j in range(9):
                self.board[i][j].draw()
    
    def mouse_select(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_state = pg.mouse.get_pressed()
        left_click = mouse_state[0]
        x = mouse_pos[0]
        y = mouse_pos[1]
        row = int(y//SQUARE_DIM)
        col = int(x//SQUARE_DIM)


        self.fMTime = pg.time.get_ticks()
        delta_time = self.fMTime - self.iMTime

        block = self.board[row][col]

        if left_click and block != None and delta_time > DTIME:
            if not block.selected and self.selected: # if block is already selected
                self.selected.deselect()
                self.hovered_block = None
                block.dehover()
                block.select()
                self.selected = block
                self.iMTime = pg.time.get_ticks()
            elif block.selected:
                block.deselect()
                self.selected = None
                self.iMTime = pg.time.get_ticks()
            elif self.selected == None:
                block.select()
                self.selected = block
                self.iMTime = pg.time.get_ticks()

    def mouse_hover(self):
        mouse_pos = pg.mouse.get_pos()
        x = mouse_pos[0]
        y = mouse_pos[1]
        row = int(y//SQUARE_DIM)
        col = int(x//SQUARE_DIM)
        block = self.board[row][col]

        # Remove hoverness from previous block
        if block and self.hovered_block and block != self.hovered_block:
            self.hovered_block.dehover()
            self.hovered_block = None

        # Hover on the new block which must not be selected
        if block and not block.selected :
            block.hover()
            self.hovered_block = block

    def keyboard_input(self):
        keys = pg.key.get_pressed()

        self.fKTime = pg.time.get_ticks()
        delta_time = self.fKTime = self.iKTime

        if delta_time > DTIME and self.selected:
            if keys[pg.K_1]:
                if self.game.solver.check_in_row(1, self.selected.row) and self.game.solver.check_in_col(1, self.selected.col) and self.game.solver.check_in_section(1, self.selected.section):
                    self.selected.set_data(1)
                    self.iKTime = pg.time.get_ticks()
            elif keys[pg.K_2]:
                if self.game.solver.check_in_row(2, self.selected.row) and self.game.solver.check_in_col(2, self.selected.col) and self.game.solver.check_in_section(2, self.selected.section):
                    self.selected.set_data(2)
                    self.iKTime = pg.time.get_ticks()
            elif keys[pg.K_3]:
                if self.game.solver.check_in_row(3, self.selected.row) and self.game.solver.check_in_col(3, self.selected.col) and self.game.solver.check_in_section(3, self.selected.section):
                    self.selected.set_data(3)
                    self.iKTime = pg.time.get_ticks()
            elif keys[pg.K_4]:
                if self.game.solver.check_in_row(4, self.selected.row) and self.game.solver.check_in_col(4, self.selected.col) and self.game.solver.check_in_section(4, self.selected.section):
                    self.selected.set_data(4)
                    self.iKTime = pg.time.get_ticks()
            elif keys[pg.K_5]:
                if self.game.solver.check_in_row(5, self.selected.row) and self.game.solver.check_in_col(5, self.selected.col) and self.game.solver.check_in_section(5, self.selected.section):
                    self.selected.set_data(5)
                    self.iKTime = pg.time.get_ticks()
            elif keys[pg.K_6]:
                if self.game.solver.check_in_row(6, self.selected.row) and self.game.solver.check_in_col(6, self.selected.col) and self.game.solver.check_in_section(6, self.selected.section):
                    self.selected.set_data(6)
                    self.iKTime = pg.time.get_ticks()
            elif keys[pg.K_7]:
                if self.game.solver.check_in_row(7, self.selected.row) and self.game.solver.check_in_col(7, self.selected.col) and self.game.solver.check_in_section(7, self.selected.section):
                    self.selected.set_data(7)
                    self.iKTime = pg.time.get_ticks()
            elif keys[pg.K_8]:
                if self.game.solver.check_in_row(8, self.selected.row) and self.game.solver.check_in_col(8, self.selected.col) and self.game.solver.check_in_section(8, self.selected.section):
                    self.selected.set_data(8)
                    self.iKTime = pg.time.get_ticks()
            elif keys[pg.K_9]:
                if self.game.solver.check_in_row(9, self.selected.row) and self.game.solver.check_in_col(9, self.selected.col) and self.game.solver.check_in_section(9, self.selected.section):
                    self.selected.set_data(9)
                    self.iKTime = pg.time.get_ticks()
            elif keys[pg.K_SPACE] and delta_time>DTIME:
                self.boardSolve()
                self.iKTime = pg.time.get_ticks()
    
    def boardSolve(self):
        if not self.game.solved:
            print(self.game.solver.solveSudoku(0))
        self.game.solved = True

    def update(self):
        self.draw_board()
        self.mouse_hover()
        self.mouse_select()
        self.keyboard_input()