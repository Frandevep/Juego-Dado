import random

def lanzar_dado():
    return random.randint(1, 6)  # Genera un número entre 1 y 6

# Preguntamos si el usuario quiere lanzar el dado
while True:
    input("Presiona Enter para lanzar el dado...")
    resultado = lanzar_dado()
    print("🎲 El dado cayó en:", resultado)
    
    # Preguntamos si quiere volver a lanzar
    opcion = input("¿Quieres lanzar de nuevo? (s/n): ").lower()
    if opcion != "s":
        print("¡Gracias por jugar!")
        break
