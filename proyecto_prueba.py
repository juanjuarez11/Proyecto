import json
import os

try:
    # 1. Cargar credenciales de forma segura
    with open("credenciales.json", "r", encoding="utf-8") as archivo:
        credencial = json.load(archivo)
    
    print("--- BIENVENIDO AL SISTEMA DE ACCESO ---")
    
    intentos_usuario = 3
    acceso_concedido = False

    # 2. Control de acceso
    while intentos_usuario > 0:
        user = input("\nPor favor, ingrese su usuario: ")
        
        # Validamos que coincida exactamente con la clave de tu JSON
        if user == credencial.get("usuario"):
            print("USUARIO CORRECTO")
            intentos_password = 3
            
            while intentos_password > 0:
                contrasena = input("Por favor, ingrese su contraseña: ")
                
                if contrasena == credencial.get("contrasena"):
                    print("\nCONTRASEÑA CORRECTA. INICIANDO SESIÓN...")
                    acceso_concedido = True
                    break # Rompe el bucle de la contraseña
                else:
                    intentos_password -= 1
                    print(f"CONTRASEÑA INCORRECTA. Intentos restantes: {intentos_password}")
            
            if acceso_concedido:
                break # Rompe el bucle del usuario si ya ingresó
        else:
            intentos_usuario -= 1
            print(f"ERROR: '{user}' no es un usuario válido. Intentos restantes: {intentos_usuario}")

    # 3. Menú Principal (Solo si el acceso fue concedido)
    if acceso_concedido:
        while True:
            print("\n" + "="*30)
            print("      MENÚ DE INVENTARIO")
            print("="*30)
            print("1. Agregar productos")
            print("2. Cargar inventario ya existente")
            print("3. Salir del sistema")
            
            try:
                opcion = int(input("Ingrese una opción (1-3): "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            match opcion:
                case 1:
                    # Cargar inventario existente primero para no borrarlo
                    inventario = []
                    if os.path.exists("catalogo.json"):
                        try:
                            with open("catalogo.json", "r", encoding="utf-8") as archivo:
                                inventario = json.load(archivo)
                        except json.JSONDecodeError:
                            inventario = []

                    cant = int(input("\n¿Cuántos productos desea agregar?: "))
                    
                    for i in range(1, cant + 1):
                        print(f"\n--- Producto {i} ---")
                        nombre = input("Nombre: ")
                        precio = float(input("Precio: "))
                        cantidad = int(input("Cantidad de unidades: "))
                        categoria = input("Categoría: ")
                        
                        producto = {
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad,
                            "categoria": categoria
                        }
                        inventario.append(producto)
                    
                    # Guardar la lista actualizada
                    with open("catalogo.json", "w", encoding="utf-8") as archivo:
                        json.dump(inventario, archivo, indent=4, ensure_ascii=False)
                    print("\n¡Productos agregados con éxito al catálogo!")

                case 2:
                    nombre_archivo = input("\nIngrese el nombre del archivo (ej. catalogo.json): ")
                    try:
                        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                            lector = json.load(archivo)
                            print("\n--- CATÁLOGO CARGADO ---")
                            print(json.dumps(lector, indent=2, ensure_ascii=False))
                    except (IOError, json.JSONDecodeError):
                        print("ERROR: Archivo no encontrado o formato inválido.")
                
                case 3:
                    print("\nSaliendo del sistema. ¡Cierre de sesión exitoso!")
                    break
                case _:
                    print("Opción no válida. Intente de nuevo.")
    else:
        print("\nAcceso denegado. Intentos agotados.")

except FileNotFoundError:
    print("ERROR CRÍTICO: El archivo 'credenciales.json' no existe.")
except Exception as e:
    print(f"ERROR INESPERADO: {e}")