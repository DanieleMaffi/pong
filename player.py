import pygame
from ball import Direction
import os
from dotenv import load_dotenv

load_dotenv()
HEIGHT, WIDTH = int(os.getenv('HEIGHT')), int(os.getenv('WIDTH'))

class Player:
    # Static player values
    width = 25
    height = 120
    max_velocity = 6
    acceleration = 1
    friction = 0.1

    def __init__(self, left, top):
        self.points = 0
        self.velocity = 0
        self.rect = pygame.Rect(left, top, Player.width, Player.height)
        self.last_direction = Direction.IDLE
        self.is_changing_direction = False

    # Adds a point to the player
    def add_point(self):
        self.points += 1

    # When False is passed it will decelerate, otherwise accelerating is default
    def accelerate(self, accelerate=True):
        if accelerate and self.velocity < self.max_velocity:
            self.velocity += self.acceleration
        elif self.velocity > 0:
            if self.velocity < 1:                   # To handle unprecise floating point arithmetic and prevent the number going negative
                self.velocity = 0
            else:
                self.velocity -= self.friction

    def __update_direction(self, direction):
        if self.last_direction != direction and self.last_direction != Direction.IDLE:          # The second conditions will assure the variable doesn't become true when the first position is 'IDLE'
            self.is_changing_direction = True
        if direction == Direction.UP  :
            self.last_direction = Direction.UP
        else:
            self.last_direction = Direction.DOWN

    # Just moves the player given a direction and updates 'is_changing_direction' if the previous direction is the opposite
    def move(self, direction):
        if self.is_changing_direction:
            if direction == Direction.UP and self.rect.top > 0:
                self.rect.top += self.velocity - self.acceleration - self.friction
            elif self.rect.top < HEIGHT - self.height:
                self.rect.top -= self.velocity - self.acceleration - self.friction
        else:
            if direction == Direction.UP and self.rect.top > 0:
                self.rect.top -= self.velocity
            elif self.rect.top < HEIGHT - self.height:
                self.rect.top += self.velocity 

        if self.rect.top > HEIGHT - self.height:
            self.velocity = 0
            self.rect.top = HEIGHT - self.height
        if self.rect.top < 0:
            self.velocity = 0
            self.rect.top = 0

        self.__update_direction(direction)          

    # Makes the player slide according to the velocity left
    def slide(self):
        if self.last_direction == Direction.UP:
            self.move(Direction.UP)
        else:
            self.move(Direction.DOWN)

    def __str__(self):
        return f'''Velocity: {self.velocity}\nIs Changing Direction: {"yes" if self.is_changing_direction else "no"}\nLast Direction: {self.last_direction}\n'''
