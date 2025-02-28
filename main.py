import pygame
import random


pygame.init()


WIDTH, HEIGHT = 500, 500
BOMB_COUNT = 10
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))


bomb_img = pygame.image.load("bomb.png")
boom_img = pygame.image.load("boom.png")


BOMB_WIDTH = bomb_img.get_width()
BOMB_HEIGHT = bomb_img.get_height()
BOOM_WIDTH = boom_img.get_width()
BOOM_HEIGHT = boom_img.get_height()


class Bomb:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, BOMB_WIDTH, BOMB_HEIGHT)
        self.exploded = False

    def draw(self):
        if not self.exploded:
            screen.blit(bomb_img, (self.x, self.y))
        else:

            boom_x = self.x - (BOOM_WIDTH - BOMB_WIDTH) // 2
            boom_y = self.y - (BOOM_HEIGHT - BOMB_HEIGHT) // 2
            screen.blit(boom_img, (boom_x, boom_y))

    def check_click(self, pos):
        if self.rect.collidepoint(pos) and not self.exploded:
            self.exploded = True
            return True
        return False


def is_valid_position(x, y, bombs):
    if x < 0 or x + BOMB_WIDTH > WIDTH or y < 0 or y + BOMB_HEIGHT > HEIGHT:
        return False

    new_rect = pygame.Rect(x, y, BOMB_WIDTH, BOMB_HEIGHT)
    for bomb in bombs:
        if new_rect.colliderect(bomb.rect):
            return False

    return True


def create_bombs():
    bombs = []
    attempts = 0
    max_attempts = 1000

    while len(bombs) < BOMB_COUNT and attempts < max_attempts:
        x = random.randint(0, WIDTH - BOMB_WIDTH)
        y = random.randint(0, HEIGHT - BOMB_HEIGHT)

        if is_valid_position(x, y, bombs):
            bombs.append(Bomb(x, y))

        attempts += 1

    return bombs


bombs = create_bombs()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for bomb in bombs:
                    bomb.check_click(event.pos)

    screen.fill(BLACK)
    for bomb in bombs:
        bomb.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
