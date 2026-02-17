import pygame
import os
#-------------------------------------------------------------------
# INIT(IALIZE)
#-------------------------------------------------------------------
pygame.init()

# SCREEN DIMENSIONS
WIDTH, HEIGHT = 640, 480
FPS = 60 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Pictures Test")
clock = pygame.time.Clock()

# COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#Adding BG Images
background = pygame.image.load(os.path.join("MovementImages, OpenBG.jpg"))

# DRAWING
screen.blit(background, (0, 0))
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) #--> Refreshes the background
"""
# player image
player_image = pygame.image.load("prince.gif")

# New character image
enemy_image = pygame.image.load("green.png")
"""
