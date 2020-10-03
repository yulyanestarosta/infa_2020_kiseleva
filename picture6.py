import pygame
from pygame.draw import *

peach = 245, 175, 127
black = 0, 0, 0
white = 255, 255, 255
green = 44, 105, 56
red = 255, 0, 0
pi = 3.14

pygame.init()
FPS = 30
sc = pygame.display.set_mode((1024, 640))
sc.fill(peach)


def leaf(x, y, w, h, angle):  # this draws one leaf
    surf = pygame.Surface((int(3 * w), h))
    surf.fill(peach)
    ellipse(surf, green, (0, 0, w, h))
    surf.set_colorkey(peach)
    surface2 = pygame.transform.rotate(surf, angle)
    surface2.set_alpha(255)
    sc.blit(surface2, (x, y))


def branch_left(x, y, w, h):  # для рефакторинга -- мне было лень думать, как одной функцией написать и правую,
    arc(sc, green, (x, y, w, h), 0, pi / 2 + pi / 10, 3)  # и левую ветки, а по идее можно так сделать


def branch_right(x, y, w, h):
    arc(sc, green, (x, y, w, h), pi / 2, pi, 3)


def branches(w, h):
    branch_left(int(0.6 * w), int(2.55 * h), 6 * w, 3 * h)
    branch_left(int(1.45 * w), int(0.88 * h), int(5.5 * w), 2 * h)  # branches of our bamboo
    branch_right(int(7.8 * w), int(2.95 * h), 6 * w, 3 * h)
    branch_right(int(7.7 * w), int(1.6 * h), 8 * w, 2 * h)


def leaves(w, h):
    leaf(3 * w, int(0.9 * h), int(0.3 * w), int(0.7 * h), 170)  # leaves of the top left branch
    leaf(int(3.6 * w), int(0.9 * h), int(0.3 * w), int(0.7 * h), 170)
    leaf(int(4.2 * w), h, int(0.3 * w), int(0.7 * h), 170)  # для рефакторинга -- напиши функцию,
    leaf(int(4.8 * w), int(h * 1.1), int(0.3 * w), int(0.7 * h), 170)  # которая целую ветку рисует

    leaf(int(2.8 * w), int(2.55 * h), int(0.3 * w), int(0.7 * h), 170)  # leaves of the down left branch
    leaf(int(3.4 * w), int(2.6 * h), int(0.3 * w), int(0.7 * h), 170)
    leaf(4 * w, int(2.8 * h), int(0.3 * w), int(0.7 * h), 170)
    leaf(int(4.5 * w), int(2.95 * h), int(0.3 * w), int(0.7 * h), 170)

    leaf(int(9.5 * w), int(3.05 * h), int(0.3 * w), int(0.7 * h), 190)  # leaves of the down right branch
    leaf(int(8.9 * w), int(3.1 * h), int(0.3 * w), int(0.7 * h), 190)
    leaf(int(8.3 * w), int(3.3 * h), int(0.3 * w), int(0.7 * h), 190)

    leaf(int(10.3 * w), int(1.65 * h), int(0.3 * w), int(0.7 * h), 190)
    leaf(int(9.5 * w), int(1.7 * h), int(0.3 * w), int(0.7 * h), 190)
    leaf(int(8.9 * w), int(1.75 * h), int(0.3 * w), int(0.7 * h), 190)
    leaf(int(8.3 * w), int(1.9 * h), int(0.3 * w), int(0.7 * h), 190)


def bamboo(x, y, w, h):
    polygon(sc, green, [[x, y - h], [x + w, y - h], [x + w, y], [x, y]])     #
    polygon(sc, green, [[x, int(y - 1.1 * h)], [x, int(y - 1.975 * h)],      #
                        [x + w, int(y - 1.975 * h)], [x + w, y - 1.1 * h]])  #
    polygon(sc, green, [[int(x + w / 2), int(y - 2 * h)],                    #
                        [int(x + w), int(y - 2.9 * h)],                      #
                        [int(x + w / 2), int(y - 3 * h)],                    # trunk of our bamboo
                        [int(x), int(y - 2.1 * h)]])                         #
    polygon(sc, green, [[int(x + w), int(y - 3.05 * h)],                     #
                        [int(x + 3 * w / 2), int(y - 3.95 * h)],             #
                        [int(x + w), int(y - 4.05 * h)],                     #
                        [int(x + w / 2), int(y - 3.15 * h)]])                #

    branches(w, h)
    leaves(w, h)


def panda(x, y, w, h):  # our panda has only three legs -- left, middle and right
    ellipse(sc, white, (x, y, w, h))  # body
    ellipse(sc, black, (x, y, w, h), 2)

    polygon(sc, black, [[x, y],
                        [x + int(0.1 * w), y],
                        [x + int(0.15 * w), y + int(1.2 * h)],
                        [x + int(0.05 * w), y + int(1.3 * h)],
                        [x - int(0.05 * w), y + int(1.1 * h)]])  # left leg
    circle(sc, black, (x + int(0.05 * w), y + int(1.2 * h)), int(h / 5))  # left foot

    ellipse(sc, black, (x + int(0.25 * w), y + int(1.25 * h), int(0.3 * w), int(0.3 * h)))   #
    ellipse(sc, black, (x + int(0.28 * w), y + int(1.28 * h), int(0.25 * w), int(0.3 * h)))  # middle foot
    ellipse(sc, black, (x + int(0.20 * w), y + int(1.30 * h), int(0.3 * w), int(0.30 * h)))  #

    polygon(sc, black, [[x + int(0.35 * w), y],
                        [x + int(0.5 * w), y],
                        [x + int(0.5 * w), y + h],
                        [x + int(0.35 * w), y + h]])  # middle leg pt 1
    polygon(sc, black, [[x + int(0.3 * w), y + int(1.5 * h)],
                        [x + int(0.55 * w), y + int(1.4 * h)],
                        [x + int(0.5 * w), y + h],
                        [x + int(0.35 * w), y + h]])  # middle leg pt 2

    circle(sc, black, (x, y - int(0.1 * h)), int(0.2 * h))  # ear 1

    circle(sc, white, (x + int(0.2 * w), y + int(0.3 * h)), int(0.55 * h))
    circle(sc, black, (x + int(0.2 * w), y + int(0.3 * h)), int(0.55 * h), 2)  # head

    circle(sc, black, (x + int(0.3 * w), y - int(0.1 * h)), int(0.2 * h))  # ear 2

    circle(sc, black, (x, y + int(0.3 * h)), int(0.1 * h))  # left eye
    circle(sc, black, (x + int(0.15 * w), y + int(0.3 * h)), int(0.1 * h))  # right eye

    circle(sc, black, (x + int(0.04 * w), y + int(0.6 * h)), int(0.07 * h))  # nose

    ellipse(sc, black, (x + int(0.85 * w), y + int(0.45 * h), int(0.2 * w), int(0.9 * h)))  # right leg
    ellipse(sc, black, (x + int(0.8 * w), y + h, int(0.2 * w), int(0.4 * h)))  # right foot


bamboo(200, 500, 30, 100)
panda(600, 200, 400, 200)
panda(300, 400, 100, 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
