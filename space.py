import pygame
from pygame.locals import *
import os
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
# load sounds
BULLET_HIT_SOUND = pygame.mixer.Sound('g/space_invadors/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('g/space_invadors/Gun+Silencer.mp3')
#load fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
#decide frame rate/ velocity etc
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
# loading spaceship images
YELLOW_SPACESHIP_IMAGE = pygame.image.load('g/space_invadors/2.png')
RED_SPACESHIP_IMAGE = pygame.image.load('g/space_invadors/1.png')
#transforming and scaling to match the window size
SPACE = pygame.transform.scale(pygame.image.load("g/space_invadors/OIP.jpeg"), (WIDTH, HEIGHT))
# intialize health
red_health=10
yellow_health=10

class Spaceship(pygame.sprite.Sprite):