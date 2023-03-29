edad = int(input("Ingrese su edad"))
antiguedad = int(input("Ingrese los años de antiguedad que tiene en el sistema financiero"))
ingreso = float(input("Que ingresos tiene en dolares??"))

if (antiguedad >= 3) and (edad>=18) and (ingreso>2500):
    print("Su credito a sido aprobado")
elif(antiguedad < 3) and (edad>=18) and (ingreso>=4000):
    print("Su credito a sido aprobado")
else:
    print("Su credito no ah sido aprobado")
    