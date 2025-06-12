import pygame
import random
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash Clone")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 200, 200)
OBSTACLE_COLOR = (255, 100, 100)
GRAVITY = 0.8
JUMP_STRENGTH = -15
OBSTACLE_WIDTH = 40
OBSTACLE_HEIGHT = 80


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(midbottom=(100, SCREEN_HEIGHT - 50))
        self.velocity_y = 0
        self.is_jumping = False

    def update(self):

        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.bottom >= SCREEN_HEIGHT - 50:
            self.rect.bottom = SCREEN_HEIGHT - 50
            self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = JUMP_STRENGTH
            self.is_jumping = True


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(OBSTACLE_COLOR)
        self.rect = self.image.get_rect(midbottom=(x, y))

    def update(self):
        self.rect.x -= 10  
        if self.rect.right < 0:
            self.kill()  


all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()


player = Player()
all_sprites.add(player)


score = 0
obstacle_timer = 0
obstacle_interval = 1200 


running = True
while running:
    dt = clock.tick(60)  


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

   
    obstacle_timer += dt
    if obstacle_timer >= obstacle_interval:
        obstacle_timer = 0
        obstacle_y = SCREEN_HEIGHT - 50
        obstacle = Obstacle(SCREEN_WIDTH, obstacle_y)
        all_sprites.add(obstacle)
        obstacles.add(obstacle)


    if pygame.sprite.spritecollide(player, obstacles, False):
        print("Game Over! Your score:", score)
        pygame.quit()
        sys.exit()

  
    score += 1

  
    all_sprites.update()

    
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

print("Thanks for playing!")
