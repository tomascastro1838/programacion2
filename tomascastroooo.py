import random

def generar_numero_aleatorio():
    return random.randint(1, 200)

def adivinar_numero():
    numero_aleatorio = generar_numero_aleatorio()
    intentos = 7

    print("¡Bienvenido al juego de adivinar el número!")
    print(f"Tienes {intentos} intentos para adivinar un número entre 1 y 20.")

    while intentos > 0:
        try:
            intento = int(input("Ingresa tu número: "))
            if intento == numero_aleatorio:
                print("¡Felicidades! Adivinaste el número.")
                break
            elif intento < numero_aleatorio:
                print("El número que intentas adivinar es mayor.")
            else:
                print("El número que intentas adivinar es menor.")
            intentos -= 1
        except ValueError:
            print("Ingresa un número válido.")

    if intentos == 0:
        print(f"Se acabaron los intentos. El número correcto era {numero_aleatorio}.")

adivinar_numero()