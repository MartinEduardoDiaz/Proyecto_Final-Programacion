import pygame

# Se inicializa Pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Figuras Geométricas")

# Color de fondo
background_color = (0, 0, 0)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Se pinta el fondo con el color negro definido previamente
    ventana.fill(background_color)

    # Formas geométricas
    pygame.draw.circle(ventana, (255, 0, 0), (400, 300), 50)  # Círculo rojo
    pygame.draw.rect(ventana, (0, 255, 0), (150, 200, 100, 50))  # Rectángulo verde
    pygame.draw.line(ventana, (0, 0, 255), (100, 100), (700, 100), 5)  # Línea azul
    
    # Triángulo
    vertices_triangulo = [(400, 110), (350, 200), (450, 200)]  # Tres puntos del triángulo
    pygame.draw.polygon(ventana, (255, 255, 0), vertices_triangulo)  # Triángulo amarillo

    # Se actualiza la pantalla
    pygame.display.update()

# Cerrar Pygame
pygame.quit()
