accesos = [
    {"ID": 1, "Nombre": "Gael", "Rol": "admin", "Estado": "activo"},
    {"ID": 2, "Nombre": "Luis", "Rol": "usuario", "Estado": "activo"},
    {"ID": 3, "Nombre": "Eva", "Rol": "invitado", "Estado": "bloqueado"}
]

agregar_ID = 4
contraseña_admin = "Di3g03VZ?"
while True:
    print('''
[1] Mostrar usuarios
[2] Agregar usuario
[3] Buscar y modificar usuario por ID
[4] Eliminar usuario
[5] Estadísticas de acceso
[6] Salir
''')
    opcion = int(input("Seleccione una opcion: "))

    # Mostrar usuarios
    if opcion == 1:
        for a in accesos:
            print(f'ID: {a["ID"]} | Nombre: {a["Nombre"]} | Rol: {a["Rol"]} | Estado: {a["Estado"]}')

    # Agregar usuario
    elif opcion == 2:
        agregarnombre = input("Introduzca el nombre del nuevo usuario: ")
        inexistente = True
        for a in accesos:
            if a["Nombre"] == agregarnombre:
                inexistente = False
                print("El usuario ya existe en la base de datos")
                
                
        if not inexistente:
            continue
        
        while True:
            print("Seleccione el rol: \n[1] invitado\n[2] usuario\n[3] admin ")
            op_rol = int(input("Seleccione un rol en el sistema para el nuevo usuario: "))
            if op_rol == 1:
                agregarrol = "invitado"
                break
            elif op_rol == 2:
                agregarrol = "usuario"
                break
            elif op_rol == 3:
                acceso = input("Ingrese la contraseña para continuar: ")
                if acceso == contraseña_admin:
                    agregarrol = "admin"
                    break
                else:
                    print("Contraseña incorrecta")
            else:
                print("La opción seleccionada no es valida, intente de nuevo")
        
        while True:
            print("Seleccione el estado: \n[1] activo\n[2] bloqueado")
            op_estado = int(input("Seleccione un estado de usuario: "))

            if op_estado == 1:
                agregar_estado = "activo"
                break
            elif op_estado == 2:
                agregar_estado = "bloqueado"
                break
            else:
                print("La opción seleccionada no existe, intentelo de nuevo")
        agregaracceso = {"ID": agregar_ID, "Nombre": agregarnombre, "Rol": agregarrol, "Estado": agregar_estado}
        accesos.append(agregaracceso)
        print("Usuario agregado correctamente")
        agregar_ID += 1
    
    #Buscar y modificar usuario por ID
    elif opcion == 3:
        busqueda = int(input("Ingrese la ID del usuario que desea buscar: "))
        encontrado = False
        for a in accesos:
            if a["ID"] == busqueda:
                encontrado = True
                while True:
                    print(f'ID: {a["ID"]} | Nombre: {a["Nombre"]} | Rol: {a["Rol"]} | Estado: {a["Estado"]}')
                    op_salida = input("Desea modificar algun valor? (si/no): ").lower()
                    if op_salida == "si":
                        print("Datos: \n[1] Nombre\n[2] Rol\n[3] Estado\n[4] Cancelar")
                        op_modificación = int(input("Seleccione una opción: "))
                        if op_modificación == 1:
                            while True:
                                modificar_nombre = input("Ingrese el nuevo nombre: ")
                                a["Nombre"] = modificar_nombre
                                break
                        elif op_modificación == 2:
                            while True:
                                print("Seleccione el rol: \n[1] invitado\n[2] usuario\n[3] admin ")
                                op_rol_mod = int(input("Seleccione el nuevo rol en el sistema para el usuario: "))
                                if op_rol_mod == 1:
                                    modificarrol = "invitado"
                                    break
                                elif op_rol_mod == 2:
                                    modificarrol = "usuario"
                                    break
                                elif op_rol_mod == 3:
                                    acceso_mod = input("Ingrese la contraseña para continuar: ")
                                    if acceso_mod == contraseña_admin:
                                        modificarrol = "admin"
                                        break
                                    else:
                                        print("Contraseña incorrecta")
                                else:
                                    print("La opción seleccionada no es valida, intente de nuevo")
                            a["Rol"] = modificarrol    
                        elif op_modificación == 3:
                            print("Seleccione el estado: \n[1] activo\n[2] bloqueado")
                            op_estado_mod = int(input("Seleccione un estado de usuario: "))

                            if op_estado_mod == 1:
                                modificarestado = "activo"
                                break
                            elif op_estado_mod == 2:
                                if a["Rol"] == "admin":
                                    acceso_mod = input("Ingrese la contraseña de administrador para continuar: ")
                                    if acceso_mod == contraseña_admin:
                                        modificarestado = "bloqueado"
                                        break
                                    else:
                                        print("contraseña incorrecta")
                                        break
                            else:
                                print("La opción seleccionada no existe, intentelo de nuevo")
                            a["Estado"] = modificarestado
                        else:
                            print("La opción seleccionada no es valida")
                    else:
                        break
    
    #Eliminar usuario
    elif opcion == 4:
        while True:
            eliminado = int(input("Ingrese el ID del usuario que desea eliminar: "))
            cancelar_eliminar = input("Cancelar? (si/no): ").lower()
            
            if cancelar_eliminar == "si":
                break

            id_encontrado = False
            eliminado_ok = False
            password_incorrecta = False

            for a in accesos:
                if eliminado == a["ID"]:
                    id_encontrado = True
                    if a["Rol"] == "admin":
                        eliminar_contraseña = input(
                            "Ingrese la contraseña para eliminar al administrador: "
                        )
                        if eliminar_contraseña == contraseña_admin:
                            accesos.remove(a)
                            eliminado_ok = True
                        else:
                            password_incorrecta = True
                    else:
                        accesos.remove(a)
                        eliminado_ok = True
                    break

            if not id_encontrado:
                print("El ID ingresado no existe")
            elif password_incorrecta:
                print("Contraseña incorrecta. No se eliminó el usuario.")
            elif eliminado_ok:
                print("El usuario fue eliminado correctamente")

            break
    elif opcion == 5:
        stats_activos = 0
        stats_bloqueados = 0
        stats_admins = 0

        print("Las estadisticas del sistema son:\n")
        for a in accesos:
            if a["Estado"] == "activo":
                stats_activos += 1
            if a["Estado"] == "bloqueado":
                stats_bloqueados += 1
            if a["Rol"] == "admin":
                stats_admins += 1
        print(f"El total de usuarios con un acceso abierto es de: {stats_activos}\nEl total de usuarios activos con un acceso bloqueado es de: {stats_bloqueados}\nEl total de administradores es de: {stats_admins}")

    else:
        break