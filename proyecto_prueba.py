import json
lista_de_usuarios = []
try:
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

                with open("credenciales.json", "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
                    if isinstance(datos, dict):
                        datos = [datos]

                p = True
                m = True
                while p:
                    username = input("Ingrese el nombre de usuario: ")
                    if any(u.get("usuario") == username for u in datos) or username == "":
                        print("¡Error! Ese nombre no es válido")
                    else:
                        print("Excelente. Ese nombre de usuario se encuentra disponible.")
                        p = False

                while m:
                    contra = input("Ingrese una contraseña: ")
                    if any(u.get("contrasena") == contra for u in datos) or contra == "":
                        print("¡Error! Por seguridad, no se puede usar un contraseña ya registrada.")
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

    if acceso_concedido:
        print("\n ---BIENVENIDO AL SISTEMA---")
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

                    cant = int(input("Cuántos productos desea agregar?: "))
                    inventario = []
                    for i in range(1, cant+1):
                        print(f"Producto {i}:")
                        nombre = input("Nombre: ").title()
                        precio = float(input("Precio: "))
                        cantidad = int(input("Cantidad: "))
                        descrip = input("Descripción: ").title()
                        producto = {
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad,
                            "descripcion": descrip}
                        inventario.append(producto)

                    with open("catalogo.json", "w", encoding="utf-8") as archivo:
                        json.dump(inventario, archivo, indent=4, ensure_ascii=False)
                        
                    with open("catalogo.json", "r", encoding="utf-8") as archivo:
                        lector = json.load(archivo)
                        print(json.dumps(lector, indent=2, ensure_ascii=False))

                    while True:
                        print("\n¿Qué operación desea realizar?")
                        print("1. Agregar producto/s")
                        print("2. Eliminar producto/s")
                        print("3. Visualizar el catálogo")
                        print("4. Volver al menú anterior")
                        opcion1 = int(input("Por favor, escoja una opción: "))
                        match opcion1:
                            case 1:
                                with open("catalogo.json", "r", encoding="utf-8") as archivo:
                                    inventario_actual = json.load(archivo)
                                cant = int(input("Cuántos productos desea agregar?: "))
                                for i in range(1, cant+1):
                                    print(f"Producto {i}:")
                                    nombre = input("Nombre: ").title()
                                    precio = float(input("Precio: "))
                                    cantidad = int(input("Cantidad: "))
                                    descrip = input("Descripción: ").title()
                                    producto = {
                                        "nombre": nombre,
                                        "precio": precio,
                                        "cantidad": cantidad,
                                        "descripcion": descrip}
                                    inventario_actual.append(producto)

                                with open("catalogo.json", "w", encoding="utf-8") as archivo:
                                    json.dump(inventario_actual, archivo, indent=4, ensure_ascii=False)
                                with open("catalogo.json", "r", encoding="utf-8") as archivo:
                                    lector = json.load(archivo)
                                    print(json.dumps(lector, indent=2, ensure_ascii=False))
                            case 2:
                                try:
                                    with open("catalogo.json", "r", encoding="utf-8") as archivo:
                                        productos = json.load(archivo)
                                except FileNotFoundError:
                                    print("El archivo no existe.")
                                    productos = []
                                if productos:
                                    prod_eliminar = input("Ingrese el nombre del producto a eliminar: ").title()
                                    prod_actualizados = [p for p in productos if p["nombre"] != prod_eliminar]
                                    if len(prod_actualizados) == len(productos):
                                        print(f"Error. El producto '{prod_eliminar}' no se encuentra en el catálogo.")
                                    else:
                                        with open("catalogo.json", "w", encoding="utf-8") as archivo:
                                            json.dump(prod_actualizados, archivo, indent=4, ensure_ascii=False)
                                        print(f"El producto '{prod_eliminar}' ha sido eliminado.")
                            case 3:
                                try:
                                    with open("catalogo.json", "r", encoding="utf-8") as archivo:
                                        datos = json.load(archivo)
                                        print(json.dumps(datos, indent=4, ensure_ascii=False))
                                except IOError:
                                    print("Error al leer el archivo.")
                            case 4:
                                print("Regresando al menú anterior...")
                                break
                            case _:
                                print("Opción inválida.")

                case 2:
                    try:
                        print("="*30)
                        print("CARGAR CATÁLOGO:")
                        nombre_cat = input("Ingrese el nombre y extensión del archivo (ej. catalogo.json): ")
                        with open(nombre_cat, "r", encoding="utf-8") as archivo:
                            lector = json.load(archivo)
                            print("CATÁLOGO CARGADO CON ÉXITO:")
                            print(json.dumps(lector, indent=2, ensure_ascii=False))

                        while True:
                            print("\n¿Qué operación desea realizar?")
                            print("1. Agregar producto/s")
                            print("2. Eliminar producto/s")
                            print("3. Actualizar datos de producto")
                            print("4. Volver al menú anterior")

                            opcion2 = int(input("Por favor, escoja una opción: "))
                            match opcion2:
                                case 1:
                                    with open(nombre_cat, "r", encoding="utf-8") as archivo:
                                        inventario_actual = json.load(archivo)
                                    cant = int(input("Cuántos productos desea agregar?: "))
                                    for i in range(1, cant+1):
                                        print(f"Producto {i}:")
                                        nombre = input("Nombre: ").title()
                                        precio = float(input("Precio: "))
                                        cantidad = int(input("Cantidad: "))
                                        descrip = input("Descripción: ").title()
                                        producto = {
                                            "nombre": nombre,
                                            "precio": precio,
                                            "cantidad": cantidad,
                                            "descripcion": descrip}
                                        inventario_actual.append(producto)

                                    with open(nombre_cat, "w", encoding="utf-8") as archivo:
                                        json.dump(inventario_actual, archivo, indent=4, ensure_ascii=False)
                                    with open(nombre_cat, "r", encoding="utf-8") as archivo:
                                        lector = json.load(archivo)
                                        print(json.dumps(lector, indent=2, ensure_ascii=False))
                                case 2:
                                    try:
                                        with open(nombre_cat, "r", encoding="utf-8") as archivo:
                                            productos = json.load(archivo)
                                    except FileNotFoundError:
                                        print("El archivo no existe.")
                                        productos = []
                                    if productos:
                                        prod_eliminar = input("Ingrese el nombre del producto a eliminar: ").title()
                                        prod_actualizados = [p for p in productos if p["nombre"] != prod_eliminar]
                                        if len(prod_actualizados) == len(productos):
                                            print(f"Error. El producto '{prod_eliminar}' no se encuentra en el catálogo.")
                                        else:
                                            with open(nombre_cat, "w", encoding="utf-8") as archivo:
                                                json.dump(prod_actualizados, archivo, indent=4, ensure_ascii=False)
                                            print(f"El producto '{prod_eliminar}' ha sido eliminado.")
                                case 3:
                                    print("Función de actualización aún no implementada.")
                                case 4:
                                    print("Regresando al menú anterior...")
                                    break
                                case _:
                                    print("Opción inválida.")
                    except IOError:
                        print("ERROR. CATÁLOGO NO ENCONTRADO")

                case 3:
                    try:
                        print("="*30)
                        print("REGISTRO DE NUEVOS USUARIOS:")

                        with open("credenciales.json", "r", encoding="utf-8") as archivo:
                            datos = json.load(archivo)
                            if isinstance(datos, dict):
                                datos = [datos]

                        p = True
                        m = True
                        while p:
                            username = input("Ingrese el nombre de usuario: ")
                            if any(u.get("usuario") == username for u in datos) or username == "":
                                print("¡Error! Ese nombre no es válido o ya existe.")
                            else:
                                print("Excelente. Ese nombre de usuario se encuentra disponible.")
                                p = False

                        while m:
                            contra = input("Ingrese una contraseña: ")
                            if any(u.get("contrasena") == contra for u in datos) or contra == "":
                                print("¡Error! Por seguridad, no se puede usar una contraseña ya registrada o en blanco.")
                            else:
                                print("Excelente. Es una buena contraseña.")
                                break 

                        new_registro = {
                            "usuario": username,
                            "contrasena": contra
                        }
                        datos.append(new_registro)
                        
                        with open("credenciales.json", "w", encoding="utf-8") as archivo:
                            json.dump(datos, archivo, indent=4, ensure_ascii=False)
                        print(f"¡Usuario '{username}' agregado exitosamente!")
                    except Exception as e:
                        print(f"Ocurrió un error al guardar el usuario: {e}")

                case 4:
                    print("Saliendo del sistema. Se cerró sesión exitosamente.")
                    break
                case _:
                    print("Opción no válida. Intente de nuevo.")

except FileNotFoundError:
    print("ERROR CRÍTICO: El archivo 'credenciales.json' no existe.")
except Exception as e:
    print(f"ERROR: {e}")