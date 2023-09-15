import pygame
from ball import Direction

class Player:
    # Static player values
    width = 25
    height = 120
    max_velocity = 6
    acceleration = 0.1

    def __init__(self, left, top):
        self.points = 0
        self.velocity = 0
        self.rect = pygame.Rect(left, top, Player.width, Player.height)
        self.last_direction = Direction.IDLE
        self.is_changing_direction = False

    # Adds a point to the player
    def add_point(self):
        self.points += 1

    # When False is appsed it will decelerate, otherwise accelerating is default
    def accelerate(self, accelerate=True):
        if accelerate and self.velocity < self.max_velocity:
            self.velocity += self.acceleration
        elif self.velocity > 0:
            if self.velocity < 1:                   # To handle unprecise floating point arithmetic and prevent the number going negative
                self.velocity = 0
            else:
                self.velocity -= self.acceleration

    def _update_direction(self, direction):
        if self.last_direction != direction:
            self.is_changing_direction = True
        if direction == Direction.UP:
            self.last_direction = Direction.UP
        else:
            self.last_direction = Direction.DOWN

    # Just moves the player given a direction and updates 'is_changing_direction' if the previous direction is the opposite
    def move(self, direction, height=0):
        if direction == Direction.UP and self.rect.top > 0:
            self.rect.top -= self.velocity
            
        elif self.rect.top < height - self.height:
            self.rect.top += self.velocity 

        self._update_direction(direction)          

    # Makes the player slide according to the velocity left
    def slide(self, height):
        if self.last_direction == Direction.UP:
            self.move(Direction.UP)
        else:
            self.move(Direction.DOWN, height)

    def __str__(self):
        return f'''Velocity: {self.velocity}\nIs Changing Direction: {"yes" if self.is_changing_direction else "no"}\nLast Direction: {self.last_direction}\n'''
