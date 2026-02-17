def Collecting_Game():
    end = False
    
    import pygame
    import sys
    import os
    pygame.font.init() #--> imports the timer font

    pygame.init()

    #Estalish screen WIDTH & HEIGHT
    WIDTH, HEIGHT = (600, 400)
    FPS = 60 #--> Smoother movement
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Emoji Game Jam")
    clock = pygame.time.Clock()

    #While game condition !!!!


    #Defining colours 
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #Defining Objects
    bg_image = pygame.image.load(os.path.join("images", "testbg.webp"))
    player_image = pygame.image.load(os.path.join("images","emoji1.png"))

    #Tracking for emoji's visible
    emoji1_visible = True
    emoji2_visible = True
    emoji3_visible = True

    # Load and scale background image & reload the background
    background = pygame.image.load(os.path.join("images","testbg.webp")) #--> loads an image instead of a rectangle
    background = pygame.transform.scale(background, (WIDTH, HEIGHT)) #--> Refreshes the background

    # player image
    player_image = pygame.image.load(os.path.join("images","Steve.png"))
    player_image = pygame.transform.scale(player_image, (64, 64))


    # emoji images
    emoji1_image = pygame.image.load(os.path.join("images","emoji1.png"))
    emoji2_image = pygame.image.load(os.path.join("images","emoji2.png"))
    emoji3_image = pygame.image.load(os.path.join("images","emoji3.png"))

    #GameOver image
    GameOver_image = pygame.image.load(os.path.join("images","GameOver.png"))
    GameOver_image = pygame.transform.scale(GameOver_image, (WIDTH, HEIGHT))

    # player location and speed
    player_x = WIDTH // 2
    player_y = HEIGHT // 2
    player_speed = 4

    #Creating object rects
    emoji_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 30, 30)

    # Incrementing the score counter
    score = 0
    score_increment = 100

    def EmojisCollected():
        return (not emoji1_visible and not emoji2_visible and not emoji3_visible)

    def GameOver_screen():
        screen.blit(GameOver_image, (0, 0))
        pygame.display.flip()

    game_over = False
    end = False


    #movement variables
    player_dx = 0 #--> "difference in X" (starts @ 0 bc it's not moving at first)
    player_dy = 0 #--> "difference in Y"

    #Movement Keys  - LUWI (NEW)
    moveleft = True
    moveup = True
    movedown = True
    moveright = True

    while not end:
        # A. Event handling: Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

        # start movement on key press (moves by 1 space)
        if event.type == pygame.KEYDOWN:
                # EXIT KEY
            if event.key == pygame.K_ESCAPE: 
                end = True
                
            # arrow keys
            if event.key == pygame.K_LEFT and moveleft == True:
                player_dx = -player_speed #-->dx is CHANGING (-speed to go LEFT)
            if event.key == pygame.K_RIGHT and moveright == True: #-->dx is CHANGING (+speed to go RIGHT)
                player_dx = player_speed
            if event.key == pygame.K_UP and moveup == True:
                player_dy = -player_speed #--> (-y is GOING UP)
            if event.key == pygame.K_DOWN and movedown == True: #--> (+y is GOING DOWN)
                player_dy = player_speed

            # end movement on key release
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_dx = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player_dy = 0

        if game_over:
            GameOver_screen()
            # Skip game logic, but DO NOT skip event handling
            pygame.display.flip()
            clock.tick(FPS)
            continue

    #to check if player exists boundaries
        if player_x <= 0:
            moveleft = False
            player_x = 10
        elif player_x >= 0: moveleft = True

        if player_y <= 0:
            moveup = False
            player_y = 10
        elif player_y >= 0: moveup = True

        if player_y >= 400:
            movedown = False
            player_y = 290
        elif player_y <= 400: movedown = True

        if player_x >= 500:
            moveright = False
            player_x = 440
        elif player_x <= 500: moveright = True




        # B. Game logic: Update player position based on input
        player_x += player_dx 
        player_y += player_dy

        p_rec = pygame.Rect(player_x, player_y, player_image.get_width(),player_image.get_height())
        e1_rect = pygame.Rect(180,40, emoji1_image.get_width(),emoji1_image.get_height())
        e2_rect = pygame.Rect(425,147, emoji2_image.get_width(),emoji2_image.get_height())
        e3_rect = pygame.Rect(43, 28, emoji3_image.get_width(),emoji3_image.get_height())

    #==============================================================
    #Score updating - emoji 1
        if p_rec.colliderect(e1_rect) and emoji1_visible==True:
            emoji1_visible = False
            score += score_increment
        

    #make a rectangle for our images w/ same width and height and X ,Y
        if p_rec.colliderect(e2_rect) and emoji2_visible==True:
            emoji2_visible = False
            score += score_increment

        if p_rec.colliderect(e3_rect) and emoji3_visible==True:
            emoji3_visible = False
            score += score_increment
    #===============================================================
        if EmojisCollected():
            game_over = True


        screen.blit(background, (0, 0))  # draw background Image ("Block Image Transfer" = blit)
        # B. draw player
        screen.blit(player_image, (player_x, player_y))  # draw player
        if emoji1_visible == True:
            screen.blit(emoji1_image, (180,40))
        if emoji2_visible == True:
            screen.blit(emoji2_image, (425, 147))
        if emoji3_visible == True:
            screen.blit(emoji3_image, (43, 28))
            #end = True --> Put inside a while loop?

        #Score font to be visible
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)



    # Quit Pygame
    pygame.quit()

Collecting_Game()