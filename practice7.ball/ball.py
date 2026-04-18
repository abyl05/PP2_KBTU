import pygame

class Ball:
    def __init__(self, screen_width, screen_height):
        self.radius = 25
        self.step = 20

        self.screen_width = screen_width
        self.screen_height = screen_height

        # Start in center
        self.x = screen_width // 2
        self.y = screen_height // 2

    def handle_input(self, key):
        if key == pygame.K_UP:
            self.move(0, -self.step)
        elif key == pygame.K_DOWN:
            self.move(0, self.step)
        elif key == pygame.K_LEFT:
            self.move(-self.step, 0)
        elif key == pygame.K_RIGHT:
            self.move(self.step, 0)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        # Boundary check (IMPORTANT)
        if self.radius <= new_x <= self.screen_width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= self.screen_height - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)