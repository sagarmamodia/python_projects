import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Tic Tac Toe')

clock = pygame.time.Clock()

def position_locator():
	x = mouse_pos[0]
	y = mouse_pos[1]
	row = 0
	col = 0
	if x > 50 and x < 150:
		col = 1
	if x > 150 and x < 250:
		col = 2
	if x > 250 and x < 350:
		col = 3
	
	if y > 50 and y < 150:
		row = 1
	if y > 150 and y < 250:
		row = 2
	if y > 250 and y < 350:
		row = 3
	 
	return (row, col)

def input_list_updator():
	global input_list, player_turn
	row = pos[0]
	col = pos[1]

	if player_turn == 0:
		if input_list[row-1][col-1] == '':
			input_list[row-1][col-1] = 'O'
			input_rect_list[row-1][col-1] = O_surf.get_rect(center = (input_pos_list[row-1][col-1]))
			screen.blit(O_surf, input_rect_list[row-1][col-1])
			player_turn = 1
	else: 
		if input_list[row-1][col-1] == '':
			input_list[row-1][col-1] = 'X'
			input_rect_list[row-1][col-1] = X_surf.get_rect(center = (input_pos_list[row-1][col-1]))
			screen.blit(X_surf, input_rect_list[row-1][col-1])
			player_turn = 0	

def check_win():
	for win_combo in win_combos:
		if input_list[win_combo[0][0]][win_combo[0][1]] == input_list[win_combo[1][0]][win_combo[1][1]] == input_list[win_combo[2][0]][win_combo[2][1]]:
			if input_list[win_combo[0][0]][win_combo[0][1]] == 'X':
				return 'X'
			if input_list[win_combo[0][0]][win_combo[0][1]] == 'O':
				return 'O'
	return False

def game_over():
	if check_win():
		return True
	for row in input_list:
		for element in row:
			if element == '':
				return False 
	return True
	
#Object_surfs
X_surf_raw = pygame.image.load('X.png').convert_alpha()
X_surf = pygame.transform.rotozoom(X_surf_raw, 0, 0.2)
O_surf_raw = pygame.image.load('O.png').convert_alpha()
O_surf = pygame.transform.rotozoom(O_surf_raw, 0, 0.2)

# User inputs
input_list = [['', '', ''], ['', '', ''], ['', '', '']]
input_pos_list = [[(100, 100), (200, 100), (300, 100)], [(100, 200,), (200, 200), (300, 200)], [(100, 300), (200, 300), (300, 300)]]
input_rect_list = [['', '', ''], ['', '', ''], ['', '', '']]

#Text Message
text_font = pygame.font.Font('Pixeltype.ttf', 50)
X_turn_message_surf = text_font.render("X's Turn", False, (255, 255, 255))
X_turn_message_rect = X_turn_message_surf.get_rect(center = (200, 25))
O_turn_message_surf = text_font.render("O's Turn", False, (255, 255, 255))
O_turn_message_rect = O_turn_message_surf.get_rect(center = (200, 25)) 

#Turn switcher
player_turn = 0 #0 for O and 1 for X

#game-over
win_combos = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)], [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
game_restart_message_1 = text_font.render("Press 'SPACE' to", False, (255, 255, 255))
game_restart_message_rect_1 = game_restart_message_1.get_rect(center = (200, 200))
game_restart_message_2 = text_font.render("restart the game", False, (255, 255, 255))
game_restart_message_rect_2 = game_restart_message_2.get_rect(center = (200, 250))
game_draw_surf = text_font.render("Game is a draw", False, (255, 255, 255))
game_draw_rect = game_draw_surf.get_rect(center = (200, 150))
game_active = True



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				#emptying input_list
				for i in range(0, 3):
					for j in range(0, 3):
						input_list[i][j] = ''

				#emptying input_rect_list
				for i in range(0, 3):
					for j in range(0, 3):
						input_rect_list[i][j] = ''
		
				game_active = True
				winner = False
				pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 400, 400))

	if game_active:

		#line - Vertical
		pygame.draw.line(screen, (255, 255, 255), (150, 50), (150, 350), 10)
		pygame.draw.line(screen, (255, 255, 255), (250, 50), (250, 350), 10)

		#line - Horizontal
		pygame.draw.line(screen, (255, 255, 255), (50, 150), (350, 150), 10)
		pygame.draw.line(screen, (255, 255, 255), (50, 250), (350, 250), 10)

		if pygame.mouse.get_pressed()[0]:
			mouse_pos = pygame.mouse.get_pos()
			pos = position_locator()
			input_list_updator()

			#Check if the game is over
			if game_over():
				winner = check_win()
				game_active = False
			
		#Whose turn it is message
		if player_turn:
			pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(137, 9, 126, 32))
			screen.blit(X_turn_message_surf, X_turn_message_rect)	
		else:
			pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(137, 9, 126, 32))
			screen.blit(O_turn_message_surf, O_turn_message_rect)


	else:
		pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 400, 400))
		
		if winner:
			game_over_message_surf = text_font.render(winner + ' is winner', False, (255, 255, 255))
			game_over_rect = game_over_message_surf.get_rect(center = (200, 150))
			screen.blit(game_over_message_surf, game_over_rect)
		else: 
			screen.blit(game_draw_surf, game_draw_rect)
		
		screen.blit(game_restart_message_1, game_restart_message_rect_1)
		screen.blit(game_restart_message_2, game_restart_message_rect_2)


	pygame.display.update()
	clock.tick(60)