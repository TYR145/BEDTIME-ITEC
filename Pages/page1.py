import pygame


def page1():
    #pygame.init()
    screen = pygame.display.set_mode((1000, 680))
    pygame.display.set_caption("PAGE 1 - HOME")

    # Home background image - HOME PAGE
    home_img = pygame.image.load("ProjectImages/house_night.jpg")
    home_img = pygame.transform.smoothscale(home_img, (1000, 680)) #--> Image dimensions (x,y)

    # Button Image - "Next"
    img_page2 = pygame.image.load("ProjectImages/play_button.png")
    img_page2 = pygame.transform.smoothscale(img_page2, (200, 100)) #--> Image dimensions (x,y)

    # Creating Button Rects - for Clicking
    rect_page2 = img_page2.get_rect(topleft=(420, 400))

    # WHILE LOOP - keeps page running until user clicks "Next" or closes window
    running = True
    while running:
        # Draw Home Screen Background
        screen.blit(home_img, (0, 0))

        # Draw image buttons
        screen.blit(img_page2, rect_page2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.display.quit()
                return "quit"
            
            # Checks if MOUSEBUTTONDOWN event happens
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_page2.collidepoint(event.pos):
                    #pygame.display.quit()
                    return "page2"
if __name__ == "__main__":
    page1()
