import pygame
from pygame.math import Vector2
#import random


"""dt = 0.001
x = 100.0
y = 200.0
vx = 100.0
vy = 0.0
m = 2.0
g = 9.81 * 200"""




pos = Vector2(100.0, 200.0)
vel = Vector2(10.0, 0.0)
m = 2.0
g = 9.81 * 50
Force = Vector2(0.0, -m * g)
acc = Vector2(0.0, 0.0)

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


    Force = Vector2(0.0, -m * g)
    acc = Force / m
    vel += acc * dt
    pos += vel * dt


    r = 16
    e = 0.9
    if pos.y <= r:
        pos.y = r
        vel.y = -e * vel.y       


    screen.fill((20,20,20))

    pygame.draw.line(screen,(200,200,200),(0,ground), (width,ground),5)

    screeny = ground - pos.y
    pygame.draw.circle(screen, (0, 255, 0),(int(pos.x), int(screeny)),r)

    pygame.display.flip()

pygame.quit()