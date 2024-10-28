import pygame 
import config
import random

from player import Player
from enemy import Enemy

def main(): 

        
    pygame.init()
    screen = pygame.display.set_mode((config.WIN_HEIGHT,config.WIN_WIDTH))
    pygame.display.set_caption("Inferno´s redemption")
    pygame.display.set_icon(config.ICON)


    screen_Background = config.menu_background

    Pj = Player()

    enemies = [Enemy(random.randint(0, config.WIN_WIDTH-2), random.randint(0, config.WIN_HEIGHT - 2)) for _ in range(20)]


    running = True 

    while running:  
        screen.fill((0,0,0))
        screen.blit(screen_Background,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if Pj.weapon_type == "bow":
                    Pj.shoot(mouse_pos)
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    Pj.switch()




        for enemy in enemies:
            enemy.draw(screen)
            
            
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Pj.attack(enemy)


    


        
        Pj.UpdatePositionWeapon()
        key = pygame.key.get_pressed()
        Pj.draw(screen)
        Pj.move(key)








        Pj.weapon.draw(screen)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main() 