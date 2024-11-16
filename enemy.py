import pygame 
import config 
import math as mt 

class Enemy():
    def __init__(self,x: int,y: int):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.radius  = 10
        self.enemy_shape = pygame.Rect(0, 0 , 50 , 60)
        self.enemy_shape.center = (self.x , self.y)
        self.life = 100
        self.estatus = True


    def draw(self, screen):
        self.enemy_shape.topleft = (self.x, self.y)
        pygame.draw.rect(screen, self.color, self.enemy_shape, 1)

            
    def death(self):
        if self.life <= 0: 
            self.life = 0
            self.estatus = False