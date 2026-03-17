# -*- coding: utf-8 -*-

import sys

inicio = ("1234", "admin")  # valores predeterminados
opcion = ("si", " ")

proveedores = {}
clientes = {}
stock = {}
ventas = {}

id_venta = 0
codig = 0

print "\n\tInicio de sesion"
user = raw_input("\n\tUsuario: ")
clave = raw_input("\n\tContraseña: ")
corte = raw_input("\n\tIngresar [Si/No]: ").lower()

while corte in opcion:

    while user != inicio[1]:  # usuario incorrecto
        print "\n\tINCORRECTO"
        user = raw_input("\n\tUsuario: ")
        clave = raw_input("\n\tContraseña: ")
        corte = raw_input("\n\tIngresar [Si/No]: ").lower()

    while clave != inicio[0]:  # clave incorrecta
        print "\n\tINCORRECTO"
        user = raw_input("\n\tUsuario: ")
        clave = raw_input("\n\tContraseña: ")
        corte = raw_input("\n\tIngresar [Si/No]: ").lower()

    print "\n\tBIENVENIDO"

    while True:  # Menú principal
        print "\n\tOpciones"
        print "\n\t1 - Proveedores"
        print "\n\t2 - Clientes"
        print "\n\t3 - Stock"
        print "\n\t4 - Ventas"
        print "\n\t5 - Informes"
        print "\n\t6 - Salir"

        menu = raw_input("\nSeleccionar: ")

        if menu == "1":  # Proveedores

            while True:  # Menú proveedores
                print "\n\tOpciones Proveedores "
                print "\n\t1 - Registrar"
                print "\n\t2 - Eliminar"
                print "\n\t3 - Editar"
                print "\n\t4 - Lista de proveedores"
                print "\n\t5 - Volver atras"
                menu = raw_input("\nSeleccionar: ")

                while menu == "1" or menu in opcion:
                    print "\n\tRegistro de proveedores"
                    print "\nComplete los siguientes datos: "
                    proveedor = []
                    cuit_proveedor = raw_input("\nNúmero de CUIT: ")
                    if cuit_proveedor:
                        if cuit_proveedor not in proveedores:   #No sobrescribir
                            apellido = raw_input("\nAPELLIDO: ").upper()
                            nombre = raw_input("\nNOMBRE: ").capitalize()
                            razon_social = raw_input("\nRazón social: ").upper()
                            telefono = raw_input("\nTelefono: ")
                            email = raw_input("\nCorreo electronico: ")
                            proveedor = [apellido, nombre, razon_social, telefono, email]
                            proveedores[cuit_proveedor] = proveedor
                            print "\nRegistrado con exito."
                        else:
                            print "\nERROR: el CUIT ya fue registrado."
                    menu = raw_input("\nRegistrar otro proveedor [Si/No]: ").lower()

                while menu == "2" or menu in opcion:
                    print "\n\tEliminar del registro"
                    quitar = raw_input("\nBusqueda por CUIT: ")
                    if quitar:
                        if quitar in cuit_proveedor:
                            print "Proveedor: ", proveedores[quitar]
                            volver = raw_input("\n¿Seguro de que quiere eliminarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                del proveedores[quitar]
                                print "\nProveedor eliminado."
                        else:
                            print "\nCUIT no encontrado."
                    menu = raw_input("\nEliminar otro proveedor [Si/No]: ").lower()

                while menu == "3" or menu in opcion:
                    print "\n\tEditar datos"
                    buscar = raw_input("\nNúmero de CUIT: ")
                    if buscar:
                        if buscar in cuit_proveedor:
                            print "Datoas actuales del proveedor: ", proveedores[buscar]
                            volver = raw_input("\n¿Seguro de que quiere editarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                print "\nENTER para mantener datos actuales."
                                edit_apellido = raw_input("\nAPELLIDO: ").upper()
                                edit_nombre = raw_input("\nNOMBRE: ").capitalize()
                                edit_razon_social = raw_input("\nRazón social: ").upper()
                                edit_telefono = raw_input("\nTelefono: ")
                                edit_email = raw_input("\nCorreo electronico: ")
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
                                print "\nLos datos se guardaron con exito."
                        else:
                            print "\nCUIT no encontrado."
                    menu = raw_input("\nEditar otro proveedor [Si/No]: ").lower()

                if menu == "4":
                    print "\n\tLista de proveedores"
                    for cuit_proveedor, proveedor in proveedores.iteritems():
                        apellido, nombre, razon_social, telefono, email = proveedor
                        print "\nCUIT: ", cuit_proveedor, " |", apellido, ",", nombre, "| Razón social:", razon_social, "| Telefono:", telefono, "|", email

                    cant_prov = len(proveedores)
                    print "\nCantidad actual: ", cant_prov

                elif menu == "5":
                    print "\n\tVolver atras"
                    volver = raw_input("\n¿Esta seguro? [Si/No]: ").lower()
                    if volver in opcion:
                        break  # Sale del bucle del menú proveedores
                else:
                    print "\nOpcion fuera de rango. Intente de nuevo."

        elif menu == "2":  # Clientes

            while True:  # Menú clientes
                print "\n\tOpciones Clientes "
                print "\n\t1 - Registrar"
                print "\n\t2 - Eliminar"
                print "\n\t3 - Editar"
                print "\n\t4 - Lista de Clientes"
                print "\n\t5 - Volver atras"
                menu = raw_input("\nSeleccionar: ")

                while menu == "1" or menu in opcion:
                    print "\n\tRegistro de clientes"
                    print "\nComplete los siguientes datos: "
                    cliente = []
                    id_cliente = raw_input("\nNúmero de DNI: ")
                    if id_cliente:
                        if id_cliente not in clientes:   #No sobrescribir
                            apellido = raw_input("\nAPELLIDO: ").upper()
                            nombre = raw_input("\nNOMBRE: ").capitalize()
                            telefono = raw_input("\nTelefono: ")
                            email = raw_input("\nCorreo electronico: ")
                            direccion = raw_input("\nDirección: ")
                            localidad = raw_input("\nLocalidad: ")
                            partido = raw_input("\nPartido: ")
                            provincia = raw_input("\nProvincia: ")
                            cliente = [apellido, nombre, telefono, email, direccion, localidad, partido, provincia]
                            clientes[id_cliente] = cliente
                            print "\nRegistrado con exito."
                        else:
                            print "\nERROR: el DNI ya fue registrado."
                    menu = raw_input("\nRegistrar otro cliente [Si/No]: ").lower()

                while menu == "2" or menu in opcion:
                    print "\n\tEliminar del registro"
                    quitar = raw_input("\nBusqueda por DNI: ")
                    if quitar:
                        if quitar in id_cliente:
                            print "Cliente: ", clientes[quitar]
                            volver = raw_input("\n¿Seguro de que quiere eliminarlo? [Si/No]: ")
                            if volver.lower() in opcion:
                                del clientes[quitar]
                                print "\nCliente eliminado."
                        else:
                            print "\nDNI no encontrado."
                    menu = raw_input("\nEliminar otro cliente [Si/No]: ").lower()

                while menu == "3" or menu in opcion:
                    print "\n\tEditar datos"
                    buscar = raw_input("\nNúmero de DNI: ")
                    if buscar:
                        if buscar in id_cliente:
                            print "Datoas actuales del cliente: ", clientes[buscar]
                            volver = raw_input("\n¿Seguro de que quiere editarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                print "\nENTER para mantener datos actuales."
                                edit_apellido = raw_input("\nAPELLIDO: ").upper()
                                edit_nombre = raw_input("\nNOMBRE: ").capitalize()
                                edit_telefono = raw_input("\nTelefono: ")
                                edit_email = raw_input("\nCorreo electronico: ")
                                edit_direccion = raw_input("\nDirección: ")
                                edit_localidad = raw_input("\nLocalidad: ")
                                edit_partido = raw_input("\nPartido: ")
                                edit_provincia = raw_input("\nProvincia: ")
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
                                print "\nLos datos se guardaron con exito."
                        else:
                            print "\nDNI no encontrado."
                    menu = raw_input("\nEditar otro cliente [Si/No]: ").lower()

                if menu == "4":
                    print "\n\tLista de Clientes"
                    for id_cliente, cliente in clientes.iteritems():
                        apellido, nombre, telefono, email, direccion, localidad, partido, provincia = cliente
                        print "\nDNI: ", id_cliente, " |", apellido, ",", nombre, "| Telefono:", telefono, "|", email, "| Dirección:", direccion, ",", localidad, ",", partido, ",", provincia

                    cant_clte = len(clientes)
                    print "\nCantidad actual: ", cant_clte

                elif menu == "5":
                    print "\n\tVolver atras"
                    volver = raw_input("\n¿Esta seguro? [Si/No]: ").lower()
                    if volver in opcion:
                        break  # Sale del bucle del menú clientes
                else:
                    print "\nOpcion fuera de rango. Intente de nuevo."

        elif menu == "3":  # Stock

            while True:  # Menú stock
                print "\n\tOpciones Stock "
                print "\n\t1 - Registrar"
                print "\n\t2 - Reponer"
                print "\n\t3 - Eliminar"
                print "\n\t4 - Editar"
                print "\n\t5 - Stock de productos"
                print "\n\t6 - Volver atras"
                menu = raw_input("\nSeleccionar: ")

                while menu == "1" or menu in opcion:
                    print "\n\tRegistro de productos"
                    print "\nComplete los siguientes datos: "
                    producto = []
                    nom_producto = raw_input("\nNombre del producto: ").capitalize().strip()
                    detalle = raw_input("\nDetalle: ").lower()

                    if nom_producto and detalle:
                        if nom_producto in stock and detalle in stock:  #No sobrescribir
                            print "\nERROR: el producto ya fue registrado."
                        else:
                            categoria = raw_input("\nCategoria: ").upper().strip()
                            if categoria:
                                id_producto = nom_producto[:1] + '-' + categoria[:3] + '-' + str(codig + 1)
                                costo = raw_input("\nCosto: $")
                                precio = raw_input("\nPrecio: $")
                                cant_total = raw_input("\nCantidad inicial: ")

                                try:  #manejar excepciones
                                    costo = int(costo)
                                    precio = int(precio)
                                    cant_total = int(cant_total)
                                except ValueError:
                                    print "\nERROR: Por favor, ingrese valores numéricos válidos para el costo, el precio y la cantidad."
                                    continue  # Volver al inicio del bucle

                                cuit_proveedor = raw_input("\nNúmero de CUIT del proveedor: ")
                                if cuit_proveedor == False:
                                    cuit_proveedor = "No identificado"

                                producto = [nom_producto, categoria, detalle, costo, precio, cant_total, cuit_proveedor]
                                stock[id_producto] = producto
                                codig += 1
                                print "\nRegistrado con exito."
                    menu = raw_input("\nIngresar otro producto [Si/No]: ").lower()

                while menu == "2" or menu in opcion:
                    print "\n\tReposición de stock"
                    buscar = raw_input("\nClave interna del producto: ").upper()
                    if buscar:
                        if buscar in id_producto:
                            print "Producto: ", stock[buscar]
                            volver = raw_input("\n¿Reponer este producto? [Si/No]: ").lower()
                            if volver in opcion:
                                edit_cantidad = raw_input("\nCantidad a ingresar: ")

                                try:
                                    edit_cantidad = int(edit_cantidad)
                                except ValueError:
                                    print "\nERROR: Por favor, ingrese valores numéricos válidos para la cantidad a reponer."
                                    continue

                                if edit_cantidad:
                                    cant_total = stock[buscar][5]
                                    stock[buscar][5] = cant_total + edit_cantidad
                                    print "\nLos datos se guardaron con exito."
                        else:
                            print "\nProducto no encontrado."
                    menu = raw_input("\nReponer otro producto [Si/No]: ").lower()

                while menu == "3" or menu in opcion:
                    print "\n\tEliminar del stock"
                    quitar = raw_input("\nBusqueda por CLAVE: ").upper()
                    if quitar:
                        if quitar in id_producto:
                            print "Producto: ", stock[quitar]
                            volver = raw_input("\n¿Seguro de que quiere eliminarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                del stock[quitar]
                                print "\nProducto eliminado."
                        else:
                            print "\nClave no encontrada."
                    menu = raw_input("\nEliminar otro producto [Si/No]: ").lower()

                while menu == "4" or menu in opcion:
                    print "\n\tEditar datos"
                    buscar = raw_input("\nClave interna del producto: ").upper()
                    if buscar:
                        if buscar in id_producto:
                            print "Datoas actuales del producto: ", stock[buscar]
                            volver = raw_input("\n¿Seguro de que quiere editarlo? [Si/No]: ").lower()
                            if volver in opcion:
                                print "\nENTER para mantener datos actuales."
                                edit_nom_producto = raw_input("\nNombre del producto: ").capitalize()
                                edit_detalle = raw_input("\nDetalle: ").lower()
                                edit_categoria = raw_input("\nCategoria: ").upper()
                                edit_costo = raw_input("\nCosto: $")
                                edit_precio = raw_input("\nPrecio: $")
                                edit_cant_total = raw_input("\nCantidad inicial: ")
                                edit_cuit_proveedor = raw_input("\nNúmero de CUIT del proveedor: ")

                                try:
                                    if edit_costo:
                                        edit_costo = int(edit_costo)
                                    if edit_precio:
                                        edit_precio = int(edit_precio)
                                    if edit_cant_total:
                                        edit_cant_total = int(edit_cant_total)
                                except ValueError:
                                    print "\nERROR: Por favor, ingrese valores numéricos válidos para el costo, el precio y la cantidad."
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
                                print "\nLos datos se guardaron con exito."
                        else:
                            print "\nProducto no encontrado."
                    menu = raw_input("\nEditar otro producto [Si/No]: ").lower()

                if menu == "5":
                    print "\n\tLista de stock"
                    cant_prod = 0
                    for id_producto, producto in stock.iteritems():
                        nom_producto, categoria, detalle, costo, precio, cant_total, cuit_proveedor = producto
                        print "\nCLAVE interna: ", id_producto, " |", nom_producto, ",", detalle, "| Costo: $", costo, "| Precio: $", precio, "|", "Cantidad: ", cant_total, "Proveedor: ", cuit_proveedor
                        cant_prod += cant_total

                    var_prod = len(stock)
                    print "\nVariedad de productos actualmente: ", var_prod
                    print "\nCantidad total de stock: ", cant_prod

                elif menu == "6":
                    print "\n\tVolver atras"
                    volver = raw_input("\n¿Esta seguro? [Si/No]: ").lower()
                    if volver in opcion:
                        break  # Sale del bucle del menú stock

                else:
                    print "\nOpcion fuera de rango. Intente de nuevo."

        elif menu == "4":  # Ventas

            while True:  # Menú ventas
                print "\n\tOpciones Ventas "
                print "\n\t1 - Ingresar"
                print "\n\t2 - Editar"
                print "\n\t3 - Eliminar"
                print "\n\t4 - historial"
                print "\n\t5 - Volver atras"
                menu = raw_input("\nSeleccionar: ")

                while menu == "1" or menu in opcion:
                    print "\nComplete los siguientes datos: "
                    dia = raw_input("\nNúmero de día: ")
                    mes = raw_input("\nNúmero de mes: ")
                    anio = raw_input("\nNúmero de año: ")
                    try:
                        if dia <= 31 and dia >= 1 and dia:
                            dia = int(dia)
                        if mes <= 12 and mes >= 1 and mes:
                                mes = int(mes)
                        if anio < 2000 and anio >= 2100 and anio:
                            anio = int(anio)
                    except ValueError:
                        print "\nERROR: Por favor, ingrese valores numéricos válidos para día, mes  y año."
                        continue
                    fecha = [dia, mes, anio]

                    cod_cliente = raw_input("\nClave de cliente: ")
                    if cod_cliente:
                        if cod_cliente not in id_cliente:
                            print "\nERROR: Cliente no registrado."
                            continue

                        print "\nProductos disponibles para la venta:"
                        for id_producto, producto in stock.iteritems():
                            nom_producto, categoria, detalle, costo, precio, cant_total, cuit_proveedor = producto
                            cant_min = cant_total
                            if cant_min > 0:
                                print "\n[" + id_producto + "]-" + nom_producto + "- Detalle:" + detalle +"- Precio: $" + str(precio)

                        total_venta = 0
                        prod_vend = []
                        while True:
                            cod_producto = raw_input("\nCodigo del producto a vender: ").upper()
                            if cod_producto not in id_producto:
                                print "\nERROR: Producto no encontrado."
                                continue
                            elif cod_producto:
                                cantidad_vent = (raw_input("\nCantidad a vender: "))
                                try:
                                    if cantidad_vent:
                                        cantidad_vent = int(cantidad_vent)
                                        if cantidad_vent > cant_total:
                                            print "Cantidad de stock no disponible."
                                except ValueError:
                                    print "\nERROR: Por favor, ingrese valores numéricos válidos para la cantidad a vender"
                                    continue

                                nom_prod = stock[cod_producto][0]
                                precio_unit = stock[cod_producto][4]
                                total_venta = total_venta + (precio_unit * cantidad_vent)
                                prod_vend = [cod_producto, nom_prod, cantidad_vent, precio_unit]

                            menu = raw_input("\nagregar otro producto a la venta [Si/No]: ").lower()
                            if menu not in opcion:
                                break

                        while True:
                            forma_pago = raw_input("\nForma de pago (efectivo, debito, credito): ").capitalize()
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
                                print "Forma de pago no valida. intente de nuevo."

                        volver = raw_input("\n¿Registrar la venta? [Si/No]: ").lower()
                        if volver in opcion:
                            id_venta += 1
                            ventas[id_venta] = [fecha, cod_cliente, prod_vend, total_final, forma_pago]
                            print "\nVenta registrada con éxito."

                    menu = raw_input("\nIngresar otra venta [Si/No]: ").lower()
                while menu == "2" or menu in opcion:
                    print "\n\tEditar datos "

                    menu = raw_input("\nEditar otra venta [Si/No]: ").lower()

                while menu == "3" or menu in opcion:
                    print "\n\tEliminar venta"

                    menu = raw_input("\nEdliminar otra venta [Si/No]: ").lower()

                if menu == "5":
                    print "\n\tHistorial de ventas"

                elif menu == "6":
                    print "\n\tVolver atras"
                    volver = raw_input("\n¿Esta seguro? [Si/No]: ").lower()
                    if volver in opcion:
                        break  # Sale del bucle del menú ventas

                else:
                    print "\nOpcion fuera de rango. Intente de nuevo."

        elif menu == "5":  # Informes
            print "Informes"

        elif menu == "6":  # Salir
            volver = raw_input("\n¿Seguro de que quiere salir? [Si/No]: ").lower()
            if volver in opcion:
                print "\n\tSaliendo del programa..."
                sys.exit()  # Termina el programa

        else:
            print "\nOpcion fuera de rango. Intente de nuevo."





