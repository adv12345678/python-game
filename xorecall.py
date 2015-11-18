#!/usr/bin/env python
# -*- coding:utf8 -*-

__author__ = 'laixintao'

import pygame
from pygame.locals import *
from sys import exit
from math import sqrt
from gameobjects.vector2 import *
from random import uniform

class Circle(object):
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

class Point(Circle):
    def __init__(self,color,position,radius):
        self.speed = 100
        self.vector = get_random_vactor()
        super(Point,self).__init__(color,position,radius)

    def heading_to(self,*direction):
        if len(direction)!=2:
            return self.vector
        else:
            self.vector=(direction[0],direction[1])
        return self.vector

    def move(self):
        time_passed = clock.tick(50)
        time_passed_seconds = time_passed / 1000.0
        self.set_position(int(self.position[0]+
                               self.speed*time_passed_seconds*self.vector[0]),
                       int(self.position[1]+
                           self.speed*time_passed_seconds*self.vector[1]))
        return True

    def bounce(self):
        self.vector = -self.vector
        counter = 0
        while self.is_bounced():
            self.move()
            print self.position,counter
            counter += 1
            if counter == 3:
                self.vector = -Vector2.from_points(background_circle.position,
                                                self.position)
                self.vector.normalise()
                print self.vector

    def is_bounced(self):
        vector_from_center = Vector2.from_points(background_circle.position,
                                             self.position)
        dis = vector_from_center[0]**2 + vector_from_center[1]**2
        dis = sqrt(dis)
        if dis+self.radius >= background_circle.radius:
            return True
        else:
            return False


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

def collision():
    pass

def get_point_list(num):
    x = 100
    y = 100
    point_list = []
    for _ in range(num):
        point = Point((255,255,0),(x,y),20)
        x+=1
        y+=1
        point_list.append(point)
    return point_list

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
clock = pygame.time.Clock()
background_circle = Circle((69,129,116),(640/2,480/2),480/2)
point_list = get_point_list(2)
point = point_list[0]
point2 = point_list[1]


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    # for point in point_list
    if point.is_bounced():
        point.bounce()
    if point2.is_bounced():
        point2.bounce()
    point.move()
    point2.move()
    pygame.draw.circle(screen,*background_circle.get_circle())
    pygame.draw.circle(screen,*point.get_circle())
    pygame.draw.circle(screen,*point2.get_circle())
    pygame.draw.circle(screen,*Circle((200,200,102),(640/2,480/2),2).get_circle()) #center

    pygame.display.update()