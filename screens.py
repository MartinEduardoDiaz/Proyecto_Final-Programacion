import random
import pygame
import config
from player import Player
from enemy import Enemy_orco, Slime
from ui import Title, lifes, Button






pygame.init()

#scene es la clase en la cual se guiaran las demas 
class Scene:
    def __init__(self,Game):
        self.Game = Game
     
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
    
    def draw(self):
        pass
    
    def exit(self):
        self.Game.GameOver = True




class MainScreen(Scene):
    
    def __init__(self, Game):
        super().__init__(Game)
        self.screen_Background = config.Menu_background
        self.title = Title(config.WIN_HEIGHT / 2 , 100, 300, 600, "Fangs Of The UnderWorld", "title", (52, 162, 140) , (60, 191, 165 ), 100)

    
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
                    self.Game.change_screen(OptionsScreen(self.Game , self.screen_Background))    
                if button.clicked and button.name == "Salir":
                    self.exit()

        
    def exit(self):
        return super().exit() 
    

class OptionsScreen(Scene):
    def __init__(self, Game, background):
        super().__init__(Game)
        self.screen_Background = background
        self.buttons =config.buttons_op
    
    def draw(self):
        self.Game.screen.blit(self.screen_Background,(0,0))
        for button in self.buttons:
            button.draw(self.Game.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()


class GameplayScreen(Scene):
    def __init__(self, Game):
        super().__init__(Game)
        self.screen_Background = config.background
        self.Pj = Player()
        self.font = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", 25)
    
        self.start_time = pygame.time.get_ticks()
        self.ronda = 1
        self.last_message_time = 0  
 

        self.rango0 = 10
        self.rango1 = 5
        
        

        self.enemies_sl = [Slime(random.randint(-800, 800), random.randint(0, config.WIN_HEIGHT) ) for _ in range(10)]
        self.enemies_gob = [Enemy_orco(random.randint(-800, 800), random.randint(0, config.WIN_HEIGHT) ) for _ in range(5)]
        self.enemies = self.enemies_gob
        self.enemies.extend(self.enemies_sl)

        self.lifecounter = lifes(1200, 10)

        self.buttons_text = ["armor","damage","speed"]
        self.but_pos = 150
        self.buttons = []
        for txt in self.buttons_text:
            self.but_pos +=200
            self.button = Button(self.but_pos,500 , 100,100, txt,txt,(26, 26, 26) , (45, 58, 69 ))
            self.buttons.append(self.button)
    

    def draw(self):
        
        elapsed_time = pygame.time.get_ticks() - self.start_time
        self.minutes = elapsed_time // 60000  
        self.seconds = (elapsed_time // 1000) % 60  
        

         

        self.timer_text = self.font.render(f"{self.minutes:02}:{self.seconds:02}", True, "white")
        self.round_text = self.font.render(f"Ronda {self.ronda}", True, "white")

        self.enemies_sl = [enemy for enemy in self.enemies_sl if enemy.estatus]
        self.enemies_gob = [enemy for enemy in self.enemies_gob if enemy.estatus]
        self.enemies = [enemy for enemy in self.enemies if enemy.estatus]

        self.Game.screen.blit(self.screen_Background,(0,0))

        self.Pj.draw(self.Game.screen)
        self.Pj.weapon.draw(self.Game.screen)
        
        self.Game.screen.blit(self.timer_text, (10, 10))

        for enemy in self.enemies:
            enemy.draw(self.Game.screen)


        self.enemiesDeath = [enemy for enemy in self.enemies if enemy.estatus == False]


        self.Game.screen.blit(self.round_text, (500, 10))
        self.lifecounter.draw(self.Game.screen)
    
        if self.Pj.exp == 15:
            for button in self.buttons:
                button.draw(self.Game.screen)


        if len(self.enemiesDeath) == len(self.enemies):
            self.enemies_sl.extend([Slime(random.randint(-800, 800), random.randint(0, config.WIN_HEIGHT)) for _ in range(10)])
            self.enemies_gob.extend([Enemy_orco(random.randint(-800, 800), random.randint(0, config.WIN_HEIGHT)) for _ in range(5)]) 
            self.enemies.extend(self.enemies_sl[-20:] + self.enemies_gob[-20:])
            self.ronda += 1

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
        self.lifecounter.update(self.Pj.life)

        mouse = pygame.mouse.get_pressed()

        for button in self.buttons:
            button.click_on()
            if button.clicked and button.name == "armor":
                self.Pj.randomStat.append("armor")
            if button.clicked and button.name == "speed":
                self.Pj.randomStat.append("speed")
            if button.clicked and button.name == "damage":
                self.Pj.randomStat.append("damage")
            

        for enemy in self.enemies:
            enemy.move(self.Pj.x, self.Pj.y)
            enemy.death()
            if self.Pj.weapon_type == "bow":
                self.Pj.weapon.update_arrows(enemy)
            if self.Pj.weapon_type == "sword" and  press:
                self.Pj.weapon.attack(enemy)
                self.Pj.atack = mouse[0]
            if enemy.estatus == False:
                self.Pj.count()
        
            enemy.colision(self.Pj , self.enemies)
    
        if not self.Pj.status:
            self.Game.change_screen(DeathScreen(self.Game, self.screen_Background, self.ronda, (self.minutes , self.seconds)))


    def exit(self):
        return super().exit()





class DeathScreen(Scene):
    def __init__(self, Game, background, points, duration):
        super().__init__(Game)
        self.screen_Background = background
        self.buttons = config.buttonsD
        self.font = pygame.font.Font("assets\Fonts\Metal_Mania\MetalMania-Regular.ttf", 25)
        self.title = Title(300 , 3, 300, 600, "Moriste", "title", (52, 162, 140) , (60, 191, 165 ), 100)
        self.points = points
        self.duration = duration
        self.text = self.font.render(f"moriste en la ronda {self.points} .........", True, "white")
        self.text_duration = self.font.render(f"Duraste {self.duration[0]:02}:{self.duration[1]:02} en la partida ...", True, "white")

        self.textEasterEgg = self.font.render(f"¿No llegaste al primer boss?", True, "white")
        self.textEasterEgg2 = self.font.render(f"BRO? Deberias mejorar eh...", True, "white")
        
        self.textNonEaster =self.font.render(f"Bien hecho", True, "white")
    
    def draw(self):
        line = self.font.render(f"__________________", True, "white")
        self.Game.screen.blit(self.screen_Background,(0,0))
        
        
        pygame.draw.rect(self.Game.screen, (26, 26, 26), (150, 150, 300, 400), border_radius=20)
        self.Game.screen.blit(self.text_duration, (160, 220))
        
        self.Game.screen.blit(line, (160, 270))
        self.Game.screen.blit(self.text, (160, 300))

        if self.points < 2:
            self.Game.screen.blit(self.textEasterEgg, (160, 400))
            self.Game.screen.blit(self.textEasterEgg2, (160, 420))
        elif self.points >=2:
            self.Game.screen.blit(self.textNonEaster, (160, 350))
        for button in self.buttons:
            button.draw(self.Game.screen)
        self.title.draw(self.Game.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
        for button in self.buttons:
                    button.click_on()
                    if button.clicked and button.name == "Reiniciar":
                        self.Game.change_screen(GameplayScreen(self.Game))
                    if button.clicked and button.name == "ir al titulo":
                        self.Game.change_screen(MainScreen(self.Game))
                    if button.clicked and button.name == "Salir":
                        self.exit()