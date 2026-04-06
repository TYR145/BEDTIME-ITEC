import pygame
from Games.Bubbles import run

def page4():
    pygame.init()
    screen = pygame.display.set_mode((1000, 680))
    pygame.display.set_caption("PAGE 4")

    # --- Load images ---
    img_back = pygame.image.load("ProjectImages/back_button.png")
    img_next = pygame.image.load("ProjectImages/next_button.png")
    img_play = pygame.image.load("ProjectImages/play_button.png")

    # Resize
    img_back = pygame.transform.smoothscale(img_back, (130, 50))
    img_next = pygame.transform.smoothscale(img_next, (130, 50))
    img_play = pygame.transform.smoothscale(img_play, (130, 50))

    # Positions (matching Page 2 & 3 layout)
    rect_back = img_back.get_rect(topleft=(50, 80))
    rect_next = img_next.get_rect(topleft=(220, 80))
    rect_play = img_play.get_rect(topleft=(135, 20))  # centered

    running = True
    while running:
        screen.fill((30, 30, 30))

        # Draw buttons
        screen.blit(img_back, rect_back)
        screen.blit(img_next, rect_next)
        screen.blit(img_play, rect_play)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Back button → Page 3
                if rect_back.collidepoint(event.pos):
                    pygame.display.quit()
                    return "page3"

                # Next button → Page 5
                if rect_next.collidepoint(event.pos):
                    pygame.display.quit()
                    return "page5"

                # Play Bubbles game
                if rect_play.collidepoint(event.pos):
                    pygame.display.quit()   # close menu window
                    run()                   # launch game
                    return "page4"          # reopen Page 4 after game ends
