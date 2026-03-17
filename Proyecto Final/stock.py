import csv

ARCHIVO = "stock.csv"
stock = {}  # diccionario con listas

def cargar_stock():
    try:
        with open(ARCHIVO, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                stock[int(row["id_producto"])] = [
                    row["nom_producto"],
                    row["categoria"],
                    row["detalle"],
                    float(row["costo"]),
                    float(row["precio"]),
                    int(row["cant_total"]),
                    row["cuit_proveedor"]
                ]
    except FileNotFoundError:
        pass

def guardar_stock():
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["id_producto", "nom_producto", "categoria", "detalle", "costo", "precio", "cant_total", "cuit_proveedor"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for id_producto, datos in stock.items():
            writer.writerow({
                "id_producto": id_producto,
                "nom_producto": datos[0],
                "categoria": datos[1],
                "detalle": datos[2],
                "costo": datos[3],
                "precio": datos[4],
                "cant_total": datos[5],
                "cuit_proveedor": datos[6]
            })

def crear_producto():
    nom_producto = input("Nombre del producto: ").strip()
    categoria = input("Categoría (ej: gaseosa, jugo, agua): ").strip()
    detalle = input("Detalle: ").strip()
    costo = float(input("Costo: ").strip())
    precio = float(input("Precio: ").strip())
    cant_total = int(input("Cantidad total: ").strip())
    cuit_proveedor = input("CUIT del proveedor: ").strip()

    id_producto = max(stock.keys(), default=0) + 1
    stock[id_producto] = [nom_producto, categoria, detalle, costo, precio, cant_total, cuit_proveedor]
    guardar_stock()
    print("\nProducto guardado.")

def leer_productos():
    if stock:
        print("\nStock de bebidas:")
        for id_producto, datos in stock.items():
            print(f"{id_producto}. {datos[0]} ({datos[1]}) - {datos[2]} - Costo: {datos[3]} - Precio: {datos[4]} - Cantidad: {datos[5]} - Proveedor: {datos[6]}")
    else:
        print("\nNo hay productos en stock.")
    print()

def actualizar_producto():
    buscar = input("ID del producto a actualizar: ").strip()
    if not buscar.isdigit():
        print("\nID inválido.")
        return
    buscar = int(buscar)
    if buscar in stock:
        datos = stock[buscar]
        nuevo_nom = input("Nuevo nombre (Enter = igual): ").strip()
        nueva_cat = input("Nueva categoría (Enter = igual): ").strip()
        nuevo_det = input("Nuevo detalle (Enter = igual): ").strip()
        nuevo_costo = input("Nuevo costo (Enter = igual): ").strip()
        nuevo_precio = input("Nuevo precio (Enter = igual): ").strip()
        nueva_cant = input("Nueva cantidad (Enter = igual): ").strip()
        nuevo_cuit = input("Nuevo CUIT proveedor (Enter = igual): ").strip()

        if nuevo_nom: datos[0] = nuevo_nom
        if nueva_cat: datos[1] = nueva_cat
        if nuevo_det: datos[2] = nuevo_det
        if nuevo_costo: datos[3] = float(nuevo_costo)
        if nuevo_precio: datos[4] = float(nuevo_precio)
        if nueva_cant: datos[5] = int(nueva_cant)
        if nuevo_cuit: datos[6] = nuevo_cuit

        stock[buscar] = datos
        guardar_stock()
        print("\nProducto actualizado.\n")
    else:
        print("\nProducto no encontrado.")

def eliminar_producto():
    buscar = input("ID del producto a eliminar: ").strip()
    if not buscar.isdigit():
        print("\nID inválido.")
        return
    buscar = int(buscar)
    if buscar in stock:
        del stock[buscar]
        guardar_stock()
        print("\nProducto eliminado.")
    else:
        print("\nProducto no encontrado.")

def menu_stock():
    cargar_stock()
    while True:
        print("=== MENÚ STOCK DE BEBIDAS ===")
        print("1. Crear  2. Leer  3. Actualizar  4. Eliminar  5. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1": crear_producto()
        elif opcion == "2": leer_productos()
        elif opcion == "3": actualizar_producto()
        elif opcion == "4": eliminar_producto()
        elif opcion == "5": break
        else: print("\nOpción inválida.")

if __name__ == "__main__":
    menu_stock()
