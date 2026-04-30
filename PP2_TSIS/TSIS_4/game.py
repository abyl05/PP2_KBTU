import pygame
import random
import time

from config import *

class Game:
    def __init__(self, settings):
        self.settings = settings

        # snake
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.dx, self.dy = CELL, 0

        # score / level
        self.score = 0
        self.level = 1

        self.last_level_score = 0
        self.level_target = 5
        self.speed = 5

        # walls
        self.walls = []
        self.generate_walls()

        # food objects
        self.food = None
        self.bonus = None
        self.super = None
        self.poison = None

        # timers
        self.t_food = time.time()
        self.t_bonus = time.time()
        self.t_super = time.time()
        self.t_poison = time.time()

        # active flags (ВАЖНО ДЛЯ ТАЙМЕРА)
        self.food_active = False
        self.bonus_active = False
        self.super_active = False
        self.poison_active = False

        self.spawn_all()

    # ---------------- SAFE SPAWN ----------------
    def safe_spawn(self):
        for _ in range(100):
            pos = (
                random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL)
            )
            if pos not in self.snake and pos not in self.walls:
                return pos
        return (0, 0)

    # ---------------- WALLS ----------------
    def generate_walls(self):
        self.walls = []

        if self.level < 4:
            return

        count = min(20 + self.level * 2, 50)

        for _ in range(count):
            self.walls.append(self.safe_spawn())

    # ---------------- SPAWN ALL ITEMS ----------------
    def spawn_all(self):
        self.food = self.safe_spawn()
        self.bonus = self.safe_spawn()
        self.super = self.safe_spawn()
        self.poison = self.safe_spawn()

        self.t_food = time.time()
        self.t_bonus = time.time()
        self.t_super = time.time()
        self.t_poison = time.time()

        self.food_active = True
        self.bonus_active = True
        self.super_active = True
        self.poison_active = True

    # ---------------- TIMER SPEED ----------------
    def life(self):
        return max(1.5, 5 - self.level * 0.3)

    # ---------------- LEVEL ----------------
    def level_up(self):
        self.level += 1
        self.last_level_score = self.score

        self.speed += 1
        self.level_target += 2

        self.generate_walls()

    # ---------------- UPDATE ----------------
    def update(self):

        head = self.snake[0]
        new = (head[0] + self.dx, head[1] + self.dy)

        if self.dx == 0 and self.dy == 0:
            return True

        # borders
        if new[0] < 0 or new[1] < 0 or new[0] >= WIDTH or new[1] >= HEIGHT:
            return False

        # self collision
        if new in self.snake[:-1]:
            return False

        # walls
        if new in self.walls:
            return False

        self.snake.insert(0, new)

        ate = False
        now = time.time()
        life = self.life()

        # ---------------- LEVEL SYSTEM ----------------
        if self.score - self.last_level_score >= self.level_target:
            self.level_up()

        # ---------------- FOOD TIMER ----------------
        if self.food_active and now - self.t_food > life:
            self.food_active = False

        if not self.food_active:
            self.food = self.safe_spawn()
            self.t_food = now
            self.food_active = True

        # ---------------- BONUS ----------------
        if self.bonus_active and now - self.t_bonus > life:
            self.bonus_active = False

        if not self.bonus_active:
            self.bonus = self.safe_spawn()
            self.t_bonus = now
            self.bonus_active = True

        # ---------------- SUPER ----------------
        if self.super_active and now - self.t_super > life:
            self.super_active = False

        if not self.super_active:
            self.super = self.safe_spawn()
            self.t_super = now
            self.super_active = True

        # ---------------- POISON ----------------
        if self.poison_active and now - self.t_poison > life:
            self.poison_active = False

        if not self.poison_active:
            self.poison = self.safe_spawn()
            self.t_poison = now
            self.poison_active = True

        # ---------------- EATING ----------------
        if new == self.food:
            self.score += 1
            self.food_active = False
            ate = True

        if new == self.bonus:
            self.score += 3
            self.bonus_active = False
            ate = True

        if new == self.super:
            self.score += 5
            self.super_active = False
            if ate == True:
                return False

        if new == self.poison:
            if len(self.snake) > 2:
                self.snake = self.snake[:-2]
            else:
                return False
            self.poison_active = False
            ate = True

        if not ate:
            self.snake.pop()

        return True

    # ---------------- DRAW ----------------
    def draw(self, screen, font):

        screen.fill(BLACK)

        color = tuple(self.settings.get("snake_color", [0, 200, 0]))

        # snake
        for s in self.snake:
            pygame.draw.rect(screen, color, (*s, CELL, CELL))

        # food
        pygame.draw.rect(screen, RED, (*self.food, CELL, CELL))
        pygame.draw.rect(screen, YELLOW, (*self.bonus, CELL, CELL))
        pygame.draw.rect(screen, BLUE, (*self.super, CELL, CELL))
        pygame.draw.rect(screen, DARK_RED, (*self.poison, CELL, CELL))

        # walls
        for w in self.walls:
            pygame.draw.rect(screen, (120,120,120), (*w, CELL, CELL))

        # UI
        screen.blit(font.render(f"Score: {self.score}", True, WHITE), (10, 10))
        screen.blit(font.render(f"Level: {self.level}", True, WHITE), (10, 30))

        # progress bar
        progress = (self.score - self.last_level_score) / self.level_target
        progress = min(progress, 1)

        pygame.draw.rect(screen, (80,80,80), (10,60,200,10))
        pygame.draw.rect(screen, (0,255,0), (10,60,200*progress,10))