import pygame
from pygame.draw import *
from math import pi, sin, cos, tan

pygame.init()

FPS = 30
X = 1300
screen = pygame.display.set_mode((X, X))

f1 = X * 3.3 / 9
f2 = X * 5.7 / 9
rect(screen, (160, 82, 45), (0, 0, X, f1))
rect(screen, (128, 128, 0), (0, f1, X, f2))



def okno(x, y, l, w):
    rect(screen, (176, 224, 230), (x, y, l, w))
    rect(screen, (135, 206, 250), (x + l / 20, y + l / 20, l / 2.4, w / 6))
    rect(screen, (135, 206, 250), ((x + l - l / 2.4) - (l / 20), y + l / 20, l / 2.4, w / 6))
    rect(screen, (135, 206, 250), (x + l / 20, (y + w - (l / 20) - w * 0.72), l / 2.4, w * 0.72))
    rect(screen, (135, 206, 250), ((x + l - l / 2.4) - (l / 20), (y + w - (l / 20) - w * 0.72), l / 2.4, w * 0.72))


def cat(x, y, l):
    surface = pygame.Surface((l, l))  # создание площади
    surface.fill((128, 128, 0))  # заливка площади
    ellipse(surface, (210, 105, 30), (l / 2, 0, l * 0.35, l))  # эллипс
    ellipse(surface, 0, (l / 2, 0, l * 0.35, l), 2)  # заливка эллипса
    surface2 = pygame.transform.rotate(surface, 75)  # поворот картинки
    screen.blit(surface2, (x + l * 1.5, y))
    pygame.display.update()
    ellipse(screen, (210, 105, 30), (x, y, l * 2, l * 0.9))  # туловище
    ellipse(screen, 0, (x, y, l * 2, l * 0.9), 2)  # обводка туловища
    ellipse(screen, (210, 105, 30), (x - l * 0.06, y + l * 0.4, l * 0.2, l * 0.4))  # передняя лапка(незаметная)
    ellipse(screen, 0, (x - l * 0.06, y + l * 0.4, l * 0.2, l * 0.4), 2)  # обводка передней лапы(незаметная)
    ellipse(screen, (210, 105, 30), (x - l * 0.2, y + l * 0.01, l * 0.75, (l * 0.75 - 10)))  # голова
    ellipse(screen, 0, (x - l * 0.2, y + l * 0.01, l * 0.75, (l * 0.75 - 10)), 2)  # обводка головы
    ellipse(screen, (210, 105, 30), (x + l * 1.4, y + l * 0.4, l * 0.6, l * 0.6))  # бедро
    ellipse(screen, 0, (x + l * 1.4, y + l * 0.4, l * 0.6, l * 0.6), 2)  # обводка бедро
    ellipse(screen, (210, 105, 30), (x + l * 1.8, y + l * 0.85, l * 0.2, l * 0.4))  # лапа задняя
    ellipse(screen, 0, (x + l * 1.8, y + l * 0.85, l * 0.2, l * 0.4), 2)  # обводка задней лапы
    ellipse(screen, (210, 105, 30), (x + l * 0.07, y + l * 0.73, l * 0.4, l * 0.2))  # лапа передняя
    ellipse(screen, 0, (x + l * 0.07, y + l * 0.73, l * 0.4, l * 0.2), 2)  # лапа передняя обводка
    ellipse(screen, (127, 255, 0), (x + l * 0.24, y + l * 0.24, l * 0.15, l * 0.22))  # правый глаз
    ellipse(screen, 0, (x + l * 0.24, y + l * 0.24, l * 0.15, l * 0.22), 2)  # обводка правого глаза
    surface = pygame.Surface((l * 0.11, l * 0.06))  # создание площади
    surface.fill((127, 255, 0))  # заливка площади
    ellipse(surface, 'white', (l * 0.01, l * 0.001, l * 0.07, l * 0.8))  # эллипс
    surface2 = pygame.transform.rotate(surface, 45)  # поворот картинки
    screen.blit(surface2, (x + l * 0.256, y + l * 0.29))
    pygame.display.update()
    ellipse(screen, (127, 255, 0), (x - l * 0.08, y + l * 0.24, l * 0.15, l * 0.22))  # левый глаз
    ellipse(screen, 0, (x - l * 0.08, y + l * 0.24, l * 0.15, l * 0.22), 2)  # обводка левого глаза
    surface = pygame.Surface((l * 0.11, l * 0.06))  # создание площади
    surface.fill((127, 255, 0))  # заливка площади
    ellipse(surface, 'white', (l * 0.02, l * 0.001, l * 0.07, l * 0.8))  # эллипс
    surface2 = pygame.transform.rotate(surface, 45)  # поворот картинки
    screen.blit(surface2, (x - l * 0.061, y + l * 0.29))
    pygame.display.update()
    ellipse(screen, 0, (x + l * 0.31, y + l * 0.27, l * 0.04, l * 0.18))  # зрачки(правый)
    ellipse(screen, 0, (x + l * 0.001, y + l * 0.27, l * 0.04, l * 0.18))  # зрачки(левый)
    polygon(screen, (255, 228, 181),
            [(x + l * 0.2, y + l * 0.5), (x + l * 0.12, y + l * 0.5), (x + l * 0.16, y + l * 0.55)])  # нос
    polygon(screen, 0, [(x + l * 0.2, y + l * 0.5), (x + l * 0.12, y + l * 0.5), (x + l * 0.16, y + l * 0.55)],
            2)  # обводка носа
    line(screen, 0, (x + l * 0.16, y + l * 0.55), (x + l * 0.16, y + l * 0.6), 2)  # продолжение рта
    arc(screen, 0, (x + l * 0.16, y + l * 0.55, l * 0.09, l * 0.09), pi, pi * 1.75, 2)  # рот
    arc(screen, 0, (x + l * 0.085, y + l * 0.55, l * 0.09, l * 0.09), pi * 1.25, pi * 1.85, 2)  # обводка рта
    polygon(screen, (210, 105, 30),
            [(x - l * 0.3, y - l * 0.05), (x - l * 0.18, y + l * 0.26), (x - l * 0.02, y + l * 0.07)])  # ухо(л)
    polygon(screen, 0, [(x - l * 0.3, y - l * 0.05), (x - l * 0.18, y + l * 0.26), (x - l * 0.02, y + l * 0.07)],
            2)  # ухо(л) обводка
    polygon(screen, (255, 222, 173), [(x - l * 0.27, y - l * 0.017), (x - l * 0.175, y + l * 0.218),
                                      (x - l * 0.05, y + l * 0.075)])  # ухо(л)(внутри)
    polygon(screen, 0, [(x - l * 0.27, y - l * 0.017), (x - l * 0.175, y + l * 0.218), (x - l * 0.05, y + l * 0.075)],
            3)  # ухо(л)(внутри)обводка
    polygon(screen, (210, 105, 30),
            [(x + l * 0.65, y - l * 0.05), (x + l * 0.52, y + l * 0.24), (x + l * 0.38, y + l * 0.075)])  # ухо(п)
    polygon(screen, 0, [(x + l * 0.65, y - l * 0.05), (x + l * 0.52, y + l * 0.24), (x + l * 0.38, y + l * 0.075)],
            2)  # ухо(п) обводка
    polygon(screen, (255, 222, 173), [(x + l * 0.62, y - l * 0.02), (x + l * 0.52, y + l * 0.2),
                                      (x + l * 0.415, y + l * 0.0724)])  # ухо(п)(внутри)
    polygon(screen, 0, [(x + l * 0.62, y - l * 0.02), (x + l * 0.52, y + l * 0.2), (x + l * 0.415, y + l * 0.0724)],
            3)  # ухо(п)(внутри)обводка
    arc(screen, 0, (x + l * 0.2, y + l * 0.48, l * 0.5, l * 0.09), pi / 4, pi * 0.96, )  # усы(п, 1)
    arc(screen, 0, (x + l * 0.2, y + l * 0.52, l * 0.5, l * 0.09), pi / 4, pi * 0.96, )  # усы(п, 2)
    arc(screen, 0, (x + l * 0.2, y + l * 0.56, l * 0.5, l * 0.09), pi / 4, pi * 0.96, )  # усы(п, 3)
    arc(screen, 0, (x - l * 0.38, y + l * 0.48, l * 0.5, l * 0.09), 0, pi * 0.75, )  # усы(л, 1)
    arc(screen, 0, (x - l * 0.38, y + l * 0.52, l * 0.5, l * 0.09), 0, pi * 0.75, )  # усы(л, 2)
    arc(screen, 0, (x - l * 0.38, y + l * 0.56, l * 0.5, l * 0.09), 0, pi * 0.75, )  # усы(л, 3)


def clubok(x, y, r):
    ### Нитка ###
    arc(screen, 'grey', (x, y, r * 0.74, r * 0.32), pi * 0.14, pi * 0.85)
    arc(screen, 'grey', (x + r * 0.663, y - r * 0.165, r * 0.74, r * 0.35), pi * 1.15, pi * 1.33)
    arc(screen, 'grey', (x + r * 0.477, y - r * 0.842, r * 0.74, r), pi * 1.5, pi * 1.7)
    arc(screen, 'grey', (x + r * 0.914, y - r * 0.035, r * 0.74, r), pi * 0.4, pi * 0.7)
    arc(screen, 'grey', (x + r * 1.198, y - r * 0.955, r * 0.74, r), pi * 1.35, pi * 1.8)
    ### Клубок ###
    circle(screen, (169, 169, 169), (x + r * 2, y - r * 0.24), r * 0.4)
    circle(screen, 0, (x + r * 2, y - r * 0.24), r * 0.4, 1)

    ### Нитки на клубке###
    surface = pygame.Surface((r * 0.39, r * 0.39))  # создание площади
    surface.fill('DarkGray')  # заливка площади
    arc(surface, 0, (-r * 0.06, r * 0.1, r * 0.3, r * 0.2), pi / 5, pi * 0.75, 1)
    arc(surface, 0, (-r * 0.06, r * 0.2, r * 0.3, r * 0.2), pi / 5, pi * 0.75, 1)
    arc(surface, 0, (-r * 0.06, r * 0.3, r * 0.3, r * 0.2), pi / 5, pi * 0.75, 1)
    arc(surface, 0, (-r * 0.04, 0, r * 0.3, r * 0.4), pi * 1.7, pi / 3, 1)
    arc(surface, 0, (r * 0.03, 0, r * 0.3, r * 0.4), pi * 1.7, pi / 3, 1)
    arc(surface, 0, (r * 0.09, 0, r * 0.3, r * 0.4), pi * 1.7, pi / 3, 1)

    surface2 = pygame.transform.rotate(surface, 45)  # поворот картинки
    screen.blit(surface2, (x + r * 1.725, y - r * 0.52))
    pygame.display.update()

okno(900, 110, 250, 350)
okno(450, 110, 250, 350)
okno(-120, 110, 250, 350)
clubok(120, 1100, 220)
clubok(120, 1000, 100)
clubok(650, 1120, 100)
clubok(120, 680, 100)
cat(750, 490, 200)
cat(720, 940, 90)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
