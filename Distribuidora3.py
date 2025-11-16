# -*- coding: utf-8 -*-

import sys

inicio = ("", "")  # valores predeterminados de ingreso
opcion = ("si", "")
# diccionarios, aca deberia traer un archivo con cositas para cargar 
proveedores = {#apellido, nombre, razon social, telefono ,email
    "1":["apellido", "nombre", "razon_social", "telefono", "email"] 
}
clientes = {#apellido, nombre, telefono, email, direccion, localidad, partido, provincia
    "1":["apellido", "nombre", "telefono", "email", "direccion", "localidad", "partido", "provincia"]
}
stock = {#nombre de producto, categoria, detalle, costo, precio, cantidad, cuit vendedor 
    "1":["nom_producto", "categoria", "detalle", 1, 1, 1, "cuit_proveedor"]
}
ventas = {#fecha,codigo_cliente, producto, total, forma de pago
    "1":[1, "cod_cliente", "prod_vend", "total_final", "forma_pago"]
}

id_venta = 1
codig = 0

print ("\n\tInicio de sesion")
user = input("\n\tUsuario: ")
clave = input("\n\tContraseña: ")
corte = input("\n\tIngresar [Si/No]: ").lower()

while corte in opcion:
    while user != inicio[1]:  # usuario incorrecto
        print ("\n\tINCORRECTO")
        user = input("\n\tUsuario: ")
        clave = input("\n\tContraseña: ")
        corte = input("\n\tIngresar [Si/No]: ").lower()
    while clave != inicio[0]:  # clave incorrecta
        print ("\n\tINCORRECTO")
        user = input("\n\tUsuario: ")
        clave = input("\n\tContraseña: ")
        corte = input("\n\tIngresar [Si/No]: ").lower()
    print ("\n\tBIENVENIDO")
    while True:  # Menú principal
        print ("\n\tOpciones")
        print ("\n\t1 - Proveedores")
        print ("\n\t2 - Clientes")
        print ("\n\t3 - Stock")
        print ("\n\t4 - Ventas")
        print ("\n\t5 - Salir")
        menu = input("\nSeleccionar: ")
        if menu == "1":  # Proveedores

            while True:  # Menú proveedores
                print ("\n\tOpciones Proveedores")
                print ("\n\t1 - Registrar")
                print ("\n\t2 - Eliminar")
                print ("\n\t3 - Editar")
                print ("\n\t4 - Lista de proveedores")
                print ("\n\t5 - Volver atras")
                menu = input("\nSeleccionar: ")

                while menu == "1" or menu in opcion:
                    print ("\n\tRegistro de proveedores")
                    print ("\nComplete los siguientes datos: ")
                    proveedor = []
                    cuit_proveedor = input("\nNúmero de CUIT: ")
                    if cuit_proveedor:
                        if cuit_proveedor not in proveedores:
                            apellido = input("\nAPELLIDO: ").upper()
                            nombre = input("\nNOMBRE: ").capitalize()
                            razon_social = input("\nRazón social: ").upper()
                            telefono = input("\nTelefono: ")
                            email = input("\nCorreo electronico: ")
                            proveedor = [apellido, nombre, razon_social, telefono, email]
                            proveedores[cuit_proveedor] = proveedor
                            print ("\nRegistrado con exito.")
                        else:
                            print ("\nERROR: el CUIT ya fue registrado.")
                    menu = input("\nRegistrar otro proveedor [Si/No]: ").lower()

                while menu == "2" or menu in opcion:
                    print ("\n\tEliminar del registro")
                    quitar = input("\nBusqueda por CUIT: ")
                    if quitar:
                        if quitar in cuit_proveedor:
                            print (f"Proveedor: {proveedores[quitar]}")
                            volver = input("\n¿Seguro de que quiere eliminarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                del proveedores[quitar]
                                print ("\nProveedor eliminado.")
                        else:
                            print ("\nCUIT no encontrado.")
                    menu = input("\nEliminar otro proveedor [Si/No]: ").lower()

                while menu == "3" or menu in opcion:
                    print ("\n\tEditar datos")
                    buscar = input("\nNúmero de CUIT: ")
                    if buscar:
                        if buscar in cuit_proveedor:
                            print (f"Datos actuales del proveedor: {proveedores[buscar]}")
                            volver = input("\n¿Seguro de que quiere editarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                print ("\nENTER para mantener datos actuales.")
                                edit_apellido = input("\nAPELLIDO: ").upper()
                                edit_nombre = input("\nNOMBRE: ").capitalize()
                                edit_razon_social = input("\nRazón social: ").upper()
                                edit_telefono = input("\nTelefono: ")
                                edit_email = input("\nCorreo electronico: ")
                                if edit_apellido:
                                    proveedores[buscar][0] = edit_apellido
                                if edit_nombre:
                                    proveedores[buscar][1] = edit_nombre
                                if edit_razon_social:
                                    proveedores[buscar][2] = edit_razon_social
                                if edit_telefono:
                                    proveedores[buscar][3] = edit_telefono
                                if edit_email:
                                    proveedores[buscar][4] = edit_email
                                print ("\nLos datos se guardaron con exito.")
                        else:
                            print ("\nCUIT no encontrado.")
                    menu = input("\nEditar otro proveedor [Si/No]: ").lower()

                if menu == "4":
                    print ("\n\tLista de proveedores")
                    for cuit_proveedor, proveedor in proveedores.items():
                        apellido, nombre, razon_social, telefono, email = proveedor
                        print (f"\nCUIT: {cuit_proveedor} | Apellido: {apellido} | Nombre: {nombre} | Razón social: {razon_social} | Telefono: {telefono} | Email: {email}")

                    cant_prov = len(proveedores)
                    print (f"\nCantidad actual: {cant_prov}")

                elif menu == "5":
                    print ("\n\tVolver atras")
                    volver = input("\n¿Esta seguro? [Si/No]: ").lower()
                    if volver in opcion:
                        break  # Sale del bucle del menú proveedores
                else:

                    print ("\nOpcion fuera de rango. Intente de nuevo.")
        elif menu == "2":  # Clientes

            while True:  # Menú clientes
                print ("\n\tOpciones Clientes ")
                print ("\n\t1 - Registrar")
                print ("\n\t2 - Eliminar")
                print ("\n\t3 - Editar")
                print ("\n\t4 - Lista de Clientes")
                print ("\n\t5 - Volver atras")
                menu = input("\nSeleccionar: ")

                while menu == "1" or menu in opcion:
                    print ("\n\tRegistro de clientes")
                    print ("\nComplete los siguientes datos: ")
                    cliente = []
                    id_cliente = input("\nNúmero de DNI: ")
                    if id_cliente:
                        if id_cliente not in clientes:   #No sobrescribir
                            apellido = input("\nAPELLIDO: ").upper()
                            nombre = input("\nNOMBRE: ").capitalize()
                            telefono = input("\nTelefono: ")
                            email = input("\nCorreo electronico: ")
                            direccion = input("\nDirección: ")
                            localidad = input("\nLocalidad: ")
                            partido = input("\nPartido: ")
                            provincia = input("\nProvincia: ")
                            cliente = [apellido, nombre, telefono, email, direccion, localidad, partido, provincia]
                            clientes[id_cliente] = cliente
                            print ("\nRegistrado con exito.")
                        else:
                            print ("\nERROR: el DNI ya fue registrado.")
                    menu = input("\nRegistrar otro cliente [Si/No]: ").lower()

                while menu == "2" or menu in opcion:
                    print ("\n\tEliminar del registro")
                    quitar = input("\nBusqueda por DNI: ")
                    if quitar:
                        if quitar in id_cliente:
                            print (f"Cliente: {clientes[quitar]}")
                            volver = input("\n¿Seguro de que quiere eliminarlo? [Si/No]: ")
                            if volver.lower() in opcion:
                                del clientes[quitar]
                                print ("\nCliente eliminado.")
                        else:
                            print ("\nDNI no encontrado.")
                    menu = input("\nEliminar otro cliente [Si/No]: ").lower()

                while menu == "3" or menu in opcion:
                    print ("\n\tEditar datos")
                    buscar = input("\nNúmero de DNI: ")
                    if buscar:
                        if buscar in clientes:
                            print (f"Datos actuales del cliente: {clientes[buscar]}")
                            volver = input("\n¿Seguro de que quiere editarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                print ("\nENTER para mantener datos actuales.")
                                edit_apellido = input("\nAPELLIDO: ").upper()
                                edit_nombre = input("\nNOMBRE: ").capitalize()
                                edit_telefono = input("\nTelefono: ")
                                edit_email = input("\nCorreo electronico: ")
                                edit_direccion = input("\nDirección: ")
                                edit_localidad = input("\nLocalidad: ")
                                edit_partido = input("\nPartido: ")
                                edit_provincia = input("\nProvincia: ")
                                if edit_apellido:
                                    clientes[buscar][0] = edit_apellido
                                if edit_nombre:
                                    clientes[buscar][1] = edit_nombre
                                if edit_telefono:
                                    clientes[buscar][2] = edit_telefono
                                if edit_email:
                                    clientes[buscar][3] = edit_email
                                if edit_direccion:
                                    clientes[buscar][4] = edit_direccion
                                if edit_localidad:
                                    clientes[buscar][5] = edit_localidad
                                if edit_partido:
                                    clientes[buscar][6] = edit_partido
                                if edit_provincia:
                                    clientes[buscar][7] = edit_provincia
                                print ("\nLos datos se guardaron con exito.")
                        else:
                            print ("\nDNI no encontrado.")
                    menu = input("\nEditar otro cliente [Si/No]: ").lower()

                if menu == "4":
                    print ("\n\tLista de Clientes")
                    for id_cliente, cliente in clientes.items():
                        apellido, nombre, telefono, email, direccion, localidad, partido, provincia = cliente
                        print (f"\nDNI: {id_cliente} | {apellido} , {nombre} | Telefono: {telefono} | {email} | Dirección:  {direccion}, {localidad}, {partido}, {provincia}")

                    cant_clte = len(clientes)
                    print (f"\nCantidad actual: ", cant_clte)

                elif menu == "5":
                    print ("\n\tVolver atras")
                    volver = input("\n¿Esta seguro? [Si/No]: ").lower()
                    if volver in opcion:
                        break  # Sale del bucle del menú clientes
                else:
                    print ("\nOpcion fuera de rango. Intente de nuevo.")
        elif menu == "3":  # Stock

            while True:  # Menú stock
                print ("\n\tOpciones Stock ")
                print ("\n\t1 - Registrar")
                print ("\n\t2 - Reponer")
                print ("\n\t3 - Eliminar")
                print ("\n\t4 - Editar")
                print ("\n\t5 - Stock de productos")
                print ("\n\t6 - Volver atras")
                menu = input("\nSeleccionar: ")

                while menu == "1" or menu in opcion:
                    print ("\n\tRegistro de productos")
                    print ("\nComplete los siguientes datos: ")
                    producto = []
                    nom_producto = input("\nNombre del producto: ").capitalize().strip()
                    detalle = input("\nDetalle: ").lower()

                    if nom_producto and detalle:
                        if nom_producto in stock and detalle in stock:
                            print ("\nERROR: el producto ya fue registrado.")
                        else:
                            categoria = input("\nCategoria: ").upper().strip()
                            if categoria:
                                id_producto = nom_producto[:1] + '-' + categoria[:3] + '-' + str(codig + 1)
                                costo = input("\nCosto: $")
                                precio = input("\nPrecio: $")
                                cant_total = input("\nCantidad inicial: ")

                                try:
                                    costo = int(costo)
                                    precio = int(precio)
                                    cant_total = int(cant_total)
                                except ValueError:
                                    print ("\nERROR: Por favor, ingrese valores numéricos válidos para el costo, el precio y la cantidad.")
                                    continue

                                cuit_proveedor = input("\nNúmero de CUIT del proveedor: ")
                                if cuit_proveedor == False:
                                    cuit_proveedor = "No identificado"

                                producto = [nom_producto, categoria, detalle, costo, precio, cant_total, cuit_proveedor]
                                stock[id_producto] = producto
                                codig += 1
                                print ("\nRegistrado con exito.")
                    menu = input("\nIngresar otro producto [Si/No]: ").lower()

                while menu == "2" or menu in opcion:
                    print ("\n\tReposición de stock")
                    buscar = input("\nClave interna del producto: ").upper()
                    if buscar:
                        if buscar in stock:
                            print (f"Producto: {stock[buscar]}")
                            volver = input("\n¿Reponer este producto? [Si/No]: ").lower()
                            if volver in opcion:
                                edit_cantidad = input("\nCantidad a ingresar: ")

                                try:
                                    edit_cantidad = int(edit_cantidad)
                                except ValueError:
                                    print ("\nERROR: Por favor, ingrese valores numéricos válidos para la cantidad a reponer.")
                                    continue

                                if edit_cantidad:
                                    cant_total = stock[buscar][5]
                                    stock[buscar][5] = cant_total + edit_cantidad
                                    print ("\nLos datos se guardaron con exito.")
                        else:
                            print ("\nProducto no encontrado.")
                    menu = input("\nReponer otro producto [Si/No]: ").lower()

                while menu == "3" or menu in opcion:
                    print ("\n\tEliminar del stock")
                    quitar = input("\nBusqueda por CLAVE: ").upper()
                    if quitar:
                        if quitar in id_producto:
                            print (f"Producto: {stock[quitar]}")
                            volver = input("\n¿Seguro de que quiere eliminarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                del stock[quitar]
                                print ("\nProducto eliminado.")
                        else:
                            print ("\nClave no encontrada.")
                    menu = input("\nEliminar otro producto [Si/No]: ").lower()

                while menu == "4" or menu in opcion:
                    print ("\n\tEditar datos")
                    buscar = input("\nClave interna del producto: ").upper()
                    if buscar:
                        if buscar in id_producto:
                            print (f"Datoas actuales del producto: ", stock[buscar])
                            volver = input("\n¿Seguro de que quiere editarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                print ("\nENTER para mantener datos actuales.")
                                edit_nom_producto = input("\nNombre del producto: ").capitalize()
                                edit_detalle = input("\nDetalle: ").lower()
                                edit_categoria = input("\nCategoria: ").upper()
                                edit_costo = input("\nCosto: $")
                                edit_precio = input("\nPrecio: $")
                                edit_cant_total = input("\nCantidad inicial: ")
                                edit_cuit_proveedor = input("\nNúmero de CUIT del proveedor: ")

                                try:
                                    if edit_costo:
                                        edit_costo = int(edit_costo)
                                    if edit_precio:
                                        edit_precio = int(edit_precio)
                                    if edit_cant_total:
                                        edit_cant_total = int(edit_cant_total)
                                except ValueError:
                                    print ("\nERROR: Por favor, ingrese valores numéricos válidos para el costo, el precio y la cantidad.")
                                    continue

                                if edit_nom_producto:
                                    stock[buscar][0] = edit_nom_producto
                                if edit_categoria:
                                    stock[buscar][1] = edit_categoria
                                if edit_detalle:
                                    stock[buscar][2] = edit_detalle
                                if edit_costo:
                                    stock[buscar][3] = edit_costo
                                if edit_precio:
                                    stock[buscar][4] = edit_precio
                                if edit_cant_total:
                                    stock[buscar][5] = edit_cant_total
                                if edit_cuit_proveedor:
                                    stock[buscar][6] = edit_cuit_proveedor
                                print ("\nLos datos se guardaron con exito.")
                        else:
                            print ("\nProducto no encontrado.")
                    menu = input("\nEditar otro producto [Si/No]: ").lower()

                if menu == "5":
                    print ("\n\tLista de stock")
                    cant_prod = 0
                    for id_producto, producto in stock.items():
                        nom_producto, detalle, costo, precio, cant_total, cuit_proveedor = producto
                        print(f"\nCLAVE interna: {id_producto} | {nom_producto}, {detalle} | Costo: ${costo} | Precio: ${precio} | Cantidad: {cant_total} | Proveedor: {cuit_proveedor}")

                    var_prod = len(stock)
                    print (f"\nVariedad de productos actualmente: {var_prod}")

                elif menu == "6":
                    print ("\n\tVolver atras")
                    volver = input("\n¿Esta seguro? [Si/No]: ").lower()
                    if volver in opcion:
                        break  # Sale del bucle del menú stock

                else:
                    print ("\nOpcion fuera de rango. Intente de nuevo.")
        elif menu == "4":  # Ventas
            while True:  # Menú ventas
                print ("\n\tOpciones Ventas ")
                print ("\n\t1 - Ingresar")
                print ("\n\t2 - Editar")
                print ("\n\t3 - Eliminar")
                print ("\n\t4 - historial")
                print ("\n\t5 - Volver atras")
                menu = input("\nSeleccionar: ")
                while menu == "1" or menu in opcion:
                    print ("\nComplete los siguientes datos: ")
                    dia = input("\nNúmero de día: ")
                    dia = int(dia)
                    mes = input("\nNúmero de mes: ")
                    mes = int(mes)
                    anio = input("\nNúmero de año: ")
                    anio = int(anio)
                    try:
                        if dia <= 31 and dia >= 1 and dia:
                            dia = int(dia)
                        if mes <= 12 and mes >= 1 and mes:
                                mes = int(mes)
                        if anio < 2000 and anio >= 2100 and anio:
                            anio = int(anio)
                    except ValueError:
                        print ("\nERROR: Por favor, ingrese valores numéricos válidos para día, mes  y año.")
                        continue
                    fecha = [dia, mes, anio]

                    cod_cliente = input("\nid del cliente: ")
                    if cod_cliente:
                        if cod_cliente not in clientes:
                            print ("\nERROR: Cliente no registrado.")
                            continue

                        print ("\nProductos disponibles para la venta:")
                        for id_producto, producto in stock.items():
                            nom_producto, categoria, detalle, costo, precio, cant_total, cuit_proveedor = producto
                            cant_min = cant_total
                            if cant_min > 0:
                                print (f"\n id: {id_producto} - nombre: {nom_producto} - Detalle:  {detalle} - Precio: $ {precio}")

                        total_venta = 0
                        prod_vend = []
                        while True:
                            cod_producto = input("\nCodigo del producto a vender: ").upper()
                            if cod_producto not in id_producto:
                                print ("\nERROR: Producto no encontrado.")
                                continue
                            elif cod_producto:
                                cantidad_vent = (input("\nCantidad a vender: "))
                                try:
                                    if cantidad_vent:
                                        cantidad_vent = int(cantidad_vent)
                                        if cantidad_vent > cant_total:
                                            print ("Cantidad de stock no disponible.")
                                except ValueError:
                                    print ("\nERROR: Por favor, ingrese valores numéricos válidos para la cantidad a vender")
                                    continue

                                nom_prod = stock[cod_producto][0]
                                precio_unit = stock[cod_producto][4]
                                total_venta = total_venta + (precio_unit * cantidad_vent)
                                prod_vend = [cod_producto, nom_prod, cantidad_vent, precio_unit]

                            menu = input("\nagregar otro producto a la venta [Si/No]: ").lower()
                            if menu not in opcion:
                                break

                        while True:
                            forma_pago = input("\nForma de pago (efectivo, debito, credito): ").capitalize()
                            descuento = 0
                            recargo = 0
                            if forma_pago:
                                if forma_pago == "Efecivo":
                                    descuento = (total_venta * 10) / 100
                                elif forma_pago == "Debito":
                                    descuento = (total_venta * 5) / 100
                                elif forma_pago == "Credito":
                                    recargo = (total_venta * 10) / 100

                                total_final = ((total_venta - descuento) + recargo)
                                break
                            else:
                                print ("Forma de pago no valida. intente de nuevo.")

                        volver = input("\n¿Registrar la venta? [Si/No]: ").lower()
                        if volver in opcion:
                            id_venta += 1
                            ventas[id_venta] = [fecha, cod_cliente, prod_vend, total_final, forma_pago]
                            print ("\nVenta registrada con éxito.")

                    menu = input("\nIngresar otra venta [Si/No]: ").lower()
                while menu == "2" or menu in opcion:
                    print ("\n\tEditar datos ")
                    buscar = input("\nid de venta: ")
                    if buscar:
                        if buscar in ventas:#codigo cliente, producto, total, forma de pago
                            print (f"Datos de la venta : {ventas[buscar]}")
                            volver = input("\n¿Seguro de que quiere editarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                print ("\nENTER para mantener datos actuales.")
                                edit_cod_cliente = input("\nId cliente: ").capitalize()
                                edit_producto = input("\nProducto: ")
                                edit_total = input("\nTotal: ")
                                edit_forma_pago = input("\nDirección: ")
                                if edit_cod_cliente:
                                    ventas[buscar][1] = edit_cod_cliente
                                if edit_producto:
                                    ventas[buscar][2] = edit_producto
                                if edit_total:
                                    ventas[buscar][3] = edit_total
                                if edit_producto:
                                    ventas[buscar][4] = edit_forma_pago
                                print ("\nLos datos se guardaron con exito.")
                        else:
                            print ("\nDNI no encontrado.")
                    menu = input("\nEditar otra venta [Si/No]: ").lower()
                while menu == "3" or menu in opcion:
                    print ("\n\tBorrar datos")
                    quitar = input("\nBusqueda por DNI: ")
                    if quitar:
                        if quitar in ventas:
                            print (f"id Venta: {ventas[quitar]}")
                            volver = input("\n¿Seguro de que quiere eliminar la venta? [Si/No]: ")
                            if volver.lower() in opcion:
                                del ventas[quitar]
                                print ("\nVenta eliminado.")
                        else:
                            print ("\nid no encontrado.")
                    menu = input("\nEliminar otra venta [Si/No]: ").lower()
                if menu == "4":               
                    print ("\n\tHistorial de ventas")  #ventas[id_venta] = [fecha, cod_cliente, [prod_vend = [cod_producto, nom_prod, cantidad_vent, precio_unit]], total_final, forma_pago]
                    for id_venta, venta in ventas.items():
                        fecha, cod_cliente, prod_vend, total_final, forma_pago = venta
                        print (f"Codigo del cliente: {cod_cliente} | id producto: {prod_vend[0]} | Producto: {prod_vend[1]} | Cantidad: {prod_vend[2]} | Precio final: {total_final} | Forma de pago: {forma_pago}")
                elif menu == "5":
                    print ("\n\tVolver atras")
                    volver = input("\n¿Esta seguro? [Si/No]: ").lower()
                    if volver in opcion:
                        break  # Sale del bucle del menú ventas

                else:
                    print ("\nOpcion fuera de rango. Intente de nuevo.")
        elif menu == "5":  # Salir
            volver = input("\n¿Seguro de que quiere salir? [Si/No]: ").lower()
            if volver in opcion:
                print ("\n\tSaliendo del programa...")
                sys.exit()  # Termina el programa
        else:
            print ("\nOpcion fuera de rango. Intente de nuevo.")





