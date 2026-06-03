import csv
print(f"{"*" * 5}BIENVENIDO A LA HERMANDAD CHINA{"*" * 5}")
with open("catalogo.csv") as archivo:
        lector=csv.reader(archivo)
        for fila in lector:
            for producto in fila:
                print(f" {producto} ",end="")
            print("")
print("MENU DE OPCCIONES:")
print("1. COMPRAR")
print("2. SALIR")
