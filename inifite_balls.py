import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

ball_radius = 5
balls = [{'pos': [width // 2, height // 2], 'speed': [5, 5], 'color': (255, 0, 0)}]

bright_colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (255, 255, 255),  # White
    (255, 192, 203),  # Pink
    (173, 216, 230)   # Light Blue
]

font = pygame.font.Font(None, 36)
counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for ball in balls:
        ball['pos'][0] += ball['speed'][0]
        ball['pos'][1] += ball['speed'][1]

        if ball['pos'][0] - ball_radius < 0 or ball['pos'][0] + ball_radius > width:
            ball['speed'][0] = -ball['speed'][0]
            random_color = bright_colors[random.randint(0, 9)]
            balls.append({'color': random_color, 'pos': [random.randint(100, 700), random.randint(100, 500)], 'speed': [random.randint(-10, 10), random.randint(-10, 10)]})
            counter += 1

        if ball['pos'][1] - ball_radius < 0 or ball['pos'][1] + ball_radius > height:
            ball['speed'][1] = -ball['speed'][1]
            random_color = bright_colors[random.randint(0, 9)]
            balls.append({'color': random_color, 'pos': [random.randint(100, 700), random.randint(100, 500)], 'speed': [random.randint(-10, 10), random.randint(-10, 10)]})
            counter += 1

    screen.fill((0, 0, 0))

    for ball in balls:
        pygame.draw.circle(screen, ball['color'], (int(ball['pos'][0]), int(ball['pos'][1])), ball_radius)
    text = font.render(f"Balls: {counter}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()

    pygame.time.Clock().tick(60)
