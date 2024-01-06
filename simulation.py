import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Set up the ball
ball_radius = 20
ball_pos = [width // 2, height // 2]
ball_speed = [5, 5]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off the walls and increase speed on collision
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
        ball_speed[0] = -ball_speed[0]
        ball_speed[0] *= 1.1  # Increase speed on collision

    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_speed[1] = -ball_speed[1]
        ball_speed[1] *= 1.1  # Increase speed on collision

    # Draw the ball on the screen
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
