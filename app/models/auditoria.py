"""
========================================
MODELO: HISTORIAL DE AUDITORÍA
========================================
Este archivo define la clase HistorialAuditoria que representa
la tabla 'historial_auditoria' en PostgreSQL.

Esta tabla registra TODAS las operaciones que se realizan en la API.
Es como un "libro de registro" donde queda escrito quién hizo qué y cuándo.
"""

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from ..database import Base


class HistorialAuditoria(Base):
    """
    📊 CLASE HISTORIAL DE AUDITORÍA - Registra todas las operaciones

    Esta clase es un modelo de SQLAlchemy que se mapea a la tabla
    'historial_auditoria' en PostgreSQL.

    ¿Para qué sirve?
    ----------------
    Cada vez que un grupo:
    - Crea un producto o cliente (CREATE)
    - Modifica un producto o cliente (UPDATE)
    - Elimina un producto o cliente (DELETE)

    Se guarda automáticamente un registro en esta tabla con:
    - Qué grupo lo hizo
    - Qué operación realizó
    - En qué tabla y registro
    - Qué datos cambió (antes y después)
    - Cuándo lo hizo (fecha y hora exacta)

    Esto permite:
    - Ver quién modificó cada cosa
    - Recuperar datos si algo se borra por error
    - Tener trazabilidad completa del sistema
    - Que el instructor vea el trabajo de cada grupo

    Ejemplo de uso:
        # SQLAlchemy creará automáticamente estos registros,
        # NO necesitas crearlos manualmente en tus endpoints.
        # La función registrar_auditoria() en los routers lo hace.

        # Pero podrías consultar así:
        historial = db.query(HistorialAuditoria)\
            .filter(HistorialAuditoria.grupo_responsable == "GRUPO_1")\
            .all()

    Campos principales:
        - id: Identificador único del registro
        - tabla_afectada: "productos" o "clientes"
        - id_registro: ID del producto/cliente afectado
        - operacion: "CREATE", "UPDATE" o "DELETE"
        - grupo_responsable: Qué grupo hizo la operación
        - datos_anteriores: Datos antes del cambio (JSON)
        - datos_nuevos: Datos después del cambio (JSON)
        - fecha_operacion: Cuándo se hizo
        - observaciones: Comentarios adicionales
    """

    # Nombre de la tabla en la base de datos PostgreSQL
    __tablename__ = "historial_auditoria"

    # ========================================
    # COLUMNAS DE IDENTIFICACIÓN
    # ========================================

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
        comment="Identificador único del registro de auditoría (PK)"
    )

    tabla_afectada = Column(
        String(50),
        nullable=False,
        index=True,       # Índice para filtrar por tabla rápidamente
        comment="Nombre de la tabla afectada (productos o clientes)"
    )
    # Valores posibles: "productos" o "clientes"

    id_registro = Column(
        Integer,
        nullable=False,
        index=True,       # Índice para buscar el historial de un registro
        comment="ID del registro afectado en su tabla"
    )
    # Este es el ID del producto o cliente que fue modificado.
    # Por ejemplo, si se modificó el producto con ID 5,
    # aquí se guarda el número 5.

    # ========================================
    # INFORMACIÓN DE LA OPERACIÓN
    # ========================================

    operacion = Column(
        String(20),
        nullable=False,
        index=True,       # Índice para filtrar por tipo de operación
        comment="Tipo de operación: CREATE, UPDATE, DELETE"
    )
    # Valores posibles:
    # - "CREATE": Se creó un nuevo registro
    # - "UPDATE": Se modificó un registro existente
    # - "DELETE": Se eliminó (lógicamente) un registro

    grupo_responsable = Column(
        String(50),
        nullable=False,
        index=True,       # Índice para ver qué hizo cada grupo
        comment="Grupo que realizó la operación"
    )
    # Este campo indica qué grupo de estudiantes realizó la operación.
    # Se toma automáticamente de settings.GRUPO_ESTUDIANTES

    # ========================================
    # DATOS DE LA OPERACIÓN (JSON)
    # ========================================

    datos_anteriores = Column(
        Text,             # Se guarda como texto (JSON serializado)
        nullable=True,    # Opcional porque CREATE no tiene datos anteriores
        comment="JSON con los datos antes de la modificación (solo UPDATE)"
    )
    # Para operaciones UPDATE, aquí se guardan los valores ANTES del cambio.
    # Ejemplo: {"nombre": "Laptop HP", "precio": 1500000, ...}
    #
    # Para CREATE y DELETE, este campo es NULL.

    datos_nuevos = Column(
        Text,             # Se guarda como texto (JSON serializado)
        nullable=True,    # Opcional
        comment="JSON con los datos después de la modificación"
    )
    # Aquí se guardan los datos NUEVOS después de la operación.
    # Para CREATE: los datos del registro creado
    # Para UPDATE: los datos modificados
    # Para DELETE: generalmente {"activo": false}

    fecha_operacion = Column(
        DateTime(timezone=True),  # Incluye zona horaria
        server_default=func.now(),  # PostgreSQL pone la fecha automáticamente
        nullable=False,
        index=True,       # Índice para ordenar por fecha
        comment="Fecha y hora de la operación"
    )
    # Se registra automáticamente cuando se crea el registro de auditoría.

    observaciones = Column(
        Text,
        nullable=True,    # Campo opcional
        comment="Comentarios adicionales sobre la operación"
    )
    # Aquí se pueden poner mensajes descriptivos como:
    # "Producto 'Laptop HP' creado por GRUPO_1"
    # "Cliente eliminado (lógicamente) por GRUPO_2"

    def __repr__(self):
        """
        Representación en string del objeto.
        Útil para debugging.

        Returns:
            str: Representación legible del registro de auditoría
        """
        return (
            f"<HistorialAuditoria("
            f"id={self.id}, "
            f"tabla='{self.tabla_afectada}', "
            f"id_registro={self.id_registro}, "
            f"operacion='{self.operacion}', "
            f"grupo='{self.grupo_responsable}', "
            f"fecha={self.fecha_operacion}"
            f")>"
        )

    def to_dict(self):
        """
        Convierte el objeto HistorialAuditoria a un diccionario.
        Útil para serializar a JSON en las respuestas de la API.

        Returns:
            dict: Diccionario con todos los campos del historial
        """
        return {
            "id": self.id,
            "tabla_afectada": self.tabla_afectada,
            "id_registro": self.id_registro,
            "operacion": self.operacion,
            "grupo_responsable": self.grupo_responsable,
            "datos_anteriores": self.datos_anteriores,
            "datos_nuevos": self.datos_nuevos,
            "fecha_operacion": self.fecha_operacion.isoformat() if self.fecha_operacion else None,
            "observaciones": self.observaciones
        }
