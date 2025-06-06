# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

target_x = random.randint(0, 640)
target_y = random.randint(0, 480)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:            
            if event.pos[0] > target_x and event.pos[0] < target_x + robot.get_width() and \
               event.pos[1] > target_y and event.pos[1] < target_y + robot.get_height(): 
                target_x = random.randint(0, 640)
                target_y = random.randint(0, 480)

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (target_x, target_y))
    pygame.display.flip()

    clock.tick(60)