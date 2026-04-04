import pygame
import os
import random

#---------------------
# Bubble Objects
#---------------------
class BubbleObject:
    class Bubbles:
        def __init__(self, x, y): #defines bubble properties
            self.visibility = 255 #--> Bubbles starts off fully opaque
            self.image = pygame.image.load(os.path.join("ProjectImages", "bubble.png")).convert_alpha() #--> transparent images
            self.image = pygame.transform.smoothscale(self.image, (180, 180)) #--> Image dimensions (x,y)
            
            # Setting image alpha (transparency) for regular bubbles
            self.image.set_alpha(200) 

            # Defining variables for movement, speed & type detection
            self.rect = self.image.get_rect(topleft=(x,y))
            self.speed = random.uniform(0.75, 2) #--> Random verticle speed for each bubble
            self.turn = 0 #--> Detecting Regular Bubbles            
            self.sway = random.uniform(-1, 1) #--> Initializing sway variable for horizontal movement

        
        def Move(self):
            # Bubble movement
            self.rect.x += self.sway
            self.rect.y -= self.speed # decrease y to go up
            # Adding Sway
            if random.random() < 0.01: #--> changing swaying movement every 0.03 seconds (randomly)
                self.sway = random.uniform(-1.5, 1.5)
                
            # Teleporting bubbles to bottom
            if self.rect.y < -120:
                self.rect.y = random.randint(480, 900) #--> coord randomized within range
                self.rect.x = random.randint(0, 450) #--> coord randomized within range
        
            """
            # Adding transparency effect to regular bubbles
            self.visibility -= 1
            if self.visibility < 0:
                self.visibility = 0
            self.image.set_alpha(self.visibility)
            """

    class SpecialBubbles:
        def __init__(self, x, y): #defines location of bubble
            self.image = pygame.image.load(os.path.join("ProjectImages", "special_bubble.png")).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (180, 180)) #--> Image dimensions (x,y)
            
            self.rect = self.image.get_rect(topleft=(x,y))
            self.speed = random.uniform(0.2, 1) #--> Random speed for each bubble
            self.turn = 1 # detecting Special Bubbles

            self.sway = random.uniform(-1, 0.5) #--> Initializing sway variable for horizontal movement (- to + controls VIBRATION)
            #self.turn = 1 #--> Initializing turn to SWITCH between Special Bubble (0)
            self.visibility = None #--> Bubbles starts off fully opaque
        
        def Move(self):
            # Special bubble movement
            self.rect.x += self.sway
            self.rect.y -= self.speed 

             # Adding Sway
            if random.random() < 0.01:
                self.sway = random.uniform(-1.5, 1.5)

            # Teleporting bubbles to bottom
            if self.rect.y < -120:
                self.rect.y = random.randint(480, 900) #-->
                self.rect.x = random.randint(0, 450)
#>>---------------------------------
# INIT
#>>---------------------------------
class Game:
    def __init__(self):
       pygame.init()
       # Creating Game window
       WIDTH, HEIGHT = 900, 500
       self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
       self.FPS = 60
       pygame.display.set_caption("Game 3: Bubbles")
       self.clock = pygame.time.Clock()
       
       # Background image
       self.background = pygame.image.load(os.path.join("ProjectImages", "OpenBG.jpg"))
       self.background = pygame.transform.smoothscale(self.background, (WIDTH, HEIGHT)) #--> Image dimensions (x,y)
       # Bubble images
       self.bubbles = []
       self.spawn_bubbles() #--> not a function yet
           
       self.running = True #--> keeps game Loop running

    #-----------------------------------
    # SPAWN BUBBLES LOGIC
    #-----------------------------------
    def spawn_bubbles(self):
            for _ in range(15):
                x = random.randint(150, 450)
                y = random.randint(500, 900)
                # Randomly choose bubble type
                if random.randint(0, 4) == 1: #--> expanding range changes percentage rate of Special bubbles spawning
                    b = BubbleObject.SpecialBubbles(x, y) #--> 1/5 numbers = 20% appearance rate (0,1,2,3,4)
                else:
                    b = BubbleObject.Bubbles(x, y)
                self.bubbles.append(b)
#>>---------------------------------
# UPDATE
#>>---------------------------------
    # Mouse click events
    def Update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
                return
        # Mouse click events: "Pop" bubbles upon click 
            # MOUSEBUTTONUP not needed bc bubbles pop immediately
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for b in self.bubbles:
                    if b.rect.collidepoint(mouse_pos):
                        if b.turn == 1: # Popping special bubbles ONLY
                            b.rect.y = random.randint(500, 900)
                            b.rect.x = random.randint(200, 450)
#>>---------------------------------
# DRAW: all images
#>>---------------------------------
    def Draw(self):
        # 1. Drawing background - FIRST
        self.screen.blit(self.background, (0,0)) 
        # 2. Drawing Bubbles (Regular & Special)
        for b in self.bubbles:
            b.Move() #--> Move function for each bubble
            self.screen.blit(b.image, b.rect)
        # 3. Updating display & setting FPS - LAST
        pygame.display.update()
        self.clock.tick(self.FPS)

#>>---------------------------------
# MAIN GAME LOOP: run logic
#>>---------------------------------
    def MainLoop(self):
        while self.running:
            self.Update()
            self.Draw()

#>>-----------<<#
def main():
    game = Game()
    game.MainLoop()

if __name__ == "__main__":
    main()
pygame.quit()
