numeros = []
cancelar = ""
while cancelar != "exit()":
    numeros.append(int(input("Ingrese un numero entero"))) 
    cancelar = input("Desea detener el programa?? Escriba exit() si no escriba no").lower()

print(sum(numeros))