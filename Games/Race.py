from cmath import rect
from pydoc import text

import pygame
import os
import time
#-------------------------------------------------------------------
# INIT(IALIZE)
#-------------------------------------------------------------------
def run():

    pygame.init()

    # SCREEN DIMENSIONSss
    WIDTH, HEIGHT = 990, 550
    FPS = 60 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Race Mechanics - BETA")
    clock = pygame.time.Clock()

    # ===========================================================
    #      ADDING IMAGES --- ADD IMAGE RECT FOR BORDER COLLISION
    # ===========================================================

    def player():
        # Defining Player
        player_image = pygame.image.load(os.path.join("ProjectImages","arrow_R.png"))
        player_image = pygame.transform.smoothscale(player_image, (55, 55))

        # Player's location and speed
        player_x = 15           # Spawnpoint
        player_y = HEIGHT - 320 # Spawnpoint
        player_speed = 2.5
        # Player Rect --> needed for border collision
        p_rect = pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())

        return player_image, player_x, player_y, player_speed, p_rect
    # CALL BACK FUNCTION --> include values defined
    player_image, player_x, player_y, player_speed, p_rect = player()

    def kid():
        # Defining Kid
        kid_image = pygame.image.load(os.path.join("ProjectImages", "kid_img.png"))
        kid_image = pygame.transform.smoothscale(kid_image, (95,95))

        # Kid's speed
        kid_speed = 2

        # Kid Rect ---> (x, y, kid)
        kid_rect = pygame.Rect(0, HEIGHT - 150, kid_image.get_width(), kid_image.get_height())

        return kid_image, kid_speed, kid_rect
    kid_image, kid_speed, kid_rect = kid()

    def assets():
        # Adding BG Images
        background = pygame.image.load(os.path.join("ProjectImages", "race_bg.jpg"))
        background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))
        #----------------------------------------------------------------------
        # Goal
        goal_image = pygame.image.load(os.path.join("ProjectImages", "race_flag.png"))
        goal_image = pygame.transform.smoothscale(goal_image, (90, 90))
        # Player's Lane
        goalP_rect = pygame.Rect(850, player_y, goal_image.get_width(), goal_image.get_height())

        # Kid's Lane
        goalK_rect = pygame.Rect(850, HEIGHT- 150, goal_image.get_width(), goal_image.get_height())

        # Border Line Image
        Borderline_image = pygame.image.load(os.path.join("ProjectImages", "borderline.png"))
        Borderline_image = pygame.transform.smoothscale(Borderline_image, (960, 40))
        # Positioning Border Line in center
        Border_y = HEIGHT - 200
        Borderline_rect = pygame.Rect(0, Border_y, 960, 40)
        return background, goal_image, goalP_rect, goalK_rect, Borderline_image, Borderline_rect 
    background, goal_image, goalP_rect, goalK_rect, Borderline_image, Borderline_rect = assets()

    #Race obstacles
    def create_obstacles():
        obstacles = []
        obs_image = pygame.image.load(os.path.join("ProjectImages", "obstacle.png"))
        obs_image = pygame.transform.smoothscale(obs_image, (65,120))

        obs_coords = [
            (150, 70),
            (300, 240),
            (450, 70),
            (600, 240),
            (750, 70)
        ]

        for x,y in obs_coords:
            rect = obs_image.get_rect(topleft = (x,y))
            obstacles.append((obs_image, rect))
        return obstacles
    obstacles = create_obstacles()

    # ----------------------------------------------------------------------
    # Adding COUNTDOWN TIMER --> Runs BEFORE the game loop starts
    def countdown(seconds): 
        font = pygame.font.SysFont('Arial', 150) #--> font style & size
        for i in range(seconds, 0, -1):
            # Drawing bg
            screen.fill((0, 0, 0)) #--> fill background with black before drawing text
            screen.blit(background, (0, 0))

            # Draw obstacles
            for obs_image, rect in obstacles:
                screen.blit(obs_image, rect)

            # Draw player + kid + goals + border
            screen.blit(player_image, p_rect)
            screen.blit(kid_image, kid_rect)
            screen.blit(goal_image, goalP_rect)
            screen.blit(goal_image, goalK_rect)
            screen.blit(Borderline_image, Borderline_rect)

            transparent = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA) #--> Create a transparent surface
            transparent.fill((0, 0, 0, 120))  # RBG & Alpha (transparency level) = 0-255 (opaque to transparent)
            screen.blit(transparent, (0, 0))

            # Drawing the timer text
            text = font.render(str(i), True, (255, 255, 255)) #--> converts string into IMAGE to DRAW & DISPLAY
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2)) #--> centering text on screen
            screen.blit(text, text_rect) #--> draws text on screen at specified location
           
            # Created RECT to tell program where to place the converted image
            pygame.display.update()
            pygame.time.delay(1000)  # Delay for 1 second = 100 ms
    countdown(3) #--> 3 second countdown before game starts

    #-------------------------------------------------------------------------
    end = False
    # Player movement Variables
    player_dx = 0 #--> Direction x
    player_dy = 0 #--> Direction y

    def show_message(text_string, duration):
        font = pygame.font.SysFont('Arial', 150)
       
        # Dark overlay
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))

        # Rendering text
        text = font.render(text_string, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Draw everything
        screen.blit(player_image, p_rect)
        screen.blit(kid_image, kid_rect)
        screen.blit(goal_image, goalP_rect)
        screen.blit(goal_image, goalK_rect)
        screen.blit(Borderline_image, Borderline_rect)
        screen.blit(overlay, (0, 0))
        screen.blit(text, text_rect)

        pygame.display.update()
        pygame.time.delay(duration)

    # =========================================
    #      GAME LOGIC: Updates player position
    # =========================================
    def game_loop():
        nonlocal end, player_dx, player_dy

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

                # Collision with obstacles
                for obs_image, rect in obstacles:
                    if p_rect.colliderect(rect):
                        if player_dx > 0:   # moving right
                            p_rect.right = rect.left
                        elif player_dx < 0: # moving left
                            p_rect.left = rect.right

                p_rect.y += player_dy
                for obs_image, rect in obstacles:
                    if p_rect.colliderect(rect):
                        if player_dy > 0:   # moving down
                            p_rect.bottom = rect.top
                        elif player_dy < 0: # moving up
                            p_rect.top = rect.bottom
            player_collision()

            # BORDERLINE COLLISION
            def border_line_collision():
               if p_rect.colliderect(Borderline_rect):
                    if player_dy > 0:   # moving down
                        p_rect.bottom = Borderline_rect.top
                    elif player_dy < 0: # moving up
                        p_rect.top = Borderline_rect.bottom
            border_line_collision()

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
                nonlocal end
                # Detecting who touches Goal first
                FinishLine_x = 850  # x-position of the goal

                # Player reaches goal
                if p_rect.colliderect(goalP_rect):
                    show_message("You won!", 2000) #--> Calls Back function to show message
                    print("You won the race!")
                    end = True
                    return FinishLine_x, end

                # Kid reaches goal
                if kid_rect.colliderect(goalK_rect):
                    show_message("You lost!", 2000) #--> Calls Back function to show message
                    print("You lost!")
                    end = True
                    return FinishLine_x, end
            goal_detection()  # ← aligned with def (same indent level)
    

            #---------------------------------------------------------------
            def draw():
                # DRAW
                screen.blit(background, (0, 0))
                
                screen.blit(Borderline_image, Borderline_rect)
                screen.blit(player_image, p_rect)
                screen.blit(kid_image, kid_rect)
                screen.blit(goal_image, goalP_rect) 
                screen.blit(goal_image, goalK_rect)

                # Drawing obstacles
                for obs_image, rect in obstacles:
                    screen.blit(obs_image, rect)
            #---------------------------------------------------------------
            # Update the display and cap frame rate
            pygame.display.flip()
            clock.tick(FPS)
            draw()
    game_loop()

    # Quit Pygame
    pygame.quit()
if __name__ == "__main__":
    run()