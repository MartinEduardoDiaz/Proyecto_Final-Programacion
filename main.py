import pygame 
from player import Player

pygame.init()
icon = pygame.image.load("assets/Icon_1.png")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Satan´s redemption")
running = True 

fondo = pygame.image.load("assets/Background_1.png")
image_width, image_height = fondo.get_size()
aspect_ratio = image_height / image_width
new_height = 1280 * aspect_ratio
fondo = pygame.transform.scale(fondo, (1280, new_height))

screen_Background = fondo
Pj = Player(100,100)
while running:
    screen.fill((0,0,0))
    screen.blit(screen_Background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    key = pygame.key.get_pressed()
    
    Pj.draw(screen)
    Pj.move(key)
    pygame.display.update()

pygame.quit()