# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

robot2 = pygame.image.load("robot.png")

x = 0
y = 30
x2 = 0
y2 = 150
clock = pygame.time.Clock()

velocity = 1
velocity2 = 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()

    if x < 0 or robot.get_width() + x >= width:
        velocity = -velocity

    if x2 < 0 or robot2.get_width() + x2 >= width:
        velocity2 = -velocity2

    x += velocity
    x2 += velocity2
    clock.tick(60)