import random

class Clown:
    def __init__(self, image, screen_rect, speed):
        self.image = image
        self.rect = image.get_rect(center=screen_rect.center)
        self.speed = speed
        self.random_direction()

    def random_direction(self):
        old_dx = getattr(self, "dx", None)
        old_dy = getattr(self, "dy", None)

        while True:
            dx = random.choice([-1, 1])
            dy = random.choice([-1, 1])
            if dx != old_dx or dy != old_dy:
                self.dx = dx
                self.dy = dy
                break

    def move(self):
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

    def bounce(self, bounds):
        if self.rect.left < 0:
            self.rect.left = 0
            self.dx *= -1

        if self.rect.right > bounds.width:
            self.rect.right = bounds.width
            self.dx *= -1

        if self.rect.top < 0:
            self.rect.top = 0
            self.dy *= -1

        if self.rect.bottom > bounds.height:
            self.rect.bottom = bounds.height
            self.dy *= -1

    def accelerate(self, amount):
        self.speed += amount

    def reset(self, center, speed):
        self.rect.center = center
        self.speed = speed
        self.random_direction()
