import pygame
from pygame.draw import *

pygame.init()
FPS = 30
sc = pygame.display.set_mode((1024, 640))

yellow = 255, 255, 0
black = 0, 0, 0
red = 255, 0, 0

sc.fill((255, 255, 255))

circle(sc, yellow, (500, 300), 200)  # head
circle(sc, black, (500, 300), 200, 2)

circle(sc, red, (420, 250), 40)
circle(sc, black, (420, 250), 22)  # left eye
circle(sc, black, (420, 250), 40, 2)

circle(sc, red, (580, 250), 35)
circle(sc, black, (580, 250), 22)  # right eye
circle(sc, black, (580, 250), 35, 2)

rect(sc, black, (400, 400, 220, 30))  # mouth
polygon(sc, black, [(330, 130), (340, 120), (470, 200), (460, 210)])  # left brow
polygon(sc, black, [(670, 150), (660, 140), (530, 210), (540, 220)])  # right brow

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
