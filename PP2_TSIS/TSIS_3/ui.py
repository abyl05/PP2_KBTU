import pygame
from persistence import load_leaderboard, save_settings


class Button:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, 200, 40)
        self.text = text
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, screen):
        pygame.draw.rect(screen, (80,80,80), self.rect)
        txt = self.font.render(self.text, True, (255,255,255))
        screen.blit(txt, (self.rect.x + 20, self.rect.y + 5))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.play = Button(100,150,"Play")
        self.leader = Button(100,220,"Leaderboard")
        self.settings = Button(100,290,"Settings")
        self.quit = Button(100,360,"Quit")

    def handle_event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.play.clicked(e.pos): return "play"
            if self.leader.clicked(e.pos): return "leader"
            if self.settings.clicked(e.pos): return "settings"
            if self.quit.clicked(e.pos): return "quit"

    def draw(self):
        self.screen.fill((0,0,0))
        self.play.draw(self.screen)
        self.leader.draw(self.screen)
        self.settings.draw(self.screen)
        self.quit.draw(self.screen)


class LeaderboardScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)

    def handle_event(self, e):
        if e.type == pygame.KEYDOWN:
            return True

    def draw(self):
        self.screen.fill((0,0,0))
        data = load_leaderboard()

        y = 50
        for i, d in enumerate(data):
            txt = self.font.render(f"{i+1}. {d['name']} {d['score']}", True, (255,255,255))
            self.screen.blit(txt, (50,y))
            y += 30


class SettingsScreen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.font = pygame.font.SysFont("Arial", 24)

    def handle_event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_s:
                self.settings["sound"] = not self.settings["sound"]
                save_settings(self.settings)
            if e.key == pygame.K_ESCAPE:
                return True

    def draw(self):
        self.screen.fill((20,20,20))
        txt = self.font.render(str(self.settings), True, (255,255,255))
        self.screen.blit(txt, (50,100))