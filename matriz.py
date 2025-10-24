import random

def generar_palabra():
    palabra = ""
    for _ in range(4):
        letra = chr(random.randint(97, 122))
        palabra += letra
    return palabra


def contar_palabras_con_vocal(matriz):
    
    if len(matriz) == 0:
        return 0
    
    if len(matriz) == 1 and len(matriz[0]) == 1:
        palabra = matriz[0][0]
        return 1 if any(vocal in palabra for vocal in "aeiou") else 0

    mitad = len(matriz) // 2
    sub1 = [fila[:mitad] for fila in matriz[:mitad]]
    sub2 = [fila[mitad:] for fila in matriz[:mitad]]
    sub3 = [fila[:mitad] for fila in matriz[mitad:]]
    sub4 = [fila[mitad:] for fila in matriz[mitad:]]
    
    c1 = contar_palabras_con_vocal(sub1)
    c2 = contar_palabras_con_vocal(sub2)
    c3 = contar_palabras_con_vocal(sub3)
    c4 = contar_palabras_con_vocal(sub4)
    
    return c1 + c2 + c3 + c4


def main():
    n = int(input("Ingrese el tamaño de la matriz cuadrada (n x n): "))

    matriz = [[generar_palabra() for _ in range(n)] for _ in range(n)]

    print("\nMatriz generada:")
    for fila in matriz:
        print("  ".join(fila))

    total_con_vocal = contar_palabras_con_vocal(matriz)
    print(f"\nTotal de palabras que contienen al menos una vocal: {total_con_vocal}")

if __name__ == "__main__":
    main()