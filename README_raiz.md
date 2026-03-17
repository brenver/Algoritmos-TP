# 🛒 Algoritmos-TP — Sistema de Gestión Comercial

> Trabajo Práctico desarrollado para la materia **Algoritmos y Estructura de Datos II**  
> Tecnicatura Superior en Análisis de Sistemas — Instituto N°179 "Dr. Carlos Pellegrini"

---

## 📌 Descripción

Este repositorio documenta la evolución de un sistema de gestión comercial desarrollado en Python a lo largo de la cursada. El proyecto partió de una versión funcional en **Python 2.7**, fue migrado a **Python 3** y culminó en una versión final modular con persistencia de datos en archivos CSV.

El sistema permite gestionar los módulos principales de un negocio: clientes, proveedores, stock y ventas.

---

## 🗂️ Estructura del repositorio

```
Algoritmos-TP/
│
├── Comercio2.py          # Versión inicial en Python 2.7
├── Comercio3.py          # Migración a Python 3
│
└── Proyecto Final/       # Versión final modular
    ├── main.py           # Punto de entrada del programa
    ├── clientes.py       # Módulo de gestión de clientes
    ├── proveedores.py    # Módulo de gestión de proveedores
    ├── stock.py          # Módulo de gestión de stock
    ├── ventas.py         # Módulo de gestión de ventas
    ├── clientes.csv      # Persistencia de datos — clientes
    ├── proveedores.csv   # Persistencia de datos — proveedores
    ├── stock.csv         # Persistencia de datos — stock
    └── ventas.csv        # Persistencia de datos — ventas
```

---

## 🚀 Evolución del proyecto

| Versión | Archivo | Descripción |
|---|---|---|
| v1 | `Comercio2.py` | Versión funcional en Python 2.7 |
| v2 | `Comercio3.py` | Migración y adaptación a Python 3 |
| v3 | `Proyecto Final/` | Refactorización modular con persistencia en CSV |

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Persistencia:** Archivos CSV (módulo `csv` de la biblioteca estándar)
- **Paradigma:** Programación estructurada / modular

---

## ▶️ Cómo ejecutar

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/brenver/Algoritmos-TP.git
   cd Algoritmos-TP/Proyecto\ Final
   ```

2. Ejecutá el programa principal:
   ```bash
   python main.py
   ```

> No requiere instalación de dependencias externas. Funciona con Python 3.x estándar.

---

## 📚 Contexto académico

Este trabajo fue desarrollado como Trabajo Práctico integrador de la materia **Algoritmos y Estructura de Datos II**, aplicando conceptos de:

- Modularización y separación de responsabilidades
- Manejo de archivos y persistencia de datos
- Estructuras de datos y su aplicación en un sistema real
- Migración y compatibilidad entre versiones de Python

---

## 👩‍💻 Autora

**Brenda** — [@brenver](https://github.com/brenver)  
Tecnicatura Superior en Análisis de Sistemas
