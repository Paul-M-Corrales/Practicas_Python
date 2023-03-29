nombre = input("Escriba su nombre")
preferencia = input("Escriba M si prefiere a MARVEL o escriba C si prefiere a CAPCOM")

nombre = nombre.upper()
preferencia = preferencia.upper()

if (preferencia == "M") and (nombre < "M") or (preferencia == "C" and nombre>= "N"):
    print("Tu grupo es el A")
else:
    print("Tu grupo es el B")
    