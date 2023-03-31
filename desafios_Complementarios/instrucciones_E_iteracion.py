numero1 = int(input("elija el primer numero"))
numero2 = int(input("elija el segundo numero"))

def menu():
    print("Este es el menu")
    print("1- Suma de los dos numeros")
    print("2- Resta del numero 1 y el numero2")
    print("3- Multiplicacion de los 2 numeros")
    print("4- Fin del programa")
    opcion_Elegida = int(input("Elige una opcion"))
    return opcion_Elegida

opcion_Elegida = menu()

while opcion_Elegida != 4:
    if opcion_Elegida == 1:
        print(numero1 + numero2)
    elif opcion_Elegida == 2:
        print(numero1 - numero2)
    elif opcion_Elegida == 3:
        print(numero1 * numero2)
    else:
        print("Opcion invalida. Vuelve a elegir")   
    print("*" *90)
    print("MUY BIEN!!! VUELVE A ELEGIR") 
    opcion_Elegida = menu()

print("El programa a finalizado")
                



