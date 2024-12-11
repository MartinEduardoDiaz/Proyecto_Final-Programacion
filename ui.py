import pygame
import config
pygame.init()


class Button():
    font = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", 40)
    
    def __init__(self , x: int , y: int , height: int, width: int, text: str, name : str, color: tuple, onpressC: tuple)-> None:

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height )
        self.name = name

        self.color = color
        self.onpresC = onpressC
        self.text = Button.font.render(text, True, "#cccccc")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

        self.hover = False
        self.pressed = False
        self.clicked = False
    
    def click_on(self):
        self.clicked = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.hover = True
            
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else: 
                if self.pressed:
                    self.pressed = False
                    self.clicked = True
        else: 
            self.pressed = False
            self.hover = False

    def draw(self,screen):
        self.current_color =  self.onpresC if self.hover else self.color
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=5)
        screen.blit(self.text, self.text_rect)




class Title(Button):
    def __init__(self, x, y, height, width, text, name, color, onpressC, size):
        super().__init__(x, y, height, width, text, name, color, onpressC)
    
        self.font = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", size)
        self.text = self.font.render(text, True, "#CCCCCC")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
        
        self.font_bottom = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", size+1)
        self.text_bottom = self.font_bottom.render(text, True, "#1E90FF")
        self.text_rect_bottom = self.text.get_rect()
        self.text_rect_bottom.center = self.rect.center

    def click_on(self):
        return super().click_on()
    

    def draw(self, screen):
        screen.blit(self.text_bottom, self.text_rect_bottom)
        screen.blit(self.text, self.text_rect)


class lifes():
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.life = 100
        self.frame = 5
        self.animations = config.animationsLife
        self.image = self.animations[self.frame]
        self.font = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", 20)
        self.textLife = self.font.render(f"{self.life}", True, "#CCCCCC")
    def draw(self, screen):
        self.image = self.animations[self.frame]
        screen.blit(self.textLife, (self.x-30, self.y+10))
        screen.blit(self.image, (self.x, self.y))
    
    def update(self,life):
        self.life = life
        self.textLife = self.font.render(f"{self.life}", True, "#CCCCCC")
        if self.life < 19:
            self.frame = 0
        elif self.life >=20 and self.life <39:
            self.frame = 1
        elif self.life >=40 and self.life <59:
            self.frame = 2
        elif self.life >=60 and self.life <79:
            self.frame = 3
        elif self.life >=80 and self.life <99:
            self.frame = 4
        else: 
            self.frame = 5