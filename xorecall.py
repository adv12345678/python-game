#!/usr/bin/python
# -*- coding:utf8 -*-

__author__ = 'laixintao'

import pygame
from pygame.locals import *
from sys import exit
from math import sqrt
from gameobjects.vector2 import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
clock = pygame.time.Clock()

x=100

class Circle():
    def __init__(self,color,position,radius):
        self.position = position
        self.color = color
        self.radius = radius

    def set_position(self,x,y):
        self.position = (x,y)

    def get_circle(self):
        return (self.color,
                self.position,
                self.radius)

background_circle = Circle((100,100,0),(640/2,480/2),480/2)
point = Circle((255,255,0),(200,200),20)
speed = 100

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    vec = Vector2.from_points(background_circle.position,
                              point.position)
    dis = vec[0]**2 + vec[1]**2
    dis = sqrt(dis)

    if dis+point.radius > background_circle.radius-1:
        if point.position[0]>background_circle.position[0]:
            speed = -100
        else:
            speed = 100
        print speed
    point.set_position(int(point.position[0]+speed*time_passed_seconds),
                       int(point.position[1]+speed*time_passed_seconds))

    pygame.draw.circle(screen,*background_circle.get_circle())
    pygame.draw.circle(screen,*point.get_circle())

    pygame.display.update()