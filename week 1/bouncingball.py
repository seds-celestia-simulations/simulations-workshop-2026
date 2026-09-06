import numpy as np
import pygame

pygame.init()

W, H = 300, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = 100.0
v = 300.0
r = 20

running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # FILL UP

    screen.fill("black")
    pygame.draw.circle(screen, "red", (x, int(y)), r)
    pygame.display.flip()

pygame.quit()