# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

x = 0
y = 0
clock = pygame.time.Clock()

velocity = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if velocity > 0 and robot.get_height() + y >= height:
        velocity = -velocity
    
    if velocity < 0 and  y <= 0:
        velocity = -velocity

    y += velocity
    clock.tick(60)