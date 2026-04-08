from Games.Race import RaceGame

import pygame


def page3():
    pygame.init()
    
    WIDTH, HEIGHT = 1000, 680
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PAGE 3 - RACE")

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
                    # Create screen + clock for the game
                    WIDTH, HEIGHT = 990, 550
                    FPS = 60
                    game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    game_clock = pygame.time.Clock()

                    # Create and run the RaceGame
                    game = RaceGame(game_screen, WIDTH, HEIGHT, FPS, game_clock)
                    game.countdown(3)
                    game.game_loop()

                    # After the race ends, return to page3

                    # need screen again because Race.py has different window dimensions than MainStory.py
                    screen = pygame.display.set_mode((1000, 680))
                    pygame.display.set_caption("PAGE 3 - RACE")

                    return "page3"

if __name__ == "__main__":
    page3()