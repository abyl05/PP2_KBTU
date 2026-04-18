import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()
ball = Ball(WIDTH, HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            ball.handle_input(event.key)

    screen.fill((255, 255, 255))  # white background

    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)