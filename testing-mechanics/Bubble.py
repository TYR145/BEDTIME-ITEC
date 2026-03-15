import pygame
import os

def run():

    pygame.init()

    global WIDTH, HEIGHT, FPS, screen, clock, bubble, BLUE, WHITE

    # SCREEN DIMENSIONSss
    WIDTH, HEIGHT = 650, 450
    FPS = 60 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bubble Clicks - BETA")
    clock = pygame.time.Clock()

    # COLOURS
    BLUE = (0, 0, 0)
    WHITE = (255, 255, 255)


    # ===========================================================
    #      ADDING IMAGES --- ADD IMAGE RECT FOR BORDER COLLISION
    # ===========================================================

    # Adding BG Images
    background = pygame.image.load(os.path.join("ProjectImages", "OpenBG.jpg"))
    background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))


    # OBJECTS:
    class Bubble: # Defining Bubble properties
        
        def __init__(self, x, y): #defines location of bubble
            self.image = pygame.image.load(os.path.join("ProjectImages", "bubble.png"))
            self.image = pygame.transform.smoothscale(self.image, (60, 60)) #--> Image dimensions (x,y)
            self.rect = self.image.get_rect(topleft=(x,y))
            self.speed = 3
            self.visibility = 255 #--> Bubbles starts fully opaque

    # List of Bubbles
    def create_bubbles():
        return [
            Bubble(100, 100),
            Bubble(300, 200),
            Bubble(500, 300)
        ]
    global bubbles
    bubbles = create_bubbles()

    # ===========================================================
    #      GAME LOGIC --- ()
    # ===========================================================
    global end, running
    end = False
    running = True

    # TEMPORARY CODE TO LOAD WINDOW
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)


    # ======================
    #      DRAWING
    # ======================

    screen.blit(background, (0, 0))
    pygame.quit()

if __name__ == "__main__":
    run()