import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    tool = 'brush'   # brush, rect, circle, eraser

    points = []
    drawing = False
    start_pos = None

    # Basic colors
    COLORS = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'white': (255, 255, 255)
    }

    canvas = pygame.Surface((640, 480))
    canvas.fill((0, 0, 0))

    while True:
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Color selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                # Tool selection
                elif event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rect'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos

                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    end_pos = event.pos

                    color = COLORS[mode]

                    if tool == 'rect':
                        rect = pygame.Rect(start_pos,
                                           (end_pos[0] - start_pos[0],
                                            end_pos[1] - start_pos[1]))
                        pygame.draw.rect(canvas, color, rect, 2)

                    elif tool == 'circle':
                        dx = end_pos[0] - start_pos[0]
                        dy = end_pos[1] - start_pos[1]
                        radius_circle = int((dx*dx + dy*dy) ** 0.5)
                        pygame.draw.circle(canvas, color, start_pos, radius_circle, 2)

                drawing = False
                points = []

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    position = event.pos

                    if tool == 'brush':
                        points.append(position)
                        points = points[-256:]

                    elif tool == 'eraser':
                        pygame.draw.circle(canvas, (0, 0, 0), position, radius)

        screen.fill((0, 0, 0))
        screen.blit(canvas, (0, 0))

        # Draw brush strokes
        if tool == 'brush':
            for i in range(len(points) - 1):
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)

        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations if iterations != 0 else 0
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


main()