import pygame
import sys
from racer import RacerGame
from persistence import load_leaderboard, load_settings, save_settings

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)
small = pygame.font.SysFont("Arial", 20)
big = pygame.font.SysFont("Arial", 50)

state = "menu"
name = ""
game = None

menu = ["Play", "Leaderboard", "Settings", "Quit"]
sel = 0

settings = load_settings()
set_opt = ["Sound", "Difficulty", "Car Color", "Back"]
set_sel = 0

game_over_time = 0
last_dist = 0


while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # MENU
        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sel = (sel - 1) % len(menu)
                if event.key == pygame.K_DOWN:
                    sel = (sel + 1) % len(menu)

                if event.key == pygame.K_RETURN:
                    if menu[sel] == "Play":
                        state = "input"
                    elif menu[sel] == "Leaderboard":
                        state = "leaderboard"
                    elif menu[sel] == "Settings":
                        state = "settings"
                    else:
                        sys.exit()

        # INPUT NAME
        elif state == "input":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN and name:
                    game = RacerGame(screen, settings)
                    game.name = name
                    state = "game"
                else:
                    name += event.unicode

        # SETTINGS
        elif state == "settings":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    set_sel = (set_sel - 1) % len(set_opt)
                if event.key == pygame.K_DOWN:
                    set_sel = (set_sel + 1) % len(set_opt)

                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    if set_opt[set_sel] == "Car Color":
                        colors = ["blue", "green"]
                        i = colors.index(settings["car_color"])
                        settings["car_color"] = colors[(i+1)%2]

                if event.key == pygame.K_RETURN and set_opt[set_sel] == "Back":
                    save_settings(settings)
                    state = "menu"

                if event.key == pygame.K_ESCAPE:
                    state = "menu"

        # GAME
        elif state == "game":
            r = game.handle_event(event)
            if r == "quit":
                state = "menu"

        # LEADERBOARD
        elif state == "leaderboard":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = "menu"


    # MENU
    if state == "menu":
        screen.blit(font.render("RACER",1,(255,255,255)),(140,100))
        for i,v in enumerate(menu):
            c = (0,255,0) if i==sel else (255,255,255)
            screen.blit(font.render(v,1,c),(140,200+i*50))

    # INPUT
    elif state == "input":
        screen.blit(font.render("Enter Name",1,(255,255,255)),(120,200))
        screen.blit(font.render(name,1,(0,255,0)),(120,250))

    # GAME
    elif state == "game":
        r = game.update()
        game.draw()

        if r == "game_over":
            last_dist = int(game.distance)
            game_over_time = pygame.time.get_ticks()
            state = "game_over"

    # GAME OVER
    elif state == "game_over":
        screen.blit(big.render("GAME OVER",1,(255,0,0)),(60,200))
        screen.blit(font.render(f"Distance: {last_dist}",1,(255,255,255)),(90,300))

        if pygame.time.get_ticks() - game_over_time > 2000:
            name = ""
            state = "menu"

    # LEADERBOARD
    elif state == "leaderboard":
        screen.blit(font.render("Leaderboard",1,(255,255,255)),(120,50))
        data = load_leaderboard()

        for i,e in enumerate(data):
            screen.blit(small.render(f"{i+1}. {e['name']} - {e['distance']}",1,(255,255,255)),(60,120+i*25))

    # SETTINGS
    elif state == "settings":
        screen.blit(font.render("Settings",1,(255,255,255)),(130,80))
        vals = [settings.get("sound","ON"),
                settings.get("difficulty","normal"),
                settings.get("car_color","blue"),
                ""]

        for i,v in enumerate(set_opt):
            col = (0,255,0) if i==set_sel else (255,255,255)
            txt = f"{v}: {vals[i]}" if v!="Back" else "Back"
            screen.blit(font.render(txt,1,col),(80,180+i*60))

    pygame.display.update()
    clock.tick(60)