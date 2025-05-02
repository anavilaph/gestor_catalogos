from models import Producto
from database import Session

def crear_producto(nombre, descripcion, precio):
    session = Session()
    nuevo = Producto(nombre=nombre, descripcion=descripcion, precio=precio)
    session.add(nuevo)
    session.commit()
    session.close()

def mostrar_productos():
    session = Session()
    productos = session.query(Producto).all()
    session.close()
    return productos

def buscar_producto_por_id(prod_id):
    session = Session()
    producto = session.query(Producto).get(prod_id)
    session.close()
    return producto

def actualización_producto(prod_id, nombre=None, descripcion=None, precio=None):
    session = Session()
    producto = session.query(Producto).get(prod_id)
    if producto:
        if nombre: producto.nombre = nombre
        if descripcion: producto.descripcion = descripcion
        if precio: producto.precio = precio
        session.commit()
    session.close()

def borrar_producto(prod_id):
    session = Session()
    producto = session.query(Producto).get(prod_id)
    if producto:
        session.delete(producto)
        session.commit()
    session.close()