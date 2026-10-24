
import random

# means of char
# B = Bastos o pica
# C = Corazones
# D = Diamantes
# T = Treboles

baraja = [["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "10B", "JB", "QB", "KB"],
          ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"],
          ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"],
          ["1T", "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "JT", "QT", "KT"]]


def repartir_naipes(jugadores):

    # Aplanar la baraja en una sola lista con los 52 naipes
    todos_los_naipes = []
    for palo in baraja:
        for naipe in palo:
            todos_los_naipes.append(naipe)

    # Mezclar la lista completa de naipes una sola vez
    random.shuffle(todos_los_naipes)

    # Índice para ir tomando naipes de la lista mezclada
    indice = 0

    # Repartir ronda a ronda: 1 naipe por jugador hasta que todos tengan 10
    # El tope de la pila es 10 (isfull()) así que repartimos 10 rondas
    for ronda in range(10):
        for jugador in jugadores:
            # Asignar el siguiente naipe de la lista mezclada
            jugador.recibir_naipe(todos_los_naipes[indice])
            indice += 1
