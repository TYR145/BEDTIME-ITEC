import pygame
#-------------------------------------------------------------------
# INIT(IALIZE)
#-------------------------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 640, 480
FPS = 60 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#-------------------------------------------------------------------
# MAIN GAME LOOP
#-------------------------------------------------------------------
# --- Initialize Jump & Player variables --- 
# Player
player_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 30, 30) # Defining the player's rectangle
player_dx = 0 #--> "difference in X" (starts @ 0 bc it's not moving at first)
player_dy = 0 #--> "difference in Y"
player_speed = 4

# OPPS 
opp_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 30, 30, 30)
opp_x = 0
opp_y = 0

# JUMP
jump = False
initial_y = player_rect.y

end = False

while not end:
    #------------------------#UPDATE:-----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
   
        # --- Handle Key Presses (KEYDOWN) ---
        if event.type == pygame.KEYDOWN:
            #LEFT
            if event.key == pygame.K_LEFT:
                player_dx = -player_speed
            #RIGHT
            if event.key == pygame.K_RIGHT:
                player_dx = player_speed

            #JUMP
            if event.key == pygame.K_UP:
                # Changing the jump & player values
                jump = True
                initial_y = player_rect.y
        # --- Handle Key Presses (KEYUP) ---
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_dx = 0
                
    # JUMPING LOGIC
    if jump == True:
        player_rect.y -= 7
        if player_rect.y <= initial_y - 70:
            jump = False
    else: 
        if player_rect.y < initial_y: #Don't do <= bc then movement will be choppy
            player_rect.y += 6 # go down

    player_rect.x += player_dx
    player_rect.y += player_dy

    #--------------------------#DRAW:-------------------------------
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_rect)

    pygame.draw.rect(screen, BLUE, opp_rect)


    pygame.display.flip()
    clock.tick(FPS)

#QUIT GAME
pygame.quit()
