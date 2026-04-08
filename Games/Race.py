import pygame
import os
import time


class PlayerObject:
    def __init__(self, image, rect, speed):
        # Defining Player
        self.image = image
        # Player Rect --> needed for border collision
        self.rect = rect
        # Player's speed
        self.speed = speed


class KidObject:
    def __init__(self, image, rect, speed):
        # Defining Kid
        self.image = image
        # Kid Rect ---> (x, y, kid)
        self.rect = rect
        # Kid's speed
        self.speed = speed


class RaceGame:
    def __init__(self, screen, width, height, fps, clock):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = fps
        self.clock = clock

        # ===========================================================
        #      ADDING IMAGES --- ADD IMAGE RECT FOR BORDER COLLISION
        # ===========================================================

        # Defining Player
        player_image = pygame.image.load(os.path.join("ProjectImages", "arrow_R.png"))
        player_image = pygame.transform.smoothscale(player_image, (55, 55))

        # Player's location and speed
        player_x = 15           # Spawnpoint
        player_y = self.HEIGHT - 320  # Spawnpoint
        player_speed = 2.5
        # Player Rect --> needed for border collision
        p_rect = pygame.Rect(player_x, player_y,
                             player_image.get_width(), player_image.get_height())

        self.player = PlayerObject(player_image, p_rect, player_speed)

        # Defining Kid
        kid_image = pygame.image.load(os.path.join("ProjectImages", "kid_img.png"))
        kid_image = pygame.transform.smoothscale(kid_image, (95, 95))

        # Kid's speed
        kid_speed = 2

        # Kid Rect ---> (x, y, kid)
        kid_rect = pygame.Rect(0, self.HEIGHT - 150,
                               kid_image.get_width(), kid_image.get_height())

        self.kid = KidObject(kid_image, kid_rect, kid_speed)

        # Adding BG Images
        self.background = pygame.image.load(os.path.join("ProjectImages", "race_bg.jpg"))
        self.background = pygame.transform.smoothscale(self.background, (self.WIDTH, self.HEIGHT))

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
            self.HEIGHT - 150,
            self.goal_image.get_width(),
            self.goal_image.get_height()
        )

        # Border Line Image
        self.Borderline_image = pygame.image.load(os.path.join("ProjectImages", "borderline.png"))
        self.Borderline_image = pygame.transform.smoothscale(self.Borderline_image, (960, 40))
        # Positioning Border Line in center
        Border_y = self.HEIGHT - 200
        self.Borderline_rect = pygame.Rect(0, Border_y, 960, 40)

        # Race obstacles
        self.obstacles = self.create_obstacles()

        # -----------------------------------------------------------------
        self.end = False
        # Player movement Variables
        self.player_dx = 0  # --> Direction x
        self.player_dy = 0  # --> Direction y

    def create_obstacles(self):
        obstacles = []
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
            obstacles.append((obs_image, rect))
        return obstacles

    # ----------------------------------------------------------------------
    # Adding COUNTDOWN TIMER --> Runs BEFORE the game loop starts
    def countdown(self, seconds):
        font = pygame.font.SysFont('Arial', 150)  # --> font style & size
        for i in range(seconds, 0, -1):
            # Drawing bg
            self.screen.fill((0, 0, 0))  # --> fill background with black before drawing text
            self.screen.blit(self.background, (0, 0))

            # Draw obstacles
            for obs_image, rect in self.obstacles:
                self.screen.blit(obs_image, rect)

            # Draw player + kid + goals + border
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.kid.image, self.kid.rect)
            self.screen.blit(self.goal_image, self.goalP_rect)
            self.screen.blit(self.goal_image, self.goalK_rect)
            self.screen.blit(self.Borderline_image, self.Borderline_rect)

            transparent = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)  # --> Create a transparent surface
            transparent.fill((0, 0, 0, 120))  # RBG & Alpha (transparency level) = 0-255 (opaque to transparent)
            self.screen.blit(transparent, (0, 0))

            # Drawing the timer text
            text = font.render(str(i), True, (255, 255, 255))  # --> converts string into IMAGE to DRAW & DISPLAY
            text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))  # --> centering text on screen
            self.screen.blit(text, text_rect)  # --> draws text on screen at specified location

            # Created RECT to tell program where to place the converted image
            pygame.display.update()
            pygame.time.delay(1000)  # Delay for 1 second = 1000 ms

    def show_message(self, text_string, duration):
        font = pygame.font.SysFont('Arial', 150)

        # Dark overlay
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))

        # Rendering text
        text = font.render(text_string, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))

        # Draw everything
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.kid.image, self.kid.rect)
        self.screen.blit(self.goal_image, self.goalP_rect)
        self.screen.blit(self.goal_image, self.goalK_rect)
        self.screen.blit(self.Borderline_image, self.Borderline_rect)
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(text, text_rect)

        pygame.display.update()
        pygame.time.delay(duration)

    # =========================================
    #      GAME LOGIC: Updates player position
    # =========================================
    def game_loop(self):
        # Local aliases to keep original variable names/feel
        p_rect = self.player.rect
        kid_rect = self.kid.rect
        obstacles = self.obstacles
        Borderline_rect = self.Borderline_rect
        goalP_rect = self.goalP_rect
        goalK_rect = self.goalK_rect
        background = self.background
        goal_image = self.goal_image
        Borderline_image = self.Borderline_image
        player_image = self.player.image
        kid_image = self.kid.image

        while not self.end:
            # Auto moves on X axis
            kid_rect.x += self.kid.speed

            # Event handling: Check for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end = True

                # EXIT KEY - "Esc"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.end = True

                    # RIGHT
                    if event.key == pygame.K_RIGHT:
                        self.player_dx = self.player.speed
                    # UP
                    if event.key == pygame.K_UP:
                        self.player_dy = -self.player.speed
                    # DOWN
                    if event.key == pygame.K_DOWN:
                        self.player_dy = self.player.speed

                # KEYUP
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.player_dx = 0
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        self.player_dy = 0

            # PLAYER MOVEMENT
            def player_collision():
                p_rect.x += self.player_dx

                # Collision with obstacles
                for obs_image, rect in obstacles:
                    if p_rect.colliderect(rect):
                        if self.player_dx > 0:   # moving right
                            p_rect.right = rect.left
                        elif self.player_dx < 0:  # moving left
                            p_rect.left = rect.right

                p_rect.y += self.player_dy
                for obs_image, rect in obstacles:
                    if p_rect.colliderect(rect):
                        if self.player_dy > 0:   # moving down
                            p_rect.bottom = rect.top
                        elif self.player_dy < 0:  # moving up
                            p_rect.top = rect.bottom

            player_collision()

            # BORDERLINE COLLISION
            def border_line_collision():
                if p_rect.colliderect(Borderline_rect):
                    if self.player_dy > 0:   # moving down
                        p_rect.bottom = Borderline_rect.top
                    elif self.player_dy < 0:  # moving up
                        p_rect.top = Borderline_rect.bottom

            border_line_collision()

            # BORDER COLLISION --> use < & > adds flexibility, to snap ONLY if player is too far
            def boarder_collision():
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

            boarder_collision()

            # GOAL DETECTION
            def goal_detection():
                # Detecting who touches Goal first
                FinishLine_x = 850  # x-position of the goal

                # Player reaches goal
                if p_rect.colliderect(goalP_rect):
                    self.show_message("You won!", 2000)  # --> Calls Back function to show message
                    print("You won the race!")
                    self.end = True
                    return FinishLine_x, self.end

                # Kid reaches goal
                if kid_rect.colliderect(goalK_rect):
                    self.show_message("You lost!", 2000)  # --> Calls Back function to show message
                    print("You lost!")
                    self.end = True
                    return FinishLine_x, self.end

            goal_detection()  # ← aligned with def (same indent level)

            #---------------------------------------------------------------
            def draw():
                # DRAW
                self.screen.blit(background, (0, 0))

                self.screen.blit(Borderline_image, Borderline_rect)
                self.screen.blit(player_image, p_rect)
                self.screen.blit(kid_image, kid_rect)
                self.screen.blit(goal_image, goalP_rect)
                self.screen.blit(goal_image, goalK_rect)

                # Drawing obstacles
                for obs_image, rect in obstacles:
                    self.screen.blit(obs_image, rect)

            #---------------------------------------------------------------
            # Update the display and cap frame rate
            pygame.display.flip()
            self.clock.tick(self.FPS)
            draw()


def run():
    pygame.init()

    # SCREEN DIMENSIONS
    WIDTH, HEIGHT = 990, 550
    FPS = 60
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Race Mechanics - BETA")
    clock = pygame.time.Clock()

    game = RaceGame(screen, WIDTH, HEIGHT, FPS, clock)
    game.countdown(3)  # --> 3 second countdown before game starts
    game.game_loop()


if __name__ == "__main__":
    run()
