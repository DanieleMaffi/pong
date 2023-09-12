import random
import pygame

class Direction:
    UPLEFT = 1
    DOWNLEFT = 2
    DOWNRIGHT = 3
    UPRIGHT = 4
    IDLE = 5

class Ball:
    width = 30
    height = 30
    velocity = 3

    def __init__(self, left, top) -> None:
        self.direction = random.randrange(1, 4)
        self.rect = pygame.Rect(left, top, Ball.width, Ball.height)
    
    def reset(self, width, height):
        self.rect.left = width//2 - Ball.width//2
        self.rect.top = height//2 - Ball.height//2
        self.direction = random.randrange(1, 4)