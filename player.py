import pygame 
import config
import math as mt


class Player():
    def __init__(self, x,y):
        #stats del juego 
        self.armor = 0
        self.life = 100
        self.velocity = 0.5
        self.weapon = [False, "sword"]
        self.pvp = False
        
        #vista en pantalla
        self.__x = x
        self.__y = y
        self.pj_shape = pygame.Rect(0, 0 , 50 , 60)
        self.pj_shape.center = (self.__x, self.__y)

        #Imagen y rect
        self.animations = config.animations
        self.frame = 0
        self.image = self.animations[self.frame]
        self.flip = False
        self.color = (255,255,255)
        self.ticks = pygame.time.get_ticks()




    def draw(self,screen)-> None:
        self.image_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(self.image_flip , self.pj_shape)
        pygame.draw.rect(screen, self.color , self.pj_shape, 1 )

    def move(self,keys):
        self.ex = 0
        self.ey = 0

        if keys[pygame.K_s]:
            self.ey += self.velocity
        if keys[pygame.K_w]:
            self.ey -= self.velocity
        if keys[pygame.K_a]:
            self.ex -= self.velocity
            self.flip = True
        if keys[pygame.K_d]:
            self.ex += self.velocity
            self.flip = False


        if self.ex != 0 and self.ey != 0:
            self.ex /= mt.sqrt(2)
            self.ey /= mt.sqrt(2)
        
        if self.ex != 0 or self.ey != 0:
            self.animate() 
        else:
            self.frame = 0
            self.image = self.animations[self.frame]
                
        self.__x += self.ex
        self.__y += self.ey 
        self.pj_shape.center = (self.__x, self.__y)


    def animate(self):
        colldown_ani =  150 #ms 
        self.image = self.animations[self.frame]
        
        if pygame.time.get_ticks() - self.ticks >= colldown_ani:
            self.frame += 1
            self.ticks = pygame.time.get_ticks()
        if self.frame >= len(self.animations):
            self.frame = 0
    

    
    def attack(self, event) -> bool:
        if event:
            self.pvp = True
        else:
            self.pvp = False
        


    def get_pos(self):
        return [self.__x, self.__y]