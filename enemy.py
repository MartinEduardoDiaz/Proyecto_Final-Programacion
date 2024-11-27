import pygame 
import config 
import math as mt 


class Enemy():
    def __init__(self):
        self.estatus = True
        self.life = 100
    def draw(self):
        pass

    def death(self):
        if self.life <= 0: 
            self.life = 0
            self.estatus = False    
            
    def move(self, to_x: int, to_y: int):
        self.ex = to_x - self.x
        self.ey = to_y - self.y
        distance = mt.sqrt((self.ex - self.x)**2 + (self.ey - self.y)**2)  
        self.enemy_shape.center = (self.x, self.y)

        if distance != 0: 
            self.ex /= distance
            self.ey /= distance
        self.x += self.ex * self.speed
        self.y += self.ey * self.speed
        self.animate()


    def colision(self,player, enemies):
        for enemy in enemies:
                if player.pj_shape.colliderect(enemy.enemy_shape):  
                    player.takeDamage(self.AD)
    def animate(self):
        pass



class Enemy_orco(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.AD = 12

        self.enemy_shape = pygame.Rect(0, 0 , 50 , 60)
        self.enemy_shape.center = (self.x , self.y)
        self.speed = 1
        self.animations= config.orco
        self.frame = 0
        self.image = self.animations[self.frame]
        self.ticks = self.ticks = pygame.time.get_ticks()



    def animate(self):
            colldown_ani =  150 #ms 
            self.image = self.animations[self.frame]
            
            if pygame.time.get_ticks() - self.ticks >= colldown_ani:
                self.frame += 1
                self.ticks = pygame.time.get_ticks()
            if self.frame >= len(self.animations):
                self.frame = 0
                
            
    def draw(self, screen):
        self.enemy_shape.topleft = (self.x, self.y)
       #pygame.draw.rect(screen, self.color, self.enemy_shape, 1)
        screen.blit(self.image , self.enemy_shape.topleft)


    def death(self):
        return super().death()
    



class Slime(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.life = 50

        self.x = x
        self.y = y
        self.frame = 0
        self.animations = config.SlimeAnimation
        self.ticks = pygame.time.get_ticks()
        self.AD = 5
        self.image = self.animations[self.frame]
        self.speed = 0.1
        self.enemy_shape = pygame.Rect(0, 0 , 42 , 30)
        self.enemy_shape.topleft = (self.x, self.y )


  
        
    def draw(self, screen):
        self.enemy_shape.center = (self.x, self.y)
        #pygame.draw.rect(screen, (255,0,0), self.enemy_shape, 1)
        screen.blit(self.image, self.image.get_rect(center=self.enemy_shape.center).topleft)



    def animate(self):
        colldown_ani =  150 #ms 
        self.image = self.animations[self.frame]
        


        if pygame.time.get_ticks() - self.ticks >= colldown_ani:
            self.frame += 1
            self.ticks = pygame.time.get_ticks()
        if self.frame >= len(self.animations):
            self.frame = 0

    def death(self):
        return super().death()



class boss(Enemy):
    def __init__(self):
        super().__init__()
        self.life = 100000