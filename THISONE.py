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

# ====================
#      IMAGES
# ====================

# Adding BG Images
background = pygame.image.load(os.path.join("ProjectImages", "OpenBG.jpg"))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Player
#player_image = pygame.image.load(os.path.join("images","Steve.png"))
#player_image = pygame.transform.scale(player_image, (64, 64))


# Enemies

# Obstacles


# ====================
#      GAME LOOP
# ====================
end = False

while not end:
    # Event handling: Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    # EXIT KEY - "Esc"
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                end = True

    # DISPLAYS IMAGE -- INSIDE the WHILE LOOP
    screen.blit(background, (0, 0)) #--> BLIT AFTER scaling image
    pygame.display.flip()
    clock.tick(FPS)


"""
# player image
player_image = pygame.image.load("prince.gif")

# New character image
enemy_image = pygame.image.load("green.png")
"""