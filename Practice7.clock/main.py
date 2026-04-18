import pygame
import sys
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

player = MusicPlayer(screen)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            player.handle_input(event.key)

    screen.fill((30, 30, 30))

    player.update()
    player.draw()

    pygame.display.flip()
    clock.tick(60)