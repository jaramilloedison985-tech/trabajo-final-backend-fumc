"""
========================================
MÓDULO DE MODELOS
========================================
Este archivo importa todos los modelos de la base de datos.

Los modelos están organizados en archivos separados:
- producto.py: Define la clase Producto (tabla productos)
- cliente.py: Define la clase Cliente (tabla clientes)
- auditoria.py: Define la clase HistorialAuditoria (tabla historial_auditoria)

¿Por qué archivos separados?
-----------------------------
Hace el código más fácil de entender y mantener.
Cada archivo tiene UNA responsabilidad: definir UN modelo.

Esto se llama "Principio de Responsabilidad Única" (SRP).
"""

# Importamos cada modelo desde su archivo correspondiente
from .producto import Producto
from .cliente import Cliente
from .auditoria import HistorialAuditoria

# __all__ define qué se exporta cuando haces: from app.models import *
__all__ = ["Producto", "Cliente", "HistorialAuditoria"]
