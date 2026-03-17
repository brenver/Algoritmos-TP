

#inicio

from proveedores import menu_proveedores
from clientes import menu_clientes
from stock import menu_stock
from ventas import menu_ventas

# predeterminadas
inicio = ("1234", "admin")  # clave, usuario
opcion = ("si", " ")

print("\n\tInicio de sesión")
user = input("\n\tUsuario: ")
clave = input("\n\tContraseña: ")
corte = input("\n\tIngresar [Si/No]: ").lower()

while corte in opcion:
    while user != inicio[1]:  # usuario incorrecto
        print("\n\tINCORRECTO")
        user = input("\n\tUsuario: ")
        clave = input("\n\tContraseña: ")
        corte = input("\n\tIngresar [Si/No]: ").lower()
    while clave != inicio[0]:  # clave incorrecta
        print("\n\tINCORRECTO")
        user = input("\n\tUsuario: ")
        clave = input("\n\tContraseña: ")
        corte = input("\n\tIngresar [Si/No]: ").lower()

    print("\n\tBIENVENIDO")

    while True:  # Menú principal
        print("\n\t=== MENÚ PRINCIPAL ===")
        print("\t1 - Proveedores")
        print("\t2 - Clientes")
        print("\t3 - Stock")
        print("\t4 - Ventas")
        print("\t5 - Salir")
        menu = input("\nSeleccionar: ")

        if menu == "1":
            menu_proveedores()
        elif menu == "2":
            menu_clientes()
        elif menu == "3":
            menu_stock()
        elif menu == "4":
            menu_ventas()
        elif menu == "5":
            print("\n\tSesión finalizada.")
            break
        else:
            print("\n\tOpción inválida.")
