import pygame
import random

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

pygame.display.set_caption("My Game")

pygame.init()

player = pygame.Rect(WIDTH//2, HEIGHT-50, 50, 50)
ball = pygame.Rect(WIDTH//2, 0, 20, 20)

running = True
while running:
    delta_time = CLOCK.tick(144) / 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-5 * delta_time, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(5 * delta_time, 0)

    ball.move_ip(0, 5 * delta_time)
    if ball.top > HEIGHT:
        ball.top = 0
        ball.left = random.randint(0, WIDTH-20)

    if player.colliderect(ball):
        ball.top = 0
        ball.left = random.randint(0, WIDTH-20)

    SCREEN.fill((0, 0, 0))
    pygame.draw.rect(SCREEN, (255, 0, 0), player)
    pygame.draw.ellipse(SCREEN, (0, 0, 255), ball)

    pygame.display.flip()   

pygame.quit()
