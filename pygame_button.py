"""
Buttons in pygame: https://thepythoncode.com/article/make-a-button-using-pygame-in-python
"""

import pygame

import os
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
FPS = 60 # Increased FPS for smoother movement
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Button Test")
clock = pygame.time.Clock()
# Adding font
font = pygame.font.SysFont("Calibri", 80)


class Buttons():
    # Define Images
    button_img = pygame.image.load(os.path.join("ProjectImages", "ButtonImage.png"))
    button_img = pygame.transform.smoothscale(button_img, (150, 60))  # resize if needed
    button_rect = button_img.get_rect(center=(WIDTH//2, HEIGHT//2))

    # Detecting mouseclicks --> similar to keydowns
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("you clicked the button")