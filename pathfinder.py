import pygame as pg
from sys import exit
from pygame.math import Vector2 as vec2
import queue

SCREEN_SIZE = 600
SPOT_SIZE = 50

PURPLE = (128,0,128)
GREEN = (50,205,50)
RED = (220,20,60)
GREY = (50, 50, 50)
YELLOW = (255,255,0)
BLUE = (0,191,255)
WHITE = (255, 255, 255)
BLACK = (5, 5, 5)


pg.init()
display = pg.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

class Spot:
	def __init__(self, pos): #pos is a tuple of row and col
		self.type = 'empty' #other types are wall, start, end, path, search
		self.color = WHITE
		self.pos = vec2(pos)
		self.rect = pg.Rect(pos[1]*SPOT_SIZE, pos[0]*SPOT_SIZE, SPOT_SIZE, SPOT_SIZE)

	def make_wall(self):
		self.type = 'wall'
		self.color = BLACK
		walls.append(self.pos)

	def make_start(self):
		self.type = 'start'
		self.color = BLUE

	def make_end(self):
		self.type = 'end'
		self.color = YELLOW
	
	def make_empty(self):
		self.type = 'empty'
		self.color = WHITE
		walls.remove(self.pos)
	
	def make_path(self):
		self.type = 'path'
		self.color = PURPLE
	
	def make_horizon(self):
		self.type = 'horizon'
		self.color = GREEN

	def draw(self):
		pg.draw.rect(display, self.color, self.rect)

grid = []
walls = []
start = None
end = None

def draw_grid_lines():
	for i in range(0, SCREEN_SIZE, SPOT_SIZE):
		pg.draw.line(display, GREY, (0, i), (SCREEN_SIZE, i)) #horizontal lines
		pg.draw.line(display, GREY, (i, 0), (i, SCREEN_SIZE)) #vertical lines

def set_spot(type, pos):
	global start, end
	row = pos[0]
	col = pos[1]
	if type == 'wall' and start and end:
		if grid[row][col].type != 'start' and grid[row][col].type != 'end':
			grid[row][col].make_wall()
	elif type == 'start':
		grid[row][col].make_start()
		start = grid[row][col]
	elif type == 'end' and start:
		if grid[row][col].type != 'start':
			grid[row][col].make_end()
			end = grid[row][col]
	elif type == 'empty':
		if grid[row][col].type == 'start':
			start = None
			grid[row][col].make_empty()
		elif grid[row][col].type == 'end':
			end = None
			grid[row][col].make_empty()
		else:
			grid[row][col].make_empty()

def mouse_action():
	mouse_pos = pg.mouse.get_pos()
	if pg.mouse.get_pressed()[0]:
		row = mouse_pos[1]//SPOT_SIZE
		col = mouse_pos[0]//SPOT_SIZE
		if not start:
			set_spot('start', (row, col))
		elif not end:
			set_spot('end', (row, col))
		else:
			set_spot('wall', (row, col))
	elif pg.mouse.get_pressed()[2]:
		row = mouse_pos[1]//SPOT_SIZE
		col = mouse_pos[0]//SPOT_SIZE
		set_spot('empty', (row, col))

def make_grid():
	for i in range(0, SCREEN_SIZE, SPOT_SIZE):
		grid.append([])
		for j in range(0, SCREEN_SIZE, SPOT_SIZE):
			row = i//SPOT_SIZE
			col = j//SPOT_SIZE
			grid[row].append(Spot((row, col)))

def draw_spots():
	for row in grid:
		for spot in row:
			spot.draw()

def valid_dir(direc, current_pos):
	new_pos = current_pos-direc
	if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < SCREEN_SIZE/SPOT_SIZE and new_pos[1] < SCREEN_SIZE/SPOT_SIZE and new_pos not in walls:
		return new_pos
	else:
		return False

#--------------------------------------------------------------
started = False
make_grid()

directions = [((-1, 0), 'L'), ((1, 0), 'R'), ((0, -1), 'U'), ((0, 1), 'D')]
search_queue = queue.Queue()
#--------------------------------------------------------------

def BSF():

	visited_squares = [vec2(start.pos)]
	search_queue.put([vec2(start.pos)])
	paths = []
	while started:
		path = search_queue.get()
		#The bug that had been a pain in the butt for so long has been fixed now. It was very small but hard to spot unless you manually
		#check the output one by one along with running theoretical tests only then will you notice the bug. The bug was that this BSF 
		#used to get stuck in an infinite loop.
		
		#The bug had to do with the way I was implementing the algorithm. I was getting a path([pos1, pos2, ...]) from queue then I was 
		#passing the last pos in it as current pos then from there I was getting nextpos which I was appending in it. 

		#Now the problem with this approach was that I was appending the left, right, up and down next positions in the same path. So the new
		#path which I was putting in the queue was path(pos1, ..., poslast, poslast+L, poslast+R, poslast+U, poslast+D). Now the problem
		#was that I was fetching current pos by the last element of path which essentially means I was only getting the poslast+D and rest of 
		#the three position were getting lost. 


		for direc in directions:
			next_pos = valid_dir(vec2(direc[0]), path[-1:][0]) 
			if next_pos and next_pos not in visited_squares:
				new_path = path + [next_pos]
				visited_squares.append(next_pos)
				search_queue.put(new_path)
				paths.append(path)
			if next_pos == vec2(end.pos):
				return path[1:]
			

def draw_path(path):
	for spot_pos in path:
		row = int(spot_pos[0])
		col = int(spot_pos[1])
		grid[row][col].make_path()


while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_SPACE:
				if start and end:
					started = True
					path = BSF()
					started = False
					draw_path(path)

	display.fill(WHITE)
	mouse_action()
	draw_spots()
	# if start:
	# 	print(start.row, start.col)
	draw_grid_lines()
	pg.display.update()