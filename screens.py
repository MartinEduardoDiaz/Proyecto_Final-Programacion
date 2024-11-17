
import random
import pygame
import config
from player import Player
from enemy import Enemy
from buttons import Title


pygame.init()

#scene es la clase en la cual se guiaran las demas 
class Scene:
    def __init__(self,Game):
        self.Game = Game
     
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def exit(self):
        self.Game.GameOver = True




#main screen  es la pantalla base, donde se manejan  los botones y demas
class MainScreen(Scene):
    
    def __init__(self, Game):
        super().__init__(Game)
        self.screen_Background = config.Menu_background
        self.title = Title(config.WIN_WIDTH / 2 , 100, 300, 600, "Fangs Of The UnderWorld", "title")

    
    def draw(self):
        self.Game.screen.blit(self.screen_Background,(0,0))
        for button in config.buttons:
            button.draw(self.Game.screen)
        self.title.draw(self.Game.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
        for button in config.buttons:
                    button.click_on()
                    if button.clicked and button.name == "Jugar":
                        self.Game.change_screen(GameplayScreen(self.Game))
                    if button.clicked and button.name == "Logros":
                        print(f"Button clicked {button.name}")  
                    if button.clicked and button.name == "Opciones":
                        print(f"Button clicked {button.name}")        
                    if button.clicked and button.name == "Salir":
                        print(f"Button clicked {button.name}")
                        self.exit()

        
    def exit(self):
        return super().exit() 
    

class GameplayScreen(Scene):
    def __init__(self, Game):
        super().__init__(Game)
        self.screen_Background = config.background
        self.Pj = Player()
        self.enemies = [Enemy(random.randint(0, config.WIN_WIDTH-2), random.randint(0, config.WIN_HEIGHT - 2)) for _ in range(12)]


    def draw(self):
        self.enemies = [enemy for enemy in self.enemies if enemy.estatus]
        self.Game.screen.blit(self.screen_Background,(0,0))
        self.Pj.draw(self.Game.screen)
        self.Pj.weapon.draw(self.Game.screen)
        for enemy in self.enemies:
            enemy.draw(self.Game.screen)

    



    def events(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.Pj.weapon_type == "bow":
                    mouse__pos = pygame.mouse.get_pos()
                    self.Pj.shoot(mouse__pos)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.Pj.switch()
        self.Pj.UpdatePositionWeapon()
        self.Pj.move(keys)

        for enemy in self.enemies: 
            enemy.death()
            enemy.move(self.Pj.x, self.Pj.y)
            if self.Pj.weapon_type == "bow":
                self.Pj.weapon.update_arrows(enemy)
        
        
        

        
    

    def exit(self):
        return super().exit()















