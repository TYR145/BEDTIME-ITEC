import pygame
from Games.Bubbles import run

def page3():
    pygame.init()
    
    WIDTH, HEIGHT = 1000, 680
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PAGE 3 - Bubbles")

    # Loading game instructions
    instructions = pygame.image.load("ProjectImages/bubbles_instructions.png")
    instructions = pygame.transform.smoothscale(instructions, (WIDTH, HEIGHT))

    # Resize -- instructions
    instructions = pygame.transform.smoothscale(instructions, (WIDTH, HEIGHT))  

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
        screen.blit(instructions, (0, 0)) #--> drawing instructions image
        screen.blit(img_back, rect_back)
        screen.blit(img_next, rect_next)
        screen.blit(img_game, rect_game)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Back button
                if rect_back.collidepoint(event.pos):
                    return "page2"

                # Next button
                if rect_next.collidepoint(event.pos):
                    return "page4"

                # Play Game button
                if rect_game.collidepoint(event.pos):
                    run()

                    # need screen again because Race.py has different window dimensions than MainStory.py
                    screen = pygame.display.set_mode((1000, 680))
                    pygame.display.set_caption("PAGE 3 - Bubbles")

                    return "page3"

if __name__ == "__main__":
    page3()