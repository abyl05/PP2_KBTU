import pygame
import sys
import datetime
import os

from tools import *

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# ======================
# STATE
# ======================
tool = "pencil"
drawing = False
start_pos = None
last_pos = None

colors = [(0,0,0), (255,0,0), (0,0,255)]
color_index = 0
color = colors[color_index]

brush_size = 2

font = pygame.font.SysFont("Arial", 20)

# text
text_mode = False
text_input = ""
text_pos = (0,0)

# ======================
# SAVE
# ======================
def save():
    os.makedirs("saves", exist_ok=True)
    name = datetime.datetime.now().strftime("saves/paint_%Y%m%d_%H%M%S.png")
    pygame.image.save(canvas, name)
    print("Saved:", name)

# ======================
# MAIN LOOP
# ======================
running = True
while running:
    screen.fill((200,200,200))
    screen.blit(canvas, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ========= KEYBOARD =========
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p: tool = "pencil"
            if event.key == pygame.K_l: tool = "line"
            if event.key == pygame.K_r: tool = "rect"
            if event.key == pygame.K_c: tool = "circle"
            if event.key == pygame.K_q: tool = "square"
            if event.key == pygame.K_w: tool = "rtri"
            if event.key == pygame.K_e: tool = "etri"
            if event.key == pygame.K_d: tool = "rhombus"
            if event.key == pygame.K_f: tool = "fill"
            if event.key == pygame.K_t: tool = "text"

            # цвета
            if event.key == pygame.K_4:
                color_index = (color_index + 1) % 3
                color = colors[color_index]

            # размер кисти
            if event.key == pygame.K_1: brush_size = 2
            if event.key == pygame.K_2: brush_size = 5
            if event.key == pygame.K_3: brush_size = 10

            # сохранить
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save()

            # текст
            if text_mode:
                if event.key == pygame.K_RETURN:
                    txt = font.render(text_input, True, color)
                    canvas.blit(txt, text_pos)
                    text_mode = False
                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

        # ========= MOUSE =========
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tool == "pencil":
                drawing = True
                last_pos = event.pos
            elif tool in ["line","rect","circle","square","rtri","etri","rhombus"]:
                start_pos = event.pos
                drawing = True
            elif tool == "fill":
                flood_fill(canvas, event.pos[0], event.pos[1], color, WIDTH, HEIGHT)
            elif tool == "text":
                text_mode = True
                text_pos = event.pos
                text_input = ""

        if event.type == pygame.MOUSEBUTTONUP:
            if tool == "pencil":
                drawing = False

            elif drawing:
                end = event.pos

                if tool == "line":
                    pygame.draw.line(canvas, color, start_pos, end, brush_size)
                elif tool == "rect":
                    draw_rectangle(canvas, color, start_pos, end, brush_size)
                elif tool == "circle":
                    draw_circle(canvas, color, start_pos, end, brush_size)
                elif tool == "square":
                    draw_square(canvas, color, start_pos, end, brush_size)
                elif tool == "rtri":
                    draw_right_triangle(canvas, color, start_pos, end, brush_size)
                elif tool == "etri":
                    draw_equilateral_triangle(canvas, color, start_pos, end, brush_size)
                elif tool == "rhombus":
                    draw_rhombus(canvas, color, start_pos, end, brush_size)

                drawing = False

        if event.type == pygame.MOUSEMOTION:
            if tool == "pencil" and drawing:
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    # ========= PREVIEW =========
    if drawing and tool != "pencil":
        mouse = pygame.mouse.get_pos()

        if tool == "line":
            pygame.draw.line(screen, color, start_pos, mouse, brush_size)
        elif tool == "rect":
            draw_rectangle(screen, color, start_pos, mouse, brush_size)
        elif tool == "circle":
            draw_circle(screen, color, start_pos, mouse, brush_size)
        elif tool == "square":
            draw_square(screen, color, start_pos, mouse, brush_size)
        elif tool == "rtri":
            draw_right_triangle(screen, color, start_pos, mouse, brush_size)
        elif tool == "etri":
            draw_equilateral_triangle(screen, color, start_pos, mouse, brush_size)
        elif tool == "rhombus":
            draw_rhombus(screen, color, start_pos, mouse, brush_size)

    # текст preview
    if text_mode:
        preview = font.render(text_input, True, color)
        screen.blit(preview, text_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
