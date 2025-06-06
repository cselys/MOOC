# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robots = [robot] * 10
angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(10):
        x = 320+math.cos(angle + i * 120)*100-robot.get_width()/2
        y = 240+math.sin(angle + i * 120)*100-robot.get_height()/2        
        window.blit(robots[i], (x, y))
    
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)

    # for i in range(number):
    #     x = width/2+math.cos(angle+2*math.pi*i/number)*radius-robot.get_width()/2
    #     y = height/2+math.sin(angle+2*math.pi*i/number)*radius-robot.get_height()/2
    #     screen.blit(robot, (x, y))
    # pygame.display.flip()