from typing import Optional

from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Producto(Base):
    __tablename__ = 'productos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[Optional[str]] = mapped_column(String)
    descripcion: Mapped[Optional[str]] = mapped_column(String)
    precio: Mapped[Optional[float]] = mapped_column(Float)
