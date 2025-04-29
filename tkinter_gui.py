import tkinter as tk
from tkinter import messagebox
from crud import crear_producto, mostrar_productos, buscar_producto_por_id, actualizar_producto, eliminar_producto

# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Catálogos")
root.geometry("600x400")

# Entrada de datos
nombre_var = tk.StringVar()
desc_var = tk.StringVar()
precio_var = tk.StringVar()
id_var = tk.StringVar()

# --- Funciones ---
def crear():
    nombre = nombre_var.get()
    desc = desc_var.get()
    try:
        precio = float(precio_var.get())
        crear_producto(nombre, desc, precio)
        messagebox.showinfo("Éxito", "Producto creado")
    except ValueError:
        messagebox.showerror("Error", "Precio inválido")

def listar():
    productos = mostrar_productos()
    lista.delete(0, tk.END)
    for p in productos:
        lista.insert(tk.END, f"ID:{p.id} | {p.nombre} - {p.descripcion} - ${p.precio}")

def buscar():
    try:
        id_ = int(id_var.get())
        p = buscar_producto_por_id(id_)
        if p:
            nombre_var.set(p.nombre)
            desc_var.set(p.descripcion)
            precio_var.set(str(p.precio))
        else:
            messagebox.showinfo("No encontrado", "Producto no existe")
    except ValueError:
        messagebox.showerror("Error", "ID inválido")

def modificar():
    try:
        id_ = int(id_var.get())
        nombre = nombre_var.get()
        desc = desc_var.get()
        precio = float(precio_var.get())
        actualizar_producto(id_, nombre, desc, precio)
        messagebox.showinfo("Éxito", "Producto actualizado")
    except ValueError:
        messagebox.showerror("Error", "Datos inválidos")

def eliminar():
    try:
        id_ = int(id_var.get())
        eliminar_producto(id_)
        messagebox.showinfo("Éxito", "Producto eliminado")
    except ValueError:
        messagebox.showerror("Error", "ID inválido")

# --- Layout ---
tk.Label(root, text="ID").grid(row=0, column=0)
tk.Entry(root, textvariable=id_var).grid(row=0, column=1)

tk.Label(root, text="Nombre").grid(row=1, column=0)
tk.Entry(root, textvariable=nombre_var).grid(row=1, column=1)

tk.Label(root, text="Descripción").grid(row=2, column=0)
tk.Entry(root, textvariable=desc_var).grid(row=2, column=1)

tk.Label(root, text="Precio").grid(row=3, column=0)
tk.Entry(root, textvariable=precio_var).grid(row=3, column=1)

tk.Button(root, text="Crear", command=crear).grid(row=4, column=0, pady=5)
tk.Button(root, text="Buscar", command=buscar).grid(row=4, column=1)
tk.Button(root, text="Modificar", command=modificar).grid(row=5, column=0)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=5, column=1)
tk.Button(root, text="Listar productos", command=listar).grid(row=6, column=0, columnspan=2)

lista = tk.Listbox(root, width=70)
lista.grid(row=7, column=0, columnspan=2, pady=10)

# Ejecutar interfaz
root.mainloop()
