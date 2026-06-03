import json
try:
    with open("catalogo.json", "r") as archivo:
        catalogo=json.load(archivo)
        for fila in catalogo:
           print(f"Nombre: {fila["Nombre"]} | Precio: {fila["Precio"]} | Cantidad: {fila["Cantidad"]} | Color: {fila["Color"]}")
    with open("catalogo.json") as archivo:
        catalogo=json.load(archivo)
        compra = input("Que producto desea comprar?: ").capitalize()
        producto_encontrado = next((p for p in catalogo if p["Nombre"].capitalize() == compra), None)
        if producto_encontrado:
            print(f"Producto: {producto_encontrado["Nombre"]}")
            print(f"Precio: {producto_encontrado["Precio"]}")
            print(f"Cantidad: {producto_encontrado["Cantidad"]}")
except Exception as e:
    print(e)