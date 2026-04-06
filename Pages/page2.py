from Games.Race import run
import pygame


def page2():
    pygame.init()
    
    # Define WIDTH & HEIGHT
    WIDTH, HEIGHT = 1000, 680
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PAGE 2")

    # Define & Load images
    img_page1 = pygame.image.load("ProjectImages/back_button.png")
    img_page3 = pygame.image.load("ProjectImages/next_button.png")

    # Resize Buttons
    img_page1 = pygame.transform.smoothscale(img_page1, (130, 50))
    img_page3 = pygame.transform.smoothscale(img_page3, (130, 50))
    
    # Creating Rects for Clicking events & Positioning Buttons
    rect_page1 = img_page1.get_rect(bottomleft=(20, HEIGHT - 20))
    rect_page3 = img_page3.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20))


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



