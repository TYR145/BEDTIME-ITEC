
import pygame
import os
import random

import pygame
import os
import random

# Define BASE_DIR FIRST
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# NOW you can print it
print("BASE_DIR =", BASE_DIR)
print("ProjectImages exists:", os.path.isdir(os.path.join(BASE_DIR, "ProjectImages")))
print("Files inside ProjectImages:", os.listdir(os.path.join(BASE_DIR, "ProjectImages")))


# Always load images relative to THIS file's folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class GameObjects:
    class Bubbles:
        def __init__(self, x, y):
            img_path = os.path.join(BASE_DIR, "ProjectImages", "bubble.png")
            self.image = pygame.image.load(img_path)
            self.image = pygame.transform.smoothscale(self.image, (180, 180))
            self.rect = self.image.get_rect(topleft=(x, y))
            self.speed = random.uniform(0.2, 1)
            self.sway = random.uniform(-1, 1)

class Game:
    def run():
        pygame.init()

        SPAWN_TIMER = 0
        SPAWN_INTERVAL = 60  # frames (1 second at 60 FPS)

        WIDTH, HEIGHT = 750, 480
        FPS = 60
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Bubbles Clicking - TESTING")
        clock = pygame.time.Clock()

        # Background
        bg_path = os.path.join(BASE_DIR, "ProjectImages", "OpenBG.jpg")
        background = pygame.image.load(bg_path)
        background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

        # Score
        score = 0
        font = pygame.font.SysFont(None, 36)

        # Bubbles
        bubbles = []
        for _ in range(20):
            x = random.randint(20, 450)
            y = random.randint(480, 1000)
            bubbles.append(GameObjects.Bubbles(x, y))

        end = False

        def update():
            nonlocal end, bubbles, score
            nonlocal SPAWN_TIMER

            SPAWN_TIMER += 1
            if SPAWN_TIMER >= SPAWN_INTERVAL:
                SPAWN_TIMER = 0
                x = random.randint(20, 450)
                y = random.randint(480, 1600)
                new_bubble = GameObjects.Bubbles(x, y)
                new_bubble.turn = random.randint(0, 1)
                bubbles.append(new_bubble)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i in range(len(bubbles) - 1, -1, -1):
                        if bubbles[i].rect.collidepoint(mouse_pos):
                            bubbles.pop(i)
                            score += 50

                            # Respawn
                            x = random.randint(20, 450)
                            y = random.randint(480, 1600)
                            bubbles.append(GameObjects.Bubbles(x, y))

            # Move bubbles
            for b in bubbles:
                b.rect.y -= b.speed
                b.rect.x += b.sway

                if b.rect.y < -120:
                    b.rect.y = random.randint(480, 1600)
                    b.rect.x = random.randint(0, 450)

        def draw():
            nonlocal score, font
            screen.blit(background, (0, 0))

            for b in bubbles:
                screen.blit(b.image, b.rect)

            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            clock.tick(FPS)

        while not end:
            update()
            draw()

        pygame.quit()

if __name__ == "__main__":
    Game.run()
