numeros = []
cancelar = ""
while cancelar != "exit()":
    numeros.append(int(input("Ingrese un numero entero"))) 
    cancelar = input("Desea detener el programa?? Escriba exit() si no escriba no").lower()
print(f"la suma parcial es de {numeros}")
print(f"la suma total es de {sum(numeros)}")