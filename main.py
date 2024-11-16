import pygame 
<<<<<<< Updated upstream
import os 



pygame.init()

ancho = 1280

alto = 500

window = pygame.display.set_mode((ancho,alto))



=======
import config
import random
from buttons import Title
from player import Player
from enemy import Enemy

def main():     
    pygame.init()
    
    #Screen DIsplay
    screen = pygame.display.set_mode((config.WIN_HEIGHT,config.WIN_WIDTH))
    pygame.display.set_caption("Fangs of The Underworld")
    pygame.display.set_icon(config.ICON)
    screen_Background = config.Menu_background
    
   
    title = Title(config.WIN_WIDTH / 2 , 100, 300, 600, "Fangs Of The UnderWorld", "title")
    Pj = Player()
    
    
    enemies = [Enemy(random.randint(0, config.WIN_WIDTH-2), random.randint(0, config.WIN_HEIGHT - 2)) for _ in range(12)]


    running = True  

    while running:  
        screen.fill((0,0,0))
        screen.blit(screen_Background,(0,0))
        enemies = [enemy for enemy in enemies if enemy.estatus]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            
        for button in config.buttons: 
            button.draw(screen)
            button.click_on()
            
            if button.clicked and button.name == "Jugar":
                print(f"Button clicked {button.name}")
            
            if button.clicked and button.name == "Logros":
                print(f"Button clicked {button.name}")
                
            if button.clicked and button.name == "Opciones":
                print(f"Button clicked {button.name}")
                
            if button.clicked and button.name == "Salir":
                print(f"Button clicked {button.name}")
                running = False

        title.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main() 
>>>>>>> Stashed changes
