import csv

#clientes = {id_cliente:[ nombre, dni, email, direccion]}
ARCHIVO = "clientes.csv"
clientes = {}
cliente = []
clave = 0


def cargar_datos():
    try:
        with open(ARCHIVO, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                clientes.append({"nombre": row["nombre"], "DNI": int(row["DNI"]), "email": row["email"], "direccion": row["direccion"]})
    except FileNotFoundError:
        pass


def guardar_datos():
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["nombre", "dni", "email", "direccion"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(clientes)


def crear_clientes():
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()
    for c in clientes:
        if c["nombre"] == nombre or c["email"] == email:
            print("\nNombre o email ya registrados.\n")
            return
    id_cliente = clave + 1
    dni = int(input("DNI: ").strip())
    direccion = input("Direccion: ").strip()
    cliente.append({"nombre": nombre, "dni": dni, "email": email, "direccion": direccion})
    clientes[id_cliente] = cliente
    guardar_datos()
    print("\nCliente guardado.")


def leer_clientes():
    if clientes:
        print("\nClientes:")
        for i, c in enumerate(clientes, start=1):
            print(f"{i}. {c['nombre']} - DNI {c['dni']}  - {c['email']} - {c['direccionl']}")
    else:
        print("\nNo hay clientes.")
    print()


def actualizar_clientes():
    buscar = input("Clave del cliente a actualizar: ").strip()
    for c in clientes:
        if c["buscar"] == id_cliente:
            nuevo_dni = input("Nueva DNI (Enter = igual): ").strip()
            nuevo_email = input("Nuevo email (Enter = igual): ").strip()
            nueva_direc = input("Nuevo email (Enter = igual): ").strip()
            c["direccion"] = nueva_direc
            if nuevo_email:
                for otro in clientes:
                    if otro["email"] == nuevo_email and otro != c:
                        print("Email ya en uso.\n")
                        return
                c["email"] = nuevo_email
            if nuevo_dni:
                c["dni"] = int(nuevo_dni)
            guardar_datos()
            print("\nCliente actualizado.\n")
            return
    print("\nCliente no encontrado.")


def eliminar_clientes():
    nombre = input("Cliente a eliminar: ").strip()
    for c in clientes:
        if c["nombre"] == nombre:
            clientes.remove(c)
            guardar_datos()
            print("\nCliente eliminado.")
            return
    print("\nCliente no encontrado.")


def menu():
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


menu()
