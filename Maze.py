import pygame
import os
#-------------------------------------------------------------------
# INIT(IALIZE)
#-------------------------------------------------------------------
pygame.init()

# SCREEN DIMENSIONSss
WIDTH, HEIGHT = 650, 450
FPS = 60 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Mechanics - BETA")
clock = pygame.time.Clock()

# COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

"""
ADD OBSTACLES BETWEEN?? 
--> enemies or just a maze like as planned... once I know how lol

ADD ending image??? Idk
--> figure out how to make new message appear when you touch exit star
"""

# ===========================================================
#      ADDING IMAGES --- ADD IMAGE RECT FOR BORDER COLLISION
# ===========================================================

# Adding BG Images
background = pygame.image.load(os.path.join("ProjectImages", "OpenBG.jpg"))
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

# ---------------------------------------------------------------------
# Player
player_image = pygame.image.load(os.path.join("ProjectImages","Arrow_R.png"))
player_image = pygame.transform.smoothscale(player_image, (35, 35))


# PLAYER Directional Sprites & Image scaling --> use "smoothscale()" to smooth edges
player_Left = pygame.image.load(os.path.join("ProjectImages", "Arrow_L.png"))
player_Left = pygame.transform.smoothscale(player_Left, (35, 35)) 

player_Right = pygame.image.load(os.path.join("ProjectImages", "Arrow_R.png"))
player_Right = pygame.transform.smoothscale(player_Right, (35, 35))

player_Up = pygame.image.load(os.path.join("ProjectImages", "Arrow_U.png"))
player_Up = pygame.transform.smoothscale(player_Up, (35, 35))

player_Down = pygame.image.load(os.path.join("ProjectImages", "Arrow_D.png"))
player_Down = pygame.transform.smoothscale(player_Down, (35, 35))

# Player's location and speed
player_currentD = player_Right # SETS CURRENT DIRECTION SPRITE
player_x = 10           # Spawnpoint
player_y = HEIGHT - 195 # Spawnpoint
player_speed = 6

# Player Rect --> needed for border collision
p_rect = pygame.Rect(player_x, player_y, player_image.get_width(),player_image.get_height())
#----------------------------------------------------------------------



# OBJECTS

# White Circles - POINTS & RECTS (Will change for individual toys)
wc1 = pygame.image.load(os.path.join("ProjectImages", "w_circle.png"))
wc1 = pygame.transform.smoothscale(wc1, (30,30)) #--> DIMENSION SCALING

wc2 = pygame.image.load(os.path.join("ProjectImages", "w_circle.png"))
wc2 = pygame.transform.smoothscale(wc2, (30,30))

wc3 = pygame.image.load(os.path.join("ProjectImages", "w_circle.png"))
wc3 = pygame.transform.smoothscale(wc3, (30,30))

wc4 = pygame.image.load(os.path.join("ProjectImages", "w_circle.png"))
wc4 = pygame.transform.smoothscale(wc4, (30,30))

wc1_rect = pygame.Rect(40,140, wc1.get_width(),wc1.get_height()) #-->(x,y) placements of points
wc2_rect = pygame.Rect(350,240, wc2.get_width(),wc2.get_height())
wc3_rect = pygame.Rect(150,370, wc3.get_width(),wc3.get_height())
wc4_rect = pygame.Rect(550,67, wc4.get_width(),wc4.get_height())



# Defining Obstacles --> Put inside def Function idk....)
def create_obstacles():
    # 1. Create an empty list to add obstacles to
    obstacles = []
    
    # 2. Define images & Scaling them
    obs_img = pygame.image.load(os.path.join("ProjectImages", "obstacle.png"))
    obs_img = pygame.transform.smoothscale(obs_img, (45,45))

    """
    TO DO:
    - REARRANGE OBSTACLE COORDINATES
    - ADD MOVING OBSTACLES --> touch = "die"? (i.e. "marbles", those wind up toys etc.)
    """
    # 3. Adding coordinates
    obs_coords = [
        # blocks exit star path 
        (10, 200),

        # TOP ROOM 
        (120, 70), (260, 75), (400, 80),

        # UPPER MID
        (150, 130), (230, 140), (310, 135), (390, 145), (470, 130),


        # near wc1 
        (90, 160), (160, 150),

        # near wc2 
        (300, 220), (380, 260), (330, 300),

        # near wc3 
        (140, 330), (210, 360), (260, 310),

        # MID ROOM 
        (250, 200), (290, 260)
    ]

    # 4. Add obstacles to list [] --> use .append to apply rect & img
    for x, y in obs_coords:
        rect = obs_img.get_rect(topleft=(x,y)) #--> adds obstacle objects
        obstacles.append((obs_img, rect))#--> also adds images & rects
    
    # 5. return the value of "obstacle"
    return obstacles
obstacles = create_obstacles() # 6. Calls back the function

# Defining Exit Star Image
eStar = pygame.image.load(os.path.join("ProjectImages", "exit_star.png"))
eStar = pygame.transform.smoothscale(eStar, (40,40))
#Rect --> for collision
eStar_rect = eStar.get_rect()



# ======================
#      GAME LOOP LOGIC
# ======================
end = False

# White Circles
wc1_visible = True
wc2_visible = True
wc3_visible= True
wc4_visible = True
# Function tracking if circles are collected
def CirclesCollected(): #--> Creating a FUNCTION to check if all are collected
    return (not wc1_visible and not wc2_visible and not wc3_visible and not wc4_visible)

# Exit Star
eStar_visible = False


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

    """
    Obstacle placemnt defined in def Obstacles()
    """

    # BORDER COLLISION --> use < & > adds flexibility, to snap ONLY if player is too far
    if p_rect.left < 6:
        p_rect.left = 6

    if p_rect.top < 7:
        p_rect.top = 7
       
    if p_rect.bottom > HEIGHT - 6:
        p_rect.bottom = HEIGHT - 6

    if p_rect.right > WIDTH - 7:
        p_rect.right = WIDTH - 7


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
        eStar_visible = True
    # Checks to end if Star is visible & Player touching the Star's rect 
    if eStar_visible and p_rect.colliderect(eStar_rect):
        end = True
        print("You won!")


# ======================
#      DRAWING
# ======================

    # Descending Order -- Which images get drawn first
    screen.blit(background, (0, 0))       # Draw BG FIRST
    screen.blit(player_currentD, p_rect)  # Draw player

    # Drawing POINTS --> PLACEMENT & VISIBILITY
    if wc1_visible == True:
        screen.blit(wc1, wc1_rect)
    if wc2_visible == True:
        screen.blit(wc2, wc2_rect)
    if wc3_visible == True:
        screen.blit(wc3, wc3_rect)
    if wc4_visible == True:
        screen.blit(wc4, wc4_rect)
    
    # Drawing Obstacles --> use "for-in" loops to iterate through lists
    for obs_img, rect in obstacles: #--> obs_rec & img are vars defined in obstacles function
        screen.blit(obs_img, rect)

        #--> Add if to detect IF PLAYER touches the object
        #--> still call it "rect" bc detecting the object TYPE
        if p_rect.colliderect(rect):
            p_rect.x -= player_dx # Collision to bounce player BACk (-=) for X
            p_rect.y -= player_dy # Collision ``` BACK `` for y

    # DRAWING Exit Star
    eStar_rect.topleft = (player_x, player_y)
    if eStar_visible == True:
        screen.blit(eStar, eStar_rect)
    


    pygame.display.flip()
    clock.tick(FPS)