
from cls_Stack import cls_Stack


class cls_Jugador:

    def __init__(self, nombre):
        # Atributos básicos del jugador
        self._nombre  = nombre
        self._partida = cls_Stack()   # Cada jugador tiene su propia pila de naipes

    #Propiedades

    @property
    def nombre(self):
        return self._nombre

    @property
    def partida(self):
        return self._partida

    #Métodos

    def recibir_naipe(self, naipe):
        #Agrega un naipe a la pila del jugador si no está llena
        if not self._partida.isfull():
            self._partida.push(naipe)

    def tiene_naipes(self):
        #Retorna True si el jugador aún tiene naipes en su pila
        return not self._partida.isempty()

    def sacar_naipe(self):
        #Saca y retorna el naipe del tope de la pila del jugador
        if not self._partida.isempty():
            return self._partida.pop()
        return None

    def __str__(self):
        return f"Jugador: {self._nombre} | Naipes: {len(self._partida)}"