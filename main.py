import pygame
import numpy as np
#import random



pos = np.array([100.0, 200.0])
vel = np.array([10.0, 0.0])
m = 2.0
g = 9.81 * 50
Force = np.array([0.0, -m * g])
acc = np.array([0.0, 0.0])

pygame.init()
width,height = 500,500



screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("1D physics Simulator")

clock = pygame.time.Clock()

ground = height - 50

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    Force = np.array([0.0, -m * g])
    acc = Force / m
    vel += acc * dt
    pos += vel * dt


    r = 16
    e = 0.9
    if pos[1] <= r:
        pos[1] = r
        vel[1] = -e * vel[1]       


    screen.fill((20,20,20))

    pygame.draw.line(screen,(200,200,200),(0,ground), (width,ground),5)

    screeny = ground - pos[1]
    pygame.draw.circle(screen, (0, 255, 0),(int(pos[0]), int(screeny)),r)

    pygame.display.flip()

pygame.quit()