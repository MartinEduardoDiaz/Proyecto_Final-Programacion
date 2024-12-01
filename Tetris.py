import pygame
import random

# Inicializamos Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 300
ALTO = 600
CELDA = 30
FILAS = ALTO // CELDA
COLUMNAS = ANCHO // CELDA

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
CIAN = (0, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NARANJA = (255, 165, 0)
PÚRPURA = (128, 0, 128)
AMARILLO = (255, 255, 0)

# Formas de las piezas (en forma de matriz)
formas = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

# Función para dibujar el tablero
def dibujar_tablero(tablero):
    for y in range(FILAS):
        for x in range(COLUMNAS):
            if tablero[y][x]:
                pygame.draw.rect(pantalla, tablero[y][x], (x * CELDA, y * CELDA, CELDA, CELDA))
            pygame.draw.rect(pantalla, BLANCO, (x * CELDA, y * CELDA, CELDA, CELDA), 1)

# Crear una nueva pieza
def nueva_pieza():
    forma = random.choice(formas)
    return [[1 if celda else 0 for celda in fila] for fila in forma]

# Verificar si una pieza puede moverse a una posición
def puede_moverse(pieza, tablero, x, y):
    for i in range(len(pieza)):
        for j in range(len(pieza[i])):
            if pieza[i][j]:
                if x + j < 0 or x + j >= COLUMNAS or y + i >= FILAS or tablero[y + i][x + j]:
                    return False
    return True

# Eliminar las líneas completas y mover las líneas superiores hacia abajo
def eliminar_lineas(tablero):
    for y in range(FILAS - 1, -1, -1):
        if all(tablero[y]):
            tablero.pop(y)
            tablero.insert(0, [0] * COLUMNAS)

# Funcion para rotar la pieza
def rotar_pieza(pieza):
    return list(zip(*pieza[::-1]))

# Función principal del juego
def juego():
    global pantalla
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Tetris')
    reloj = pygame.time.Clock()

    # Inicialización del tablero (todo vacío)
    tablero = [[0] * COLUMNAS for _ in range(FILAS)]

    pieza_actual = nueva_pieza()
    x_pieza = COLUMNAS // 2 - len(pieza_actual[0]) // 2
    y_pieza = 0

    # Velocidad de la caída de las piezas
    velocidad = 500  # Milisegundos
    ultima_caida = pygame.time.get_ticks()

    # Juego activado
    juego_activado = True

    while juego_activado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_activado = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    if puede_moverse(pieza_actual, tablero, x_pieza - 1, y_pieza):
                        x_pieza -= 1
                if evento.key == pygame.K_RIGHT:
                    if puede_moverse(pieza_actual, tablero, x_pieza + 1, y_pieza):
                        x_pieza += 1
                if evento.key == pygame.K_DOWN:
                    if puede_moverse(pieza_actual, tablero, x_pieza, y_pieza + 1):
                        y_pieza += 1
                if evento.key == pygame.K_UP:
                    pieza_rotada = rotar_pieza(pieza_actual)
                    if puede_moverse(pieza_rotada, tablero, x_pieza, y_pieza):
                        pieza_actual = pieza_rotada

        # Comprobamos si la pieza ha llegado al fondo
        if pygame.time.get_ticks() - ultima_caida > velocidad:
            ultima_caida = pygame.time.get_ticks()

            if puede_moverse(pieza_actual, tablero, x_pieza, y_pieza + 1):
                y_pieza += 1
            else:
                # La pieza se "fija" en el tablero
                for i in range(len(pieza_actual)):
                    for j in range(len(pieza_actual[i])):
                        if pieza_actual[i][j]:
                            tablero[y_pieza + i][x_pieza + j] = CIAN

                # Eliminamos las líneas completas
                eliminar_lineas(tablero)

                # Generamos una nueva pieza
                pieza_actual = nueva_pieza()
                x_pieza = COLUMNAS // 2 - len(pieza_actual[0]) // 2
                y_pieza = 0

                # Comprobamos si la nueva pieza puede entrar
                if not puede_moverse(pieza_actual, tablero, x_pieza, y_pieza):
                    juego_activado = False

        # Limpiamos la pantalla
        pantalla.fill(NEGRO)

        # Dibujamos el tablero y la pieza actual
        dibujar_tablero(tablero)

        for i in range(len(pieza_actual)):
            for j in range(len(pieza_actual[i])):
                if pieza_actual[i][j]:
                    pygame.draw.rect(pantalla, CIAN, ((x_pieza + j) * CELDA, (y_pieza + i) * CELDA, CELDA, CELDA))

        pygame.display.update()

        # Establecemos los FPS
        reloj.tick(30)

    pygame.quit()

juego()
