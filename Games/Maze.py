import pygame
import os

#-----------------------------------------
# Maze Game Class (modular like Bubbles)
#-----------------------------------------
class MazeGame:
    def __init__(self):
        pygame.init()

        # Window
        self.WIDTH, self.HEIGHT = 650, 450
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Game 4: Maze")
        self.clock = pygame.time.Clock()

        # Background
        self.background = pygame.image.load(os.path.join("ProjectImages", "livingroom.jpg"))
        self.background = pygame.transform.smoothscale(self.background, (self.WIDTH, self.HEIGHT))

        # Player sprites
        self.player_Right = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("ProjectImages", "arrow_R.png")), (35, 35)
        )
        self.player_Left = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("ProjectImages", "arrow_L.png")), (35, 35)
        )
        self.player_Up = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("ProjectImages", "arrow_U.png")), (35, 35)
        )
        self.player_Down = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("ProjectImages", "arrow_D.png")), (35, 35)
        )

        self.player_current = self.player_Right
        self.player_speed = 6
        self.p_rect = pygame.Rect(10, self.HEIGHT - 195, 25, 25)  #--> player collision rect size

        # Movement
        self.dx = 0
        self.dy = 0

        # -----------------------------
        # TOYS
        # -----------------------------
        toy_folder = os.path.join("ProjectImages", "ToysImages")
        toy_files = [
            "bluebunny_toy.png",
            "bookbear_toy.png",
            "pinkbear_toy.png",
            "star_toy.png"
        ]

        self.wc_images = [
            pygame.transform.smoothscale(
                pygame.image.load(os.path.join(toy_folder, file)), (50, 50)
            )
            for file in toy_files
        ]

        self.wc_rects = [
            pygame.Rect(40, 140, 50, 50),
            pygame.Rect(350, 240, 50, 50),
            pygame.Rect(150, 370, 50, 50),
            pygame.Rect(550, 67, 50, 50),
        ]
        self.wc_visible = [True, True, True, True]

        # Assign each collectible a fixed toy image
        self.collectibles = [
            (self.wc_images[0], self.wc_rects[0]),
            (self.wc_images[1], self.wc_rects[1]),
            (self.wc_images[2], self.wc_rects[2]),
            (self.wc_images[3], self.wc_rects[3])
        ]

        # -----------------------------
        # EXIT STAR
        # -----------------------------
        self.eStar = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("ProjectImages", "exit_star.png")), (40, 40)
        )
        self.eStar_rect = self.eStar.get_rect(topleft=(580, 30))
        self.eStar_visible = False

        # -----------------------------
        # OBSTACLES
        # -----------------------------
        self.obstacles = self.create_obstacles()

        # Game running flag
        self.running = True

    # Ending screen:
    def show_message(self, text_string, duration=2000):
        font = pygame.font.SysFont('Arial', 50)
        # Render the text
        text_surface = font.render(text_string, True, (255, 255, 255))  #--> green text

        # Center the text on the screen
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))

        # Draw the final frame (background + toys + obstacles)
        self.screen.blit(self.background, (0, 0))

        for (img, rect), visible in zip(self.collectibles, self.wc_visible):
            if visible:
                self.screen.blit(img, rect)

        for obs_img, rect in self.obstacles:
            self.screen.blit(obs_img, rect)

        # Draw the message centered
        self.screen.blit(text_surface, text_rect)

        pygame.display.update()
        pygame.time.delay(duration)

    #-----------------------------------------
    # Create obstacles
    #-----------------------------------------
    def create_obstacles(self):

        # Load all toy images once
        self.toy_folder = os.path.join("ProjectImages", "ToysImages")
        self.toy_files = [
            "bluebunny_toy.png",
            "bookbear_toy.png",
            "pinkbear_toy.png",
            "star_toy.png"
        ]

        self.toy_images = [
            pygame.transform.smoothscale(
                pygame.image.load(os.path.join(self.toy_folder, file)), (45, 45)
            )
            for file in self.toy_files
        ]

        # coordinates for obstacles (not super challenging tbh)
        coords = [
            # TOP (keeps exit star reachable)
            (90, 40), (230, 45), (360, 50), (500, 40),

            # UPPER MIDDLE
            (140, 110), (260, 120), (380, 115), (480, 130),

            # NEAR EXIT STAR
            (520, 90), (560, 140),

            # MIDDLE
            (80, 200), (160, 220), (240, 200),
            (320, 220), (400, 200), (480, 220),

            # MIDDLE (near toy #2)
            (300, 260), (360, 300), (420, 260),

            # MIDDLE (near toy #3)
            (100, 300), (160, 340), (220, 310),

            # BOTTOM
            (450, 320), (520, 360),
            (200, 380), (320, 390), (460, 380)
        ]

        obs_img = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("ProjectImages", "obstacle.png")), (30, 30)
        )

        obstacles = []
        for x, y in coords:
            rect = obs_img.get_rect(topleft=(x, y))
            obstacles.append((obs_img, rect))

        return obstacles

    #-----------------------------------------
    # Update logic (events + movement)
    #-----------------------------------------
    def Update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_LEFT:
                    self.dx = -self.player_speed
                    self.player_current = self.player_Left
                if event.key == pygame.K_RIGHT:
                    self.dx = self.player_speed
                    self.player_current = self.player_Right
                if event.key == pygame.K_UP:
                    self.dy = -self.player_speed
                    self.player_current = self.player_Up
                if event.key == pygame.K_DOWN:
                    self.dy = self.player_speed
                    self.player_current = self.player_Down

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.dx = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    self.dy = 0

        # Move player
        self.p_rect.x += self.dx
        self.p_rect.y += self.dy

        # Border collision
        self.p_rect.left = max(self.p_rect.left, 6)
        self.p_rect.top = max(self.p_rect.top, 7)
        self.p_rect.bottom = min(self.p_rect.bottom, self.HEIGHT - 6)
        self.p_rect.right = min(self.p_rect.right, self.WIDTH - 7)

        # Circle collision
        for i, rect in enumerate(self.wc_rects):
            if self.wc_visible[i] and self.p_rect.colliderect(rect):
                self.wc_visible[i] = False

        # Star appears when all circles collected
        if all(not v for v in self.wc_visible):
            self.eStar_visible = True

        # Win condition
        if self.eStar_visible and self.p_rect.colliderect(self.eStar_rect):
            print("You completed the maze!")
            self.running = False

        # Obstacle collision
        for obs_img, rect in self.obstacles:
            if self.p_rect.colliderect(rect):
                self.p_rect.x -= self.dx
                self.p_rect.y -= self.dy

    #-----------------------------------------
    # Draw everything
    #-----------------------------------------
    def Draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player_current, self.p_rect)

        # Drawing Toys (each collectible keeps its own image)
        for (img, rect), visible in zip(self.collectibles, self.wc_visible):
            if visible:
                self.screen.blit(img, rect)

        # Obstacles
        for obs_img, rect in self.obstacles:
            self.screen.blit(obs_img, rect)

        # Exit star
        if self.eStar_visible:
            self.screen.blit(self.eStar, self.eStar_rect)

        pygame.display.flip()
        self.clock.tick(self.FPS)

    #-----------------------------------------
    # Main loop
    #-----------------------------------------
    def MainLoop(self):
        while self.running:
            self.Update()
            self.Draw()


#-----------------------------------------
# run() wrapper
#-----------------------------------------
def run():
    game = MazeGame()
    game.MainLoop()
    return

if __name__ == "__main__":
    run()
