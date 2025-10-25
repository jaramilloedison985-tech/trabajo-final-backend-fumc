"""
========================================
MODELO: CLIENTE
========================================
Este archivo define la clase Cliente que representa
la tabla 'clientes' en PostgreSQL.

Cada instancia de esta clase es un cliente de la tienda virtual.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import text
from typing import Any
from ..database import Base


class Cliente(Base):
    """
    👥 CLASE CLIENTE - Representa un cliente de la tienda

    Esta clase es un modelo de SQLAlchemy que se mapea a la tabla
    'clientes' en PostgreSQL. Cada atributo es una columna de la tabla.

    Ejemplo de uso:
        # Crear un nuevo cliente
        nuevo_cliente = Cliente(
            nombre="María González",
            email="maria@email.com",
            telefono="+57 300 123 4567",
            ciudad="Medellín",
            grupo_creador="GRUPO_1"
        )

    Campos principales:
        - id: Identificador único (se genera automáticamente)
        - nombre: Nombre completo del cliente
        - email: Correo electrónico (ÚNICO)
        - telefono: Número de teléfono
        - direccion: Dirección de entrega
        - ciudad: Ciudad de residencia
        - documento: Número de documento (ÚNICO)

    Campos de auditoría:
        - activo: Si está activo o fue eliminado (lógicamente)
        - fecha_creacion: Cuándo se creó
        - fecha_actualizacion: Última modificación
        - grupo_creador: Qué grupo lo creó
        - grupo_ultima_modificacion: Último grupo que lo modificó
    """

    # Nombre de la tabla en la base de datos PostgreSQL
    __tablename__ = "clientes"

    # ========================================
    # COLUMNAS PRINCIPALES
    # ========================================

    id = Column(
        Integer,
        primary_key=True,  # Clave primaria
        index=True,        # Índice para búsquedas rápidas
        autoincrement=True,  # Auto-incrementa automáticamente
        comment="Identificador único del cliente (PK)"
    )

    nombre = Column(
        String(100),      # Máximo 100 caracteres
        nullable=False,   # Campo obligatorio
        comment="Nombre completo del cliente"
    )

    email = Column(
        String(150),
        nullable=False,   # Campo obligatorio
        unique=True,      # ⚠️ NO puede haber emails duplicados
        index=True,       # Índice para búsquedas rápidas por email
        comment="Correo electrónico del cliente (único en toda la BD)"
    )
    # El email es ÚNICO en toda la base de datos.
    # Si dos grupos intentan crear clientes con el mismo email,
    # el segundo dará error.

    telefono = Column(
        String(20),
        nullable=True,    # Campo opcional
        comment="Número de teléfono del cliente"
    )

    direccion = Column(
        Text,             # Texto largo
        nullable=True,    # Campo opcional
        comment="Dirección de entrega del cliente"
    )

    ciudad = Column(
        String(100),
        nullable=True,    # Campo opcional
        index=True,       # Índice para filtrar por ciudad
        comment="Ciudad de residencia"
    )

    documento = Column(
        String(20),
        nullable=True,    # Campo opcional
        unique=True,      # ⚠️ NO puede haber documentos duplicados
        index=True,       # Índice para búsquedas por documento
        comment="Número de documento de identidad (único)"
    )
    # El documento también es ÚNICO.
    # Dos clientes no pueden tener el mismo documento.

    # ========================================
    # COLUMNAS DE AUDITORÍA Y CONTROL
    # ========================================

    activo = Column(
        Boolean,
        default=True,     # Por defecto todos los clientes están activos
        nullable=False,
        comment="Indica si el cliente está activo (eliminación lógica)"
    )
    # Eliminación lógica: en lugar de borrar el cliente,
    # solo lo marcamos como inactivo (activo = False).

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
        comment="Nombre del grupo de estudiantes que creó el cliente"
    )
    # Se llena automáticamente con settings.GRUPO_ESTUDIANTES

    grupo_ultima_modificacion = Column(
        String(50),
        nullable=True,    # Opcional porque al crear es NULL
        comment="Nombre del grupo que hizo la última modificación"
    )

    def __repr__(self):
        """
        Representación en string del objeto.
        Útil para debugging y logs.

        Returns:
            str: Representación legible del cliente
        """
        return (
            f"<Cliente(id={self.id}, nombre='{self.nombre}', " f"email='{self.email}')>"
        )

    def to_dict(self) -> dict[str, Any]:
        """
        Convierte el objeto Cliente a un diccionario.
        Útil para serializar a JSON.

        Returns:
            dict: Diccionario con todos los campos del cliente
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "documento": self.documento,
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
