import csv

ARCHIVO = "proveedores.csv"
proveedores = {}  # diccionario con listas


def cargar_datos():
    try:
        with open(ARCHIVO, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                proveedores[row["cuit_proveedor"]] = [
                    row["apellido"],
                    row["nombre"],
                    row["razon_social"],
                    row["tipo_prov"],
                    row["email"]
                ]
    except FileNotFoundError:
        pass


def guardar_datos():
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["cuit_proveedor", "apellido", "nombre", "razon_social", "tipo_prov", "email"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for cuit, datos in proveedores.items():
            writer.writerow({
                "cuit_proveedor": cuit,
                "apellido": datos[0],
                "nombre": datos[1],
                "razon_social": datos[2],
                "tipo_prov": datos[3],
                "email": datos[4]
            })


def crear_proveedor():
    cuit = input("CUIT: ").strip()
    if cuit in proveedores:
        print("\nCUIT ya registrado.\n")
        return
    apellido = input("Apellido: ").strip()
    nombre = input("Nombre: ").strip()
    razon_social = input("Razón social: ").strip()
    tipo_prov = input("Tipo de proveedor: ").strip()
    email = input("Email: ").strip()
    for datos in proveedores.values():
        if datos[4] == email:
            print("\nEmail ya registrado.\n")
            return
    proveedores[cuit] = [apellido, nombre, razon_social, tipo_prov, email]
    guardar_datos()
    print("\nProveedor guardado.")


def leer_proveedores():
    if proveedores:
        print("\nProveedores:")
        for cuit, datos in proveedores.items():
            print(f"{cuit} - {datos[0]}, {datos[1]} - {datos[2]} - {datos[3]} - {datos[4]}")
    else:
        print("\nNo hay proveedores.")
    print()


def actualizar_proveedor():
    cuit = input("CUIT del proveedor a actualizar: ").strip()
    if cuit in proveedores:
        datos = proveedores[cuit]
        nuevo_apellido = input("Nuevo apellido (Enter = igual): ").strip()
        nuevo_nombre = input("Nuevo nombre (Enter = igual): ").strip()
        nueva_razon = input("Nueva razón social (Enter = igual): ").strip()
        nuevo_tipo = input("Nuevo tipo proveedor (Enter = igual): ").strip()
        nuevo_email = input("Nuevo email (Enter = igual): ").strip()

        if nuevo_apellido: datos[0] = nuevo_apellido
        if nuevo_nombre: datos[1] = nuevo_nombre
        if nueva_razon: datos[2] = nueva_razon
        if nuevo_tipo: datos[3] = nuevo_tipo
        if nuevo_email:
            for otro_cuit, otro in proveedores.items():
                if otro[4] == nuevo_email and otro_cuit != cuit:
                    print("Email ya en uso.\n")
                    return
            datos[4] = nuevo_email

        proveedores[cuit] = datos
        guardar_datos()
        print("\nProveedor actualizado.\n")
    else:
        print("\nProveedor no encontrado.")


def eliminar_proveedor():
    cuit = input("CUIT del proveedor a eliminar: ").strip()
    if cuit in proveedores:
        del proveedores[cuit]
        guardar_datos()
        print("\nProveedor eliminado.")
    else:
        print("\nProveedor no encontrado.")


def menu_proveedores():
    cargar_datos()
    while True:
        print("=== MENÚ PROVEEDORES ===")
        print("1. Crear  2. Leer  3. Actualizar  4. Eliminar  5. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1": crear_proveedor()
        elif opcion == "2": leer_proveedores()
        elif opcion == "3": actualizar_proveedor()
        elif opcion == "4": eliminar_proveedor()
        elif opcion == "5": break
        else: print("\nOpción inválida.")

if __name__ == "__main__":
    menu_proveedores()