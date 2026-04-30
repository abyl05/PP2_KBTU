import pygame, sys, json
from game import Game
from db import *
from config import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 24)

init()

# -------- SETTINGS --------
def load_settings():
    try:
        return json.load(open("settings.json"))
    except:
        return {"snake_color":[0,200,0],"grid":False,"sound":True}

def save_settings(s):
    json.dump(s, open("settings.json","w"))

settings = load_settings()

# -------- STATE --------
state = "menu"
name = ""
game = None
pid = None

clock = pygame.time.Clock()

while True:
    screen.fill((0,0,0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        # MENU
        if state == "menu":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    state = "input"
                if e.key == pygame.K_2:
                    state = "leaderboard"
                if e.key == pygame.K_3:
                    state = "settings"
                if e.key == pygame.K_4:
                    sys.exit()

        # INPUT
        elif state == "input":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and name:
                    pid = get_player(name)
                    game = Game(settings)
                    game.dx, game.dy = CELL, 0
                    state = "game"

                elif e.key == pygame.K_BACKSPACE:
                    name = name[:-1]

                else:
                    if len(name) < 10:
                        name += e.unicode

        # GAME
        elif state == "game":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT: game.dx,game.dy=-CELL,0
                if e.key == pygame.K_RIGHT: game.dx,game.dy=CELL,0
                if e.key == pygame.K_UP: game.dx,game.dy=0,-CELL
                if e.key == pygame.K_DOWN: game.dx,game.dy=0,CELL

        # SETTINGS
        elif state == "settings":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    settings["grid"] = not settings["grid"]

                if e.key == pygame.K_2:
                    settings["sound"] = not settings["sound"]

                if e.key == pygame.K_3:
                    settings["snake_color"] = [0,255,0]

                if e.key == pygame.K_4:
                    settings["snake_color"] = [0,0,255]

                if e.key == pygame.K_ESCAPE:
                    save_settings(settings)
                    state = "menu"

        # LEADERBOARD
        elif state == "leaderboard":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    state = "menu"

    # -------- MENU --------
    if state == "menu":
        screen.blit(font.render("1 PLAY",True,WHITE),(250,150))
        screen.blit(font.render("2 LEADERBOARD",True,WHITE),(250,200))
        screen.blit(font.render("3 SETTINGS",True,WHITE),(250,250))
        screen.blit(font.render("4 QUIT",True,WHITE),(250,300))

    # -------- INPUT --------
    elif state == "input":
        screen.blit(font.render("NAME: "+name,True,GREEN),(200,200))

    # -------- GAME --------
    elif state == "game":
        if not game.update():
            save_score(pid,game.score,game.level)
            state = "menu"
            name = ""
            game = None
        else:
            game.draw(screen,font)

    # -------- SETTINGS --------
    elif state == "settings":
        screen.blit(font.render("1 GRID",True,WHITE),(250,150))
        screen.blit(font.render("1 GRID",False,WHITE),(250,150))
        screen.blit(font.render("2 SOUND",True,WHITE),(250,150))
        screen.blit(font.render("2 SOUND",False,WHITE),(250,200))
        screen.blit(font.render("3 GREEN",True,WHITE),(250,250))
        screen.blit(font.render("4 BLUE",True,WHITE),(250,300))
        screen.blit(font.render("ESC SAVE",True,WHITE),(250,350))

    # -------- LEADERBOARD --------
    elif state == "leaderboard":
        data = leaderboard()
        y = 150
        for i,row in enumerate(data):
            screen.blit(font.render(f"{i+1}. {row[0]} {row[1]}",True,WHITE),(200,y))
            y += 30

        screen.blit(font.render("ESC BACK",True,WHITE),(250,450))

    pygame.display.update()
    clock.tick(FPS)