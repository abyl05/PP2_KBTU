import pygame
from collections import deque
import math

# ======================
# FLOOD FILL
# ======================
def flood_fill(surface, x, y, new_color, width, height):
    target = surface.get_at((x, y))
    if target == new_color:
        return

    q = deque([(x, y)])

    while q:
        px, py = q.popleft()

        if px < 0 or px >= width or py < 0 or py >= height:
            continue

        if surface.get_at((px, py)) != target:
            continue

        surface.set_at((px, py), new_color)

        q.extend([
            (px+1, py), (px-1, py),
            (px, py+1), (px, py-1)
        ])

# ======================
# SHAPES
# ======================
def draw_rectangle(surface, color, start, end, size):
    rect = pygame.Rect(start, (end[0]-start[0], end[1]-start[1]))
    pygame.draw.rect(surface, color, rect, size)

def draw_circle(surface, color, start, end, size):
    radius = int(math.hypot(end[0]-start[0], end[1]-start[1]))
    pygame.draw.circle(surface, color, start, radius, size)

def draw_square(surface, color, start, end, size):
    s = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
    rect = pygame.Rect(start, (s, s))
    pygame.draw.rect(surface, color, rect, size)

def draw_right_triangle(surface, color, start, end, size):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, color, points, size)

def draw_equilateral_triangle(surface, color, start, end, size):
    side = abs(end[0]-start[0])
    height = side * math.sqrt(3) / 2
    p1 = start
    p2 = (start[0] + side, start[1])
    p3 = (start[0] + side/2, start[1] - height)
    pygame.draw.polygon(surface, color, [p1, p2, p3], size)

def draw_rhombus(surface, color, start, end, size):
    cx = (start[0] + end[0]) // 2
    cy = (start[1] + end[1]) // 2
    points = [
        (cx, start[1]),
        (end[0], cy),
        (cx, end[1]),
        (start[0], cy)
    ]
    pygame.draw.polygon(surface, color, points, size)