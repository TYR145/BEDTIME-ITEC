import pygame


def page1():
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("PAGE 1")

    # Button Image - "Next"
    img_page2 = pygame.image.load("ProjectImages/next_button.png")
    img_page2 = pygame.transform.smoothscale(img_page2, (130, 50)) #--> Image dimensions (x,y)

   # Creating Button Rects - for Clicking
    rect_page2 = img_page2.get_rect(topleft=(220, 80))

    # WHILE LOOP - keeps page running until user clicks "Next" or closes window
    running = True
    while running:
        screen.fill((30, 30, 30)) #--> background colour
        
        # Draw image buttons
        screen.blit(img_page2, rect_page2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return "quit"
            
            # Checks if MOUSEBUTTONDOWN event happens
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_page2.collidepoint(event.pos):
                    pygame.display.quit()
                    return "page2"

