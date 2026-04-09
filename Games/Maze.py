import pygame
import os

#-----------------------------------------
# Maze Game Class (modular like Bubbles)
#-----------------------------------------
class MazeGame:
    def __init__(self):
        pygame.init()

        # Window
        self.WIDTH, self.HEIGHT = 1000, 680
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Game 4: Maze")
        self.clock = pygame.time.Clock()

        # Background
        self.background = pygame.image.load(os.path.join("ProjectImages", "background.jpg"))
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
        self.p_rect = pygame.Rect(10, self.HEIGHT - 195, 35, 35)

        # Movement
        self.dx = 0
        self.dy = 0

        # White circles
        wc_img = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("ProjectImages", "w_circle.png")), (30, 30)
        )
        self.wc_img = wc_img

        self.wc_rects = [
            pygame.Rect(40, 140, 30, 30),
            pygame.Rect(350, 240, 30, 30),
            pygame.Rect(150, 370, 30, 30),
            pygame.Rect(550, 67, 30, 30),
        ]
        self.wc_visible = [True, True, True, True]

        # Exit star
        self.eStar = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("ProjectImages", "exit_star.png")), (40, 40)
        )
        self.eStar_rect = self.eStar.get_rect(topleft=(900, 50))
        self.eStar_visible = False

        # Obstacles
        self.obstacles = self.create_obstacles()

        # Game running flag
        self.running = True

    #-----------------------------------------
    # Create obstacles
    #-----------------------------------------
    def create_obstacles(self):
        obs_img = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("ProjectImages", "obstacle.png")), (45, 45)
        )

        coords = [
            (10, 200),
            (120, 70), (260, 75), (400, 80),
            (150, 130), (230, 140), (310, 135), (390, 145), (470, 130),
            (90, 160), (160, 150),
            (300, 220), (380, 260), (330, 300),
            (140, 330), (210, 360), (260, 310),
            (250, 200), (290, 260)
        ]

        return [(obs_img, obs_img.get_rect(topleft=(x, y))) for x, y in coords]

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

        # Circles
        for visible, rect in zip(self.wc_visible, self.wc_rects):
            if visible:
                self.screen.blit(self.wc_img, rect)

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
# run() wrapper (like Bubbles)
#-----------------------------------------
def run():
    game = MazeGame()
    game.MainLoop()
    return

if __name__ == "__main__":
    run()
