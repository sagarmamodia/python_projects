import pygame as pg

class Solve:
    def __init__(self, board): #board is a collection of blocks
        self.board = board
    
    def solveSudoku(self, index):
        if index>80:
            return True
        row, col = self.indexToRowCol(index)
        block = self.board.board[row][col]
        if block.permanent == True:
            return self.solveSudoku(index+1)
        for i in range(1, 10):
            if self.check_in_row(i, row) and self.check_in_col(i, col) and self.check_in_section(i, block.section):
                block.put_data(i)
                solution = self.solveSudoku(index+1)
                if solution:
                    return True
                
        block.remove_data()
        return False

    def indexToRowCol(self, index):
        row = index//9
        col = index % 9
        return (row, col)

    def check_in_row(self, num, row): # row are numbers 0 to 8
        for block in self.board.board[row]:
            if block.data == num:
                return False
        return True
    
    def check_in_col(self, num, col): # col are numbered 0 to 8
        for i in range(9):
            if self.board.board[i][col].data == num:
                return False
        return True

    def check_in_section(self, num, sectionNumber): # sections are numbered 0 to 8
        section_rows = self.board.sections[sectionNumber][0]
        section_cols = self.board.sections[sectionNumber][1]
        for i in range(section_rows[0], section_rows[1]+1):
            for j in range(section_cols[0], section_cols[1]+1):
                if self.board.board[i][j].data == num:
                    return False
        return True
        

