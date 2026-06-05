import json
try:
    with open("credenciales.json", "r") as archivo:
        credencial = {archivo}
        print("INICIANDO SESIÓN")
        autentificacion = input("Por favor, ingrese su usuario: ")
        if autentificacion in credencial.keys():
            print("EXCELENTE, USUARIO CORRECTO")
            contrasena = input("Por favor, Ingrese su contraseña: ")
            if contrasena in credencial:
                print("CONTRASEÑA CORRECTA")
                print("BIENVENIDO AL SISTEMA")
                print("1. Agregar un producto")
                print("2. Cargar inventario ya existente")
                opcion = int(input("Ingrese una opción (1-2): "))
                match opcion:
                    case 1:
                        
            else:
                print("CONTRASEÑA INCORRECTA")

        else:
            print(f"ERROR: {credencial} no está en la lista de usuarios")
except Exception as e:
    print("ERROR: {e}")