"""
========================================
APLICACIÓN PRINCIPAL - FASTAPI
========================================
Este es el archivo principal que inicia la API.
Aquí se configuran todos los routers y se crea la aplicación FastAPI.

CURSO: Frameworks para desarrollo web - Backend
INSTITUCIÓN: FUMC
PROYECTO: API de Tienda Virtual con PostgreSQL
"""

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Importar routers (endpoints organizados por módulos)
from app.routers import productos_router, clientes_router, auditoria_router

# Importar configuración y base de datos
from app.config import settings
from app.database import engine, Base

# ========================================
# CREAR LAS TABLAS EN LA BASE DE DATOS
# ========================================
"""
Esta línea crea todas las tablas definidas en los modelos
si no existen en la base de datos.

IMPORTANTE: En producción se usaría Alembic para migraciones,
pero para el curso esto es más simple y directo.
"""
Base.metadata.create_all(bind=engine)


# ========================================
# CREAR LA APLICACIÓN FASTAPI
# ========================================
app = FastAPI(
    # Información que aparece en la documentación
    title="API Tienda Virtual - FUMC",
    description="""
    ## 🛒 API REST para Tienda Virtual

    Esta API fue desarrollada como proyecto final del curso de
    **Frameworks para desarrollo web - Backend** en FUMC.

    ### Funcionalidades:

    * **Productos**: CRUD completo (Crear, Leer, Actualizar, Eliminar)
    * **Clientes**: Gestión completa de clientes
    * **Auditoría**: Trazabilidad de todas las operaciones

    ### Características técnicas:

    * Base de datos: PostgreSQL en la nube
    * Framework: FastAPI (Python)
    * Validación automática con Pydantic
    * Documentación automática (OpenAPI/Swagger)
    * Eliminación lógica (soft delete)
    * Sistema de auditoría por grupos de estudiantes

    ### Grupo responsable: {}

    ---

    **Documentación interactiva**: Puedes probar todos los endpoints
    directamente desde esta interfaz haciendo clic en "Try it out".
    """.format(settings.GRUPO_ESTUDIANTES),
    version="1.0.0",
    contact={
        "name": "FUMC - Curso Backend",
        "url": "https://www.fumc.edu.co",
    },
    license_info={
        "name": "MIT License",
    },
)


# ========================================
# CONFIGURAR CORS
# ========================================
"""
CORS (Cross-Origin Resource Sharing) permite que navegadores web
accedan a la API desde diferentes dominios.

Esto es necesario si vas a consumir la API desde un frontend
que esté en un dominio diferente.
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los headers
)


# ========================================
# INCLUIR LOS ROUTERS (ENDPOINTS)
# ========================================
"""
Los routers agrupan endpoints relacionados.
Cada router tiene un prefijo que se agrega a todas sus rutas.
"""

# Router de productos: /productos
app.include_router(
    productos_router,
    # tags=["Productos"]  # Ya está definido en el router
)

# Router de clientes: /clientes
app.include_router(
    clientes_router,
    # tags=["Clientes"]  # Ya está definido en el router
)

# Router de auditoría: /auditoria
app.include_router(
    auditoria_router,
    # tags=["Auditoría"]  # Ya está definido en el router
)


# ========================================
# ENDPOINTS RAÍZ Y DE INFORMACIÓN
# ========================================

@app.get(
    "/",
    tags=["Información"],
    summary="Endpoint raíz",
    description="Página de bienvenida de la API con información básica."
)
async def root():
    """
    Endpoint raíz de la API.
    Devuelve información básica y enlaces útiles.
    """
    return {
        "mensaje": "¡Bienvenido a la API de Tienda Virtual! 🛒",
        "curso": "Frameworks para desarrollo web - Backend",
        "institucion": "FUMC",
        "grupo": settings.GRUPO_ESTUDIANTES,
        "version": "1.0.0",
        "documentacion": "/docs",
        "documentacion_alternativa": "/redoc",
        "endpoints_disponibles": {
            "productos": "/productos",
            "clientes": "/clientes",
            "auditoria": "/auditoria"
        },
        "base_de_datos": {
            "tipo": "PostgreSQL",
            "host": settings.DB_HOST,
            "nombre": settings.DB_NAME,
            "estado": "✅ Conectado"
        }
    }


@app.get(
    "/health",
    tags=["Información"],
    summary="Estado de salud de la API",
    description="Verifica que la API esté funcionando correctamente."
)
async def health_check():
    """
    Health check endpoint.
    Útil para monitoreo y verificación de que el servidor está activo.
    """
    return {
        "status": "OK",
        "mensaje": "La API está funcionando correctamente ✅",
        "grupo": settings.GRUPO_ESTUDIANTES
    }


@app.get(
    "/info",
    tags=["Información"],
    summary="Información detallada de la API",
    description="Obtiene información técnica de la configuración de la API."
)
async def info():
    """
    Información técnica de la API.
    """
    return {
        "api": {
            "nombre": "API Tienda Virtual FUMC",
            "version": "1.0.0",
            "framework": "FastAPI",
            "lenguaje": "Python 3.8+"
        },
        "base_de_datos": {
            "motor": "PostgreSQL",
            "host": settings.DB_HOST,
            "puerto": settings.DB_PORT,
            "nombre_bd": settings.DB_NAME,
            "usuario": settings.DB_USER
        },
        "grupo": {
            "nombre": settings.GRUPO_ESTUDIANTES,
            "mensaje": "Todas las operaciones se registran con este nombre de grupo"
        },
        "endpoints": {
            "productos": {
                "listar": "GET /productos/",
                "crear": "POST /productos/",
                "obtener": "GET /productos/{id}",
                "actualizar": "PUT /productos/{id}",
                "eliminar": "DELETE /productos/{id}",
                "buscar": "GET /productos/buscar/nombre?query=..."
            },
            "clientes": {
                "listar": "GET /clientes/",
                "crear": "POST /clientes/",
                "obtener": "GET /clientes/{id}",
                "actualizar": "PUT /clientes/{id}",
                "eliminar": "DELETE /clientes/{id}",
                "buscar_nombre": "GET /clientes/buscar/nombre?query=...",
                "buscar_email": "GET /clientes/buscar/email/{email}"
            },
            "auditoria": {
                "listar": "GET /auditoria/",
                "por_grupo": "GET /auditoria/grupo/{nombre_grupo}",
                "por_tabla": "GET /auditoria/tabla/{nombre_tabla}",
                "por_operacion": "GET /auditoria/operacion/{tipo}",
                "por_registro": "GET /auditoria/registro/{tabla}/{id}"
            }
        }
    }


# ========================================
# MANEJO DE ERRORES GLOBAL
# ========================================
"""
Estos handlers capturan errores que no fueron manejados específicamente
en los endpoints y devuelven respuestas JSON formateadas.
"""

@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Handler para errores 404 (No encontrado)"""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "No encontrado",
            "detalle": "El recurso solicitado no existe",
            "ruta": str(request.url)
        }
    )


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Handler para errores 500 (Error interno del servidor)"""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Error interno del servidor",
            "detalle": "Ocurrió un error inesperado. Contacta al administrador.",
            "grupo": settings.GRUPO_ESTUDIANTES
        }
    )


# ========================================
# PUNTO DE ENTRADA PARA DESARROLLO
# ========================================
"""
Este bloque solo se ejecuta cuando corres el archivo directamente
con: python main.py

NO se ejecuta cuando se usa uvicorn desde la terminal o VS Code.
"""
if __name__ == "__main__":
    import uvicorn

    print("=" * 60)
    print("🚀 INICIANDO API DE TIENDA VIRTUAL - FUMC")
    print("=" * 60)
    print(f"Grupo: {settings.GRUPO_ESTUDIANTES}")
    print(f"Base de datos: {settings.DB_HOST}/{settings.DB_NAME}")
    print("=" * 60)
    print("\n📖 Documentación disponible en:")
    print("   http://127.0.0.1:8000/docs")
    print("   http://127.0.0.1:8000/redoc")
    print("\n✅ Servidor iniciado. Presiona Ctrl+C para detener.\n")

    # Iniciar el servidor
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # Permite conexiones externas
        port=8000,
        reload=True  # Reinicia automáticamente al detectar cambios en el código
    )
