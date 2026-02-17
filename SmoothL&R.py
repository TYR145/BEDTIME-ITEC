# 6.4.py 
# using pygame library and images

import pygame
# to install PyGame: open a command prompt and type "python -m pip install -U pygame --user"

#-------------------------------------------------------------------
# INITIALIZATION
#-------------------------------------------------------------------
# A. Initialize Pygame
pygame.init()

# B. Create the game window and clock
WIDTH, HEIGHT = 640, 480
FPS = 60 # Increased FPS for smoother movement
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example")
clock = pygame.time.Clock()

# C. Define game variables
#-----------------------------------------------------------
# 6.4 using images
#<<---------------------------------------------------------
# background image
# Load and scale background image
background = pygame.image.load("map.jpg") #--> loads an image instead of a rectangle

# player image
player_image = pygame.image.load("prince.gif")

# New character image
enemy_image = pygame.image.load("green.png")

#>>---------------------------------------------------------
# player location and speed
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 3

#movement variables (NEW)
player_dx = 0 #--> "difference in X" (starts @ 0 bc it's not moving at first)
player_dy = 0 #--> "difference in Y"

#(Determines if the player should be moving or not (& which direction))


# enemy location and speed
enemy_x = WIDTH // 2
enemy_y = HEIGHT // 2
enemy_speed = 5

#movement variables (NEW)
enemy_dx = 0 #--> "difference in X" (starts @ 0 bc it's not moving at first)
enemy_dy = 0 #--> "difference in Y"

#-------------------------------------------------------------------
# MAIN GAME LOOP
#-------------------------------------------------------------------
end = False
while not end:
    #---------------------------------------------------------------
    # UPDATE: 
    #---------------------------------------------------------------
    # A. Event handling: Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

        # start movement on key press (moves by 1 space)
        if event.type == pygame.KEYDOWN:
            # arrow keys
            if event.key == pygame.K_LEFT:
                player_dx = -player_speed #-->dx is CHANGING (-speed to go LEFT)
            if event.key == pygame.K_RIGHT: #-->dx is CHANGING (+speed to go RIGHT)
                player_dx = player_speed
            if event.key == pygame.K_UP:
                player_dy = -player_speed #--> (-y is GOING UP)
            if event.key == pygame.K_DOWN: #--> (+y is GOING DOWN)
                player_dy = player_speed


            # Escape key 
            if event.key == pygame.K_ESCAPE:
                end = True
                
        # end movement on key release
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_dx = 0
                
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player_dy = 0

    # B. Game logic: Update player position based on input
    player_x += player_dx 
    player_y += player_dy

    #C. Enemy movements (AUTO)
    enemy_x += 1


    #---------------------------------------------------------------
    # DRAW
    #---------------------------------------------------------------
    # A. draw background (no need to clear screen)
    #---------------------------------------------------------
    # 6.4 using images
    #<<---------------------------------------------------------------
    screen.blit(background, (0, 0))  # draw background Image ("Block Image Transfer" = blit)
    # B. draw player
    screen.blit(player_image, (player_x, player_y))  # draw player

    #C. Draw enemy
    screen.blit(enemy_image, (enemy_x, enemy_y))  # draw player
    #>>---------------------------------------------------------------
    # C. Update the display and cap frame rate
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
