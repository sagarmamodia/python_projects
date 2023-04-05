import pygame
from sys import exit
from random import randint, choice

pygame.init()

clock = pygame.time.Clock()
game_active = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_jump = pygame.image.load('graphics/Player/jump.png')
        self.player_index = 0
        self.player_walk = [player_walk_1, player_walk_2]
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200, 300))
        self.gravity = 0


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20    

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity 
        if self.rect.bottom > 300:
            self.rect.bottom = 300

    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.image = self.player_walk[int(self.player_index)]
            self.player_index += 0.1
            if self.player_index >= 2: self.player_index = 0


    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'snail':
            snail_image_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_image_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_image_1, snail_image_2]
            y_pos = 300
    
        if type == 'fly':
            fly_image_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_image_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_image_1, fly_image_2]
            y_pos = 200
        
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom = (randint(1000, 1100), y_pos))

    def animation(self):
        self.index += 0.1
        if self.index > len(self.frames): self.index = 0
        self.image = self.frames[int(self.index)]

    def destroy(self):
        if self.rect.x < -100:
            self.kill()

    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy()

def display_score():
    global score
    current_time = pygame.time.get_ticks() - start_time
    score = int(current_time / 100)
    current_time_surf = text_font.render(str(int(current_time / 100)), False, (64, 64, 64))
    current_time_rect = current_time_surf.get_rect(center = (400, 50))
    screen.blit(current_time_surf, (400, 50))

def collission_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle, False):
        obstacle.empty()
        return False
    else:
        return True

#Main Display Surface
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

#Background
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

#Text
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#Game-Over Message
restart_game_surf = text_font.render('Press Space to Start', False, (0, 0, 0))
restart_game_rect = restart_game_surf.get_rect(center = (400, 350))
start_time = 0

player_stand_surf = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()

#CLASSES----------------------------------------------------------------------------------------------------

#Sprite Group for Obstacles
obstacle = pygame.sprite.Group()

#Sprite Group for player
player = pygame.sprite.GroupSingle()
player.add(Player())

#-----------------------------------------------------------------------------------------------------------

#player_gravity = 0

player_surf_scaled = pygame.transform.rotozoom(player_stand_surf, 0, 2)
player_rect_scaled = player_surf_scaled.get_rect(center = (400, 200))


#CLASSES
enemy_spawn_timer = pygame.USEREVENT + 4
pygame.time.set_timer(enemy_spawn_timer, 1500)

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active: 
            
            #CLASSES---------------------------------------------------------------------------------------
            if event.type == enemy_spawn_timer:
                 obstacle.add(Obstacle(choice(['fly', 'snail', 'snail'])))
        else: 
            if event.type == pygame.KEYDOWN:
                if game_active == False and event.key == pygame.K_SPACE:
                        game_active = True
                        start_time = pygame.time.get_ticks()


    if game_active:
        
        screen.blit(ground_surf, (0, 300))
        screen.blit(sky_surf, (0, 0))

        #CLASSES----------------------------------------------------------------------------------------
        player.draw(screen)
        player.update()

        obstacle.draw(screen)
        obstacle.update()

        display_score()

        game_active = collission_sprite()
    else:
        #Defining final score message
        score_message_surf = text_font.render('Your score: ' + str(score), False, (111, 196, 169))
        score_message_rect = score_message_surf.get_rect(center = (400, 50))

        #Fill the screen background
        screen.fill((0,76,150))
        screen.blit(player_surf_scaled, player_rect_scaled)
        screen.blit(restart_game_surf, restart_game_rect)
        screen.blit(score_message_surf, score_message_rect)


    pygame.display.update()
    clock.tick(60)
