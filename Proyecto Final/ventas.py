import csv
from stock import stock, cargar_stock, guardar_stock

ARCHIVO = "ventas.csv"
ventas = {}

def cargar_ventas():
    try:
        with open(ARCHIVO, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                fecha = [int(row["dia"]), int(row["mes"]), int(row["anio"])]
                prod_vend = [row["nom_prod"], int(row["cantidad_vent"]), float(row["precio_unit"])]
                ventas[int(row["id_venta"])] = [
                    fecha,
                    row["cod_cliente"],
                    prod_vend,
                    float(row["total_final"]),
                    row["forma_pago"]
                ]
    except FileNotFoundError:
        pass

def guardar_ventas():
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["id_venta","dia","mes","anio","cod_cliente",
                  "nom_prod","cantidad_vent","precio_unit","total_final","forma_pago"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for id_venta, datos in ventas.items():
            fecha, cod_cliente, prod_vend, total_final, forma_pago = datos
            writer.writerow({
                "id_venta": id_venta,
                "dia": fecha[0],
                "mes": fecha[1],
                "anio": fecha[2],
                "cod_cliente": cod_cliente,
                "nom_prod": prod_vend[0],
                "cantidad_vent": prod_vend[1],
                "precio_unit": prod_vend[2],
                "total_final": total_final,
                "forma_pago": forma_pago
            })

def crear_venta():
    cargar_stock()  # asegura que stock esté cargado
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anio = int(input("Año: "))
    cod_cliente = input("Código cliente: ").strip()
    id_producto = int(input("ID del producto vendido: ").strip())

    if id_producto not in stock:
        print("\nProducto no encontrado en stock.\n")
        return

    nom_prod, categoria, detalle, costo, precio, cant_total, cuit_proveedor = stock[id_producto]

    cantidad = int(input("Cantidad: "))
    if cantidad > cant_total:
        print("\nNo hay suficiente stock disponible.\n")
        return

    # descontar stock
    stock[id_producto][5] -= cantidad
    guardar_stock()

    total_final = cantidad * precio
    forma_pago = input("Forma de pago (efectivo/debito/credito): ").strip().lower()

    id_venta = max(ventas.keys(), default=0) + 1
    fecha = [dia, mes, anio]
    prod_vend = [nom_prod, cantidad, precio]

    ventas[id_venta] = [fecha, cod_cliente, prod_vend, total_final, forma_pago]
    guardar_ventas()
    print("\nVenta registrada y stock actualizado.")

def leer_ventas():
    if ventas:
        print("\nVentas registradas:")
        for id_venta, datos in ventas.items():
            fecha, cod_cliente, prod_vend, total_final, forma_pago = datos
            print(f"{id_venta}. {fecha[0]}/{fecha[1]}/{fecha[2]} - Cliente {cod_cliente} - "
                  f"{prod_vend[0]} x{prod_vend[1]} (${prod_vend[2]} c/u) - "
                  f"Total: ${total_final} - Pago: {forma_pago}")
    else:
        print("\nNo hay ventas registradas.")

def menu_ventas():
    cargar_ventas()
    while True:
        print("=== MENÚ VENTAS ===")
        print("1. Crear  2. Leer  3. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1": crear_venta()
        elif opcion == "2": leer_ventas()
        elif opcion == "3": break
        else: print("\nOpción inválida.")

if __name__ == "__main__":
    menu_ventas()
