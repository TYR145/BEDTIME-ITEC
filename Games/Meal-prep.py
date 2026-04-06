import pygame
import os
import random

def run():
    pygame.init()
    WIDTH, HEIGHT = 650, 450
    FPS = 60 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Meal Prep - BETA")

#drawing the background + objects 
    background = pygame.image.load(os.path.join("ProjectImages", "OpenBG.jpg"))
    background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

if __name__ == "__main__":
        run()