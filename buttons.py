import pygame
import config
pygame.init()


class Button():
    font = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", 40)
    
    def __init__(self , x: int , y: int , height: int, width: int, text: str, name : str)-> None:

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height )
        self.name = name

        self.text = Button.font.render(text, True, "#000000")
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
        self.color = (50, 60, 80, 200) if self.hover else (70, 80, 90, 100 )
        pygame.draw.rect(screen, self.color, self.rect, border_radius=5)
        screen.blit(self.text, self.text_rect)




class Title(Button):
    def __init__(self, x: int, y: int, height: int, width: int, text: str, name: str) -> None:
        super().__init__(x, y, height, width, text, name)
        self.font = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", 100)
        self.text = self.font.render(text, True, "black")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
        
        self.font_bottom = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", 101)
        self.text_bottom = self.font_bottom.render(text, True, "white")
        self.text_rect_bottom = self.text.get_rect()
        self.text_rect_bottom.center = self.rect.center

    
    def click_on(self):
        return super().click_on()
    

    def draw(self, screen):
        screen.blit(self.text_bottom, self.text_rect_bottom)
        screen.blit(self.text, self.text_rect)
