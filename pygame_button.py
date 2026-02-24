"""
Buttons in pygame: https://thepythoncode.com/article/make-a-button-using-pygame-in-python
"""
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
"""

# RESOURCE: https://www.geeksforgeeks.org/python/mmouse-clicks-on-sprites-in-pygame/

import pygame


class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.callback = callback

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()


def on_click():
    color = (255, 0, 0) if sprite.image.get_at(
        (0, 0)) != (255, 0, 0) else (0, 255, 0)
    sprite.image.fill(color)


pygame.init()
screen = pygame.display.set_mode((400, 300))

sprite = ClickableSprite(pygame.Surface((100, 100)), 50, 50, on_click)
group = pygame.sprite.GroupSingle(sprite)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    group.update(events)
    screen.fill((255, 255, 255))
    group.draw(screen)
    pygame.display.update()

pygame.quit()