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
player_image = pygame.image.load(os.path.join("ProjectImages","Arrow_R.png"))
player_image = pygame.transform.scale(player_image, (55, 55))


# Player DIRECTION SPRITES & Scale Images
player_Left = pygame.image.load(os.path.join("ProjectImages", "Arrow_L.png"))
player_Left = pygame.transform.scale(player_Left, (55, 55)) 

player_Right = pygame.image.load(os.path.join("ProjectImages", "Arrow_R.png"))
player_Right = pygame.transform.scale(player_Right, (55, 55))

player_Up = pygame.image.load(os.path.join("ProjectImages", "Arrow_U.png"))
player_Up = pygame.transform.scale(player_Up, (55, 55))

player_Down = pygame.image.load(os.path.join("ProjectImages", "Arrow_D.png"))
player_Down = pygame.transform.scale(player_Down, (55, 55))

# Player's location and speed
player_currentD = player_Right # SETS CURRENT DIRECTION SPRITE
player_x = 10           # Spawnpoint
player_y = HEIGHT - 195 # Spawnpoint
player_speed = 4


# Enemies

# Obstacles


# ====================
#      GAME LOOP
# ====================
end = False

# Player movement Variables
player_dx = 0 #--> Direction x
player_dy = 0 #--> Direction y

while not end:
    # Event handling: Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

        # EXIT KEY - "Esc"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                end = True
                
            # LEFT
            if event.key == pygame.K_a:
                player_dx = -player_speed
                player_currentD = player_Left
            # RIGHT
            if event.key == pygame.K_d:
                player_dx = player_speed
                player_currentD = player_Right
            # UP
            if event.key == pygame.K_w:
                player_dy = -player_speed
                player_currentD = player_Up
            # DOWN
            if event.key == pygame.K_s:
                player_dy = player_speed
                player_currentD = player_Down

        if event.type == pygame.KEYUP:
                if event.key in (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s):
                    player_dx = 0
                    player_dy = 0


    #====Game logic: Update player position based on input=====
    player_x += player_dx 
    player_y += player_dy
    p_rec = pygame.Rect(player_x, player_y, player_image.get_width(),player_image.get_height())

    screen.blit(background, (0, 0)) #Draw Background FIRST
    screen.blit(player_currentD, (player_x, player_y))  # draw player
    pygame.display.flip()
    clock.tick(FPS)


"""
# player image
player_image = pygame.image.load("prince.gif")

# New character image
enemy_image = pygame.image.load("green.png")
"""