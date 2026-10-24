
import time
from cls_Jugador  import cls_Jugador
from Subrutinas   import repartir_naipes


def imprimir_encabezado(jugadores):
    """Imprime la fila de nombres de los jugadores como encabezado de columnas."""
    encabezado = ""
    for jugador in jugadores:
        # Cada columna ocupa 8 caracteres para que queden alineadas
        encabezado += jugador.nombre.ljust(8)
    print(encabezado)
    print("-" * (8 * len(jugadores)))


def imprimir_fila(naipes_turno, jugadores):

    fila = ""
    for i in range(len(jugadores)):
        if naipes_turno[i] is not None:
            fila += naipes_turno[i].ljust(8)
        else:
            fila += " ".ljust(8)
    print(fila)


def jugar(jugadores):

    ganador       = None
    naipe_ganador = None

    # Lista donde vamos acumulando los naipes que ya salieron de cada jugador
    # (para poder filtrar corazones al final)
    naipes_obtenidos = []
    for jugador in jugadores:
        naipes_obtenidos.append([])

    print()
    imprimir_encabezado(jugadores)

    # El juego corre mientras haya naipes y nadie haya ganado
    juego_activo = True

    while juego_activo:

        naipes_turno = []
        for jugador in jugadores:
            naipes_turno.append(None)

        todos_sin_naipes = True

        for i in range(len(jugadores)):

            jugador = jugadores[i]

            # Verificar si este jugador aún tiene naipes
            if jugador.tiene_naipes():
                todos_sin_naipes = False

                # Sacar el naipe del tope de su pila
                naipe = jugador.sacar_naipe()
                naipes_turno[i] = naipe
                naipes_obtenidos[i].append(naipe)

                # Verificar si es la Reina de Corazones
                if naipe == "QC":
                    ganador       = jugador
                    naipe_ganador = naipe
                    juego_activo  = False

            # Esperar 2 segundos entre jugadores (solo si el juego sigue activo)
            if juego_activo and i < len(jugadores) - 1:
                time.sleep(2)

        # Imprimir la fila de este turno
        imprimir_fila(naipes_turno, jugadores)

        # Si todos los jugadores ya no tienen naipes, terminar
        if todos_sin_naipes:
            juego_activo = False

    # Retornar también los naipes acumulados para filtrar corazones
    return ganador, naipes_obtenidos


#Programa principal

print()
print("Buscando a la Reina de Corazones")
print()

# Crear las instancias de los 4 jugadores
jugadores = [
    cls_Jugador("Merlina"),
    cls_Jugador("Pericles"),
    cls_Jugador("Tio Lucas"),
    cls_Jugador("Homero")
]

# Repartir naipes de forma aleatoria sin repetir
print("Repartiendo naipes...")
repartir_naipes(jugadores)
print("¡Naipes repartidos! Iniciando el juego.")

# Ejecutar el juego
ganador, naipes_obtenidos = jugar(jugadores)

print()
print("Fin del juego")
print()

# Mostrar resultado
if ganador is not None:
    # Obtener el índice del ganador para acceder a sus naipes acumulados
    indice_ganador = 0
    for i in range(len(jugadores)):
        if jugadores[i].nombre == ganador.nombre:
            indice_ganador = i
            break

    print(f"¡{ganador.nombre} encontró la Reina de Corazones!")
    print()

    # Obtener la lista de naipes de Corazón del ganador usando List Comprehension
    corazones = [naipe for naipe in naipes_obtenidos[indice_ganador] if naipe.endswith("C")]

    print(f"Naipes de Corazón obtenidos por {ganador.nombre}:")
    print(corazones)

else:
    print("Nadie encontró la Reina de Corazones. ¡El juego terminó en empate!")