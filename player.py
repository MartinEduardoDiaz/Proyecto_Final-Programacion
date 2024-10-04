import pygame 
import math as mt


class Player():
    def __init__(self, x,y):
        self.armor = 0
        self.life = 100
        self.x = x
        self.y = y
        self.velocity = 0.5
        self.imagen = pygame.image.load("characters/frame_0.png")
        
    def draw(self,screen):
        self.imagen = pygame.transform.scale(self.imagen, (30,40))
        screen.blit(self.imagen, (self.x,self.y))

    def move(self,keys):
        self.ex = 0
        self.ey = 0

        if keys[pygame.K_s]:
            self.ey += self.velocity
        if keys[pygame.K_w]:
            self.ey -= self.velocity
        if keys[pygame.K_a]:
            self.ex -= self.velocity
        if keys[pygame.K_d]:
            self.ex += self.velocity

        if self.ex != 0 and self.ey != 0:
            self.ex /= mt.sqrt(2)
            self.ey /= mt.sqrt(2) 
        
        self.x += self.ex
        self.y += self.ey 
