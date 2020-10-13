import pygame
from pygame.draw import *
from random import randint
from math import *
pygame.init()

# let's define colors of our balls
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)
colors = [red, blue, yellow, green, magenta, cyan]

num = 3
radius_min = 20
radius_max = 100
width = 1200
height = 600
FPS = 60
screen = pygame.display.set_mode((width, height))
pygame.time.delay(2000)
screen.fill(black)
pygame.display.update()

count = 0


def new_balls(num): # this function draws num balls
    global x, y, r, v, angle, color
    x = []
    y = []
    r = []
    v = []
    angle = []
    color = []
    for i in range(num):
        x.append(randint(radius_max, width - radius_max))
        y.append(randint(radius_max, height - radius_max))
        r.append(randint(radius_min, radius_max))
        v.append(randint(10, 500))
        v[i] = float(v[i])
        angle.append(randint(0, 360))
        angle[i] = radians(angle[i])
        color.append(colors[randint(0, 5)])
        circle(screen, color[i], (x[i], y[i]), r[i])


def respawn(i):  # this function creates a new ball if player clicked successfully
    x[i] = randint(radius_max, width - radius_max)
    y[i] = randint(radius_max, height - radius_max)
    r[i] = randint(radius_min, radius_max)
    v[i] = randint(10, 500)
    angle[i] = randint(0, 360)
    angle[i] = radians(angle[i])
    color[i] = colors[randint(0, 5)]
    circle(screen, color[i], (x[i], y[i]), r[i])
    pygame.display.update()


def move_balls(num):  # this function moves our balls
    global x, y, r, v, angle, color, angle
    for i in range(num):
        circle(screen, black, (x[i], y[i]), r[i])
        x[i] += round(v[i] / FPS * cos(angle[i]))
        y[i] -= round(v[i] / FPS * sin(angle[i]))
        circle(screen, color[i], (x[i], y[i]), r[i])
        pygame.display.update()
    hit_check(num)


def score(points):  # this function counts how many times the click was successful and shows us the number
    rect(screen, green, (0, 0, 150, 40))
    my_font = pygame.font.Font(None, 50)
    string = "Удачных попаданий: " + str(points)
    if points < 0:
        text_color = red
    else:
        text_color = black
    text = my_font.render(string, 1, text_color)
    screen.blit(text, (3, 3))


def hit_check(num):  # this function checks if the ball hit the wall and turns it back
    global x, y, r, angle
    for i in range(num):
        if x[i] + r[i] > width - 10:
            angle[i] = radians(90 + randint(10, 170))
        if x[i] - r[i] < 0 + 10:
            angle[i] = radians(randint(10, 170) - 90)
        if y[i] + r[i] > height - 10:
            angle[i] = radians(randint(10, 170))
        if y[i] - r[i] < 0 + 10:
            angle[i] = radians(randint(10, 170) - 180)
        angle[i] %= 2 * pi


def check_click(event, num):  # this function checks if the player clicked successfully
    global count, x, y, r, v, angle, color
    coord = event.pos
    for i in range(num):
        if (x[i] - coord[0]) ** 2 + (y[i] - coord[1]) ** 2 <= r[i] ** 2:
            count += 1
            circle(screen, black, (x[i], y[i]), r[i])
            respawn(i)


pygame.display.update()
clock = pygame.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    new_balls(num)
    pygame.display.update()
    f = True
    while f:
        clock.tick(FPS)
        move_balls(num)
        score(count)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                f = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check_click(event, num)
    screen.fill(black)
    pygame.display.update()

pygame.quit()
