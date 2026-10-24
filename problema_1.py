"""================================================================================================
Institute...: Universidad Técnica Nacional
Campus......: Pacífico
Career......: Tecnologías de Información
Period......: 3-2026
Document....: exa_01.py
Goals.......: Evaluación de expresiones matemáticas usando una pila (Stack)
Professor...: Jorge Ruiz (york)
Student.....: Caleb Fernandez Buzano
================================================================================================"""

from cls_Stack import cls_Stack


def analizar_expresion(expresion):

    # Analiza si los agrupadores de una expresión matemática están bien escritos.

    pila = cls_Stack()

    # Validar que la pila esté vacía antes de usarla
    if not pila.isempty():
        print("Error: la pila no está vacía al inicio.")
        return False

    # Definir cuáles son los agrupadores de apertura y cierre
    aperturas = "([{"
    cierres   = ")]}"

    # Recorrer la expresión carácter por carácter
    for caracter in expresion:

        # Si el carácter es un agrupador de apertura, lo apilamos
        if caracter in aperturas:
            pila.push(caracter)

        # Si el carácter es un agrupador de cierre, revisamos la pila
        elif caracter in cierres:

            # Si la pila está vacía, hay un cierre sin apertura
            if pila.isempty():
                print(f"  Error: se encontró '{caracter}' de cierre pero nunca se abrió.")
                return False

            # Sacamos el último agrupador abierto
            ultimo_abierto = pila.pop()

            # Verificamos que el cierre corresponda con la apertura
            # Buscamos el índice del cierre en ")]}" y lo comparamos con el índice en "([{"
            indice_cierre  = cierres.index(caracter)
            indice_apertura = aperturas.index(ultimo_abierto)

            if indice_cierre != indice_apertura:
                print(f"  Error: se abrió con '{ultimo_abierto}' pero se cerró con '{caracter}'.")
                return False

    # Al terminar el recorrido, la pila debe estar vacía
    # Si no está vacía, hay agrupadores que se abrieron pero nunca se cerraron
    if not pila.isempty():
        print(f"  Error: quedaron {len(pila)} agrupador(es) sin cerrar.")
        return False

    # Validar que la pila quedó vacía al finalizar
    if not pila.isempty():
        print("Error: la pila no quedó vacía al finalizar.")
        return False

    return True


# Programa principal

print()
print(" Evaluador de Expresiones Matemáticas ")
print()

continuar = True

while continuar:

# Captura la expresión del usuario
    expresion = input("Ingrese una expresión matemática: ")

    print()

# Llamar al método de análisis y mostrar el resultado
    resultado = analizar_expresion(expresion)

    if resultado:
        print(f"  La expresión '{expresion}' está BIEN escrita.")
    else:
        print(f"  La expresión '{expresion}' está MAL escrita.")

    print()

# Preguntar si desea continuar
    respuesta = input("¿Desea evaluar otra expresión? (si/no): ").strip().lower()
    continuar = (respuesta == "si")
    print()

print("Programa finalizado.")