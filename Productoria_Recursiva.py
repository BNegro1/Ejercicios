'''

Sumatoria y productoria recursiva

'''




def sumatoria(n):
    if n == 0:
        return 0
    return (n + sumatoria(n-1))

def productoria(n):
    if n == 0:
        return 1
    return (n*productoria(n-1))

while True:
    print(''' 
                Menú de aritmetica
        1) Cálculo de sumatoria.
        2) Cálculo de productoria.
        3) Salir.
        
          ''')
    op = int(input("Ingrese una opción: "))
    if op == 1:
        numero = int(input("Ingrese un número para calcular su sumatoria: "))
        print(f'El cálculo de la sumatoria de {numero} es: {sumatoria(numero)}')
    elif op == 2:
        numero = int(input("Ingrese un número para calcular su productoria: "))
        print(f'El cálculo de la productoria de {numero} es: {productoria(numero)}')
    elif op == 3:
        print("Saliendo correctamente del programa.")
        break   
