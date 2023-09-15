import argparse
import pygame
from player import Player
from ball import Ball
from ball import Direction
import arabic

# pygame setup
HEIGHT, WIDTH = 720, 1280
FONT_SIZE = 192

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("My Game")
text_points = pygame.font.Font(None, FONT_SIZE)
text_render = text_points.render('0 - 0', True, (100,100,100, 55))

arabic = arabic.Arabic()

player1 = Player(30, HEIGHT//2 - 60)
player2 = Player(WIDTH - (30 + Player.width), HEIGHT//2 - 60)

ball = Ball(WIDTH//2 - Ball.width//2, HEIGHT//2 - Ball.height//2)

def direction_change_handler(player: Player):
    player.accelerate(False) if player.is_changing_direction else player.accelerate()
    if player.velocity == 0:
        player.is_changing_direction = False
    return

def movement(alone):
    pressed_keyes = pygame.key.get_pressed()
    if pressed_keyes[pygame.K_w]:
        direction_change_handler(player1)
        player1.move(Direction.UP)

    if pressed_keyes[pygame.K_s]:
        direction_change_handler(player1)
        player1.move(Direction.DOWN, HEIGHT)

    if not pressed_keyes[pygame.K_w] and not pressed_keyes[pygame.K_s]:
        player1.accelerate(False)
        player1.slide(HEIGHT)

    if not alone:
        if pressed_keyes[pygame.K_UP]:
            direction_change_handler(player2)
            player2.move(Direction.UP)
            
        if pressed_keyes[pygame.K_DOWN]:
            direction_change_handler(player2)
            player2.move(Direction.DOWN, HEIGHT)

        if not pressed_keyes[pygame.K_UP] and not pressed_keyes[pygame.K_DOWN]:
            player2.accelerate(False)
            player2.slide(HEIGHT)
    else:
        if ball.rect.top < HEIGHT//2:
            direction_change_handler(player2)
            player2.move(Direction.UP)
        else:
            direction_change_handler(player2)
            player2.move(Direction.DOWN)
        
        if player2.last_direction == Direction.UP:
            player2.move(Direction.UP)
        else:
            player2.move(Direction.DOWN, HEIGHT)
        
    if ball.direction == Direction.UPLEFT:
        ball.rect.top -= Ball.velocity
        ball.rect.left -= Ball.velocity
    if ball.direction == Direction.DOWNLEFT:
        ball.rect.top += Ball.velocity
        ball.rect.left -= Ball.velocity
    if ball.direction == Direction.DOWNRIGHT:
        ball.rect.top += Ball.velocity
        ball.rect.left += Ball.velocity
    if ball.direction == Direction.UPRIGHT:
        ball.rect.top -= Ball.velocity
        ball.rect.left += Ball.velocity

def collisions():
    global text_render
    if ball.rect.top == 0:
        if ball.direction == Direction.UPLEFT:
            ball.direction = Direction.DOWNLEFT
        else:
            ball.direction = Direction.DOWNRIGHT

    if ball.rect.top == HEIGHT - Ball.height:
        if ball.direction == Direction.DOWNLEFT:
            ball.direction = Direction.UPLEFT
        else:
            ball.direction = Direction.UPRIGHT

    if ball.rect.left <= -Ball.width*10 or ball.rect.left >= WIDTH + Ball.width*10:
        arabic.ninth_chord.play()
        if ball.rect.left <= 0:
            player2.add_point()
        else:
            player1.add_point()
            
        text_render = text_points.render(f'{player1.points} - {player2.points}', True, (100,100,100, 50))
        ball.reset(WIDTH, HEIGHT)

    if player1.rect.colliderect(ball.rect):
        arabic.degrees[arabic.note_degree].play()
        arabic.next_note()
        if ball.direction == Direction.DOWNLEFT:
            ball.direction = Direction.DOWNRIGHT
        else:
            ball.direction = Direction.UPRIGHT

    if player2.rect.colliderect(ball.rect):
        arabic.degrees[arabic.note_degree].play()
        arabic.next_note()
        if ball.direction == Direction.DOWNRIGHT:
            ball.direction = Direction.DOWNLEFT
        else:
            ball.direction = Direction.UPLEFT

def draw_elements():
    screen.fill((0,0,0))     
    screen.blit(text_render, (WIDTH//2 - FONT_SIZE//1.5, HEIGHT//2 - FONT_SIZE//3))                               # Setting the background
    pygame.draw.rect(screen, (255,255,255, 1), player1.rect)     # Drawing the player
    pygame.draw.rect(screen, (255,255,255, 1), player2.rect) 
    pygame.draw.ellipse(screen, (255,255,255, 1), ball.rect)

parser = argparse.ArgumentParser(description="Elaborato")
parser.add_argument( "-a", "--alone", nargs='?', type=bool, default=False, const=True, help="Single player mode")
args = parser.parse_args()

alone = args.alone

if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        print(player2)

        clock.tick(144)
        movement(alone)
        collisions()
        draw_elements()

        pygame.display.flip()                                   # Refreshing the screen

    pygame.quit()