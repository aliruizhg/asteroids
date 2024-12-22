import pygame
from circleshape import CircleShape 
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,WHITE,self.position,self.radius,2)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rotation_angle= random.uniform(20,50)
            angle1=self.velocity.rotate(rotation_angle)
            angle2=self.velocity.rotate(-rotation_angle)
            new_radius= self.radius - ASTEROID_MIN_RADIUS
            child1=Asteroid(self.position.x,self.position.y, new_radius)
            child1.velocity=angle1*1.2
            child2=Asteroid(self.position.x,self.position.y, new_radius)
            child2.velocity=angle2*1.2
