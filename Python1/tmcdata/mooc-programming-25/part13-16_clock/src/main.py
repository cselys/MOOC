# WRITE YOUR SOLUTION HERE:
import pygame
import math
from datetime import datetime

pygame.init()
display = pygame.display.set_mode((640, 480))

center = (320, 240)

clock = pygame.time.Clock()
now = datetime.now()
times = now.time().strftime("%H:%M:%S").split(":")
sec = int (times[2])
x = 50
y = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()    
    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 0, 0), center, 205)
    pygame.draw.circle(display, (0, 0, 0), center, 200)
    pygame.draw.circle(display, (255, 0, 0), center, 10)

    pygame.draw.line(display, (0, 0, 255), center, (center[0] + math.cos(2*math.pi * (sec-15)/60)*190, center[1]+ math.sin(2*math.pi* (sec-15)/60)*190), 1)
    pygame.draw.line(display, (0, 0, 255), center, (center[0] + math.cos(2*math.pi * (int(times[1])-15)/60)*170, center[1]+ math.sin(2*math.pi* (int(times[1])-15)/60)*170), 2)
    pygame.draw.line(display, (0, 0, 255), center, (center[0] + math.cos(2*math.pi * (int(times[0]) * 5 -15)/60)*120, center[1]+ math.sin(2*math.pi* (int(times[0]) * 5-15)/60)*120), 4)
    
    pygame.display.flip()

    if sec < 60:
        sec += 1
    else:
        sec = 0

    clock.tick(1)

