
import random
import pygame
import config
from player import Player
from enemy import Enemy_orco, Slime
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
        self.font = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", 25)
    
        self.start_time = pygame.time.get_ticks()

        self.last_message_time = 0  
 

        self.rango0 = 10
        self.rango1 = 5
        
        
        self.enemies_sl = [Slime(random.randint(-800, 800), random.randint(0, config.WIN_HEIGHT) ) for _ in range(10)]
        self.enemies_gob = [Enemy_orco(random.randint(-800, 800), random.randint(0, config.WIN_HEIGHT) ) for _ in range(5)]
        self.enemies = self.enemies_gob
        self.enemies.extend(self.enemies_sl)



    def draw(self):

        elapsed_time = pygame.time.get_ticks() - self.start_time
        minutes = elapsed_time // 60000  
        seconds = (elapsed_time // 1000) % 60  


        if pygame.time.get_ticks() - self.last_message_time >= 15000:  

            self.last_message_time = pygame.time.get_ticks() 
            self.enemies_sl.extend([Slime(random.randint(-800, 800), random.randint(0, config.WIN_HEIGHT)) for _ in range(10)])
            self.enemies_gob.extend([Enemy_orco(random.randint(-800, 800), random.randint(0, config.WIN_HEIGHT)) for _ in range(5)])
            self.enemies.extend(self.enemies_sl[-20:] + self.enemies_gob[-20:])


        self.timer_text = self.font.render(f"{minutes:02}:{seconds:02}", True, "white")

        self.enemies_sl = [enemy for enemy in self.enemies_sl if enemy.estatus]
        self.enemies_gob = [enemy for enemy in self.enemies_gob if enemy.estatus]

        self.enemies = [enemy for enemy in self.enemies if enemy.estatus]

        self.Game.screen.blit(self.screen_Background,(0,0))

        self.Pj.draw(self.Game.screen)
        self.Pj.weapon.draw(self.Game.screen)
        
        self.Game.screen.blit(self.timer_text, (10, 10))
        
        for enemy in self.enemies_sl:
            enemy.draw(self.Game.screen)


        for enemy in self.enemies_gob:
            enemy.draw(self.Game.screen)

       
    def events(self):
        press = False
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.Pj.weapon_type == "bow":
                    mouse__pos = pygame.mouse.get_pos()
                    self.Pj.shoot(mouse__pos)
                elif self.Pj.weapon_type == "sword":
                    self.Pj.atackAni(self.Game.screen)
                    press = True 
                else: 
                    press = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.Pj.switch()
        
        self.Pj.UpdatePositionWeapon()
        self.Pj.move(keys)



        mouse = pygame.mouse.get_pressed()
        for enemy in self.enemies_sl:
            enemy.move(self.Pj.x, self.Pj.y)
            enemy.death()
            if self.Pj.weapon_type == "bow":
                self.Pj.weapon.update_arrows(enemy)
            if self.Pj.weapon_type == "sword" and  press:
                self.Pj.weapon.attack(enemy)
                self.Pj.atack = mouse[0]

        
        for enemy in self.enemies_gob:
            enemy.move(self.Pj.x, self.Pj.y)
            enemy.death()
            if self.Pj.weapon_type == "bow":
                self.Pj.weapon.update_arrows(enemy)
            if self.Pj.weapon_type == "sword" and  press:
                self.Pj.weapon.attack(enemy)
                self.Pj.atack = mouse[0]
        for enemy in self.enemies:
            enemy.colision(self.Pj , self.enemies)

    def exit(self):
        return super().exit()















