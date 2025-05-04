# gestor_catalogos 

Aplicación de escritorio desarrollada en Python que permite gestionar productos mediante una interfaz gráfica intuitiva. Utiliza SQLite como sistema de gestión de base de datos, SQLAlchemy como ORM y Tkinter como interfaz gráfica.

##  Dependencias

- Python 3.10+
- Tkinter
- SQLite
- SQLAlchemy

## Instalación

1. Clonamos el repositorio:
```bash
git clone https://github.com/anavilaph/gestor_catalogos.git
cd gestor_catalogos

2. Instalamos las dependencias:
pip install -r requirements.txt

3. Creamos base de datos:
-- crear_base_datos.sql

DROP TABLE IF EXISTS productos;

CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
);

INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Producto A', 'Descripción del producto A', 10.99, 50),
('Producto B', 'Descripción del producto B', 5.49, 20),
('Producto C', 'Descripción del producto C', 7.99, 15);
Para crear la base de datos usando este script:

sqlite3 productos.db < crear_base_datos.sql

4. Cómo ejecutarlo: 
Lanzamos la aplicación con:
python main.py

Se abre la interfaz gráfica para poder hacer lo siguiente:

Añadir productos
Buscar productos
Modificar productos existentes
Eliminar productos del catálogo

5. Estructura final del proyecto

gestor_catalogos/
├── crud.py              # Funciones CRUD
├── database.py          # Configuración de la base de datos
├── main.py              # Punto de entrada de la aplicación
├── models.py            # Definición de modelos con SQLAlchemy
├── tkinter_gui.py       # Interfaz de usuario con Tkinter
├── productos.db         # Base de datos SQLite
├── crear_base_datos.sql # Script SQL para recrear la base de datos
├── requirements.txt     # Lista de dependencias
└── README.md            # Este archivo


Autor
Proyecto desarrollado por Ana Vila y Blanca Flores
