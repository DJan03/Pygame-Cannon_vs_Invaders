import pygame
import random


FPS = 60
WIDTH, HEIGHT = 600, 400
GRAVITY = 9.8
RUNNING = True


class Target:
    shape_radius = 10
    color = (255, 255, 0)
    speed = 10

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.speed = Target.speed
        self.radius = Target.shape_radius
        self.color = Target.color

    def move(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Ball:
    shape_radius = 5
    color = (255, 0, 0)

    def __init__(self, x: int, y: int, velocity_x: float, velocity_y: float):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.shape_radius = Ball.shape_radius
        self.color = Ball.color

    def move(self):
        pass

    def collide(self, target: Target):
        pass

    def draw(self, screen):
        pass

    def bounce(self):
        pass


class Cannon:
    color = (50, 50, 50)

    def __init__(self, x: int, y: int, fire_power: float):
        self.x = x
        self.y = y
        self.fire_power = fire_power
        self.color = Cannon.color
        self.aim_x = x
        self.aim_y = y

    def move(self, direction):
        pass

    def aim(self, position):
        pass

    def fire(self, balls: Ball):
        pass

    def draw(self, screen):
        pass


def generate_targets(targets, count=10):
    t = Target.shape_radius
    for _ in range(count):
        x, y = random.randint(t, WIDTH - t), random.randint(t, HEIGHT // 2 - t)
        targets.append(Target(x, y))


def input_handler(events, cannon: Cannon):
    global RUNNING
    for event in events:
        if event.type == pygame.QUIT:
            RUNNING = False


def update_objects(cannon: Cannon, balls, targets):
    for target in targets:
        target.move()

    for ball in balls:
        ball.move()
        for target in targets:
            ball.collide(target)


def draw_objects(screen, cannon: Cannon, balls, targets):
    screen.fill((120, 120, 120))

    for ball in balls:
        ball.draw(screen)

    for target in targets:
        target.draw(screen)

    cannon.draw(screen)

    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    cannon = Cannon(WIDTH // 2, HEIGHT * 9 // 10, 5)
    balls = []
    targets = []
    generate_targets(targets)

    while RUNNING:
        input_handler(pygame.event.get(), cannon)

        update_objects(cannon, balls, targets)
        draw_objects(screen, cannon, balls, targets)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
