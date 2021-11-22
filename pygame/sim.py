from numpy import true_divide
import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

TILEMAP = [
    25,23,20,19,20,19,19,21,20,17,14,13,14,15,15,18,21,22,22,22,22,22,20,18,18,21,23,25,27,31,32,30,
    28,25,22,21,20,19,19,19,18,16,14,12,13,15,18,20,22,23,22,21,21,21,20,19,20,22,24,25,27,29,30,29,
    28,25,23,21,20,18,17,17,15,15,14,12,13,16,19,20,21,22,22,22,20,20,20,22,23,24,24,25,26,26,26,26,
    27,24,21,19,17,17,17,16,14,13,13,13,13,16,18,19,20,21,22,21,20,20,20,22,22,22,22,24,25,24,22,21,
    25,23,20,18,16,16,15,14,12,12,12,12,13,16,18,18,18,19,19,19,19,19,19,19,20,20,21,23,23,20,18,17,
    24,22,21,18,16,14,12,11,10,10,11,10,11,14,17,17,16,16,17,18,18,17,17,17,17,18,19,19,18,15,14,15,
    23,22,20,18,16,13,11,9,7,7,8,9,10,13,16,15,14,14,16,17,18,17,16,16,14,14,15,15,13,11,10,12,
    23,22,20,17,15,13,10,7,5,4,6,8,10,12,14,12,12,12,14,15,16,17,17,14,11,10,11,12,10,8,8,10,
    21,21,19,18,16,13,8,5,2,3,4,7,9,10,10,10,11,12,12,13,15,17,15,12,9,10,11,10,8,7,9,11,
    19,19,18,17,16,13,8,5,2,2,4,6,7,8,9,9,11,13,13,13,14,15,13,10,8,9,10,9,7,6,9,11,
    16,17,17,16,15,12,8,5,2,2,4,5,6,7,8,9,11,13,15,15,15,13,11,8,7,8,9,8,6,5,8,10,
    15,16,16,15,12,9,6,5,3,2,3,4,5,7,8,8,10,12,14,15,14,11,8,7,6,5,5,6,4,4,6,9,
    13,14,13,11,9,6,5,6,4,3,3,3,4,6,8,9,11,11,11,11,11,8,6,5,4,2,2,2,1,0,3,6,
    13,13,10,7,6,5,6,7,5,4,4,3,3,6,8,10,12,11,7,6,6,4,2,1,1,0,-1,-1,-3,-3,0,3,
    15,13,8,6,5,5,6,7,6,5,5,3,3,5,8,10,12,10,5,2,0,-1,-4,-4,-2,-1,-2,-2,-3,-3,-1,2,
    16,13,10,8,7,5,5,7,6,5,5,4,4,7,8,9,10,8,4,1,-2,-4,-6,-6,-4,-4,-4,-3,-3,-2,0,4
]

TILESIZE = 4
TILES_X = TILESIZE * 32
TILES_Y = TILESIZE * 32
SCREEN_WIDTH = TILES_X * TILESIZE
SCREEN_HEIGHT = TILES_Y * TILESIZE

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tiles = TILEMAP
        self.tilemap_x = TILES_X
        self.tilemap_y = TILES_Y
        self.tilesize = TILESIZE

    def update(self):
        pressed_keys = pygame.key.get_pressed()

    def draw(self, surface):
        for i in range(len(TILEMAP)):
            if i > 31:
                fermaui = True
            
            posx = (i % 32) * self.tilesize
            posy = int(i / 32) * self.tilesize
            color = WHITE
            if(TILEMAP[i] < 0):
                color = GREEN
            elif (TILEMAP[i] > 0):
                color = RED
            elif (TILEMAP[i] == 2):
                color = BLUE
            else:
                color = BLACK

            pygame.draw.rect(DISPLAYSURF, color, (posx, posy, self.tilesize, self.tilesize))


M = Map()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    M.update()

    DISPLAYSURF.fill(WHITE)
    M.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
