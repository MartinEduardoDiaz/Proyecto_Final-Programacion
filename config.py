import pygame 
"""
ARCHIVO DE CONFIGURACIONES GENERALES 
-window size
"""



#funcion para escalar imagenes a un porcentaje
def img_scale(image , scale):
    height = image.get_height()
    Width = image.get_width()
    img = pygame.transform.scale(image , (height * scale, Width * scale))
    return img

#configuracion de ventana
WIN_HEIGHT = 1280
WIN_WIDTH = 720 
ICON = pygame.image.load("assets/images/UI/Icon_1.png")
"""
#Menu background
menu_background = pygame.image.load("assets/images/backgrounds/Background_1.png")
image_scale = menu_background.get_height() / menu_background.get_width()
new_height = WIN_HEIGHT * image_scale
menu_background = pygame.transform.scale(menu_background, (WIN_HEIGHT, new_height)) 

"""

#personaje 
pj_scale = 1
animations = []
for x in range(3): 
            img = pygame.image.load(f"assets/images/characters/player/frame_{x}.png")
            img = img_scale(img , pj_scale)
            animations.append(img)
        




















