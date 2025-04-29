from database import Base, engine
from models import Producto

Base.metadata.create_all(bind=engine)
from crud import *
from tabulate import tabulate


def menu():
    while True:
        print("\n--- GESTOR DE CATÁLOGOS ---")
        print("1. Crear producto")
        print("2. Ver productos")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Salir")

        opc = input("Elige una opción: ")

        if opc == "1":
            nombre = input("Nombre: ")
            desc = input("Descripción: ")
            precio = float(input("Precio: "))
            crear_producto(nombre, desc, precio)
        elif opc == "2":
            productos = mostrar_productos()
            tabla = [[p.id, p.nombre, p.descripcion, p.precio] for p in productos]
            print(tabulate(tabla, headers=["ID", "Nombre", "Descripción", "Precio"]))
        elif opc == "3":
            id_ = int(input("ID: "))
            p = buscar_producto_por_id(id_)
            if p:
                print(f"{p.nombre} - {p.descripcion} - {p.precio}")
            else:
                print("No encontrado")
        elif opc == "4":
            id_ = int(input("ID a modificar: "))
            nombre = input("Nuevo nombre (o Enter): ") or None
            desc = input("Nueva descripción (o Enter): ") or None
            precio = input("Nuevo precio (o Enter): ")
            precio = float(precio) if precio else None
            actualizar_producto(id_, nombre, desc, precio)
        elif opc == "5":
            id_ = int(input("ID a eliminar: "))
            eliminar_producto(id_)
        elif opc == "6":
            break


if __name__ == "__main__":
    menu()
