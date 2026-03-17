import csv

ARCHIVO = "clientes.csv"
clientes = {}  # diccionario con listas


def cargar_datos():
    try:
        with open(ARCHIVO, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                clientes[int(row["id_cliente"])] = [
                    row["nombre"],
                    int(row["dni"]),
                    row["email"],
                    row["direccion"]
                ]
    except FileNotFoundError:
        pass


def guardar_datos():
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["id_cliente", "nombre", "dni", "email", "direccion"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for id_cliente, datos in clientes.items():
            writer.writerow({
                "id_cliente": id_cliente,
                "nombre": datos[0],
                "dni": datos[1],
                "email": datos[2],
                "direccion": datos[3]
            })


def crear_clientes():
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()
    for datos in clientes.values():
        if datos[0] == nombre or datos[2] == email:
            print("\nNombre o email ya registrados.\n")
            return
    id_cliente = max(clientes.keys(), default=0) + 1
    dni = int(input("DNI: ").strip())
    direccion = input("Direccion: ").strip()
    clientes[id_cliente] = [nombre, dni, email, direccion]
    guardar_datos()
    print("\nCliente guardado.")


def leer_clientes():
    if clientes:
        print("\nClientes:")
        for id_cliente, datos in clientes.items():
            print(f"{id_cliente}. {datos[0]} - DNI {datos[1]} - {datos[2]} - {datos[3]}")
    else:
        print("\nNo hay clientes.")
    print()


def actualizar_clientes():
    buscar = input("ID del cliente a actualizar: ").strip()
    if not buscar.isdigit():
        print("\nID inválido.")
        return
    buscar = int(buscar)
    if buscar in clientes:
        datos = clientes[buscar]
        nuevo_dni = input("Nueva DNI (Enter = igual): ").strip()
        nuevo_email = input("Nuevo email (Enter = igual): ").strip()
        nueva_direc = input("Nueva dirección (Enter = igual): ").strip()
        if nuevo_dni:
            datos[1] = int(nuevo_dni)
        if nuevo_email:
            for otro_id, otro in clientes.items():
                if otro[2] == nuevo_email and otro_id != buscar:
                    print("Email ya en uso.\n")
                    return
            datos[2] = nuevo_email
        if nueva_direc:
            datos[3] = nueva_direc
        clientes[buscar] = datos
        guardar_datos()
        print("\nCliente actualizado.\n")
    else:
        print("\nCliente no encontrado.")


def eliminar_clientes():
    buscar = input("ID del cliente a eliminar: ").strip()
    if not buscar.isdigit():
        print("\nID inválido.")
        return
    buscar = int(buscar)
    if buscar in clientes:
        del clientes[buscar]
        guardar_datos()
        print("\nCliente eliminado.")
    else:
        print("\nCliente no encontrado.")


def menu_clientes():
    cargar_datos()
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Crear  2. Leer  3. Actualizar  4. Eliminar  5. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1": crear_clientes()
        elif opcion == "2": leer_clientes()
        elif opcion == "3": actualizar_clientes()
        elif opcion == "4": eliminar_clientes()
        elif opcion == "5": break
        else: print("\nOpcion inválida.")

if __name__ == "__main__":
    menu_clientes()
