import json
try:
    with open("credenciales.json", "r", encoding= "utf-8") as archivo:
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
    print("")
    opcion_inicio = int(input("Elija una opción (1-2): "))
    print("")

    match opcion_inicio:
        case 1:
            try:
                print("="*30)
                print("--INICIO DE SESIÓN--:")
                print("="*30)
                print("")

                intentos_usuario=3
                acceso_concedido = False

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
                                intentos_contrasena-=1
                                print(f"CONTRASEÑA INCORRECTA. Intentos restantes: {intentos_contrasena}")

                        if acceso_concedido:
                            break

                    else:
                        intentos_usuario-=1
                        print(f"ERROR: {user} no está en la lista de usuarios. Intentos restantes {intentos_usuario}")
            except Exception as e:
                print(f"ERROR. {e}")
        case 2:
            try:
                print("="*30)
                print("REGISTRO DE USUARIO:")
                        
                with open("credenciales.json","r", encoding= "utf-8")as archivo:
                    datos=json.load(archivo)
                    if isinstance (datos, dict):
                        datos=[datos]
                        
                p = True
                m = True
                while p:
                    username=input("Ingrese el nombre de usuario: ")
                    if any(u.get("usuario")==username for u in datos) or username == "":
                        print("¡Error! Ese nombre no es válido")
                                
                    else:
                        print("Excelente. Ese nombre de usuario se encuentra disponible.")
                        p = False

                while m:
                    contra=input("Ingrese una contraseña: ")
                    if any(u.get("contrasena")== contra for u in datos) or contra == "":
                        print("¡Error! Por seguridad, no se puede usar esa contraseña.")

                    else:
                        print("Excelente. Es una buena contraseña")
                        m = False

                new_registro={
                    "usuario":username,
                    "contrasena":contra
                }
                datos.append(new_registro)
                            
                with open("credenciales.json","w", encoding= "utf-8")as archivo:
                    json.dump(datos,archivo, indent=4, ensure_ascii=False)
                print(f"¡Usuario {username} agregado exitosamente!")
                acceso_concedido = True
            except Exception as e:
                print(f"Ocurrio un error al guardar el usuario: {e}")
        case _:
            print("ERROR. Opción no valida")
            acceso_concedido = False
    if acceso_concedido:
        print("\n ---BIENVENIDO AL SISTEMA---")
        while True:           
            print("1. Crear catálogo desde cero")
            print("2. Cargar catálogo ya existente")
            print("3. Agregar nuevos usuarios")
            print("4. Salir del sistema")
            opcion = int(input("Ingrese una opción (1-4): "))
            match opcion:
                case 1:
                    try: 
                        print("="*30)
                        print("CREACIÓN DE CATÁLOGO")
                        while True:
                            nombre_cat_nuevo = input("Ingrese el nombre que quiere que tenga su catálogo y el dominio .json (ej: catalogo.json): ")
                            if nombre_cat_nuevo == "":
                                print("ERROR. ESTE NOMBRE NO ES VALIDO PARA EL NOMBRE DEL CATALOGO")
                            else:
                                break
                        cant = int(input("Cuántos productos desea agregar?: "))
                        inventario = []
                        for i in range(1, cant+1):
                            print(f"Producto {i}:")
                            while True:
                                id_prod = input("ID del producto (Formato 0000): ")
                                if id_prod == "":
                                    print("Error. Este campo no puede estar vacio")
                                elif any(p.get("id") == id_prod for p in inventario):
                                    print(f"Error. El ID {id_prod} ya está registrado. Ingrese otro por favor")
                                else:
                                    break
                            nombre = input("Nombre: ").title()
                            while True:
                                precio = float(input("Precio: "))
                                if precio < 0 or precio == "":
                                    print("ERROR. No se acepta este valor")
                                else:
                                    break
                            while True:
                                cantidad = int(input("Cantidad: "))
                                if cantidad <= 0 or cantidad == "":
                                    print("ERROR. No se acepta este valor.")
                                else:
                                    break
                            descrip = input("Descripción: ").title()
                            producto = {
                                "id": id_prod,
                                "nombre": nombre,
                                "precio": precio,
                                "cantidad": cantidad,
                                "descripcion": descrip}
                            inventario.append(producto)

                        with open(nombre_cat_nuevo, "w", encoding= "utf-8") as archivo:
                            json.dump(inventario, archivo, indent=4, ensure_ascii=False)
                    except Exception as e:
                        print(f"ERROR. {e}")
                    print("CATALOGO CREADO CON ÉXITO")
                    print("="*30)
                    while True:
                        print("Que operación desea realizar?")
                        print("1. Agregar producto/s")
                        print("2. Eliminar producto")
                        print("3. Actualizar datos de un producto")
                        print("4. Visualizar el catálogo")
                        print("5. Registrar venta")
                        print("6. Volver al menu anterior")
                        opcion1 = int(input("Por favor, escoja una opción: "))
                        match opcion1:
                            case 1:
                                try:
                                    print("="*30)
                                    print("AGREGAR PRODUCTOS")
                                    with open(nombre_cat_nuevo, "r") as archivo:
                                        inventario_actual = json.load(archivo)
                                        cant = int(input("Cuántos productos desea agregar?: "))
                                        for i in range(1, cant+1):
                                            print(f"Producto {i}:")
                                            while True:
                                                id_prod = input("ID del producto (Formato 0000): ")
                                                if id_prod == "":
                                                    print("Error. Este campo no puede quedar vacio")
                                                elif any(p.get("id") == id_prod for p in inventario_actual):
                                                    print(f"Error. El ID {id_prod} ya está registrado. Ingrese otro por favor")
                                                else:
                                                    break
                                            
                                            nombre = input("Nombre: ").title()
                                            while True:
                                                precio = float(input("Precio: "))
                                                if precio < 0 or precio == "":
                                                    print("ERROR. No se acepta este valor")
                                                else:
                                                    break
                                            while True:
                                                cantidad = int(input("Cantidad: "))
                                                if cantidad <= 0 or cantidad == "":
                                                    print("ERROR. No se acepta este valor.")
                                                else:
                                                    break
                                            descrip = input("Descripción: ").title()
                                            producto = {
                                                "id": id_prod,
                                                "nombre": nombre,
                                                "precio": precio,
                                                "cantidad": cantidad,
                                                "descripcion": descrip}
                                            inventario_actual.append(producto)

                                    with open(nombre_cat_nuevo, "w", encoding= "utf-8") as archivo:
                                        json.dump(inventario_actual, archivo, indent=4, ensure_ascii=False)
                                    print("CATALOGO ACTUALIZADO CON EXITO")
                                    print("="*30)
                                except Exception as e:
                                    print(f"ERROR. {e}")
                            case 2:
                                try:
                                    print("="*30)
                                    print("ELIMINAR PRODUCTO")
                                    with open(nombre_cat_nuevo, "r", encoding="utf-8") as archivo:
                                        productos = json.load(archivo)
                                except FileNotFoundError:
                                    print("El archivo no existe.")
                                    productos = []
                                prod_eliminar = input("Ingrese el ID del producto a eliminar: ")
                                prod_actualizados = [p for p in productos if p["id"] != prod_eliminar]
                                if len(prod_actualizados) == len(productos):
                                    print(f"Error. El producto con ID {prod_eliminar} no se encuentra en el catálogo.")
                                else:
                                    with open(nombre_cat_nuevo, "w", encoding= "utf-8") as archivo:
                                        json.dump(prod_actualizados, archivo, indent=4, ensure_ascii=False)
                                    print(f"El producto con ID {prod_eliminar} ha sido eliminado.")
                                    print("="*30)
                            case 3:
                                try:
                                    print("="*30)
                                    print("MODIFICAR DATOS DE PRODUCTO")
                                    with open(nombre_cat_nuevo, "r", encoding="utf-8") as archivo:
                                        productos = json.load(archivo)

                                    id_buscar = input("Ingrese el ID del producto que desea modificar: ").strip()
                                    producto_encontrado = None
                                    for p in productos:
                                        if p["id"] == id_buscar:
                                            producto_encontrado = p
                                            break
                                    
                                    if producto_encontrado is not None:
                                        print(f"\nProducto encontrado: {producto_encontrado['nombre']}")
                                        print("¿Qué dato desea modificar?")
                                        print("1. Nombre")
                                        print("2. Precio")
                                        print("3. Cantidad")
                                        print("4. Descripción")

                                        opcion_mod = int(input("Seleccione una opción (1-4): "))

                                        match opcion_mod:
                                            case 1:
                                                nuevo_nombre = input("Ingrese el nuevo nombre: ").strip().title()
                                                producto_encontrado["nombre"] = nuevo_nombre
                                            case 2:
                                                while True:
                                                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                                                    if nuevo_precio < 0 or nuevo_precio == "":
                                                        print("ERROR. No se acepta este valor")
                                                    else:
                                                        producto_encontrado["precio"] = nuevo_precio
                                                        break
                                            case 3:
                                                while True:
                                                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                                                    if nueva_cantidad <= 0 or nueva_cantidad == "":
                                                        print("ERROR. No se acepta este valor")
                                                    else:
                                                        producto_encontrado["cantidad"] = nueva_cantidad
                                                        break
                                            case 4:
                                                nueva_desc = input("Ingrese la nueva descripción: ").strip().title()
                                                producto_encontrado["descripcion"] = nueva_desc
                                            case _:
                                                print("Opción no válida. No se hicieron cambios.")
                                        
                                        with open(nombre_cat_nuevo, "w", encoding="utf-8") as archivo:
                                            json.dump(productos, archivo, indent= 4, ensure_ascii=False)
                                        print("Producto actualizado con éxito")
                                        print("="*30)
                                    else:
                                        print(f"Error. El producto con ID {id_buscar} no existe.")
                                except Exception as e:
                                    print(f"Error al realizar la operación. {e}")
                            case 4:
                                try:
                                    print("="*30)
                                    print("VISUALIZAR CATALOGO")
                                    with open(nombre_cat_nuevo,"r",encoding="utf-8")as archivo:
                                        datos=json.load(archivo)
                                        print(json.dumps(datos, indent=4, ensure_ascii=False))
                                    print("="*30)
                                except Exception as e:
                                    print(f"Error. Surgió un error al ejecutar esta tarea. {e}")
                            case 5:
                                try:
                                    print("="*30)
                                    print("REGISTRAR VENTA DE PRODUCTO")
                                    with open(nombre_cat_nuevo, "r", encoding="utf-8") as archivo:
                                        productos = json.load(archivo)

                                    id_buscar = input("Ingrese el ID del producto vendido: ").strip()
                                    
                                    producto_encontrado = None
                                    for p in productos:
                                        if p["id"] == id_buscar:
                                            producto_encontrado = p
                                            break
                                    
                                    if producto_encontrado is not None:
                                        print(f"Producto: {producto_encontrado['nombre']} | Existencias actuales: {producto_encontrado['cantidad']}")
                                        
                                        cant_vender = int(input("¿Cuántas unidades se vendieron?: "))
                                        
                                        if cant_vender > producto_encontrado["cantidad"]:
                                            print(f"¡Error! No hay suficiente stock. Solo quedan {producto_encontrado['cantidad']} unidades.")
                                        elif cant_vender <= 0:
                                            print("¡Error! La cantidad vendida debe ser mayor a cero.")
                                        else:
                                            producto_encontrado["cantidad"] -= cant_vender

                                            total_venta = cant_vender * producto_encontrado["precio"]
                                            
                                            with open(nombre_cat_nuevo, "w", encoding="utf-8") as archivo:
                                                json.dump(productos, archivo, indent=4, ensure_ascii=False)
                                            
                                            print("="*30)
                                            print("¡VENTA REGISTRADA CON ÉXITO!")
                                            print(f"Unidades vendidas: {cant_vender}")
                                            print(f"Total a cobrar: ${total_venta:.2f}")
                                            print(f"Existencias restantes en inventario: {producto_encontrado['cantidad']}")
                                            print("="*30)
                                            
                                    else:
                                        print(f"Error. El producto con ID {id_buscar} no existe.")
                                        
                                except Exception as e:
                                    print(f"Error al registrar la venta: {e}")
                            case 6:
                                print("Regresando al menu anterior...")
                                print("="*30)
                                break
                            case _:
                                    print("Opción inválida.")

                case 2:
                    try:
                        print("="*30)
                        print("CARGAR CATALOGO")
                        nombre_cat = input("Ingrese el nombre y dominio del archivo (ej: inventario.json): ")
                        with open(nombre_cat, "r", encoding= "utf-8") as archivo:
                            lector = json.load(archivo)
                            print("CATALOGO CARGADO CON EXITO:")
                            print("="*30)
                        
                        while True:
                            print("Que operación desea realizar?")
                            print("1. Agregar producto/s")
                            print("2. Eliminar producto")
                            print("3. Actualizar datos de un producto")
                            print("4. Visualizar el catálogo")
                            print("5. Registrar venta")
                            print("6. Volver al menu anterior")
                            opcion2 = int(input("Por favor, escoja una opción: "))
                            match opcion2:
                                case 1:
                                    try:
                                        print("="*30)
                                        print("AGREGAR PRODUCTOS")
                                        with open(nombre_cat, "r") as archivo:
                                            cant = int(input("Cuántos productos desea agregar?: "))
                                            inventario_actual = json.load(archivo)
                                            for i in range(1, cant+1):
                                                print(f"Producto {i}:")
                                                while True:
                                                    id_prod = input("ID del producto (Formato 0000): ")
                                                    if id_prod == "":
                                                        print("Error. Este campo no puede quedar vacio")
                                                    elif any(p.get("id") == id_prod for p in inventario_actual):
                                                        print(f"Error. El ID {id_prod} ya está registrado. Ingrese otro por favor")
                                                    else:
                                                        break
                                            
                                                nombre = input("Nombre: ").title()
                                                while True:
                                                    precio = float(input("Precio: "))
                                                    if precio < 0 or precio == "":
                                                        print("ERROR. No se acepta este valor")
                                                    else:
                                                        break
                                                while True:
                                                    cantidad = int(input("Cantidad: "))
                                                    if cantidad <= 0 or cantidad == "":
                                                        print("ERROR. No se acepta este valor.")
                                                    else:
                                                        break
                                                descrip = input("Descripción: ").title()
                                                producto = {
                                                    "id": id_prod,
                                                    "nombre": nombre,
                                                    "precio": precio,
                                                    "cantidad": cantidad,
                                                    "descripcion": descrip}
                                                inventario_actual.append(producto)

                                        with open(nombre_cat, "w", encoding= "utf-8") as archivo:
                                            json.dump(inventario_actual, archivo, indent=4, ensure_ascii=False)
                                        print("PRODUCTOS AGREGADOS CON EXITO")
                                        print("="*30)
                                    except Exception as e:
                                        print(f"Error: {e}")
                                    
                                case 2:
                                    try:
                                        print("="*30)
                                        print("ELIMINAR PRODUCTO")
                                        with open(nombre_cat, "r", encoding="utf-8") as archivo:
                                            productos = json.load(archivo)
                                    except FileNotFoundError:
                                        print("El archivo no existe.")
                                        productos = []
                                    prod_eliminar = input("Ingrese el ID del producto a eliminar: ")
                                    prod_actualizados = [p for p in productos if p["id"] != prod_eliminar]
                                    if len(prod_actualizados) == len(productos):
                                        print(f"Error. El producto con ID {prod_eliminar} no se encuentra en el catálogo.")
                                    else:
                                        with open(nombre_cat, "w", encoding= "utf-8") as archivo:
                                            json.dump(prod_actualizados, archivo, indent=4, ensure_ascii=False)
                                        print(f"El producto con ID {prod_eliminar} ha sido eliminado.")
                                        print("="*30)
                                case 3:
                                    try:
                                        print("="*30)
                                        print("MODIFICAR DATOS DE PRODUCTO")
                                        with open(nombre_cat, "r", encoding="utf-8") as archivo:
                                            productos = json.load(archivo)

                                        id_buscar = input("Ingrese el ID del producto que desea modificar: ").strip()
                                        producto_encontrado = None
                                        for p in productos:
                                            if p["id"] == id_buscar:
                                                producto_encontrado = p
                                                break
                                        
                                        if producto_encontrado is not None:
                                            print(f"\nProducto encontrado: {producto_encontrado['nombre']}")
                                            print("¿Qué dato desea modificar?")
                                            print("1. Nombre")
                                            print("2. Precio")
                                            print("3. Cantidad")
                                            print("4. Descripción")

                                            opcion_mod = int(input("Seleccione una opción (1-4): "))

                                            match opcion_mod:
                                                case 1:
                                                    nuevo_nombre = input("Ingrese el nuevo nombre: ").strip().title()
                                                    producto_encontrado["nombre"] = nuevo_nombre
                                                case 2:
                                                    while True:
                                                        nuevo_precio = float(input("Ingrese el nuevo precio: "))
                                                        if nuevo_precio < 0 or nuevo_precio == "":
                                                            print("ERROR. No se acepta este valor")
                                                        else:
                                                            producto_encontrado["precio"] = nuevo_precio
                                                            break
                                                case 3:
                                                    while True:
                                                        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                                                        if nueva_cantidad <= 0 or nueva_cantidad == "":
                                                            print("ERROR. No se acepta este valor")
                                                        else:
                                                            producto_encontrado["cantidad"] = nueva_cantidad
                                                            break
                                                case 4:
                                                    nueva_desc = input("Ingrese la nueva descripción: ").strip().title()
                                                    producto_encontrado["descripcion"] = nueva_desc
                                                case _:
                                                    print("Opción no válida. No se hicieron cambios.")
                                            
                                            with open(nombre_cat, "w", encoding="utf-8") as archivo:
                                                json.dump(productos, archivo, indent= 4, ensure_ascii=False)
                                            print("Producto actualizado con éxito")
                                            print("="*30)
                                        else:
                                            print(f"Error. El producto con ID {id_buscar} no existe.")
                                    except Exception as e:
                                        print(f"Error al realizar la operación. {e}")
                                case 4:
                                    try:
                                        print("="*30)
                                        print("VISUALIZAR CATALOGO")
                                        with open(nombre_cat,"r",encoding="utf-8")as archivo:
                                            datos=json.load(archivo)
                                            print(json.dumps(datos, indent=4, ensure_ascii=False))
                                            print("="*30)
                                    except Exception as e:
                                        print(f"Error. Surgió un error al ejecutar esta tarea. {e}")
                                case 5:
                                    try:
                                        print("="*30)
                                        print("REGISTRAR VENTA DE PRODUCTO")
                                        with open(nombre_cat, "r", encoding="utf-8") as archivo:
                                            productos = json.load(archivo)

                                        id_buscar = input("Ingrese el ID del producto vendido: ").strip()
                                        
                                        producto_encontrado = None
                                        for p in productos:
                                            if p["id"] == id_buscar:
                                                producto_encontrado = p
                                                break
                                        
                                        if producto_encontrado is not None:
                                            print(f"Producto: {producto_encontrado['nombre']} | Existencias actuales: {producto_encontrado['cantidad']}")
                                            
                                            cant_vender = int(input("¿Cuántas unidades se vendieron?: "))
                                            
                                            if cant_vender > producto_encontrado["cantidad"]:
                                                print(f"¡Error! No hay suficiente stock. Solo quedan {producto_encontrado['cantidad']} unidades.")
                                            elif cant_vender <= 0:
                                                print("¡Error! La cantidad vendida debe ser mayor a cero.")
                                            else:
                                                producto_encontrado["cantidad"] -= cant_vender

                                                total_venta = cant_vender * producto_encontrado["precio"]
                                                
                                                with open(nombre_cat, "w", encoding="utf-8") as archivo:
                                                    json.dump(productos, archivo, indent=4, ensure_ascii=False)
                                                
                                                print("="*30)
                                                print("¡VENTA REGISTRADA CON ÉXITO!")
                                                print(f"Unidades vendidas: {cant_vender}")
                                                print(f"Total a cobrar: ${total_venta:.2f}")
                                                print(f"Existencias restantes en inventario: {producto_encontrado['cantidad']}")
                                                print("="*30)
                                                
                                        else:
                                            print(f"Error. El producto con ID {id_buscar} no existe.")
                                            
                                    except Exception as e:
                                        print(f"Error al registrar la venta: {e}")

                                case 6:
                                    print("Regresando al menu anterior...")
                                    print("="*30)
                                    break
                                case _:
                                    print("Opción inválida.")
                    except IOError:
                        print("ERROR. CATÁLOGO NO ENCONTRADO")
                case 3:
                    try:
                        print("="*30)
                        print("REGISTRO DE USUARIOS:")
                        
                        with open("credenciales.json","r", encoding= "utf-8")as archivo:
                            datos=json.load(archivo)
                            if isinstance (datos, dict):
                                datos=[datos]
                        
                        p = True
                        m = True
                        while p:
                            username=input("Ingrese el nombre de usuario: ")
                            if any(u.get("usuario")==username for u in datos) or username == "":
                                print("¡Error! Ese nombre no es válido")
                                
                            else:
                                print("Excelente. Ese nombre de usuario se encuentra disponible.")
                                p = False

                                while m:
                                    contra=input("Ingrese una contraseña: ")
                                    if any(u.get("contrasena")== contra for u in datos) or contra == "":
                                        print("¡Error! Por seguridad, no se puede usar un contraseña ya registrada.")

                                    else:
                                        print("Excelente. Es una buena contraseña")
                                        break

                        new_registro={
                            "usuario":username,
                            "contrasena":contra
                        }
                        datos.append(new_registro)
                        with open("credenciales.json","w", encoding= "utf-8")as archivo:
                            json.dump(datos,archivo, indent=4, ensure_ascii=False)
                        print(f"¡Usuario {username} agregado exitosamente!")
                        print("="*30)
                    except Exception as e:
                        print(f"Ocurrio un error al guardar el usuario: {e}")

                case 4:
                    print("Saliendo del sistema. Se cerró sesión exitosamente")
                    print("="*30)
                    break
                case _:
                    print("Opción no válida. Intente de nuevo.")  
except FileNotFoundError:
    print("ERROR CRÍTICO: El archivo 'credenciales.json' no existe.")
except Exception as e:
    print(f"ERROR: {e}")