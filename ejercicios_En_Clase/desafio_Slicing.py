cadena = "acitametaM,5.8,otipeP ordeP"
cadena_Volteada = cadena[::-1]
nombre_Alumno = cadena_Volteada[0:12]
nota = cadena_Volteada[13:16]
materia = cadena_Volteada[17:]
cadena_Formateada = nombre_Alumno + " a sacado un " + nota + " en " + materia
print(cadena_Formateada )