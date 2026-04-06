from Games.Race import run
import pygame


def page2():
    pygame.init()
    screen = pygame.display.set_mode((1000, 680))
    pygame.display.set_caption("PAGE 2")

    # --- Load images ---
    img_page1 = pygame.image.load("ProjectImages/back_button.png")
    img_page3 = pygame.image.load("ProjectImages/next_button.png")

    # Resize if needed
    img_page1 = pygame.transform.smoothscale(img_page1, (130, 50))
    img_page3 = pygame.transform.smoothscale(img_page3, (130, 50))

   # Creating Rects for Clicking events
    rect_page1 = img_page1.get_rect(topleft=(50, 80))
    rect_page3 = img_page3.get_rect(topleft=(220, 80))

    running = True
    while running:
        screen.fill((30, 30, 30))

        # Draw image buttons
        screen.blit(img_page1, rect_page1)
        screen.blit(img_page3, rect_page3)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_page1.collidepoint(event.pos):
                    pygame.quit()
                    return "page1"

                if rect_page3.collidepoint(event.pos):
                    pygame.quit()
                    return "page3"



