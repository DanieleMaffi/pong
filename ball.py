import random
import pygame

class Direction:
    UPLEFT = 1
    DOWNLEFT = 2
    DOWNRIGHT = 3
    UPRIGHT = 4
    IDLE = 5
    UP = 6
    DOWN = 7

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

    def move(self):
        if self.direction == Direction.UPLEFT:
            self.rect.top -= Ball.velocity
            self.rect.left -= Ball.velocity
        if self.direction == Direction.DOWNLEFT:
            self.rect.top += Ball.velocity
            self.rect.left -= Ball.velocity
        if self.direction == Direction.DOWNRIGHT:
            self.rect.top += Ball.velocity
            self.rect.left += Ball.velocity
        if self.direction == Direction.UPRIGHT:
            self.rect.top -= Ball.velocity
            self.rect.left += Ball.velocity

    def bounce(self, height):
        if self.rect.top == 0:
            if self.direction == Direction.UPLEFT:
                self.direction = Direction.DOWNLEFT
            else:
                self.direction = Direction.DOWNRIGHT

        if self.rect.top == height - Ball.height:
            if self.direction == Direction.DOWNLEFT:
                self.direction = Direction.UPLEFT
            else:
                self.direction = Direction.UPRIGHT