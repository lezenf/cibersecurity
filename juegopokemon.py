import random

class Pokemon:
    def __init__(self, nombre, tipo, puntos_vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.puntos_vida = puntos_vida
        self.ataque = ataque

    def atacar(self, oponente):
        oponente.puntos_vida -= self.ataque
        print(f"{self.nombre} ataca a {oponente.nombre} y le hace {self.ataque} puntos de daño.")

    def esta_vivo(self):
        return self.puntos_vida > 0


def jugar():
    pikachu = Pokemon("Pikachu", "Eléctrico", 100, 10)
    squirtle = Pokemon("Squirtle", "Agua", 80, 8)
    bulbasaur = Pokemon("Bulbasaur", "Planta", 90, 9)
    charmander = Pokemon("Charmander", "Fuego", 95, 11)

    oponentes = [squirtle, bulbasaur, charmander]
    oponente_actual = random.choice(oponentes)

    print("¡Bienvenido a la batalla Pokémon!")
    nombre = input("Por favor, ingresa tu nombre de entrenador: ")
    jugador = Pokemon(nombre, "Entrenador", 120, 12)

    print(f"\n{jugador.nombre}, has elegido a {jugador.nombre} como tu Pokémon inicial.")
    print(f"\nTu oponente actual es {oponente_actual.nombre}. ¡Que comience la batalla!")

    while jugador.esta_vivo() and oponente_actual.esta_vivo():
        print("\n--- Tu turno ---")
        jugador.atacar(oponente_actual)
        if not oponente_actual.esta_vivo():
            break

        print("\n--- Turno del oponente ---")
        oponente_actual.atacar(jugador)

    if jugador.esta_vivo():
        print("\n¡Felicidades! Has derrotado al oponente.")
    else:
        print("\n¡Has sido derrotado! Mejor suerte la próxima vez.")

jugar()