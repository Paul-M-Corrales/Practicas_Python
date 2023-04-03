"""  Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False). """

lista = int(input("Escribe un numero entre 0 y 9"))
while True:
    if (lista < 0) or (lista > 9):
        lista = int(input("Escribe un numero entre 0 y 9"))
    else:
        print(lista)
        break
