from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import random

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
score = 0
a = -5
number_of_targets = int(input("Number of targets: "))


class ball:
    def __init__(self, x=40, y=500):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = random.randint(10, 30)
        self.vx = 0
        self.vy = 0
        self.t = 0
        self.color = choice(['blue', 'magenta', 'pink', 'purple'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        Y = 600
        X = 800
        if (abs(self.x + self.vx - X / 2) < X / 2 - self.r) and (abs(self.y + self.vy - Y / 2) < Y / 2 - self.r):
            self.x += self.vx
            self.y += self.vy
        elif (abs(self.x + self.vx - X / 2) > X / 2 - self.r) and (abs(self.y + self.vy - Y / 2) < Y / 2 - self.r):
            self.vx = -self.vx
        elif (abs(self.x + self.vx - X / 2) < X / 2 - self.r) and (abs(self.y + self.vy - Y / 2) > Y / 2 - self.r):
            self.vy = -self.vy
            self.x += self.vx
        else:
            self.vy = -self.vy
            self.vx = -self.vx
        self.vy -= a

        self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:
            return True
        else:
            return False


class gun:

    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 500, 50, 420, width=9)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 500) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='red')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 500,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    500 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='red')
        else:
            canv.itemconfig(self.id, fill='black')


class target:

    def __init__(self):
        self.points = 0
        self.live = 1
        self.vx = random.randint(0, 5)
        self.vy = random.randint(0, 5)
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.vx = 0
        self.vy = 0
        self.x = -100
        self.y = -100
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        self.points += points

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        '''
    '''

        Y = 600
        X = 800
        if (abs(self.x + self.vx - X / 2) < X / 2 - self.r) and (abs(self.y + self.vy - Y / 2) < Y / 2 - self.r):
            self.x += self.vx
            self.y += self.vy
        elif (abs(self.x + self.vx - X / 2) > X / 2 - self.r) and (abs(self.y + self.vy - Y / 2) < Y / 2 - self.r):
            self.vx = -self.vx
        elif (abs(self.x + self.vx - X / 2) < X / 2 - self.r) and (abs(self.y + self.vy - Y / 2) > Y / 2 - self.r):
            self.vy = -self.vy
            self.x += self.vx
        else:
            self.vy = -self.vy
            self.vx = -self.vx

        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )


screen1 = canv.create_text(400, 300, text='', font='28')
points = canv.create_text(30, 30, text=score, font='28')
g1 = gun()
balls = []
targets = []
bullet = 0
for i in range(number_of_targets):
    targets.append(target())


def new_game(event=''):
    global gun, screen1, balls, bullet, targets, score
    for i in targets:
        i.new_target()
        i.live = 1
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    flag = False
    for i in targets:
        if i.live == 1:
            flag = True
    while flag or balls:
        for b in balls:
            b.move()
            for i in range(len(targets)):
                if b.hittest(targets[i]) and targets[i].live:
                    targets[i].live = 0
                    targets[i].hit()
                    score += targets[i].points
                    canv.create_rectangle(10, 10, 50, 50, fill='red')
                    points = canv.create_text(30, 30, text=score, font='28')
                    canv.itemconfig(screen1,
                                    text='You destroyed the target in ' + str(bullet) + ' shot(s)')
        for t in targets:
            t.move()
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()

tk.mainloop()
