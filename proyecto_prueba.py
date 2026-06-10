import json

try:
    # 1. Cargar las credenciales de usuario al principio
    with open("credenciales.json", "r", encoding="utf-8") as archivo:
        credencial = json.load(archivo)
        if isinstance(credencial, dict):
            lista_de_usuarios = [credencial]
        else:
            lista_de_usuarios = credencial

    print("="*30)
    print("BIENVENIDO AL SISTEMA ACCESO")
    print("="*30)
    print("1. Iniciar sesion")
    print("2. Registrarse")
    opcion_inicio = int(input("Elija una opción (1-2): "))
    
    acceso_concedido = False

    match opcion_inicio:
        case 1:
            print("="*30)
            print("INICIO DE SESIÓN:")
            intentos_usuario = 3

            while intentos_usuario > 0:
                user = input("Por favor, ingrese su usuario: ")
                usuario_encontrado = None
                
                for u in lista_de_usuarios:
                    if u["usuario"] == user:
                        usuario_encontrado = u
                        break
                
                if usuario_encontrado is not None:
                    print("USUARIO CORRECTO")
                    intentos_contrasena = 3

                    while intentos_contrasena > 0:
                        contrasena = input("Por favor, Ingrese su contraseña: ")
                        if str(contrasena) == str(usuario_encontrado["contrasena"]):
                            print("CONTRASEÑA CORRECTA. INICIANDO SESIÓN....")
                            acceso_concedido = True
                            break
                        else:
                            intentos_contrasena -= 1
                            print(f"CONTRASEÑA INCORRECTA. Intentos restantes: {intentos_contrasena}")
                    
                    if acceso_concedido:
                        break
                else:
                    intentos_usuario -= 1
                    print(f"ERROR: {user} no está en la lista de usuarios. Intentos restantes {intentos_usuario}")

        case 2:
            try:
                print("="*30)
                print("REGISTRO DE USUARIO:")
                
                # Volvemos a leer para asegurarnos de tener los datos más frescos
                with open("credenciales.json", "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
                    if isinstance(datos, dict):
                        datos = [datos]
                
                p = True
                username = ""
                while p:
                    username = input("Ingrese el nombre de usuario: ")
                    if any(u.get("usuario") == username for u in datos) or username == "":
                        print("¡Error! Ese nombre no es válido o ya existe")
                    else:
                        print("Excelente. Ese nombre de usuario se encuentra disponible.")
                        p = False

                m = True
                contra = ""
                while m:
                    contra = input("Ingrese una contraseña: ")
                    if any(u.get("contrasena") == contra for u in datos) or contra == "":
                        print("¡Error! Por seguridad, no se puede usar una contraseña ya registrada o vacía.")
                    else:
                        print("Excelente. Es una buena contraseña")
                        m = False

                new_registro = {
                    "usuario": username,
                    "contrasena": contra
                }
                datos.append(new_registro)
                
                with open("credenciales.json", "w", encoding="utf-8") as archivo:
                    json.dump(datos, archivo, indent=4, ensure_ascii=False)
                
                print(f"¡Usuario {username} agregado exitosamente!")
                acceso_concedido = True
                
            except Exception as e:
                print(f"Ocurrio un error al guardar el usuario: {e}")

    # ==================== MENÚ PRINCIPAL DEL SISTEMA ====================
    if acceso_concedido:
        print("\n--- BIENVENIDO AL SISTEMA ---")
        while True:           
            print("\n1. Crear catálogo desde cero")
            print("2. Cargar catálogo ya existente")
            print("3. Agregar nuevos usuarios")
            print("4. Salir del sistema")
            opcion = int(input("Ingrese una opción (1-4): "))
            
            match opcion:
                case 1:
                    print("="*30)
                    print("CREACIÓN DE CATÁLOGO")
                    cant = int(input("¿Cuántos productos desea agregar?: "))
                    inventario = []
                    
                    for i in range(1, cant + 1):
                        print(f"Producto {i}:")
                        nombre = input("Nombre: ")
                        precio = float(input("Precio: "))
                        cantidad = int(input("Cantidad: "))
                        categoria = input("Categoría: ")
                        
                        producto = {
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad,
                            "categoria": categoria
                        }
                        inventario.append(producto)

                    # Guardar el catálogo (Bloque independiente)
                    with open("catalogo.json", "w", encoding="utf-8") as archivo:
                        json.dump(inventario, archivo, indent=4, ensure_ascii=False)
                    
                    print("\nCatálogo creado con éxito:")
                    print(json.dumps(inventario, indent=2, ensure_ascii=False))
                    
                    # Submenú de operaciones
                    while True:
                        print("\n¿Qué operación desea realizar?")
                        print("1. Agregar producto/s")
                        print("2. Eliminar producto/s")
                        print("3. Actualizar datos de producto")
                        print("4. Volver al menú anterior")
                        opcion1 = int(input("Por favor, escoja una opción: "))
                        
                        match opcion1:
                            case 1:
                                cant = int(input("¿Cuántos productos desea añadir?: "))
                                # Se lee el archivo existente para no borrar lo anterior
                                with open("catalogo.json", "r", encoding="utf-8") as archivo:
                                    inventario_actual = json.load(archivo)
                                
                                for i in range(1, cant + 1):
                                    print(f"Nuevo Producto {i}:")
                                    nombre = input("Nombre: ")
                                    precio = float(input("Precio: "))
                                    cantidad = int(input("Cantidad: "))
                                    categoria = input("Categoría: ")
                                    
                                    producto = {
                                        "nombre": nombre,
                                        "precio": precio,
                                        "cantidad": cantidad,
                                        "categoria": categoria
                                    }
                                    inventario_actual.append(producto)
                                
                                with open("catalogo.json", "w", encoding="utf-8") as archivo:
                                    json.dump(inventario_actual, archivo, indent=4, ensure_ascii=False)
                                print("¡Productos agregados!")
                                
                            case 2:
                                print("Función de eliminar en desarrollo...")
                            case 3:
                                print("Función de actualizar en desarrollo...")
                            case 4:
                                print("Regresando al menú anterior...")
                                break
                            case _:
                                print("Opción inválida.")

                case 2:
                    try:
                        print("="*30)
                        print("CARGAR CATÁLOGO:")
                        nombre_archivo = input("Ingrese el nombre y extensión del archivo (ej: catalogo.json): ")
                        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                            lector = json.load(archivo)
                        
                        print("CATÁLOGO CARGADO CON ÉXITO:")
                        print(json.dumps(lector, indent=2, ensure_ascii=False))
                        
                        while True:
                            print("\n¿Qué operación desea realizar?")
                            print("1. Agregar producto/s")
                            print("2. Eliminar producto/s")
                            print("3. Actualizar datos de producto")
                            print("4. Volver al menú anterior")
                            opcion1 = int(input("Por favor, escoja una opción: "))
                            
                            match opcion1:
                                case 1:
                                    print("Función de agregar en desarrollo...")
                                case 2:
                                    print("Función de eliminar en desarrollo...")
                                case 3:
                                    print("Función de actualizar en desarrollo...")
                                case 4:
                                    print("Regresando al menú anterior...")
                                    break
                                case _:
                                    print("Opción inválida.")
                    except FileNotFoundError:
                        print("ERROR. CATÁLOGO NO ENCONTRADO")
                    except Exception as e:
                        print(f"Error al cargar archivo: {e}")

                case 3:
                    try:
                        print("="*30)
                        print("REGISTRO DE USUARIOS EN EL SISTEMA:")
                        with open("credenciales.json", "r", encoding="utf-8") as archivo:
                            datos = json.load(archivo)
                            if isinstance(datos, dict):
                                datos = [datos]
                        
                        username = input("Ingrese el nuevo nombre de usuario: ")
                        if any(u.get("usuario") == username for u in datos) or username == "":
                            print("¡Error! Ese nombre no es válido o ya existe.")
                        else:
                            contra = input("Ingrese una contraseña: ")
                            if any(u.get("contrasena") == contra for u in datos) or contra == "":
                                print("¡Error! Contraseña inválida o ya en uso.")
                            else:
                                new_registro = {"usuario": username, "contrasena": contra}
                                datos.append(new_registro)
                                with open("credenciales.json", "w", encoding="utf-8") as archivo:
                                    json.dump(datos, archivo, indent=4, ensure_ascii=False)
                                print(f"¡Usuario {username} agregado exitosamente!")
                    except Exception as e:
                        print(f"Ocurrió un error al guardar el usuario: {e}")

                case 4:
                    print("Saliendo del sistema. Se cerró sesión exitosamente.")
                    break
                case _:
                    print("Opción no válida. Intente de nuevo.")
            
except FileNotFoundError:
    print("ERROR CRÍTICO: El archivo 'credenciales.json' no existe. Por favor créalo con un formato [] o {} vacío.")
except Exception as e:
    print(f"ERROR GENERAL: {e}")