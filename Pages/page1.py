import pygame


def page1():
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("PAGE 2")

    # --- Load images ---
    img_page2 = pygame.image.load("ProjectImages/next_button.png")

    # Resize if needed
    img_page2 = pygame.transform.smoothscale(img_page2, (130, 50))

   # Creating Rects for Clicking events
    rect_page2 = img_page2.get_rect(topleft=(220, 80))

    running = True
    while running:
        screen.fill((30, 30, 30))
        # Draw image buttons
        screen.blit(img_page2, rect_page2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_page2.collidepoint(event.pos):
                    pygame.display.quit()
                    return "page2"

