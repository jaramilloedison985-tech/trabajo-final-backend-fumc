"""
========================================
ROUTER DE PRODUCTOS
========================================
Este archivo contiene todos los endpoints relacionados con productos.
Cada función es un endpoint de la API.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import json
from datetime import datetime

from ..database import get_db
from ..models import Producto, HistorialAuditoria
from ..schemas import ProductoCreate, ProductoUpdate, ProductoResponse, MensajeResponse
from ..config import settings

# ========================================
# CREAR EL ROUTER
# ========================================
"""
APIRouter agrupa endpoints relacionados.
Todos los endpoints de este archivo empezarán con /productos
"""
router = APIRouter(
    prefix="/productos",  # Prefijo para todos los endpoints de este router
    tags=["Productos"],   # Tag para agrupar en la documentación
    responses={
        404: {"description": "Producto no encontrado"},
        400: {"description": "Solicitud inválida"}
    }
)


# ========================================
# FUNCIÓN AUXILIAR: REGISTRAR AUDITORÍA
# ========================================
def registrar_auditoria(
    db: Session,
    tabla: str,
    id_registro: int,
    operacion: str,
    datos_anteriores: dict = None,
    datos_nuevos: dict = None,
    observaciones: str = None
):
    """
    Registra una operación en el historial de auditoría.

    Args:
        db: Sesión de base de datos
        tabla: Nombre de la tabla afectada
        id_registro: ID del registro afectado
        operacion: Tipo de operación (CREATE, UPDATE, DELETE)
        datos_anteriores: Datos antes de la modificación (dict)
        datos_nuevos: Datos nuevos (dict)
        observaciones: Comentarios adicionales
    """
    auditoria = HistorialAuditoria(
        tabla_afectada=tabla,
        id_registro=id_registro,
        operacion=operacion,
        grupo_responsable=settings.GRUPO_ESTUDIANTES,
        datos_anteriores=json.dumps(datos_anteriores, default=str) if datos_anteriores else None,
        datos_nuevos=json.dumps(datos_nuevos, default=str) if datos_nuevos else None,
        observaciones=observaciones
    )
    db.add(auditoria)
    db.commit()


# ========================================
# ENDPOINT: CREAR PRODUCTO
# ========================================
@router.post(
    "/",
    response_model=ProductoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo producto",
    description="Crea un nuevo producto en la tienda virtual. El grupo que crea el producto queda registrado en auditoría."
)
async def crear_producto(
    producto: ProductoCreate,
    db: Session = Depends(get_db)
):
    """
    Crea un nuevo producto.

    - **nombre**: Nombre del producto (obligatorio, 3-200 caracteres)
    - **descripcion**: Descripción detallada (opcional)
    - **precio**: Precio en pesos colombianos (obligatorio, mayor a 0)
    - **stock**: Cantidad en inventario (opcional, por defecto 0)
    - **categoria**: Categoría del producto (opcional)
    - **imagen_url**: URL de la imagen (opcional)

    Returns:
        ProductoResponse: Producto creado con todos sus campos
    """

    # Convertir el schema de Pydantic a un diccionario
    producto_dict = producto.model_dump()

    # Crear el objeto del modelo de SQLAlchemy
    db_producto = Producto(
        **producto_dict,  # Desempaquetar el diccionario
        grupo_creador=settings.GRUPO_ESTUDIANTES  # Registrar el grupo creador
    )

    # Agregar a la sesión de base de datos
    db.add(db_producto)

    # Guardar en la base de datos
    db.commit()

    # Refrescar para obtener los campos generados automáticamente (id, fecha_creacion, etc.)
    db.refresh(db_producto)

    # Registrar en auditoría
    registrar_auditoria(
        db=db,
        tabla="productos",
        id_registro=db_producto.id,
        operacion="CREATE",
        datos_nuevos=producto_dict,
        observaciones=f"Producto '{db_producto.nombre}' creado por {settings.GRUPO_ESTUDIANTES}"
    )

    return db_producto


# ========================================
# ENDPOINT: LISTAR PRODUCTOS
# ========================================
@router.get(
    "/",
    response_model=List[ProductoResponse],
    summary="Listar todos los productos",
    description="Obtiene la lista de todos los productos. Por defecto solo muestra productos activos."
)
async def listar_productos(
    skip: int = 0,          # Número de registros a saltar (paginación)
    limit: int = 100,       # Máximo de registros a devolver
    incluir_inactivos: bool = False,  # Si True, incluye productos eliminados lógicamente
    categoria: str = None,  # Filtrar por categoría
    db: Session = Depends(get_db)
):
    """
    Lista productos con opciones de filtrado y paginación.

    - **skip**: Número de productos a saltar (para paginación)
    - **limit**: Máximo de productos a devolver
    - **incluir_inactivos**: Si es True, incluye productos eliminados
    - **categoria**: Filtrar por categoría específica

    Returns:
        List[ProductoResponse]: Lista de productos
    """

    # Crear la consulta base
    query = db.query(Producto)

    # Filtrar por activos/inactivos
    if not incluir_inactivos:
        query = query.filter(Producto.activo == True)

    # Filtrar por categoría si se especifica
    if categoria:
        query = query.filter(Producto.categoria == categoria)

    # Ordenar por fecha de creación (más recientes primero)
    query = query.order_by(Producto.fecha_creacion.desc())

    # Aplicar paginación y ejecutar consulta
    productos = query.offset(skip).limit(limit).all()

    return productos


# ========================================
# ENDPOINT: OBTENER PRODUCTO POR ID
# ========================================
@router.get(
    "/{producto_id}",
    response_model=ProductoResponse,
    summary="Obtener un producto específico",
    description="Obtiene los detalles de un producto por su ID."
)
async def obtener_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    """
    Obtiene un producto por su ID.

    - **producto_id**: ID del producto a buscar

    Returns:
        ProductoResponse: Datos del producto

    Raises:
        HTTPException 404: Si el producto no existe
    """

    # Buscar el producto en la base de datos
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    # Si no existe, retornar error 404
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con ID {producto_id} no encontrado"
        )

    return producto


# ========================================
# ENDPOINT: ACTUALIZAR PRODUCTO
# ========================================
@router.put(
    "/{producto_id}",
    response_model=ProductoResponse,
    summary="Actualizar un producto",
    description="Actualiza los datos de un producto existente. Solo se actualizan los campos enviados."
)
async def actualizar_producto(
    producto_id: int,
    producto_actualizado: ProductoUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualiza un producto existente.

    Solo se actualizan los campos que se envíen en el request.
    Los campos no enviados mantienen su valor actual.

    - **producto_id**: ID del producto a actualizar
    - Campos opcionales: nombre, descripcion, precio, stock, categoria, imagen_url, activo

    Returns:
        ProductoResponse: Producto actualizado

    Raises:
        HTTPException 404: Si el producto no existe
    """

    # Buscar el producto
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con ID {producto_id} no encontrado"
        )

    # Guardar datos anteriores para auditoría
    datos_anteriores = {
        "nombre": producto.nombre,
        "descripcion": producto.descripcion,
        "precio": float(producto.precio),
        "stock": producto.stock,
        "categoria": producto.categoria,
        "imagen_url": producto.imagen_url,
        "activo": producto.activo
    }

    # Actualizar solo los campos que fueron enviados
    update_data = producto_actualizado.model_dump(exclude_unset=True)

    for campo, valor in update_data.items():
        setattr(producto, campo, valor)  # Establecer el nuevo valor

    # Registrar quién hizo la modificación
    producto.grupo_ultima_modificacion = settings.GRUPO_ESTUDIANTES

    # Guardar cambios
    db.commit()
    db.refresh(producto)

    # Registrar en auditoría
    registrar_auditoria(
        db=db,
        tabla="productos",
        id_registro=producto.id,
        operacion="UPDATE",
        datos_anteriores=datos_anteriores,
        datos_nuevos=update_data,
        observaciones=f"Producto '{producto.nombre}' actualizado por {settings.GRUPO_ESTUDIANTES}"
    )

    return producto


# ========================================
# ENDPOINT: ELIMINAR PRODUCTO (LÓGICO)
# ========================================
@router.delete(
    "/{producto_id}",
    response_model=MensajeResponse,
    summary="Eliminar un producto (eliminación lógica)",
    description="Marca un producto como inactivo (eliminación lógica). El producto no se borra físicamente de la base de datos."
)
async def eliminar_producto(
    producto_id: int,
    db: Session = Depends(get_db)
):
    """
    Elimina un producto de forma lógica (no lo borra de la BD).

    La eliminación es lógica: solo marca el producto como 'activo = False'.
    Esto permite mantener historial y recuperar el producto si es necesario.

    - **producto_id**: ID del producto a eliminar

    Returns:
        MensajeResponse: Confirmación de eliminación

    Raises:
        HTTPException 404: Si el producto no existe
        HTTPException 400: Si el producto ya está inactivo
    """

    # Buscar el producto
    producto = db.query(Producto).filter(Producto.id == producto_id).first()

    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con ID {producto_id} no encontrado"
        )

    # Verificar si ya está inactivo
    if not producto.activo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El producto '{producto.nombre}' ya está inactivo"
        )

    # Guardar datos para auditoría
    datos_anteriores = {
        "nombre": producto.nombre,
        "activo": producto.activo
    }

    # Marcar como inactivo
    producto.activo = False
    producto.grupo_ultima_modificacion = settings.GRUPO_ESTUDIANTES

    db.commit()

    # Registrar en auditoría
    registrar_auditoria(
        db=db,
        tabla="productos",
        id_registro=producto.id,
        operacion="DELETE",
        datos_anteriores=datos_anteriores,
        datos_nuevos={"activo": False},
        observaciones=f"Producto '{producto.nombre}' eliminado (lógicamente) por {settings.GRUPO_ESTUDIANTES}"
    )

    return MensajeResponse(
        mensaje=f"Producto '{producto.nombre}' eliminado correctamente",
        detalle="Eliminación lógica: el producto está marcado como inactivo"
    )


# ========================================
# ENDPOINT: BUSCAR PRODUCTOS
# ========================================
@router.get(
    "/buscar/nombre",
    response_model=List[ProductoResponse],
    summary="Buscar productos por nombre",
    description="Busca productos que contengan el texto especificado en su nombre."
)
async def buscar_productos_por_nombre(
    query: str,  # Texto a buscar
    db: Session = Depends(get_db)
):
    """
    Busca productos por nombre (búsqueda parcial).

    - **query**: Texto a buscar en el nombre del producto

    Returns:
        List[ProductoResponse]: Productos que coinciden con la búsqueda
    """

    if not query or len(query) < 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La búsqueda debe tener al menos 2 caracteres"
        )

    # Búsqueda usando ILIKE (case-insensitive en PostgreSQL)
    # %query% encuentra el texto en cualquier parte del nombre
    productos = db.query(Producto)\
        .filter(Producto.activo == True)\
        .filter(Producto.nombre.ilike(f"%{query}%"))\
        .all()

    return productos
