import pygame

pygame.init()

screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Ta-Te-Ti")

fondo = pygame.image.load('static/fondo-tateti.jpg')
fondo = pygame.transform.scale(fondo, (450, 450))

circulo = pygame.image.load('static/circulo.png')
circulo = pygame.transform.scale(circulo, (125, 125))

equis = pygame.image.load('static/cruz.png')
equis = pygame.transform.scale(equis, (125, 125))

tablero = [['', '', ''],
           ['', '', ''],
           ['', '', '']]
turno = 'X'
game_over = False

def verificar_ganador():
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != '':
            return fila[0]

    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != '':
            return tablero[0][col]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != '':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != '':
        return tablero[0][2]

    return None

while not game_over: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (mouseX >= 40 and mouseX < 415) and \
               (mouseY >= 50 and mouseY < 425): 
                fila =  (mouseY - 50) // 125
                col = (mouseX - 40) // 125
                if tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    if turno == 'X':
                        turno = 'O'
                    else:
                        turno = 'X'
                    ganador = verificar_ganador()
                    if ganador:
                        print("¡Ha ganado el jugador", ganador, "!")
                        game_over = True

    screen.blit(fondo, (0, 0))
    
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'X':
                screen.blit(equis, (40 + col * 125, 50 + fila * 125))
            elif tablero[fila][col] == 'O':
                screen.blit(circulo, (40 + col * 125, 50 + fila * 125))
    
    pygame.display.update()

pygame.quit()
