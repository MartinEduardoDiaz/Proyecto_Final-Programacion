import pygame 
import config
import random

from weapons import Melee
from player import Player
from enemy import Enemy

pygame.init()


screen = pygame.display.set_mode((config.WIN_HEIGHT,config.WIN_WIDTH))
pygame.display.set_caption("Inferno´s redemption")
pygame.display.set_icon(config.ICON)


#screen_Background = config.menu_background

Pj = Player(config.WIN_WIDTH / 2 ,config.WIN_HEIGHT / 2)
enemies = [Enemy(random.randint(0, config.WIN_WIDTH-2), random.randint(0, config.WIN_HEIGHT - 2)) for _ in range(0,20)]


running = True 

while running:
    screen.fill((0,0,0))
    #screen.blit(screen_Background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            Pj.attack(event)



    sword = Melee(10, 10 , Pj.get_pos()[0], Pj.get_pos()[1])











    key = pygame.key.get_pressed()
    









    for enemy in enemies:
        enemy.draw(screen)
        
    Pj.draw(screen)
    Pj.move(key)
    sword.draw(screen)
    pygame.display.update()

pygame.quit()