import os

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")


def dibujar_menu_princial():
    print("SISTEMA DE VIAJES")
    print("[1] Comprar pasajes")
    print("[2] Mostrar ubicaciones disponibles")
    print("[3] ver listado de pasajeros")
    print("[7] salir")

def comparar_pasajes():
    clear()
    print("COMPRA DE PASAJES")
    cantidad = input("ingrese la cantidad de pasajes: ")

def mostrar_ubicaciones():
    clear()
    print("UBICACIONES")
    input("")

def ver_listado():
    clear()
    print("LISTADO DE PASAJEROS")
    input("")

def buscar_pasajero():
    clear()
    print("BÚSQUEDA DE PASAJEROS")
    input("")

def reasingar_asiento():
    clear()
    print("REASIGNACIÓN DE ASIENTOS")
    input("")

def mostrar_ganancias():
    clear()
    print("MOSTRAR GANANCIAS")
    input("")

def programa_principal():
    opcion = int(0)
    while opcion != 7:
        clear()
        dibujar_menu_princial()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            comparar_pasajes()
        elif opcion == "2":
            mostrar_ubicaciones()
        elif opcion == "3":
            ver_listado()
        elif opcion == "4":
            buscar_pasajero()
        elif opcion == "5":
            reasingar_asiento()
        elif opcion == "6":
            mostrar_ganancias()
        else:
            input("Opción inválida, presione cualquier tecla")

programa_principal()


