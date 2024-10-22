import pygame 
import config 
import math as mt 

class Enemy():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.enemy_shape = pygame.Rect(0, 0 , 50 , 60)
        self.enemy_shape.center = (self.x, self.y)

    def draw(self, screen):
        self.enemy_shape.topleft = (self.x, self.y)
        pygame.draw.rect(screen, self.color, self.enemy_shape)