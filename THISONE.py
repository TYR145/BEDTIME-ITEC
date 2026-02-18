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

# White Circles - POINTS
wc1 = pygame.image.load(os.path.join("ProjectImages", "w_circle.png"))
wc1 = pygame.transform.smoothscale(wc1, (40,40)) #--> DIMENSIONS

wc2 = pygame.image.load(os.path.join("ProjectImages", "w_circle.png"))
wc2 = pygame.transform.smoothscale(wc2, (40,40))

wc3 = pygame.image.load(os.path.join("ProjectImages", "w_circle.png"))
wc3 = pygame.transform.smoothscale(wc3, (40,40))

wc4 = pygame.image.load(os.path.join("ProjectImages", "w_circle.png"))
wc4 = pygame.transform.smoothscale(wc4, (40,40))

# White Circle - RECTS
wc1_rect = pygame.Rect(40,140, wc1.get_width(),wc1.get_height())
wc2_rect = pygame.Rect(350,240, wc2.get_width(),wc2.get_height())
wc3_rect = pygame.Rect(150,370, wc3.get_width(),wc3.get_height())
wc4_rect = pygame.Rect(550,67, wc4.get_width(),wc4.get_height())

#----------------------------------------------------------------------
# Exit Star Image
es = pygame.image.load(os.path.join("ProjectImages", "exit_star.png"))
es = pygame.transform.smoothscale(es, (40,40))
#Rect --> for collision
es_rect = es.get_rect()
# ---------------------------------------------------------------------

# ====================
#      GAME LOOP
# ====================
end = False

# White Circles
wc1_visible = True
wc2_visible = True
wc3_visible= True
wc4_visible = True
# Function tracking if circles are collected
def CirclesCollected(): #--> Creating a FUNCTION to check if all are collected
    return (not wc1_visible and not wc2_visible and not wc3_visible and not wc4_visible)


# Exit Stars
es_visible = False


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
    # COLLISION DETECTION of White Circles
    if p_rect.colliderect(wc1_rect):
        wc1_visible = False
    if p_rect.colliderect(wc2_rect):
        wc2_visible = False
    if p_rect.colliderect(wc3_rect):
        wc3_visible = False
    if p_rect.colliderect(wc4_rect):
        wc4_visible = False
    
    if CirclesCollected():
        es_visible = True
    # Checks to end if Star is visible & Player touching the Star's rect 
    if es_visible and p_rect.colliderect(es_rect):
        end = True

    # Descending Order -- Which images get drawn first
    screen.blit(background, (0, 0))       # Draw BG FIRST
    screen.blit(player_currentD, p_rect)  # Draw player

    # DRAWING White Circles --> PLACEMENT & VISIBILITY
    if wc1_visible == True:
        screen.blit(wc1, wc1_rect)
    if wc2_visible == True:
        screen.blit(wc2, wc2_rect)
    if wc3_visible == True:
        screen.blit(wc3, wc3_rect)
    if wc4_visible == True:
        screen.blit(wc4, wc4_rect)

    # DRAWING Exit Star
    es_rect.topleft = (400, 300)
    if es_visible == True:
        screen.blit(es, es_rect)
    


    pygame.display.flip()
    clock.tick(FPS)