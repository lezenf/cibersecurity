import random

def jugar_ahorcado():
    palabras = ['python', 'programacion', 'juego', 'computadora', 'desarrollo']
    palabra_secreta = random.choice(palabras)
    intentos_restantes = 6
    letras_adivinadas = []

    while intentos_restantes > 0:
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1:
            print("Por favor, ingresa solo una letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya has ingresado esa letra. Intenta nuevamente.")
            continue

        if letra not in palabra_secreta:
            intentos_restantes -= 1
            print(f"La letra '{letra}' no está en la palabra secreta. Te quedan {intentos_restantes} intentos.")
        else:
            letras_adivinadas.append(letra)

        palabra_actual = ""
        for letra_secreta in palabra_secreta:
            if letra_secreta in letras_adivinadas:
                palabra_actual += letra_secreta
            else:
                palabra_actual += "_"

        print(f"Palabra actual: {palabra_actual}")

        if palabra_actual == palabra_secreta:
            print("¡Felicitaciones! Has adivinado la palabra secreta.")
            break

    if intentos_restantes == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra secreta era:", palabra_secreta)

jugar_ahorcado()