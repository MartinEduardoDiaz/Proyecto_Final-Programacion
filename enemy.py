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
        self.speed = 0.1

    def draw(self, screen):
        self.enemy_shape.topleft = (self.x, self.y)
        pygame.draw.rect(screen, self.color, self.enemy_shape, 1)

            
    def death(self):
        if self.life <= 0: 
            self.life = 0
            self.estatus = False
    
    
    def move(self, to_x: int, to_y: int):
        self.ex = to_x - self.x
        self.ey = to_y - self.y
        distance = mt.sqrt((self.ex - self.x)**2 + (self.ey - self.y)**2)  

        if distance != 0: 
            self.ex /= distance
            self.ey /= distance
        self.x += self.ex * self.speed
        self.y += self.ey * self.speed

    