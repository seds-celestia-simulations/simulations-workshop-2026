import numpy as np
import pygame

pygame.init()

W, H = 300, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

FPS = 60
x = W // 2
y = 100.0
v = 300.0
r = 20
g = 500

running = True

while running:
    dt = clock.tick(FPS) / 1000  # ms since last frame -> seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # FILL UP
    y += v*dt

    if y+r > H: # condition for collision -> bottom edge past the floor

        # offset = how far the ball sank in. Undo it or the ball stays
        # overlapping next frame and sticks. See README.
        offset = y+r - H
        y -= offset

        v *= -1  # flat floor -> elastic bounce is a sign flip

    v += g*dt  # gravity after the move: semi-implicit Euler

    screen.fill("black")
    pygame.draw.circle(screen, "red", (x, int(y)), r)
    pygame.display.flip()

pygame.quit()
