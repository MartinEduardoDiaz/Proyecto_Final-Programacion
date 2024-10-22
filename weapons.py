import pygame
import math as mt 




class Weapon():
    def __init__(self,AD, colldown):
        self.AD = AD
        self.colldown = colldown
    

    def attack(self,other):
        other.life -= self.AD
        if other.life <= 0:
            other.death()


class Melee(Weapon):
    def __init__(self, AD, colldown, x , y):
        super().__init__(AD, colldown)
        self.__x = x 
        self.__y = y

    def attack(self, other):
        return super().attack(other)
    
    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), (self.__x, self.__y), 50 , 1 )