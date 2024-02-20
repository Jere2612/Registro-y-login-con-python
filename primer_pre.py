# Practicar el concepto de funciones. Preparar la parte logica para el registro de usuarios.

# Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales 

# El proyecto debe compartirse utilizando Colab bajo el nombre "Primera pre-Entrega+Apellido".

# Creo un diccionario con porlomenos 3 elementos y luego a la hora de registrar agrego elemento y valido con while.

usuarios = {"Jeremias":"123456","Maximo":"261215"}
nombre_usuario_agregado = input("Ingrese nuevo nombre de usuario que desea registrar: ")
contraseña_usuario_agregado = input("Ingrese contraseña para su nombre de usuario ingresado: ")

def agregar_registro(nombre:str,contraseña:str,diccionario:dict):
    diccionario[nombre] = contraseña
    return diccionario

def mostrar_info(diccionario:dict):
    print("Esta es la lista de todos los usuarios registrados: ")
    for clave, valor in diccionario.items():
        print(f"Nombre de usuario: {clave}  Contraseña: {valor}")

def ingreso_sistema(entrada_nombre: str, entrada_contraseña: str, diccionario: dict):
    intentos = 0
    respuesta = "si"
    
    while respuesta.lower() == "si" and intentos < 3:
        entrada_nombre = input("Ingrese su nombre de usuario: ")
        entrada_contraseña = input("Contraseña: ")

        if entrada_nombre in diccionario and entrada_contraseña == diccionario[entrada_nombre]:
            print(f"Bienvenido/a {entrada_nombre}!")
            break
        elif entrada_nombre in diccionario and entrada_contraseña != diccionario[entrada_nombre]:
            if intentos == 0:
                respuesta = input("Usuario o contraseña incorrectas. Le quedan 2 intentos, ¿Desea volver a intentarlo? (si/no): ")
            elif intentos == 1:
                respuesta = input("Usuario o contraseña incorrectas. Le quedan 1 intentos, ¿Desea volver a intentarlo? (si/no): ")
            intentos +=1
        else:
            if intentos == 0:
                respuesta = input("Usuario o contraseña incorrectas. Le quedan 2 intentos, ¿Desea volver a intentarlo? (si/no): ")
            elif intentos == 1:
                respuesta = input("Usuario o contraseña incorrectas. Le quedan 1 intentos, ¿Desea volver a intentarlo? (si/no): ")
            intentos += 1

    if intentos == 3 or respuesta == "no":
        print("Gracias por usar nuestro registro.")

agregar_registro(nombre_usuario_agregado,contraseña_usuario_agregado,usuarios)
mostrar_info(usuarios)
ingreso_sistema("nombre", "contraseña", usuarios)