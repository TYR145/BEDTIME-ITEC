import pygame

def page6():
    
    screen = pygame.display.get_surface()   #get_surface() uses previous window created!
    pygame.display.set_caption("PAGE 6 - END")

    WIDTH, HEIGHT = screen.get_size()


    # Loading game ENDING IMG
    ending_img = pygame.image.load("ProjectImages/ending_img.png")
    ending_img = pygame.transform.smoothscale(ending_img, (WIDTH, HEIGHT))

    # Resize -- ENDING IMG
    ending_img = pygame.transform.smoothscale(ending_img, (WIDTH, HEIGHT))  


    # defining Button IMAGES
    img_back = pygame.image.load("ProjectImages/back_button.png")
    img_next = pygame.image.load("ProjectImages/next_button.png")


    font = pygame.font.SysFont("arial", 50)
    text = font.render("You did it!", True, (255, 255, 255))

    # Scaling the buttons (x,y) DIMENSIONS !!
    img_back = pygame.transform.smoothscale(img_back, (130, 50))
    img_next = pygame.transform.smoothscale(img_next, (130, 50))


    # Button rects to make them clickable
    rect_back = img_back.get_rect(bottomleft=(20, HEIGHT - 20)) #-->"back" button
    rect_next = img_next.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20)) #--> "next" button (back to page 1)

    rect_text = text.get_rect(center=(WIDTH // 2, HEIGHT - 120)) #--> "You did it!" text



    running = True
    while running:
        screen.fill((0, 0, 0)) #--> black background for ending page
        screen.blit(ending_img, (0, 0)) #--> drawing ending image
        # Drawing the buttons
        screen.blit(img_back, rect_back)
        screen.blit(img_next, rect_next)
        screen.blit(text, rect_text)

        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            # ESC key to quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"
                
            # Mouse click events for buttons - BACK BUTTON
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_back.collidepoint(event.pos):
                    return "page4"

                # Mouse click events for buttons - NEXT BUTTON (back to page 1)
                if rect_next.collidepoint(event.pos):
                    return "page1"
                


if __name__ == "__main__":
    page6()