import pygame 
import config
from weapons import Sword, Bow
import math as mt



class Player():
    def __init__(self):
        #stats del juego 
        self.armor = 0
        self.life = 100
        self.velocity = 2
        self.weapon_type =  "sword"
        
        #vista en pantalla
        self.x = (config.WIN_WIDTH / 2)
        self.y = (config.WIN_HEIGHT / 2)
        self.weapon =Sword(8, self.x, self.y)
        self.pj_shape = pygame.Rect(0, 0 , 49 , 60)
        self.pj_shape.center = (self.x, self.y)

        #Imagen y rect
        self.animationsMove = config.animations_movement
        self.animationsAttackSw = config.animations_attack_sw
        self.frame = 0
        self.image = self.animationsMove[self.frame]
        self.flip = True
        self.color = (255,255,255)
        self.ticks = pygame.time.get_ticks()
        

        self.pj_move = False
        self.atack = False
        self.status = True

    #Draw Funcion para dibujar al personaje  en la pantalla
    def draw(self,screen)-> None:
        self.image_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(self.image_flip , self.pj_shape)
        #pygame.draw.rect(screen, self.color , self.pj_shape, 1 )
    
    def move(self,keys):
        self.ex = 0
        self.ey = 0
        if keys[pygame.K_s]:
            self.ey += self.velocity
        if keys[pygame.K_w]:
            self.ey -= self.velocity
        if keys[pygame.K_a]:
            self.ex -= self.velocity
            self.flip = False
        if keys[pygame.K_d]:
            self.ex += self.velocity
            self.flip = True


        if self.ex != 0 and self.ey != 0:
            self.ex /= mt.sqrt(2)
            self.ey /= mt.sqrt(2)
        
        if self.ex != 0 or self.ey != 0:
            self.pj_move = True
            self.animate() 
        else:
            self.frame = 0
            self.image = self.animationsMove[self.frame]
                
        self.x += self.ex
        self.y += self.ey 
        self.pj_shape.center = (self.x, self.y)



    def animate(self):
        colldown_ani = 150  #ms
        self.attack_timer = pygame.time.get_ticks()

        if self.pj_move:
            self.image = self.animationsMove[self.frame]
            if pygame.time.get_ticks() - self.ticks >= colldown_ani:
                self.frame += 1
                self.ticks = pygame.time.get_ticks()
            if self.frame >= len(self.animationsMove):
                self.frame = 0



    def atackAni(self,screen):
        
        if self.atack:
            aux = pygame.time.get_ticks()
            for i in range(len(self.animationsAttackSw)):
                    print(aux)
                    self.image = self.animationsAttackSw[i]
                    self.draw(screen)
                    pygame.display.update()
                    pygame.time.wait(10) 
            self.atack = False




    def attack(self, other):
        if self.weapon_type == "sword":
            self.weapon.attack(other)


    def shoot(self, mouse):
        self.weapon.shoot( self.x , self.y, mouse)



    def switch(self):
        if self.weapon_type == "sword":
            self.weapon_type = "bow"
            self.weapon = Bow(8)

        elif self.weapon_type == "bow" :
            self.weapon_type = "sword"
            self.weapon = Sword(6, self.x, self.y)



    def UpdatePositionWeapon(self):
        if self.weapon_type == "sword":
            self.weapon.update_position(self.x , self.y)

    def takeDamage(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.status = False
            print("mori")