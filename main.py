import pygame
import random
import sys

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

GRID_SIZE = 18
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_GRAY = (200, 200, 200)


def render(screen, snake, apple):
    screen.fill(WHITE)
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (0, y), (SCREEN_WIDTH, y))
    for segment in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )
    pygame.draw.rect(
        screen, RED, (apple[0] * CELL_SIZE, apple[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = [[GRID_SIZE // 2, GRID_SIZE // 2]]
    apple = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
    direction = "NONE"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        head = snake[0].copy()
        if direction == "UP":
            head[1] -= 1
            if head[1] < 0:
                head[1] = GRID_SIZE - 1
        elif direction == "DOWN":
            head[1] += 1
            if head[1] == GRID_SIZE:
                head[1] = 0
        elif direction == "LEFT":
            head[0] -= 1
            if head[0] < 0:
                head[0] = GRID_SIZE - 1
        elif direction == "RIGHT":
            head[0] += 1
            if head[0] == GRID_SIZE:
                head[0] = 0

        if head == apple:
            apple = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
        else:
            if head in snake[1:]:
                running = False
            else:
                snake.pop()

        snake.insert(0, head)

        render(screen, snake, apple)
        clock.tick(10)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
