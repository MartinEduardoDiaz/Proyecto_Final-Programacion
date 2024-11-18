import pygame 
import config 
import math as mt 

#Super clase enemy 
class Enemy():
    def __init__(self, type,str, x: int, y: int):
        self.type = type
        self.estatus = True
        self.life = 100
        self.x = x
        self.y = y
    def draw(self):
        pass

    def death(self): #metodo que actualiza el estado de el enemigo dependiendo si su vida baja hasta 0 o menos
        if self.life <= 0: 
            self.life = 0
            self.estatus = False    
            
    def move(self):
        pass

    def animate(self):
        pass



class Enemy_orco(Enemy):
    def __init__(self, type, str, x: int, y: int):
        super().__init__(type, str, x, y)
        self.color = (255, 0, 0)
        self.enemy_shape = pygame.Rect(0, 0 , 50 , 60)
        self.enemy_shape.center = (self.x , self.y)
        self.speed = 1.5
        self.animations_move= 2.5
        self.image = None


    def draw(self, screen):
        self.enemy_shape.topleft = (self.x, self.y)
        pygame.draw.rect(screen, self.color, self.enemy_shape, 1)


            
    def death(self):
        return super().death()
    
    
    def move(self, to_x: int, to_y: int):
        self.ex = to_x - self.x
        self.ey = to_y - self.y
        distance = mt.sqrt((self.ex - self.x)**2 + (self.ey - self.y)**2)  

        if distance != 0: 
            self.ex /= distance
            self.ey /= distance
        self.x += self.ex * self.speed
        self.y += self.ey * self.speed

    def animate(self):
        pass 


class slime(Enemy):
    def __init__(self, type, str, x: int, y: int):
        super().__init__(type, str, x, y)
