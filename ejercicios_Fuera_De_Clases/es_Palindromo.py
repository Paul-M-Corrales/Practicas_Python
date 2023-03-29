texto = str(input("ingrese palabra para saber si es Palindromo"))
texto_Invertido = texto[::-1]
if (texto == texto_Invertido):
    print("es palindromo")
else:
    print("no es palindromo")  

    
