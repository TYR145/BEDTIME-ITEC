import pygame
from Games.Maze import run

def page4():
    #pygame.init()
    WIDTH, HEIGHT = 1000, 680
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PAGE 4 - Maze")

    # Loading game instructions
    instructions = pygame.image.load("ProjectImages/maze_instructions.png")
    instructions = pygame.transform.smoothscale(instructions, (WIDTH, HEIGHT))

    # Resize -- instructions
    instructions = pygame.transform.smoothscale(instructions, (WIDTH, HEIGHT))  


    # Defining images for buttons (Back, Next, Play)
    img_back = pygame.image.load("ProjectImages/back_button.png")
    img_next = pygame.image.load("ProjectImages/next_button.png")
    img_play = pygame.image.load("ProjectImages/play_button.png")

    # Dimensions of buttons (same as Previous Pages)
    img_back = pygame.transform.smoothscale(img_back, (130, 50))
    img_next = pygame.transform.smoothscale(img_next, (130, 50))
    img_play = pygame.transform.smoothscale(img_play, (130, 50))

    # Positions of Buttons (matching Page 2 & 3 layout)
    rect_back = img_back.get_rect(bottomleft=(20, HEIGHT - 20)) #-->"back" button
    rect_next = img_next.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20)) #--> "next" button
    rect_play = img_play.get_rect(topleft=(425, 610))  #--> "play" button (bottom center)

    running = True
    while running:
        screen.blit(instructions, (0, 0)) #--> drawing instructions image
        # Draw buttons
        screen.blit(img_back, rect_back)
        screen.blit(img_next, rect_next)
        screen.blit(img_play, rect_play)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.display.quit()
                return "quit"
            
            # Escape key exits game window
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "page4"

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Back button to Page 3
                if rect_back.collidepoint(event.pos):
                    return "page3"

                # Next button to Page 5
                if rect_next.collidepoint(event.pos):
                    return "page5"

                # Play Game Button
                if rect_play.collidepoint(event.pos):  
                    run()                
                    return "page4"      #-->returns to Page 4 when pygame is completed
if __name__ == "__main__":
    page4()