print("A continuacion te pediremos algunos datos para sacar el promedio final de tu equipo")
partidos_Ganados = int(input("Ingrese con numeros cantidas de partidos ganados"))*3
print(partidos_Ganados)
partidos_Empatados = int( input("Ingrese con numeros cantidas de partidos empatados"))*1
print(partidos_Empatados)
partidos_Perdidos = int(input("Ingrese con numeros cantidas de partidos perdidos") )*0
print(partidos_Perdidos)

Promedio = int(partidos_Ganados + partidos_Empatados + partidos_Perdidos)/20
print("El promedio de tu equipo es de " + str(Promedio))