"""
Este archivo hace que la carpeta 'routers' sea un paquete de Python.
"""

from .productos import router as productos_router
from .clientes import router as clientes_router
from .auditoria import router as auditoria_router
