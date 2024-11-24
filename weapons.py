import pygame
import math as mt 
import config

class Weapon():
    def __init__(self,AD):
        self.AD = AD

    def attack(self,other):
        other.life -= self.AD
        if other.life <= 0:
            other.death()


class Sword(Weapon):
    def __init__(self, AD, x , y):
        super().__init__(AD)
        self.x = x
        self.y = y
        self.range = 50 
    

    def attack(self, other):
        enemy_radius = max(other.enemy_shape.width, other.enemy_shape.height) / 2
        distance = mt.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        

        if distance <= self.range + enemy_radius:
            super().attack(other)

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.range, 1 )



class Arrow():
    def __init__(self, AD, x , y , mouse):
        self.AD = AD
        self.x = x 
        self.y = y
        self.active = True
        angle = mt.atan2(mouse[1] - self.y, mouse[0] - self.x)
        self.vx = mt.cos(angle) * 1
        self.vy = mt.sin(angle) * 1
        self.rect = pygame.Rect(self.x, self.y, 10,10)
        self.animations = config.dagaAni
        self.frame = 0
        self.image = self.animations[self.frame]
        self.ticks = pygame.time.get_ticks()
    def move(self):
        if self.active:
            self.x += self.vx
            self.y += self.vy
            self.rect.topleft = (self.x, self.y)
            self.animate()
    def draw(self, screen):
        if self.active:
            #pygame.draw.rect(screen,(255,255,255), self.rect)
            screen.blit(self.image , self.rect.topleft)

    def animate(self):
        colldown_ani =  200 #ms 
        self.image = self.animations[self.frame]
        


        if pygame.time.get_ticks() - self.ticks >= colldown_ani:
            self.frame += 1
            self.ticks = pygame.time.get_ticks()
        if self.frame >= len(self.animations):
            self.frame = 0


    


class Bow(Weapon):
    def __init__(self, AD):
        super().__init__(AD)
        self.carcaj = []

    def shoot(self, x , y , mouse):
        arrow = Arrow(self.AD, x , y , mouse)
        self.carcaj.append(arrow)

    def draw(self, screen):
        for arrow in self.carcaj:
            arrow.draw(screen)
            arrow.move()

    def update_arrows(self, enemy):
        for arrow in self.carcaj:
            if arrow.rect.colliderect(enemy.enemy_shape):
                super().attack(enemy)
                arrow.active = False 
        self.carcaj = [arrow for arrow in self.carcaj if arrow.active]

    
    






































 

