""" Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto)) """


numeros_Del_0_Al_10 = list(range(0,11,1))
numeros_Del_menos10_Al_0 = list(range(-10,1,1))
numeros_Pares_0_Al_20 = list(range(0,21,2))
numeros_Impares_menos20_Al_0 = list(range(-19,0,2))
numeros_Multiplos_De_5_Del_0_Al_50 = list(range(0,51,5))

print(numeros_Del_0_Al_10)
print("-" * 100)
print(numeros_Del_menos10_Al_0)
print("-" * 100)
print(numeros_Pares_0_Al_20)
print("-" * 100)
print(numeros_Impares_menos20_Al_0)
print("-" * 100)
print(numeros_Multiplos_De_5_Del_0_Al_50)


    