import pygame

class Player:
    width = 25
    height = 120
    max_velocity = 6
    acceleration = 0.1

    def __init__(self, left, top):
        self.points = 0
        self.velocity = 0
        self.rect = pygame.Rect(left, top, Player.width, Player.height)

    def add_point(self):
        self.points += 1

    # When False is appsed it will decelerate, otherwise True is default
    def accelerate(self, accelerate=True):
        if accelerate and self.velocity < self.max_velocity:
            self.velocity += self.acceleration
        elif self.velocity > 0:
            self.velocity -= self.acceleration
