import pygame as pg
from sys import exit
from pygame.math import Vector2 as vec2
from settings import *
from pygame import mixer

class Game():
	def __init__(self):
		pg.init()
		self.display = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pg.display.set_caption('Pong')
		self.over = False
		self.font = pg.font.SysFont('Castellar', 100)
		self.sound = mixer.Sound('laser.wav')
		
		self.ball = Ball((400, 200)) #creating a ball
		self.bat_r = Bat('right')
		self.bat_l = Bat('left')
		self.life_r = HEALTH
		self.life_l = HEALTH

		self.clock = pg.time.Clock()


	def draw_canvas(self):
		self.display.fill(BG_COLOR)
		pg.draw.line(self.display, BAT_COLOR, (int(SCREEN_WIDTH/2), 0), (int(SCREEN_WIDTH/2), SCREEN_HEIGHT), 2)

	def collision_detection(self):
		if self.ball.rect.colliderect(self.bat_r.rect):
			self.ball.velocity.x *= -1
			self.sound.play()
		if self.ball.rect.colliderect(self.bat_l.rect):
			self.ball.velocity.x *= -1
			self.sound.play()
		
		#collision with the walls
		if self.ball.rect.x > SCREEN_WIDTH-BALL_SIZE:
			self.ball.velocity.x *= -1
			self.life_r -= 1
			self.sound.play()
		if self.ball.rect.x < BALL_SIZE:
			self.ball.velocity.x *= -1
			self.life_l -= 1
			self.sound.play()

		if self.ball.rect.y >= SCREEN_HEIGHT-BALL_SIZE or self.ball.rect.y < BALL_SIZE:
			self.ball.velocity.y *= -1
			self.sound.play()
	
	def game_over(self):
		self.display.fill(BG_COLOR)
		if self.life_r == 0:
			winner_msg = self.font.render('Left side has won', True, WHITE)
		else:
			winner_msg = self.font.render('Right side has won', True, WHITE)
		winner_rect = winner_msg.get_rect(center = (SCREEN_WIDTH/2, 2*SCREEN_HEIGHT/6))
		self.display.blit(winner_msg, winner_rect)

	def restart_game(self):

		#button------------------------------------------------------------------------
		restart_button = self.font.render('Restart', True, WHITE)
		restart_button_rect = restart_button.get_rect(center = (SCREEN_WIDTH/2, 4*SCREEN_HEIGHT/6))
		self.display.blit(restart_button, restart_button_rect)

		button_width = restart_button_rect.right-restart_button_rect.left
		button_height = restart_button_rect.bottom-restart_button_rect.top

		pg.draw.rect(self.display, BAT_COLOR, pg.Rect(restart_button_rect.x, restart_button_rect.y, button_width, button_height), 1)

		mouse_pos = pg.mouse.get_pos()
		x = mouse_pos[0]
		y = mouse_pos[1]
		if x < restart_button_rect.right and x > restart_button_rect.x and y < restart_button_rect.bottom and y > restart_button_rect.top:
			pg.draw.rect(self.display, BAT_COLOR, pg.Rect(restart_button_rect.x, restart_button_rect.y, button_width, button_height))
			self.display.blit(restart_button, restart_button_rect)
			if pg.mouse.get_pressed()[0]:
				self.over = False
				self.life_r = HEALTH
				self.life_l = HEALTH
				self.ball.pos = vec2(BALL_POS_INITIAL)
		#---------------------------------------------------------------------------------------



	def life(self):
		left_life = self.font.render(f'{self.life_l}', True, RED)
		left_rect = left_life.get_rect(center = (SCREEN_WIDTH/4, 40))
		self.display.blit(left_life, left_rect)

		rect_right = left_life.get_rect(center = (3*SCREEN_WIDTH/4, 40))
		life_right = self.font.render(f'{self.life_r}', True, RED)
		self.display.blit(life_right, rect_right)


	def run(self):
		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					exit()

			if self.life_r == 0 or self.life_l == 0:
				self.over = True

			if not self.over:		
				self.draw_canvas()

				self.collision_detection()

				self.ball.update()
				self.bat_r.update()
				self.bat_l.update()
				self.life()
			else:
				self.game_over()
				self.restart_game()

			pg.display.update()
			self.clock.tick(60)


class Ball():
	def __init__(self, pos):
		self.velocity = vec2(BALL_VELOCITY)
		self.pos = vec2(pos)
		self.rect = pg.Rect(self.pos.x-BALL_SIZE, self.pos.y-BALL_SIZE, BALL_SIZE*2, BALL_SIZE*2)
	
	def draw(self):
		pg.draw.circle(game.display, WHITE, (int(self.pos.x), int(self.pos.y)), BALL_SIZE)
		# pg.draw.rect(game.display, BAT_COLOR, self.rect, 2)

	def move(self):
		self.pos += self.velocity
		self.rect = pg.Rect(self.pos.x-BALL_SIZE, self.pos.y-BALL_SIZE, BALL_SIZE*2, BALL_SIZE*2)

	def update(self):
		self.draw()
		self.move()


class Bat():
	def __init__(self, typ):
		self.type = typ
		if self.type == 'right':
			self.rect = pg.Rect(SCREEN_WIDTH-BAT_WIDTH, SCREEN_HEIGHT/2-BAT_HEIGHT/2, BAT_WIDTH, BAT_HEIGHT)
		if self.type == 'left':
			self.rect = pg.Rect(0, SCREEN_HEIGHT/2-BAT_HEIGHT/2, BAT_WIDTH, BAT_HEIGHT)

	def draw(self):
		pg.draw.rect(game.display, BAT_COLOR, self.rect)

	def move_r(self):
		keys = pg.key.get_pressed()
		if keys[pg.K_UP] and self.rect.y > 0:
			self.rect.y -= BAT_SPEED
		elif keys[pg.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
			self.rect.y += BAT_SPEED

	def move_l(self):
		keys = pg.key.get_pressed()
		if keys[pg.K_w] and self.rect.y > 0:
			self.rect.y -= BAT_SPEED
		elif keys[pg.K_s] and self.rect.bottom < SCREEN_HEIGHT:
			self.rect.y += BAT_SPEED


	def update(self):
		if self.type == 'right':
			self.move_r()
		if self.type == 'left':
			self.move_l()
		self.draw()


game = Game()
game.run()

