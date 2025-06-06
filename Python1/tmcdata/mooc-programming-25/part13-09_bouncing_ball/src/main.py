# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.png")

x = 0
y = 0
clock = pygame.time.Clock()

xvelocity = 5
yvelocity = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    if ball.get_height() + y >= height or y < 0:
        yvelocity = -yvelocity

    if ball.get_width() + x >= width or x < 0:
        xvelocity = -xvelocity

    x += xvelocity
    y += yvelocity
    clock.tick(60)
