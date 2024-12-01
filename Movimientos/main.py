import pygame
from triangulo import Triangulo

pygame.init()

ventana = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Movimiento de Triangulo")

background_color = (0, 0, 0)

# Instancia de la clase Triangulo
# Posición inicial del Triangulo en el plano
triangulo = Triangulo(400, 100)  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Estado de las teclas
    teclas = pygame.key.get_pressed()

    # Mover el triángulo
    triangulo.mover(teclas)

    # Pintar el fondo
    ventana.fill(background_color)

    # Dibujar el triángulo
    triangulo.dibujar(ventana)

    # Actualizar la pantalla
    pygame.display.update()

# Cerrar Pygame
pygame.quit()
