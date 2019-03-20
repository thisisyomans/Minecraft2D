#pygame module and sys module, sys for exiting window we create
import pygame, sys

#import some useful constants
from pygame.locals import *

#constants representing colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#constants representing different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

#a dictionary linking resources to colors
colors = {
	DIRT : BROWN,
	GRASS : GREEN,
	WATER : BLUE,
	COAL : BLACK
}

#list representing tilemap
tilemap = [
	[GRASS, COAL, DIRT],
	[WATER, WATER, GRASS],
	[COAL, GRASS, WATER],
	[DIRT, GRASS, COAL],
	[GRASS, WATER, DIRT]
]

#game dimensions
TILESIZE = 40
MAPWIDTH = 3
MAPHEIGHT = 5

#init pygame module
pygame.init()

#make new drawing surface, width=300, height=300
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

#window caption/title
pygame.display.set_caption("Minecraft 2D")

#loop (repeat) forever
while True:
	for event in pygame.event.get(): #get all user events
		if event.type == QUIT: #if user wants to quit
			pygame.quit() #end game
			sys.exit() #close window
	
	#loop thru each row
	for row in range(MAPHEIGHT):
		#loop thru each column in the row
		for column in range(MAPWIDTH):
			#draw the resource at that position in the tilemap, using the correct color
				pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

	pygame.display.update()
