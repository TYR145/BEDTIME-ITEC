# Adding floating bubbles to the screen

import pygame
import os
import random

class Bubbles:
    def __init__(self, x, y): #defines location of bubble
        self.image = pygame.image.load(os.path.join("ProjectImages", "bubble.png"))
        self.image = pygame.transform.smoothscale(self.image, (180, 180)) #--> Image dimensions (x,y)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = random.uniform(0.4, 2) #--> Random speed for each bubble
        self.visibility = 150 #--> Bubbles starts off fully opaque

class SpecialBubbles:
    def __init__(self, x, y): #defines location of bubble
        self.image = pygame.image.load(os.path.join("ProjectImages", "special_bubble.png"))
        self.image = pygame.transform.smoothscale(self.image, (180, 180)) #--> Image dimensions (x,y)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = random.uniform(0.5, 2) #--> Random speed for each bubble
        #self.visibility = 255 #--> Bubbles starts off fully opaque

def run():
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
        #--------------------bubble_speed = 2-----------------------
        
        
        # Background Image
        background = pygame.image.load(os.path.join("ProjectImages", "OpenBG.jpg"))
        background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

        # Bubble Images (regular & special)
        bubble = pygame.image.load(os.path.join("ProjectImages", "bubble.png"))
        bubble = pygame.transform.smoothscale(bubble, (120, 120)) #--> Image dimensions (x,y)

        special_bubble = pygame.image.load(os.path.join("ProjectImages", "special_bubble.png"))
        special_bubble = pygame.transform.smoothscale(special_bubble, (120, 120)) #--> Image dimensions (x,y)

        # Adding bubbles movement
        
        
        for b in range(10): #--> Adding 8 bubbles to the list
            x = random.randint(0, 450) #--> spawning bubbles within screen bounds
            y = random.randint(480, 1000)
            b = Bubbles(x, y) #--> assigning b to the properties assigned in the CLASS "Bubbles"
            #b.turn = random.randint(0,1) #--> Random switch between regular and special bubble images (0 for regular, 1 for special)
            bubbles.append(b)


    #-------------------------------------------------------#
    #   UPDATE: Changing variables & Adding movements       #
    #-------------------------------------------------------#
    def update():
        global screen, clock, background, bubble, special_bubble, x, y, end, FPS, i
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        # Adding movement to the bubbles --> each one individually
        for b in range(10):
            bubbles[b].rect.y -= bubbles[b].speed
            #bubbles[b].rect.x += random.uniform(-0.8, 0.8) #--> uniform() shaking HORI spacing to bubbles
            if bubbles[b].rect.y < -120:
                bubbles[b].rect.y = random.randint(480, 1000) #--> randomly spawning bubbles at bottom of the screen
                bubbles[b].rect.x = random.randint(0, 450) #--> ensuring bubble is within screen bounds

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
if __name__ == "__main__":
    run()