generacion = int(input("Escriba su año de nacimiento"))

if (generacion >= 1920) and (generacion <=1940):
    print(f"Tu generacion es.... GENERACION SILENCIOSA ya que naciste en el año {generacion} ")
elif(generacion >= 1946) and (generacion <= 1964):
    print(f"Tu generacion es.... BABY BOOMER ya que naciste en el año {generacion} ")
elif(generacion >= 1965) and (generacion <= 1979):
    print(f"Tu generacion es.... GENERACION X ya que naciste en el año {generacion} ")
elif(generacion >= 1980) and (generacion <= 2000):
    print(f"Tu generacion es.... GENERACION Y ya que naciste en el año {generacion} ")
elif(generacion >= 2001) and (generacion <= 2010):
    print(f"Tu generacion es.... GENERACION Z ya que naciste en el año {generacion} ")
else:
    print("NO EXISTE GENERACION ASOCIADA")