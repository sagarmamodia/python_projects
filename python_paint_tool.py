import pygame
from sys import exit

pygame.init()

#CONSTANTS--------------------------------------------------------------------------------------------------------
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BUTTON_DIMENSION = 20
BUTTON_DIMENSION_2 = (60, 20) 
PIXEL_WIDTH = 10
BORDER_WIDTH = 1
BRUSH_SIZE = 6

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = (155, 179, 192)
GREY = (80, 80, 80)
GREEN = (0, 225, 0)
RED = (250,128,114)

ERASE_BUTTON_POS = (40, 520)
COLOR_BUTTON_POS = (40, 560)
BLACK_BUTTON_POS = (80, 560)
RED_BUTTON_POS = (120, 560)
GREEN_BUTTON_POS = (160, 560)

MINUS_BUTTON_POS = (120, 520)
BRUSH_SIZE_TEXT_POS = (160, 520)
PLUS_BUTTON_POS = (200, 520)

#-----------------------------------------------------------------------------------------------------------------

#-VARIABLES-------------------------------------------------------------------------------------------------------
BRUSH_COLOR = BLACK
BORDER_COLOR = GREEN
#-----------------------------------------------------------------------------------------------------------------

#-BUTTONS---------------------------------------------------------------------------------------------------------
BUTTON_1 = 'ERASE'
BUTTON_2 = 'C-COLOR'
BUTTON_3 = 'C-BLACK'
BUTTON_4 = 'C-RED'
BUTTON_5 = 'C-GREEN'
BUTTON_6 = 'B--'
BUTTON_7 = 'B-+'
#-----------------------------------------------------------------------------------------------------------------

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Paint 1.0')
screen.fill(WHITE)
clock = pygame.time.Clock()

def pos_locator(x, y):
	col = int(x / PIXEL_WIDTH) 
	row = int(y / PIXEL_WIDTH)
	return (row, col)

def button_locator(x, y):
	if x > ERASE_BUTTON_POS[0] and x < ERASE_BUTTON_POS[0] + 80 and y > ERASE_BUTTON_POS[1] and y < ERASE_BUTTON_POS[1] + 20:
		return BUTTON_1
	if x > 40 and x < 60 and y > 560 and y < 580:
		return BUTTON_2
	if x > BLACK_BUTTON_POS[0] and x < BLACK_BUTTON_POS[0] + BUTTON_DIMENSION and y > BLACK_BUTTON_POS[1] and y < BLACK_BUTTON_POS[1] + BUTTON_DIMENSION:
		return BUTTON_3 
	if x > RED_BUTTON_POS[0] and x < RED_BUTTON_POS[0] + BUTTON_DIMENSION and y > RED_BUTTON_POS[1] and y < RED_BUTTON_POS[1] + BUTTON_DIMENSION:
		return BUTTON_4 
	if x > GREEN_BUTTON_POS[0] and x  < GREEN_BUTTON_POS[0] + BUTTON_DIMENSION and y > GREEN_BUTTON_POS[1] and y < GREEN_BUTTON_POS[1] + BUTTON_DIMENSION:
		return BUTTON_5 
	if x > MINUS_BUTTON_POS[0] and x < MINUS_BUTTON_POS[0] + BUTTON_DIMENSION and y > MINUS_BUTTON_POS[1] and y < MINUS_BUTTON_POS[1] + BUTTON_DIMENSION:
		return BUTTON_6
	if x > PLUS_BUTTON_POS[0] and x< PLUS_BUTTON_POS[0] + BUTTON_DIMENSION and y > PLUS_BUTTON_POS[1] and y < PLUS_BUTTON_POS[1] + BUTTON_DIMENSION:
		return BUTTON_7

def draw():
	mouse_pos = pygame.mouse.get_pos()
	if pygame.mouse.get_pressed()[0] and mouse_pos[1] < SCREEN_WIDTH:
		position = pos_locator(mouse_pos[0], mouse_pos[1])
		if BRUSH_SIZE == 1:
			pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * position[1], PIXEL_WIDTH * position[0], PIXEL_WIDTH, PIXEL_WIDTH))
		
		if BRUSH_SIZE == 2:	
			pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * position[1], PIXEL_WIDTH * position[0], PIXEL_WIDTH, PIXEL_WIDTH))
		
			for i in range(1, BRUSH_SIZE):
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] - i), PIXEL_WIDTH * position[0], PIXEL_WIDTH, PIXEL_WIDTH))
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] + i), PIXEL_WIDTH * position[0], PIXEL_WIDTH, PIXEL_WIDTH))
			
			for i in range(1, BRUSH_SIZE):
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * position[1], PIXEL_WIDTH * (position[0] - i), PIXEL_WIDTH, PIXEL_WIDTH))
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] - i), PIXEL_WIDTH * (position[0] - i), PIXEL_WIDTH, PIXEL_WIDTH))
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] + i), PIXEL_WIDTH * (position[0] - i), PIXEL_WIDTH, PIXEL_WIDTH))

			for i in range(1, BRUSH_SIZE):
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * position[1], PIXEL_WIDTH * (position[0] + i), PIXEL_WIDTH, PIXEL_WIDTH))
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] - i), PIXEL_WIDTH * (position[0] + i), PIXEL_WIDTH, PIXEL_WIDTH))
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] + i), PIXEL_WIDTH * (position[0] + i), PIXEL_WIDTH, PIXEL_WIDTH))

		if BRUSH_SIZE >= 3:	
			pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * position[1], PIXEL_WIDTH * position[0], PIXEL_WIDTH, PIXEL_WIDTH))
		
			for i in range(1, BRUSH_SIZE):
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] - i), PIXEL_WIDTH * position[0], PIXEL_WIDTH, PIXEL_WIDTH))
				pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] + i), PIXEL_WIDTH * position[0], PIXEL_WIDTH, PIXEL_WIDTH))
			
			for i in range(1, BRUSH_SIZE):
				for j in range(1, BRUSH_SIZE):
					pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * position[1], PIXEL_WIDTH * (position[0] - i), PIXEL_WIDTH, PIXEL_WIDTH))
					pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] - j), PIXEL_WIDTH * (position[0] - i), PIXEL_WIDTH, PIXEL_WIDTH))
					pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] + j), PIXEL_WIDTH * (position[0] - i), PIXEL_WIDTH, PIXEL_WIDTH))

			for i in range(1, BRUSH_SIZE):
				for j in range(1, BRUSH_SIZE):
					pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * position[1], PIXEL_WIDTH * (position[0] + i), PIXEL_WIDTH, PIXEL_WIDTH))
					pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] - j), PIXEL_WIDTH * (position[0] + i), PIXEL_WIDTH, PIXEL_WIDTH))
					pygame.draw.rect(screen, BRUSH_COLOR, pygame.Rect(PIXEL_WIDTH * (position[1] + j), PIXEL_WIDTH * (position[0] + i), PIXEL_WIDTH, PIXEL_WIDTH))

	
def hover(x, y):
	if x > 40 and x < 60 and y > 560 and y < 580:
		pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(COLOR_BUTTON_POS[0], COLOR_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION), BORDER_WIDTH)
	else:
		pygame.draw.rect(screen, COLOR, pygame.Rect(COLOR_BUTTON_POS[0], COLOR_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION))

	if x > BLACK_BUTTON_POS[0] and x < BLACK_BUTTON_POS[0] + BUTTON_DIMENSION and y > BLACK_BUTTON_POS[1] and y < BLACK_BUTTON_POS[1] + BUTTON_DIMENSION:
		pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(BLACK_BUTTON_POS[0], BLACK_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION), BORDER_WIDTH)
	else:
		pygame.draw.rect(screen, BLACK, pygame.Rect(BLACK_BUTTON_POS[0], BLACK_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION))

	if x > ERASE_BUTTON_POS[0] and x < ERASE_BUTTON_POS[0] + 80 and y > ERASE_BUTTON_POS[1] and y < ERASE_BUTTON_POS[1] + 20:
		pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(ERASE_BUTTON_POS[0], ERASE_BUTTON_POS[1], BUTTON_DIMENSION_2[0], BUTTON_DIMENSION_2[1]), BORDER_WIDTH)
	else:
		pygame.draw.rect(screen, GREY, pygame.Rect(ERASE_BUTTON_POS[0], ERASE_BUTTON_POS[1], BUTTON_DIMENSION_2[0], BUTTON_DIMENSION_2[1]))

	if x > RED_BUTTON_POS[0] and x < RED_BUTTON_POS[0] + BUTTON_DIMENSION and y > RED_BUTTON_POS[1] and y < RED_BUTTON_POS[1] + BUTTON_DIMENSION:
		pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(RED_BUTTON_POS[0], RED_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION), BORDER_WIDTH)
	else:
		pygame.draw.rect(screen, RED, pygame.Rect(RED_BUTTON_POS[0], RED_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION))

	if x > GREEN_BUTTON_POS[0] and x < GREEN_BUTTON_POS[0] + BUTTON_DIMENSION and y > GREEN_BUTTON_POS[1] and y < GREEN_BUTTON_POS[1] + BUTTON_DIMENSION:
		pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(GREEN_BUTTON_POS[0], GREEN_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION), BORDER_WIDTH)
	else:
		pygame.draw.rect(screen, GREEN, pygame.Rect(GREEN_BUTTON_POS[0], GREEN_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION))

	if x > MINUS_BUTTON_POS[0] and x < MINUS_BUTTON_POS[0] + BUTTON_DIMENSION and y > MINUS_BUTTON_POS[1] and y < MINUS_BUTTON_POS[1] + BUTTON_DIMENSION:
		pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(MINUS_BUTTON_POS[0], MINUS_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION), BORDER_WIDTH)
	else:
		pygame.draw.rect(screen, GREY, pygame.Rect(MINUS_BUTTON_POS[0], MINUS_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION))
	
	if x > PLUS_BUTTON_POS[0] and x < PLUS_BUTTON_POS[0] + BUTTON_DIMENSION and y > PLUS_BUTTON_POS[1] and y < PLUS_BUTTON_POS[1] + BUTTON_DIMENSION:
		pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(PLUS_BUTTON_POS[0], PLUS_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION), BORDER_WIDTH)
	else:
		pygame.draw.rect(screen, GREY, pygame.Rect(PLUS_BUTTON_POS[0], PLUS_BUTTON_POS[1], BUTTON_DIMENSION, BUTTON_DIMENSION))
	
def button_action(button_pressed):
	global BRUSH_COLOR, BRUSH_SIZE
	if button_pressed == BUTTON_1:
		BRUSH_COLOR = WHITE
	if button_pressed == BUTTON_2:
		BRUSH_COLOR = COLOR
	if button_pressed == BUTTON_3:
		BRUSH_COLOR = BLACK
	if button_pressed == BUTTON_4:
		BRUSH_COLOR = RED
	if button_pressed == BUTTON_5:
		BRUSH_COLOR = GREEN
	if button_pressed == BUTTON_6:
		if BRUSH_SIZE > 1: BRUSH_SIZE -= 1
	if button_pressed == BUTTON_7:
		if BRUSH_SIZE < 10: BRUSH_SIZE += 1


text_font = pygame.font.Font(None, 30)
erase_button_text = text_font.render('Erase', False, WHITE)
minus_button_text = text_font.render('-', False, WHITE)
plus_button_text = text_font.render('+', False, WHITE)


watermark_text = text_font.render('Developed by Sagar', True, RED)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	# for i in range(1, int(SCREEN_WIDTH / PIXEL_WIDTH)):
	# 	pygame.draw.line(screen, BLACK, (i * PIXEL_WIDTH, 0), (i * PIXEL_WIDTH, SCREEN_WIDTH))
	# for i in range(1, int(SCREEN_WIDTH / PIXEL_WIDTH)):
	# 	pygame.draw.line(screen, BLACK, (0, i * PIXEL_WIDTH), (SCREEN_WIDTH, i * PIXEL_WIDTH))
	# pygame.draw.line(screen, BLACK, (0, 400), (400, 400))

	draw()
	mouse_pos = pygame.mouse.get_pos()

	hover(mouse_pos[0], mouse_pos[1])
	screen.blit(erase_button_text, (ERASE_BUTTON_POS[0] + 3, ERASE_BUTTON_POS[1] + 1.5))
	screen.blit(minus_button_text, (MINUS_BUTTON_POS[0] + 6, MINUS_BUTTON_POS[1] + 0.8))

	brush_size_text = text_font.render(str(BRUSH_SIZE), False, BLACK)
	pygame.draw.rect(screen, WHITE, pygame.Rect(160, 520, BUTTON_DIMENSION, BUTTON_DIMENSION))
	pygame.draw.rect(screen, GREY, pygame.Rect(160, 520, BUTTON_DIMENSION, BUTTON_DIMENSION), 2)
	screen.blit(brush_size_text, (160 + 5, 520 + 1))

	screen.blit(plus_button_text, (PLUS_BUTTON_POS[0] + 4, PLUS_BUTTON_POS[1] - 1))

	screen.blit(watermark_text, (190, 410))

	if pygame.mouse.get_pressed()[0]:
		button_action(button_locator(mouse_pos[0], mouse_pos[1]))


	pygame.display.update()
	clock.tick(60)