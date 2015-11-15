#!/usr/bin/env python
# -*- coding:utf8 -*-

__author__ = 'laixintao'

import pygame
from pygame.locals import *
from sys import exit
from math import sqrt
from gameobjects.vector2 import *
from random import uniform

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
clock = pygame.time.Clock()

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

def get_random_float(start,end,decimals=1):
    float1 = uniform(start,end)
    float1 = round(float1,decimals)
    return float1

def get_random_vactor():
    "To generate a random direction for every ball."
    x = get_random_float(-10,10)
    y = get_random_float(-10,10)
    random_vactor = Vector2(x,y).normalise()
    return random_vactor

background_circle = Circle((100,100,0),(640/2,480/2),480/2)
point = Circle((255,255,0),(200,200),20)
speed = 100
vector = get_random_vactor()
print vector

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    vec = Vector2.from_points(background_circle.position,
                              point.position)
    dis = vec[0]**2 + vec[1]**2
    dis = sqrt(dis)

    if int(dis+point.radius) >= background_circle.radius-4:
        print "before ->",vector
        vec_normal = vec
        vec_normal.normalise()
        au = vec_normal * vector
        d = au * vec_normal
        vector = 2*d - vector
        vector.normalise()
        # vector = -vector
        
        print "after ->",vector
        # point.set_position(int(point.position[0]+speed*time_passed_seconds*vector[0]),
        #                int(point.position[1]+speed*time_passed_seconds*vector[1]))
        # point.set_position(int(point.position[0]+speed*time_passed_seconds*vector[0]),
        #                int(point.position[1]+speed*time_passed_seconds*vector[1]))
        # point.set_position(int(point.position[0]+speed*time_passed_seconds*vector[0]),
        #                int(point.position[1]+speed*time_passed_seconds*vector[1]))

    point.set_position(int(point.position[0]+speed*time_passed_seconds*vector[0]),
                       int(point.position[1]+speed*time_passed_seconds*vector[1]))

    pygame.draw.circle(screen,*background_circle.get_circle())
    pygame.draw.circle(screen,*point.get_circle())

    pygame.display.update()