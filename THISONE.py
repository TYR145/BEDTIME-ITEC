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
#      IMAGES --- ADD PLAYER IMAGE RECT FOR BORDER COLLISION
# ====================

# Adding BG Images
background = pygame.image.load(os.path.join("ProjectImages", "OpenBG.jpg"))
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

# ---------------------------------------------------------------------
# Player
player_image = pygame.image.load(os.path.join("ProjectImages","Arrow_R.png"))
player_image = pygame.transform.smoothscale(player_image, (55, 55))


# Player DIRECTION SPRITES & Scale Images --> use "smoothscale()" to smooth edges
player_Left = pygame.image.load(os.path.join("ProjectImages", "Arrow_L.png"))
player_Left = pygame.transform.smoothscale(player_Left, (55, 55)) 

player_Right = pygame.image.load(os.path.join("ProjectImages", "Arrow_R.png"))
player_Right = pygame.transform.smoothscale(player_Right, (55, 55))

player_Up = pygame.image.load(os.path.join("ProjectImages", "Arrow_U.png"))
player_Up = pygame.transform.smoothscale(player_Up, (55, 55))

player_Down = pygame.image.load(os.path.join("ProjectImages", "Arrow_D.png"))
player_Down = pygame.transform.smoothscale(player_Down, (55, 55))

# Player's location and speed
player_currentD = player_Right # SETS CURRENT DIRECTION SPRITE
player_x = 10           # Spawnpoint
player_y = HEIGHT - 195 # Spawnpoint
player_speed = 6

# Player Rect --> needed for border collision
p_rect = pygame.Rect(player_x, player_y, player_image.get_width(),player_image.get_height())
# ---------------------------------------------------------------------

# Enemies

# ---------------------------------------------------------------------
# Obstacles

# Yellow Circles - POINTS
yc1 = pygame.image.load(os.path.join("ProjectImages", "yellow_circle.png"))
yc1 = pygame.transform.smoothscale(yc1, (40,40)) #--> DIMENSIONS

yc2 = pygame.image.load(os.path.join("ProjectImages", "yellow_circle.png"))
yc2 = pygame.transform.smoothscale(yc2, (40,40))

yc3 = pygame.image.load(os.path.join("ProjectImages", "yellow_circle.png"))
yc3 = pygame.transform.smoothscale(yc3, (40,40))

yc4 = pygame.image.load(os.path.join("ProjectImages", "yellow_circle.png"))
yc4 = pygame.transform.smoothscale(yc4, (40,40))

#YELLOW CIRCLE Rects
yc1_rect = pygame.Rect(40,140, yc1.get_width(),yc1.get_height())
yc2_rect = pygame.Rect(350,240, yc2.get_width(),yc2.get_height())
yc3_rect = pygame.Rect(150,370, yc3.get_width(),yc3.get_height())
yc4_rect = pygame.Rect(550,67, yc4.get_width(),yc4.get_height())
# ---------------------------------------------------------------------

# ====================
#      GAME LOOP
# ====================
end = False

yc1_visible = True
yc2_visible = True
yc3_visible= True
yc4_visible = True

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


# =========================================
#      GAME LOGIC: Updates player position
# =========================================
    p_rect.x += player_dx 
    p_rect.y += player_dy


    # Points Visible



    # BORDER COLLISION --> use < & > adds flexibility, to snap ONLY if player is too far
    if p_rect.left < 6:
        p_rect.left = 6

    if p_rect.top < 7:
        p_rect.top = 7
       
    if p_rect.bottom > HEIGHT - 6:
        p_rect.bottom = HEIGHT - 6

    if p_rect.right > WIDTH - 7:
        p_rect.right = WIDTH - 7

    #----------------------------
    # Collecting Points Updates
    #----------------------------
    # COLLISION DETECTION of Yellow Circles
    if p_rect.colliderect(yc1_rect):
            yc1_visible = False
    if p_rect.colliderect(yc2_rect):
            yc2_visible = False
    if p_rect.colliderect(yc3_rect):
            yc3_visible = False
    if p_rect.colliderect(yc4_rect):
            yc4_visible = False

    # Descending Order -- Which images get drawn first
    screen.blit(background, (0, 0))       # Draw BG FIRST
    screen.blit(player_currentD, p_rect)  # Draw player

    # DRAWING yellow circles --> PLACEMENT & VISIBILITY
    if yc1_visible == True:
        screen.blit(yc1, yc1_rect)
    if yc2_visible == True:
        screen.blit(yc2, yc2_rect)
    if yc3_visible == True:
        screen.blit(yc3, yc3_rect)
    if yc4_visible == True:
        screen.blit(yc4, yc4_rect)
    


    pygame.display.flip()
    clock.tick(FPS)