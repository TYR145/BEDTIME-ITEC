# Adding floating bubbles to the screen

import pygame
import os
import random

class GameObjects:
    class Bubbles:
        def __init__(self, x, y): #defines location of bubble
            self.image = pygame.image.load(os.path.join("ProjectImages", "bubble.png"))
            self.image = pygame.transform.smoothscale(self.image, (180, 180)) #--> Image dimensions (x,y)
            self.rect = self.image.get_rect(topleft=(x,y))
            self.speed = random.uniform(0.5, 1) #--> Random speed for each bubble
            self.sway = random.uniform(-1, 1) #--> Initializing sway variable for horizontal movement
            self.turn = 0 #--> Initializing turn to SWITCH between Regular Bubble (1)
            self.visibility = None #--> Bubbles starts off fully opaque

    # --> THESE WILL BE CLICKABLE INSTEAD
    class SpecialBubbles:
        def __init__(self, x, y): #defines location of bubble
            self.image = pygame.image.load(os.path.join("ProjectImages", "special_bubble.png"))
            self.image = pygame.transform.smoothscale(self.image, (180, 180)) #--> Image dimensions (x,y)
            self.rect = self.image.get_rect(topleft=(x,y))
            self.speed = random.uniform(0.2, 1) #--> Random speed for each bubble
            self.sway = random.uniform(-1, 0.5) #--> Initializing sway variable for horizontal movement (- to + controls VIBRATION)
            self.turn = 1 #--> Initializing turn to SWITCH between Special Bubble (0)
            self.visibility = None #--> Bubbles starts off fully opaque

class Game:
    def run(self):
        global screen, clock, background, bubble, special_bubble, end, FPS
        # OBJECTS (List, Global variables, etc.)

        # Global variables
        screen = None
        clock = None
        background = None
        bubble = None
        special_bubble = None
        end = None
        FPS = None


        # List --> adding bubbles to a list to easily manage them
        bubbles = []

        #-------------------------------------------------------#
        #   INITIALIZATION: Defining variables & Adding Images  #
        #-------------------------------------------------------#
        def init():
            global screen, clock, background, bubble, special_bubble, x, y, end, FPS, i
            pygame.init()

            # Creating game window & clock
            WIDTH, HEIGHT = 750, 480
            FPS = 60
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Bubbles Clicking - TESTING")
            clock = pygame.time.Clock()

            # Define game variables
            # Background Image
            background = pygame.image.load(os.path.join("ProjectImages", "OpenBG.jpg"))
            background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

            # Bubble Images (regular & special)
            bubble = pygame.image.load(os.path.join("ProjectImages", "bubble.png"))
            bubble = pygame.transform.smoothscale(bubble, (110, 110)) #--> Image dimensions (x,y)

            special_bubble = pygame.image.load(os.path.join("ProjectImages", "special_bubble.png"))
            special_bubble = pygame.transform.smoothscale(special_bubble, (110, 110)) #--> Image dimensions (x,y)

            # Adding bubbles movement
            for i in range(15): #--> Adding (number) of bubbles to the list
                x = random.randint(200, 450) #--> spawning bubbles within screen bounds
                y = random.randint(500, 900)
                b = GameObjects.Bubbles(x, y) #--> assigning b to the properties assigned in the CLASS "Bubbles"
                b.turn = random.randint(0,1) #--> Random switch between regular and special bubble images (0 for regular, 1 for special)
                bubbles.append(b)


        #-------------------------------------------------------#
        #   UPDATE: Changing variables & Adding movements       #
        #-------------------------------------------------------#
        def update():
            global screen, clock, background, bubble, special_bubble, x, y, end, FPS, i
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                # Change to --> Popping Special_Bubbles (ONLY)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos() #--> get_pos() for tracking the POSITION of mouse (x,y)
                    for b in bubbles[:]:
                        if b.rect.collidepoint(mouse_pos): #--> click on bubbles teleports them to the bottom again
                            b.rect.y = random.randint(500, 900)
                            b.rect.x = random.randint(200, 450)
                """
                If changed to special bubbles only, use .remove() for the special_bubbles
                """

            # Adding movement to the bubbles --> each one individually
            for b in bubbles: #--> spawning (number) of bubbles
                b.rect.y -= b.speed
                b.rect.x += b.sway #--> Adding horizontal sway movement to the bubbles
                
                # TOP BORDER --> teleports bubbles to bottom
                if b.rect.y < -120:
                    b.rect.y = random.randint(480, 900) #--> randomly spawning bubbles at bottom of the screen
                    b.rect.x = random.randint(0, 450) #--> ensuring bubble is within screen bounds
                if random.random() < 0.01: #--> changing swaying movement every 0.03 seconds (randomly)
                    b.sway = random.uniform(-1.5, 1.5)

                """
                # Changing between images
                bubbles[b].turn = 1- bubbles[b].turn #--> toggles between bubble (0) & special_bubble images (1)
                if (bubbles[b].turn == 0):
                    bubbles[b].image = bubble
                else:
                    bubbles[b].image = special_bubble
                """
        #-----------------------------#
        #   DRAW: Drawing all images  #
        #-----------------------------#
        def draw():
            global screen, clock, background, bubble, special_bubble, bubble_speed, end, FPS

            # 1. Draw background
            screen.blit(background, (0, 0))
            # 2. Draw bubbles (using objects directly from the list)
            for b in bubbles:
                screen.blit(b.image, b.rect)
            
            # 3. Update display & set FPS
            pygame.display.flip()
            clock.tick(FPS)


        #-------------------------------------------------------#
        #   MAIN GAME LOOP: Calling functions & Drawing        #
        #-------------------------------------------------------#
        def MainLoop():
            global end

            end = False
            while not end:
                update() # --> Calling the update function FROM the CLASS called Update
                draw()


        # Run the game
        init() #--> Calling the init function FROM the CLASS called Initialization
        MainLoop()

        # Quit Pygame
        pygame.quit()

#>>-----------------------------------<<
if __name__ == "__main__":
    game = Game() #--> creating Game() object & assigning it to "game"
    game.run() #--> running methods & properties in class called "Game()"