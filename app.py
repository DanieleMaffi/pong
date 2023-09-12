import pygame
import random

# pygame setup
HEIGHT, WIDTH = 720, 1280
FONT_SIZE = 192

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("My Game")
text_points = pygame.font.Font(None, FONT_SIZE)
text_render = text_points.render(f'0 - 0', True, (100,100,100, 55))

# Common player info
player_info = {
    'width': 25,
    'height': 120,
    'velocity': 6,
    'points': 0
}
player1 = pygame.Rect(30, HEIGHT//2 - 60, player_info['width'], player_info["height"])
player2 = pygame.Rect(WIDTH - (30 + player_info["width"]), HEIGHT//2 - 60, player_info["width"], player_info["height"])

ball_info = {
    'width': 30,
    'height': 30,
    'velocity': 3,
    'points': 0
}
ball = pygame.Rect(WIDTH//2 - ball_info["width"]//2, HEIGHT//2 - ball_info["height"]//2, ball_info["width"], ball_info["height"])

points = {
    'player1': 0,
    'player2': 0
}

class Direction:
    UPLEFT = 1
    DOWNLEFT = 2
    DOWNRIGHT = 3
    UPRIGHT = 4 

def init_ball():
    return random.randrange(1, 4)

def movement():
    pressed_keyes = pygame.key.get_pressed()
    if pressed_keyes[pygame.K_w] and player1.top > 0:
        player1.top -= player_info['velocity']
    if pressed_keyes[pygame.K_s] and player1.top < HEIGHT - player_info["height"]:
        player1.top += player_info['velocity']
    if pressed_keyes[pygame.K_UP] and player2.top > 0:
        player2.top -= player_info['velocity']
    if pressed_keyes[pygame.K_DOWN] and player2.top < HEIGHT - player_info["height"]:
        player2.top += player_info['velocity']

    if ball_direction == Direction.UPLEFT:
        ball.top -= ball_info['velocity']
        ball.left -= ball_info['velocity']
    if ball_direction == Direction.DOWNLEFT:
        ball.top += ball_info['velocity']
        ball.left -= ball_info['velocity']
    if ball_direction == Direction.DOWNRIGHT:
        ball.top += ball_info['velocity']
        ball.left += ball_info['velocity']
    if ball_direction == Direction.UPRIGHT:
        ball.top -= ball_info['velocity']
        ball.left += ball_info['velocity']

def collisions():
    global ball_direction, player1, player2, text_render, points
    if ball.top == 0:
        if ball_direction == Direction.UPLEFT:
            ball_direction = Direction.DOWNLEFT
        else:
            ball_direction = Direction.DOWNRIGHT

    if ball.top == HEIGHT - ball_info['height']:
        if ball_direction == Direction.DOWNLEFT:
            ball_direction = Direction.UPLEFT
        else:
            ball_direction = Direction.UPRIGHT

    if ball.left <= -ball_info['width']*10 or ball.left >= WIDTH + ball_info['width']*10:
        if ball.left <= 0:
            points['player2'] += 1
        else:
            points['player1'] += 1
        ball.left = WIDTH//2 - ball_info["width"]//2
        ball.top = HEIGHT//2 - ball_info["height"]//2
            
        text_render = text_points.render(f'{points["player1"]} - {points["player2"]}', True, (100,100,100, 50))
        ball_direction = init_ball()

    if player1.colliderect(ball):
        if ball_direction == Direction.DOWNLEFT:
            ball_direction = Direction.DOWNRIGHT
        else:
            ball_direction = Direction.UPRIGHT

    if player2.colliderect(ball):
        if ball_direction == Direction.DOWNRIGHT:
            ball_direction = Direction.DOWNLEFT
        else:
            ball_direction = Direction.UPLEFT

def draw_elements():
    screen.fill((0,0,0))                                    # Setting the background
    pygame.draw.rect(screen, (255,255,255, 1), player1)     # Drawing the player
    pygame.draw.rect(screen, (255,255,255, 1), player2) 
    pygame.draw.ellipse(screen, (255,255,255, 1), ball)
    screen.blit(text_render, (WIDTH//2 - FONT_SIZE//1.5, HEIGHT//2 - FONT_SIZE//3))

ball_direction = init_ball()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    movement()
    collisions()
    draw_elements()

    pygame.display.flip()                                   # Refreshing the screen

pygame.quit()