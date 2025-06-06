# # WRITE YOUR SOLUTION HERE:
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

    if robot.get_width() + x < width and y == 0:
        x += velocity
    elif robot.get_width() + x == width and robot.get_height() + y <  height:
        y += velocity
    elif x > 0 and robot.get_height() + y == height:
        x -= velocity
    elif x == 0 and y > 0:
        y -= velocity
    
    clock.tick(260)