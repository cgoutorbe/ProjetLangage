import pygame
from pygame.locals import *

DIRT = 1
GRASS = 2
WATER = 3

GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

colours = {
            DIRT:YELLOW,
            WATER:BLUE,
            GRASS:GREEN,
}
TILESIZE = 40
MAPWIDTH = 3
MAPHEIGHT = 3


#Building a tilemap
tilemap = [[GRASS,GRASS,WATER],
            [DIRT,DIRT,WATER],
            [WATER,DIRT,WATER]
            ]
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAYSURF,colours[tilemap[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

    pygame.display.update()
