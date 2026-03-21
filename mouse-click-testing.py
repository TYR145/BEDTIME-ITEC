
import pygame
import os
import random


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
            self.turn = 0
            self.visibility = None

    class SpecialBubbles:
        def __init__(self, x, y):
            img_path = os.path.join(BASE_DIR, "ProjectImages", "special_bubble.png")
            self.image = pygame.image.load(img_path)
            self.image = pygame.transform.smoothscale(self.image, (180, 180))
            self.rect = self.image.get_rect(topleft=(x, y))
            self.speed = random.uniform(0.3, 4)
            self.sway = random.uniform(-1, 0.5)
            self.turn = 1
            self.visibility = None


class Game:
    def run():
        pygame.init()

        WIDTH, HEIGHT = 750, 480
        FPS = 60
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Bubbles Clicking - TESTING")
        clock = pygame.time.Clock()

        # Load background
        bg_path = os.path.join(BASE_DIR, "ProjectImages", "OpenBG.jpg")
        background = pygame.image.load(bg_path)
        background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

        # Load bubble images
        bubble_path = os.path.join(BASE_DIR, "ProjectImages", "bubble.png")
        bubble_img = pygame.image.load(bubble_path)
        bubble_img = pygame.transform.smoothscale(bubble_img, (110, 110))

        special_path = os.path.join(BASE_DIR, "ProjectImages", "special_bubble.png")
        special_bubble_img = pygame.image.load(special_path)
        special_bubble_img = pygame.transform.smoothscale(special_bubble_img, (110, 110))

        # Create bubble list
        bubbles = []
        for _ in range(20):
            x = random.randint(20, 450)
            y = random.randint(480, 1000)
            b = GameObjects.Bubbles(x, y)
            b.turn = random.randint(0, 1)
            bubbles.append(b)

        end = False

        # ---------------------- UPDATE ---------------------- #
        def update():
            nonlocal end, bubbles

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True

                # CLICK TO POP BUBBLES
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    for i in range(len(bubbles) - 1, -1, -1):
                        if bubbles[i].rect.collidepoint(mouse_pos):
                            bubbles.pop(i)

            # Move bubbles
            for b in bubbles:
                b.rect.y -= b.speed
                b.rect.x += b.sway

                if b.rect.y < -120:
                    b.rect.y = random.randint(480, 1600)
                    b.rect.x = random.randint(0, 450)

                if random.random() < 0.01:
                    b.sway = random.uniform(-1.5, 1.5)

        # ---------------------- DRAW ---------------------- #
        def draw():
            screen.blit(background, (0, 0))

            for b in bubbles:
                screen.blit(b.image, b.rect)

            pygame.display.flip()
            clock.tick(FPS)

        # ---------------------- MAIN LOOP ---------------------- #
        while not end:
            update()
            draw()

        pygame.quit()


if __name__ == "__main__":
    Game.run()
