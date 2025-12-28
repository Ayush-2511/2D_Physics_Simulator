import pygame
#import random


dt = 0.001
x = 100.0
y = 200.0
vx = 100.0
vy = 0.0
m = 2.0
g = 9.81 * 200


pygame.init()
width,height = 500,500



screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("1D physics Simulator")

clock = pygame.time.Clock()

ground = height - 50

running = True
while running:
    clock.tick(600)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #X- corrdinate
    Fx = 0.0
    ax = Fx/m
    vx = vx + ax*dt
    x = x + vx*dt

    #Y- corrdinate
    Fy = -m *g
    ay = Fy/m
    vy = vy + ay*dt
    y = y + vy*dt

    r = 16
    e = 0.9
    if y <= r:
        y = r
        vy = -e * vy       


    screen.fill((20,20,20))

    pygame.draw.line(screen,(200,200,200),(0,ground), (width,ground),5)

    screeny = ground - y
    pygame.draw.circle(screen, (0, 255, 0),(x, int(screeny)),r)

    pygame.display.flip()

pygame.quit()