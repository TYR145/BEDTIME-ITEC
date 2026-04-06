from Games.Race import run
import pygame

def page3():
    pygame.init()
    WIDTH, HEIGHT = 1000, 680
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PAGE 3")

    # Load images
    img_back = pygame.image.load("ProjectImages/back_button.png")
    img_next = pygame.image.load("ProjectImages/next_button.png")
    img_game = pygame.image.load("ProjectImages/play_button.png")

    # Resize
    img_back = pygame.transform.smoothscale(img_back, (130, 50))
    img_next = pygame.transform.smoothscale(img_next, (130, 50))
    img_game = pygame.transform.smoothscale(img_game, (130, 50))

    # Positions
    rect_back = img_back.get_rect(bottomleft=(20, HEIGHT - 20)) #(topleft=(50, 80))
    rect_next = img_next.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20)) #(topleft=(220, 80))
    rect_game = img_game.get_rect(topleft=(425, 610))  # centered

    running = True
    while running:
        screen.fill((30, 30, 30))

        screen.blit(img_back, rect_back)
        screen.blit(img_next, rect_next)
        screen.blit(img_game, rect_game)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Back button
                if rect_back.collidepoint(event.pos):
                    pygame.display.quit()
                    return "page2"

                # Next button
                if rect_next.collidepoint(event.pos):
                    pygame.display.quit()
                    return "page4"

                # Game button
                if rect_game.collidepoint(event.pos):
                    pygame.display.quit()   # close page window
                    run()                   # launch the game
                    return "page3"          # reopen this page after game ends
