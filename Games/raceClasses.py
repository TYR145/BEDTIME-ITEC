
from cmath import rect
from pydoc import text

import pygame
import os
import time


class Player:
    def __init__(self, height):
        # Defining Player
        self.player_image = pygame.image.load(os.path.join("ProjectImages", "arrow_R.png"))
        self.player_image = pygame.transform.smoothscale(self.player_image, (55, 55))

        # Player's location and speed
        self.player_x = 15           # Spawnpoint
        self.player_y = height - 320 # Spawnpoint
        self.player_speed = 2.5

        # Player Rect --> needed for border collision
        self.p_rect = pygame.Rect(
            self.player_x,
            self.player_y,
            self.player_image.get_width(),
            self.player_image.get_height()
        )


class Kid:
    def __init__(self, height):
        # Defining Kid
        self.kid_image = pygame.image.load(os.path.join("ProjectImages", "kid_img.png"))
        self.kid_image = pygame.transform.smoothscale(self.kid_image, (95, 95))

        # Kid's speed
        self.kid_speed = 2

        # Kid Rect ---> (x, y, kid)
        self.kid_rect = pygame.Rect(
            0,
            height - 150,
            self.kid_image.get_width(),
            self.kid_image.get_height()
        )


class Assets:
    def __init__(self, width, height, player_y):
        # Adding BG Images
        self.background = pygame.image.load(os.path.join("ProjectImages", "race_bg.jpg"))
        self.background = pygame.transform.smoothscale(self.background, (width, height))

        # Goal
        self.goal_image = pygame.image.load(os.path.join("ProjectImages", "race_flag.png"))
        self.goal_image = pygame.transform.smoothscale(self.goal_image, (90, 90))

        # Player's Lane
        self.goalP_rect = pygame.Rect(
            850,
            player_y,
            self.goal_image.get_width(),
            self.goal_image.get_height()
        )

        # Kid's Lane
        self.goalK_rect = pygame.Rect(
            850,
            height - 150,
            self.goal_image.get_width(),
            self.goal_image.get_height()
        )

        # Border Line Image
        self.Borderline_image = pygame.image.load(os.path.join("ProjectImages", "borderline.png"))
        self.Borderline_image = pygame.transform.smoothscale(self.Borderline_image, (960, 40))

        # Positioning Border Line in center
        Border_y = height - 200
        self.Borderline_rect = pygame.Rect(0, Border_y, 960, 40)


class Obstacles:
    def __init__(self):
        self.obstacles = []
        obs_image = pygame.image.load(os.path.join("ProjectImages", "obstacle.png"))
        obs_image = pygame.transform.smoothscale(obs_image, (65, 120))

        obs_coords = [
            (150, 70),
            (300, 240),
            (450, 70),
            (600, 240),
            (750, 70)
        ]

        for x, y in obs_coords:
            rect = obs_image.get_rect(topleft=(x, y))
            self.obstacles.append((obs_image, rect))


class UI:
    def __init__(self, screen):
        self.screen = screen

    def show_message(self, text_string, duration, player, kid, assets):
        font = pygame.font.SysFont('Arial', 150)

        # Dark overlay
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))

        # Rendering text
        text = font.render(text_string, True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )

        # Draw everything
        self.screen.blit(assets.background, (0, 0))
        self.screen.blit(player.player_image, player.p_rect)
        self.screen.blit(kid.kid_image, kid.kid_rect)
        self.screen.blit(assets.goal_image, assets.goalP_rect)
        self.screen.blit(assets.goal_image, assets.goalK_rect)
        self.screen.blit(assets.Borderline_image, assets.Borderline_rect)
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(text, text_rect)

        pygame.display.update()
        pygame.time.delay(duration)


class Countdown:
    def __init__(self, screen, width, height, background, obstacles, player, kid, assets):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.background = background
        self.obstacles = obstacles
        self.player = player
        self.kid = kid
        self.assets = assets

    def start(self, seconds):
        font = pygame.font.SysFont('Arial', 150)  #--> font style & size
        for i in range(seconds, 0, -1):
            # Drawing bg
            self.screen.fill((0, 0, 0))  #--> fill background with black before drawing text
            self.screen.blit(self.background, (0, 0))

            # Draw obstacles
            for obs_image, rect in self.obstacles:
                self.screen.blit(obs_image, rect)

            # Draw player + kid + goals + border
            self.screen.blit(self.player.player_image, self.player.p_rect)
            self.screen.blit(self.kid.kid_image, self.kid.kid_rect)
            self.screen.blit(self.assets.goal_image, self.assets.goalP_rect)
            self.screen.blit(self.assets.goal_image, self.assets.goalK_rect)
            self.screen.blit(self.assets.Borderline_image, self.assets.Borderline_rect)

            transparent = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)  #--> Create a transparent surface
            transparent.fill((0, 0, 0, 120))  # RBG & Alpha (transparency level) = 0-255 (opaque to transparent)
            self.screen.blit(transparent, (0, 0))

            # Drawing the timer text
            text = font.render(str(i), True, (255, 255, 255))  #--> converts string into IMAGE to DRAW & DISPLAY
            text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))  #--> centering text on screen
            self.screen.blit(text, text_rect)  #--> draws text on screen at specified location

            pygame.display.update()
            pygame.time.delay(1000)  # Delay for 1 second = 1000 ms


class GameLoop:
    def __init__(self, screen, clock, FPS, width, height, player, kid, assets, obstacles, ui):
        self.screen = screen
        self.clock = clock
        self.FPS = FPS
        self.WIDTH = width
        self.HEIGHT = height

        self.player = player
        self.kid = kid
        self.assets = assets
        self.obstacles = obstacles
        self.ui = ui

        self.end = False
        self.player_dx = 0  #--> Direction x
        self.player_dy = 0  #--> Direction y

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end = True

            # EXIT KEY - "Esc"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.end = True

                # RIGHT
                if event.key == pygame.K_RIGHT:
                    self.player_dx = self.player.player_speed
                # UP
                if event.key == pygame.K_UP:
                    self.player_dy = -self.player.player_speed
                # DOWN
                if event.key == pygame.K_DOWN:
                    self.player_dy = self.player.player_speed

            # KEYUP
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player_dx = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    self.player_dy = 0

    def player_collision(self):
        p_rect = self.player.p_rect

        p_rect.x += self.player_dx

        # Collision with obstacles
        for obs_image, rect in self.obstacles:
            if p_rect.colliderect(rect):
                if self.player_dx > 0:   # moving right
                    p_rect.right = rect.left
                elif self.player_dx < 0: # moving left
                    p_rect.left = rect.right

        p_rect.y += self.player_dy
        for obs_image, rect in self.obstacles:
            if p_rect.colliderect(rect):
                if self.player_dy > 0:   # moving down
                    p_rect.bottom = rect.top
                elif self.player_dy < 0: # moving up
                    p_rect.top = rect.bottom

    def border_line_collision(self):
        p_rect = self.player.p_rect
        Borderline_rect = self.assets.Borderline_rect

        if p_rect.colliderect(Borderline_rect):
            if self.player_dy > 0:   # moving down
                p_rect.bottom = Borderline_rect.top
            elif self.player_dy < 0: # moving up
                p_rect.top = Borderline_rect.bottom

    def boarder_collision(self):
        # BORDER COLLISION --> use < & > adds flexibility, to snap ONLY if player is too far
        p_rect = self.player.p_rect
        kid_rect = self.kid.kid_rect

        # Player
        if p_rect.left < 6:
            p_rect.left = 6

        if p_rect.top < 7:
            p_rect.top = 7

        if p_rect.bottom > self.HEIGHT - 6:
            p_rect.bottom = self.HEIGHT - 6

        if p_rect.right > self.WIDTH - 7:
            p_rect.right = self.WIDTH - 7

        # Kid
        if kid_rect.left < 6:
            kid_rect.left = 6

        if kid_rect.top < 7:
            kid_rect.top = 7

        if kid_rect.bottom > self.HEIGHT - 6:
            kid_rect.bottom = self.HEIGHT - 6

        if kid_rect.right > self.WIDTH - 7:
            kid_rect.right = self.WIDTH - 7

    def goal_detection(self):
        # Detecting who touches Goal first
        FinishLine_x = 850  # x-position of the goal

        p_rect = self.player.p_rect
        kid_rect = self.kid.kid_rect
        goalP_rect = self.assets.goalP_rect
        goalK_rect = self.assets.goalK_rect

        # Player reaches goal
        if p_rect.colliderect(goalP_rect):
            self.ui.show_message("You won!", 2000, self.player, self.kid, self.assets)
            print("You won the race!")
            self.end = True
            return FinishLine_x, self.end

        # Kid reaches goal
        if kid_rect.colliderect(goalK_rect):
            self.ui.show_message("You lost!", 2000, self.player, self.kid, self.assets)
            print("You lost!")
            self.end = True
            return FinishLine_x, self.end

    def draw(self):
        # DRAW
        self.screen.blit(self.assets.background, (0, 0))

        self.screen.blit(self.assets.Borderline_image, self.assets.Borderline_rect)
        self.screen.blit(self.player.player_image, self.player.p_rect)
        self.screen.blit(self.kid.kid_image, self.kid.kid_rect)
        self.screen.blit(self.assets.goal_image, self.assets.goalP_rect)
        self.screen.blit(self.assets.goal_image, self.assets.goalK_rect)

        # Drawing obstacles
        for obs_image, rect in self.obstacles:
            self.screen.blit(obs_image, rect)

    def run(self):
        while not self.end:
            # Auto moves on X axis
            self.kid.kid_rect.x += self.kid.kid_speed

            # Event handling: Check for user input
            self.handle_events()

            # PLAYER MOVEMENT + COLLISIONS
            self.player_collision()

            # BORDERLINE COLLISION
            self.border_line_collision()

            # BORDER COLLISION
            self.boarder_collision()

            # GOAL DETECTION
            self.goal_detection()

            # Update the display and cap frame rate
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.FPS)


class RaceGame:
    def __init__(self):
        pygame.init()

        # SCREEN DIMENSIONS
        self.WIDTH, self.HEIGHT = 990, 550
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Race Mechanics - BETA")
        self.clock = pygame.time.Clock()

        # Create game objects
        self.player = Player(self.HEIGHT)
        self.kid = Kid(self.HEIGHT)
        self.assets = Assets(self.WIDTH, self.HEIGHT, self.player.player_y)
        self.obstacles = Obstacles().obstacles
        self.ui = UI(self.screen)
        self.countdown = Countdown(
            self.screen,
            self.WIDTH,
            self.HEIGHT,
            self.assets.background,
            self.obstacles,
            self.player,
            self.kid,
            self.assets
        )

    def run(self):
        # COUNTDOWN BEFORE GAME STARTS
        self.countdown.start(3)

        # GAME LOOP
        game_loop = GameLoop(
            self.screen,
            self.clock,
            self.FPS,
            self.WIDTH,
            self.HEIGHT,
            self.player,
            self.kid,
            self.assets,
            self.obstacles,
            self.ui
        )
        game_loop.run()

        # Quit Pygame
        pygame.quit()


if __name__ == "__main__":
    game = RaceGame()
    game.run()
