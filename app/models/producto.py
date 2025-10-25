"""
========================================
MODELO: PRODUCTO
========================================
Este archivo define la clase Producto que representa
la tabla 'productos' en PostgreSQL.

Cada instancia de esta clase es un producto en la tienda virtual.
"""

from sqlalchemy import Column, Integer, String, Numeric, Boolean, DateTime, Text
from sqlalchemy.sql import text
from typing import Any
from ..database import Base


class Producto(Base):
    """
    📦 CLASE PRODUCTO - Representa un producto de la tienda

    Esta clase es un modelo de SQLAlchemy que se mapea a la tabla
    'productos' en PostgreSQL. Cada atributo es una columna de la tabla.

    Ejemplo de uso:
        # Crear un nuevo producto
        nuevo_producto = Producto(
            nombre="Laptop HP",
            precio=1500000,
            stock=10,
            categoria="Electrónica",
            grupo_creador="GRUPO_1"
        )

    Campos principales:
        - id: Identificador único (se genera automáticamente)
        - nombre: Nombre del producto
        - descripcion: Descripción detallada
        - precio: Precio en pesos colombianos
        - stock: Cantidad disponible
        - categoria: Categoría del producto
        - imagen_url: URL de la imagen

    Campos de auditoría:
        - activo: Si está activo o fue eliminado (lógicamente)
        - fecha_creacion: Cuándo se creó
        - fecha_actualizacion: Última modificación
        - grupo_creador: Qué grupo lo creó
        - grupo_ultima_modificacion: Último grupo que lo modificó
    """

    # Nombre de la tabla en la base de datos PostgreSQL
    __tablename__ = "productos"

    # ========================================
    # COLUMNAS PRINCIPALES
    # ========================================

    id = Column(
        Integer,
        primary_key=True,  # Es la clave primaria de la tabla
        index=True,        # Se crea un índice para búsquedas rápidas
        autoincrement=True,  # PostgreSQL incrementa automáticamente
        comment="Identificador único del producto (PK)"
    )

    nombre = Column(
        String(200),      # Máximo 200 caracteres
        nullable=False,   # Campo obligatorio (no puede ser NULL)
        index=True,       # Índice para búsquedas por nombre
        comment="Nombre del producto"
    )

    descripcion = Column(
        Text,             # Texto largo sin límite específico
        nullable=True,    # Campo opcional (puede ser NULL)
        comment="Descripción detallada del producto"
    )

    precio = Column(
        Numeric(10, 2),   # Hasta 10 dígitos totales, 2 decimales
                          # Ejemplo: 99999999.99
        nullable=False,   # Campo obligatorio
        comment="Precio del producto en pesos colombianos"
    )

    stock = Column(
        Integer,
        nullable=False,
        default=0,        # Si no se especifica, será 0
        comment="Cantidad disponible en inventario"
    )

    categoria = Column(
        String(100),
        nullable=True,    # Campo opcional
        index=True,       # Índice para filtrar por categoría rápidamente
        comment="Categoría del producto (Electrónica, Ropa, etc.)"
    )

    imagen_url = Column(
        String(500),
        nullable=True,    # Campo opcional
        comment="URL de la imagen del producto"
    )

    # ========================================
    # COLUMNAS DE AUDITORÍA Y CONTROL
    # ========================================

    activo = Column(
        Boolean,
        default=True,     # Por defecto todos los productos están activos
        nullable=False,
        comment="Indica si el producto está activo (eliminación lógica)"
    )
    # ¿Qué es eliminación lógica?
    # En lugar de borrar el producto de la base de datos (DELETE),
    # solo lo marcamos como inactivo (activo = False).
    # Esto permite mantener el historial y recuperarlo si es necesario.

    fecha_creacion = Column(
        DateTime(timezone=True),  # Incluye zona horaria
        server_default=text("NOW()"),  # PostgreSQL pone fecha automáticamente
        nullable=False,
        comment="Fecha y hora de creación del registro",
    )

    fecha_actualizacion = Column(
        DateTime(timezone=True),
        server_default=text("NOW()"),  # Fecha inicial
        onupdate=text("NOW()"),  # Se actualiza automáticamente al modificar
        nullable=False,
        comment="Fecha y hora de última actualización",
    )

    grupo_creador = Column(
        String(50),
        nullable=False,
        index=True,       # Índice para filtrar por grupo
        comment="Nombre del grupo de estudiantes que creó el producto"
    )
    # Este campo se llena automáticamente con el valor de
    # settings.GRUPO_ESTUDIANTES desde el archivo .env

    grupo_ultima_modificacion = Column(
        String(50),
        nullable=True,    # Opcional porque al crear es NULL
        comment="Nombre del grupo que hizo la última modificación"
    )

    def __repr__(self):
        """
        Representación en string del objeto.
        Se usa cuando haces print(producto) o en el debugger.

        Returns:
            str: Representación legible del producto
        """
        return (
            f"<Producto(id={self.id}, nombre='{self.nombre}', "
            f"precio={self.precio}, stock={self.stock})>"
        )

    def to_dict(self) -> dict[str, Any]:
        """
        Convierte el objeto Producto a un diccionario.
        Útil para serializar a JSON o para debugging.

        Returns:
            dict: Diccionario con todos los campos del producto
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": (
                float(self.precio)  # type: ignore
                if self.precio is not None  # type: ignore
                else None
            ),
            "stock": self.stock,
            "categoria": self.categoria,
            "imagen_url": self.imagen_url,
            "activo": self.activo,
            "fecha_creacion": (
                self.fecha_creacion.isoformat()
                if self.fecha_creacion is not None  # type: ignore
                else None
            ),
            "fecha_actualizacion": (
                self.fecha_actualizacion.isoformat()
                if self.fecha_actualizacion is not None  # type: ignore
                else None
            ),
            "grupo_creador": self.grupo_creador,
            "grupo_ultima_modificacion": self.grupo_ultima_modificacion,
        }
