#  Proyecto Final —  Comercial

> Versión final del sistema, desarrollada en **Python 3** con arquitectura modular y persistencia en archivos CSV.

---

##  Módulos del sistema

El sistema está dividido en módulos independientes, cada uno responsable de una entidad del negocio:

| Módulo | Archivo | Datos |
|---|---|---|
| 👥 Clientes | `clientes.py` | `clientes.csv` |
| 🏭 Proveedores | `proveedores.py` | `proveedores.csv` |
| 📦 Stock | `stock.py` | `stock.csv` |
| 🧾 Ventas | `ventas.py` | `ventas.csv` |
| 🚀 Principal | `main.py` | — |

---

##  Funcionalidades

- **Gestión de clientes:** alta, baja, modificación y consulta de clientes
- **Gestión de proveedores:** registro y administración de proveedores
- **Control de stock:** seguimiento del inventario de productos
- **Registro de ventas:** operaciones de venta con trazabilidad
- **Persistencia automática:** los datos se guardan en archivos CSV entre sesiones

---

##  Estructura de datos

Cada módulo maneja su propia entidad y persiste la información en un archivo `.csv` correspondiente. Esto permite que los datos se conserven entre ejecuciones sin necesidad de una base de datos externa.

```
Proyecto Final/
├── main.py           ← Menú principal e integración de módulos
├── clientes.py       ← Lógica de clientes
├── proveedores.py    ← Lógica de proveedores
├── stock.py          ← Lógica de stock
├── ventas.py         ← Lógica de ventas
├── clientes.csv      ← Datos persistidos
├── proveedores.csv   ← Datos persistidos
├── stock.csv         ← Datos persistidos
└── ventas.csv        ← Datos persistidos
```

---

##  Ejecución

```bash
python main.py
```

El programa presenta un menú interactivo desde el cual se accede a cada módulo del sistema.

---

##  Decisiones de diseño

- **Modularización:** cada entidad tiene su propio archivo `.py`, facilitando el mantenimiento y la extensión del sistema.
- **CSV como persistencia:** se eligió este formato por su simplicidad y compatibilidad con la biblioteca estándar de Python, sin dependencias externas.
- **Menú principal centralizado:** `main.py` actúa como integrador, manteniendo los módulos desacoplados entre sí.
