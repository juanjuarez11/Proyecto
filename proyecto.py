import json
try:
    with open("credenciales.json", "r", encoding= "utf-8") as archivo:
        credencial = json.load(archivo)
        print("BIENVENIDO AL SISTEMA ACCESO")

        intentos_usuario=3
        acceso_concedido = False

        while intentos_usuario > 0:
            user = input("Por favor, ingrese su usuario: ")

            if user == credencial["usuario"]:
                print("USUARIO CORRECTO")
                intentos_contrasena = 3

                while intentos_contrasena > 0:
                    contrasena = input("Por favor, Ingrese su contraseña: ")
                    if contrasena == credencial["contrasena"] and not acceso_concedido:
                        print("CONTRASEÑA CORRECTA. INICIANDO SESIÓN....")
                        acceso_concedido = True
                        break
                    else:
                        intentos_contrasena-=1
                        print(f"CONTRASEÑA INCORRECTA. Intentos restantes: {intentos_contrasena}")
                if acceso_concedido:
                        break
            else:
                intentos_usuario-=1
                print(f"ERROR: {user} no está en la lista de usuarios")
                print(f"Intentos restantes {intentos_usuario}")

    if acceso_concedido:
        while True:           
            print("BIENVENIDO AL SISTEMA")
            print("1. Agregar productos")
            print("2. Cargar inventario ya existente")
            print("3. Salir del sistema")
            opcion = int(input("Ingrese una opción (1-3): "))
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
                case 3:
                    print("Saliendo del sistema. Se cerró sesión exitosamente")
                    break
                case _:
                    print("Opción no válida. Intente de nuevo.")
            
    else:
        print("Intentos agotados. Saliendo del sistema")
except FileNotFoundError:
    print("ERROR CRÍTICO: El archivo 'credenciales.json' no existe.")
except Exception as e:
    print(f"ERROR: {e}")