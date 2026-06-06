import json
try:
    with open("credenciales.json", "r", encoding= "utf-8") as archivo:
        credencial = json.load(archivo)
        print(credencial)
        print("BIENVENIDO")
        user = input("Por favor, ingrese su usuario: ")
        if user in credencial.values():
            print("USUARIO CORRECTO")
            contrasena = input("Por favor, Ingrese su contraseña: ")
            if contrasena in credencial.values():
                print("CONTRASEÑA CORRECTA")
                print("INICIANDO SESION")
                print("BIENVENIDO AL SISTEMA")
                print("1. Agregar productos")
                print("2. Cargar inventario ya existente")
                opcion = int(input("Ingrese una opción (1-2): "))
                match opcion:
                    case 1:
                        with open("catalogo.json", "w", encoding="utf-8") as archivo:
                            nombre = ""
                            precio = 0
                            cantidad = 0
                            categoria = ""
                            cant = int(input("Cuántos productos desea agregar?: "))
                            inventario = []
                            for i in range(1, cant+1):
                                nombre = input(f"Ingrese nombre del producto {i}: ")
                                precio = float(input(f"Ingrese el precio del producto {i}: "))
                                cantidad = int(input(f"Cantidad de unidades del producto {i}: "))
                                categoria = input(f"Ingrese la categoría del producto {i}: ")
                                producto = {
                                    "nombre": nombre,
                                    "precio": precio,
                                    "cantidad": cantidad,
                                    "categoria": categoria}
                                inventario.append(producto)
                            json.dump(inventario, archivo, indent=4, ensure_ascii=False)
                    case 2:
                        try:
                            nombre = input("Ingrese el nombre y dominio del archivo: ")
                            with open(nombre, "r") as archivo:
                                lector = json.load(archivo)

                        except IOError:
                            print("ERROR. CATÁLOGO NO ENCONTRADO")
            else:
                print("CONTRASEÑA INCORRECTA")

        else:
            print(f"ERROR: {user} no está en la lista de usuarios")
except Exception as e:
    print(f"ERROR: {e}")