""" Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente. """


numero = int(input("elige un numero impar"))
es_par = numero % 2
while True:
    if es_par == 0:
        print("Ese numero es par")
        numero = int(input("elige un numero impar"))
        es_par = numero % 2
    else:
        print("Perfecto ese numero es impar") 
        break