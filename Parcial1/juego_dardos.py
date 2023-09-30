import random
TURNOS = 10
RONDAS = 20
APUESTA = 100
def puntos_dardo():
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    distancia_al_centro = x**2 + y**2
    if distancia_al_centro <= 0.2**2:
        return 50
    elif distancia_al_centro <= 0.5**2:
        return 25
    elif distancia_al_centro <= 1:
        return 10
    else:
        return 0
def jugar_ronda():
    puntos_jugador1 = sum(puntos_dardo() for _ in range(TURNOS))
    puntos_jugador2 = sum(puntos_dardo() for _ in range(TURNOS))
    if puntos_jugador1 > puntos_jugador2:
        return APUESTA
    elif puntos_jugador2 > puntos_jugador1:
        return -APUESTA
    else:
        return 0
def juego_noche():
    ganancias_jugador1 = 0
    ganancias_jugador2 = 0
    for _ in range(RONDAS):
        ganancia_ronda = jugar_ronda()
        ganancias_jugador1 += ganancia_ronda
        ganancias_jugador2 -= ganancia_ronda  # Si el jugador 1 gana, el jugador 2 pierde, y viceversa
    return ganancias_jugador1, ganancias_jugador2
if __name__ == "__main__":
    ganancias_j1, ganancias_j2 = juego_noche()
    print(f"Ganancias Jugador 1: {ganancias_j1} unidades")
    print(f"Ganancias Jugador 2: {ganancias_j2} unidades")
