import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Trace Simulation")

ball_radius = 5
ball_pos = [width // 2, height // 2]
ball_speed = [5, 5]
ball_color = (255, 255, 255)

trace_length = 5  # Number of previous positions to keep in the trace
trace = 1.5
ball_trace = []    # List to store previous positions
count = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_speed[1] = -ball_speed[1]

    if count % trace == 0: 
        ball_trace.append((int(ball_pos[0]), int(ball_pos[1])))
    if len(ball_trace) > trace_length:
        ball_trace.pop(0)  # Remove the oldest position if trace length exceeds

    screen.fill((0, 0, 0))
    count += 1

    for position in ball_trace:
        pygame.draw.circle(screen, ball_color, position, ball_radius)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
