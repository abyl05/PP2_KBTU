import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
CELL = 20  # size of one block
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Font for score
font = pygame.font.SysFont("Arial", 20)


# Generate food NOT on snake
def generate_food(snake):
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            return (x, y)


def main():
    # Initial snake (list of segments)
    snake = [(100, 100), (80, 100), (60, 100)]

    # Initial direction
    dx, dy = CELL, 0

    food = generate_food(snake)

    score = 0
    level = 1
    speed = 5  # initial speed

    running = True
    while running:
        clock.tick(speed)

        # --- EVENTS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Control snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -CELL
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, CELL
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -CELL, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = CELL, 0

        # --- MOVE SNAKE ---
        head_x, head_y = snake[0]
        new_head = (head_x + dx, head_y + dy)

        # --- WALL COLLISION ---
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT
        ):
            print("Game Over! Hit the wall.")
            running = False

        # --- SELF COLLISION ---
        if new_head in snake:
            print("Game Over! Hit yourself.")
            running = False

        snake.insert(0, new_head)

        # --- FOOD COLLISION ---
        if new_head == food:
            score += 1

            # LEVEL UP every 3 foods
            if score % 3 == 0:
                level += 1
                speed += 2  # increase speed

            food = generate_food(snake)
        else:
            snake.pop()  # remove tail if no food eaten

        # --- DRAW ---
        screen.fill(BLACK)

        # Draw snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

        # Draw food
        pygame.draw.rect(screen, RED, (*food, CELL, CELL))

        # Draw score & level
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)

        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 30))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()