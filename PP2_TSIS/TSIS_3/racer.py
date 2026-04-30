import pygame
import random
import os
from persistence import save_score

# ===================== PATH =====================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE_DIR, "assets")

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

PLAYER_SIZE = (40, 70)
ENEMY_SIZE = (40, 70)
COIN_SIZE = (25, 25)
POWER_SIZE = (30, 30)
EVENT_SIZE = (60, 20)


# ===================== PLAYER =====================
class Player(pygame.sprite.Sprite):
    def __init__(self, color="blue"):
        super().__init__()

        file_map = {
            "blue": "Player_blue.png",
            "green": "Player_green.png"
        }

        img_file = file_map.get(color, "Player_blue.png")

        img = pygame.image.load(os.path.join(ASSETS, img_file)).convert_alpha()
        self.image = pygame.transform.smoothscale(img, PLAYER_SIZE)

        self.rect = self.image.get_rect(center=(200, 500))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5

        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5


# ===================== ENEMY =====================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        img = pygame.image.load(os.path.join(ASSETS, "Enemy.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(img, ENEMY_SIZE)

        self.rect = self.image.get_rect(center=(random.randint(40, 360), -100))

    def update(self, speed):
        self.rect.y += speed

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = -100
            self.rect.centerx = random.randint(40, 360)


# ===================== COIN =====================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        img = pygame.image.load(os.path.join(ASSETS, "coin.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(img, COIN_SIZE)

        self.rect = self.image.get_rect(center=(random.randint(40, 360), -120))

    def update(self, speed):
        self.rect.y += speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.centerx = random.randint(40, 360)
            self.rect.y = -120


# ===================== POWERUPS =====================
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.type = random.choice(["nitro", "shield"])

        img_name = "nitro.png" if self.type == "nitro" else "shield.png"

        img = pygame.image.load(os.path.join(ASSETS, img_name)).convert_alpha()
        self.image = pygame.transform.smoothscale(img, POWER_SIZE)

        self.rect = self.image.get_rect(center=(random.randint(40, 360), -150))

    def update(self, speed):
        self.rect.y += speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# ===================== ROAD EVENTS =====================
class RoadEvent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.type = random.choice(["oil", "boost"])
        img_name = "oil.png" if self.type == "oil" else "boost.png"

        img = pygame.image.load(os.path.join(ASSETS, img_name)).convert_alpha()
        self.image = pygame.transform.smoothscale(img, EVENT_SIZE)

        self.rect = self.image.get_rect(center=(random.randint(60, 340), -80))

    def update(self, speed):
        self.rect.y += speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# ===================== GAME =====================
class RacerGame:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.bg = pygame.image.load(os.path.join(ASSETS, "AnimatedStreet.png")).convert()
        self.bg = pygame.transform.scale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # 🎨 COLOR
        color = settings.get("car_color", "blue")
        self.player = Player(color)

        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.events = pygame.sprite.Group()

        self.all = pygame.sprite.Group(self.player)

        # enemies
        for _ in range(3):
            e = Enemy()
            self.enemies.add(e)
            self.all.add(e)

        # coin
        self.coin = Coin()
        self.coins.add(self.coin)
        self.all.add(self.coin)

        # difficulty
        diff = settings.get("difficulty", "normal")

        if diff == "easy":
            self.speed = 3
        elif diff == "hard":
            self.speed = 6
        else:
            self.speed = 4

        self.score = 0
        self.distance = 0

        self.active_power = None
        self.power_timer = 0

        self.name = ""

        self.font = pygame.font.SysFont("Arial", 20)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "quit"

    def update(self):
        self.player.move()

        for e in self.enemies:
            e.update(self.speed)

        for c in self.coins:
            c.update(self.speed)

        for p in self.powerups:
            p.update(self.speed)

        for ev in self.events:
            ev.update(self.speed)

        # spawn powerups
        if random.random() < 0.01:
            p = PowerUp()
            self.powerups.add(p)
            self.all.add(p)

        # spawn events
        if random.random() < 0.01:
            ev = RoadEvent()
            self.events.add(ev)
            self.all.add(ev)

        # coins
        for c in pygame.sprite.spritecollide(self.player, self.coins, False):
            self.score += 10
            c.rect.y = -120

        # powerups
        for p in pygame.sprite.spritecollide(self.player, self.powerups, True):

            self.active_power = p.type

            if p.type == "nitro":
                self.speed = 10
                self.power_timer = pygame.time.get_ticks() + 2000

            elif p.type == "shield":
                self.power_timer = pygame.time.get_ticks() + 5000

        # events
        for ev in pygame.sprite.spritecollide(self.player, self.events, True):
            if ev.type == "oil":
                self.speed = max(2, self.speed - 2)
            else:
                self.speed += 2

        # nitro end
        if self.active_power == "nitro":
            if pygame.time.get_ticks() > self.power_timer:
                self.speed = 4
                self.active_power = None

        # collision
        if pygame.sprite.spritecollideany(self.player, self.enemies):

            if self.active_power == "shield":
                self.active_power = None
            else:
                save_score(
                    self.name if self.name else "Unknown",
                    self.score,
                    self.distance
                )
                return "game_over"

        self.distance += self.speed

    def draw(self):

        self.screen.blit(self.bg, (0, 0))

        self.all.draw(self.screen)

        self.screen.blit(self.font.render(f"Name: {self.name}", True, (255,255,255)), (10, 10))
        self.screen.blit(self.font.render(f"Score: {self.score}", True, (255,255,255)), (10, 30))
        self.screen.blit(self.font.render(f"Dist: {int(self.distance)}", True, (255,255,255)), (10, 50))
        self.screen.blit(self.font.render(f"Power: {self.active_power}", True, (255,255,255)), (10, 70))