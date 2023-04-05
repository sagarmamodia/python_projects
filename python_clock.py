import pygame as pg
import math
from sys import exit 
import datetime

pg.init()


#CONSTANTS-------------------------------------------------------------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


CLOCK_RADIUS = 200
MINUTE_PIN_LEN = 170
HOUR_PIN_LEN = 150
SECOND_PIN_LEN = 120
HOUR_PIN_WIDTH = 8
MINUTE_PIN_WIDTH =4
SECOND_PIN_WIDTH = 2 

#----------------------------------------------------------------------------------------------------------------------

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
# pg.draw.circle(screen, (255, 255, 255), (200, 200), 180)



def convert_to_pg_coordinates(R, theta):
    x1 = math.cos(math.radians(-theta))*R
    y1 = math.sin(math.radians(-theta))*R
    return (int(SCREEN_WIDTH/2+x1)-4, int(SCREEN_HEIGHT/2-y1)-4)


def move_pins():
    current_time = datetime.datetime.now()
    pg.draw.line(screen, RED, (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)), convert_to_pg_coordinates(SECOND_PIN_LEN, current_time.second * 360/60-90), SECOND_PIN_WIDTH)
    pg.draw.line(screen, BLACK, (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)), convert_to_pg_coordinates(MINUTE_PIN_LEN, (current_time.minute + current_time.second/60) * 360/60-90), MINUTE_PIN_WIDTH)
    pg.draw.line(screen, BLACK, (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)), convert_to_pg_coordinates(HOUR_PIN_LEN, (current_time.hour + current_time.minute/60 + current_time.second/3600) * 360/12-90), HOUR_PIN_WIDTH)

def print_text(text, position):
    font = pg.font.SysFont("Castellar", 20, True, False)
    surface = font.render(text, True, BLACK)
    screen.blit(surface, position)

def draw_numbers():
    for i in range(1, 13):
        print_text(str(i), convert_to_pg_coordinates(170, i*30 - 90))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.fill(WHITE)
    
    draw_numbers()
    move_pins()

    pg.draw.circle(screen, BLACK, (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)), CLOCK_RADIUS, 5)
    pg.draw.circle(screen, BLACK, (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)), 10)

    
    pg.display.update()

