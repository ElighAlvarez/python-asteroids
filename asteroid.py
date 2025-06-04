from circleshape import CircleShape
import pygame, random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            left_angle = self.velocity.rotate(-1 * random.uniform(20, 50))
            right_angle = self.velocity.rotate(random.uniform(20, 50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            left_child = Asteroid(self.position.x, self.position.y, new_radius)
            right_child = Asteroid(self.position.x, self.position.y, new_radius)

            left_child.velocity = left_angle * 1.2
            right_child.velocity = right_angle * 1.2

        self.kill()


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
