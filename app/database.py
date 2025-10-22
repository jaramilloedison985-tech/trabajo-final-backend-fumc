"""
========================================
CONFIGURACIÓN DE BASE DE DATOS
========================================
Este archivo maneja la conexión a PostgreSQL usando SQLAlchemy.
SQLAlchemy es un ORM (Object-Relational Mapping) que nos permite
trabajar con la base de datos usando objetos de Python en lugar
de escribir SQL directamente.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# ========================================
# MOTOR DE BASE DE DATOS
# ========================================
"""
El 'engine' es el punto de entrada de SQLAlchemy a la base de datos.
Se encarga de gestionar las conexiones.

Parámetros:
- connect_args: {"check_same_thread": False} es para SQLite, pero no afecta a PostgreSQL
- pool_pre_ping: True verifica que la conexión esté viva antes de usarla
- echo: False significa que no imprimirá todas las queries SQL (útil para debugging si es True)
"""
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,  # Verifica conexiones antes de usarlas
    echo=False  # Cambia a True si quieres ver las queries SQL en consola
)

# ========================================
# FÁBRICA DE SESIONES
# ========================================
"""
SessionLocal es una clase que crea sesiones de base de datos.
Una sesión es como una "conversación" con la base de datos donde
puedes hacer varias operaciones (INSERT, UPDATE, SELECT, etc.)
"""
SessionLocal = sessionmaker(
    autocommit=False,  # No hacer commit automático (lo haremos manualmente)
    autoflush=False,   # No hacer flush automático
    bind=engine        # Asociar con nuestro engine de PostgreSQL
)

# ========================================
# CLASE BASE PARA MODELOS
# ========================================
"""
Todos los modelos de base de datos heredarán de esta clase Base.
Es la forma en que SQLAlchemy sabe qué clases representan tablas.
"""
Base = declarative_base()


# ========================================
# FUNCIÓN PARA OBTENER SESIÓN DE BD
# ========================================
def get_db():
    """
    Generador que proporciona una sesión de base de datos.

    Se usa con FastAPI para inyectar la sesión en los endpoints.
    El 'yield' hace que la sesión se cierre automáticamente después
    de que el endpoint termine de ejecutarse.

    Uso en endpoints:
        @app.get("/ejemplo")
        def ejemplo(db: Session = Depends(get_db)):
            # Aquí ya tienes 'db' disponible para usar
            ...

    Yields:
        Session: Sesión de base de datos para realizar operaciones
    """
    db = SessionLocal()  # Crear nueva sesión
    try:
        yield db  # Proporcionar la sesión al endpoint
    finally:
        db.close()  # Cerrar la sesión cuando termine (siempre se ejecuta)
