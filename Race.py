import pygame
import os
#-------------------------------------------------------------------
# INIT(IALIZE)
#-------------------------------------------------------------------
pygame.init()

# SCREEN DIMENSIONSss
WIDTH, HEIGHT = 960, 450
FPS = 60 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Mechanics - BETA")
clock = pygame.time.Clock()

"""
UI to add:
- 3 Second Start Countdown 
- Distance counter in metres (??) --> Maybe not since we see the start to end
- Obstacles for Player (challenging)
- Have kid take "rests" to allow player to catch up
"""


# ===========================================================
#      ADDING IMAGES --- ADD IMAGE RECT FOR BORDER COLLISION
# ===========================================================

def player():
    # Defining Player
    player_image = pygame.image.load(os.path.join("ProjectImages","Arrow_R.png"))
    player_image = pygame.transform.smoothscale(player_image, (45, 45))

    # Player's location and speed
    player_x = 10           # Spawnpoint
    player_y = HEIGHT - 320 # Spawnpoint
    player_speed = 8
    # Player Rect --> needed for border collision
    p_rect = pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())

    return player_image, player_x, player_y, player_speed, p_rect
# CALL BACK FUNCTION --> include values defined
player_image, player_x, player_y, player_speed, p_rect = player()


def kid():
    # Defining Kid
    kid_image = pygame.image.load(os.path.join("ProjectImages", "kid_img.png"))
    kid_image = pygame.transform.smoothscale(kid_image, (65,65))

    # Kid's speed
    kid_speed = 1

    # Kid Rect ---> (x, y, kid)
    kid_rect = pygame.Rect(0, HEIGHT - 150, kid_image.get_width(), kid_image.get_height())

    return kid_image, kid_speed, kid_rect
kid_image, kid_speed, kid_rect = kid()

def assets():
    # Adding BG Images
    background = pygame.image.load(os.path.join("ProjectImages", "OpenBG.jpg"))
    background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))
    #----------------------------------------------------------------------
    # Goal
    goal_image = pygame.image.load(os.path.join("ProjectImages", "exit_star.png"))
    goal_image = pygame.transform.smoothscale(goal_image, (50, 50))

    # Player's Lane
    goalP_rect = pygame.Rect(850, player_y, goal_image.get_width(), goal_image.get_height())

    # Kid's Lane
    goalK_rect = pygame.Rect(850, HEIGHT- 150, goal_image.get_width(), goal_image.get_height())

    return background, goal_image, goalP_rect, goalK_rect
background, goal_image, goalP_rect, goalK_rect = assets()

# ---------------------------------------------------------------------
#-------------------------------------------------------------------------

# ======================
#      GAME LOOP LOGIC
# ======================

end = False

# Player movement Variables
player_dx = 0 #--> Direction x
player_dy = 0 #--> Direction y


# =========================================
#      GAME LOGIC: Updates player position
# =========================================
def game_loop():
    global end, player_dx, player_dy

    while not end:
        # Auto moves on X axis
        kid_rect.x += kid_speed

        # Event handling: Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

            # EXIT KEY - "Esc"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    end = True
                
                # RIGHT
                if event.key == pygame.K_RIGHT:
                    player_dx = player_speed
                # UP
                if event.key == pygame.K_UP:
                    player_dy = -player_speed
                # DOWN
                if event.key == pygame.K_DOWN:
                    player_dy = player_speed
            # KEYUP
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player_dx = 0
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        player_dy = 0
        
        # PLAYER MOVEMENT
        def player_collision():
            p_rect.x += player_dx 
            p_rect.y += player_dy
        player_collision()

        # BORDER COLLISION --> use < & > adds flexibility, to snap ONLY if player is too far
        def boarder_collision():
            # Player
            if p_rect.left < 6:
                p_rect.left = 6

            if p_rect.top < 7:
                p_rect.top = 7
            
            if p_rect.bottom > HEIGHT - 6:
                p_rect.bottom = HEIGHT - 6

            if p_rect.right > WIDTH - 7:
                p_rect.right = WIDTH - 7

            # Kid
            if kid_rect.left < 6:
                kid_rect.left = 6

            if kid_rect.top < 7:
                kid_rect.top = 7
            
            if kid_rect.bottom > HEIGHT - 6:
                kid_rect.bottom = HEIGHT - 6

            if kid_rect.right > WIDTH - 7:
                kid_rect.right = WIDTH - 7
        boarder_collision()

        # GOAL DETECTION
        def goal_detection():
            # Detecting who touches Goal first
            FinishLine_x = 850  # x-position of the goal

            # Player reaches goal
            if p_rect.colliderect(goalP_rect):
                print("You win!")
                global end
                end = True
                return FinishLine_x, end

            # Kid reaches goal
            if kid_rect.colliderect(goalK_rect):
                print("You lose!")
                end = True
                return FinishLine_x, end
        goal_detection()  # ← aligned with def (same indent level)
  

        #---------------------------------------------------------------
        def draw():
            # DRAW
            screen.blit(background, (0, 0))
            screen.blit(player_image, p_rect)
            screen.blit(kid_image, kid_rect)
            screen.blit(goal_image, goalP_rect) 
            screen.blit(goal_image, goalK_rect)
        #---------------------------------------------------------------
        # Update the display and cap frame rate
        pygame.display.flip()
        clock.tick(FPS)
        draw()
game_loop()

# Quit Pygame
pygame.quit()