"""
========================================
ROUTER DE AUDITORÍA
========================================
Endpoints para consultar el historial de auditoría.
Permite ver qué grupos han hecho qué operaciones.
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta

from ..database import get_db
from ..models import HistorialAuditoria
from ..schemas import AuditoriaResponse

# ========================================
# CREAR EL ROUTER
# ========================================
router = APIRouter(
    prefix="/auditoria",
    tags=["Auditoría"],
    responses={404: {"description": "No se encontraron registros"}}
)


# ========================================
# ENDPOINT: LISTAR HISTORIAL COMPLETO
# ========================================
@router.get(
    "/",
    response_model=List[AuditoriaResponse],
    summary="Listar historial de auditoría",
    description="Obtiene el historial de todas las operaciones realizadas en la API."
)
async def listar_historial(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Lista el historial de auditoría con paginación.

    - **skip**: Registros a saltar
    - **limit**: Máximo de registros a devolver

    Returns:
        List[AuditoriaResponse]: Historial de operaciones
    """

    historial = db.query(HistorialAuditoria)\
        .order_by(HistorialAuditoria.fecha_operacion.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()

    return historial


# ========================================
# ENDPOINT: FILTRAR POR GRUPO
# ========================================
@router.get(
    "/grupo/{nombre_grupo}",
    response_model=List[AuditoriaResponse],
    summary="Ver operaciones de un grupo",
    description="Obtiene todas las operaciones realizadas por un grupo específico."
)
async def historial_por_grupo(
    nombre_grupo: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Filtra el historial por grupo.

    - **nombre_grupo**: Nombre del grupo a buscar

    Returns:
        List[AuditoriaResponse]: Operaciones del grupo
    """

    historial = db.query(HistorialAuditoria)\
        .filter(HistorialAuditoria.grupo_responsable == nombre_grupo)\
        .order_by(HistorialAuditoria.fecha_operacion.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()

    return historial


# ========================================
# ENDPOINT: FILTRAR POR TABLA
# ========================================
@router.get(
    "/tabla/{nombre_tabla}",
    response_model=List[AuditoriaResponse],
    summary="Ver operaciones en una tabla",
    description="Obtiene todas las operaciones realizadas en una tabla específica (productos o clientes)."
)
async def historial_por_tabla(
    nombre_tabla: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Filtra el historial por tabla.

    - **nombre_tabla**: Nombre de la tabla (productos o clientes)

    Returns:
        List[AuditoriaResponse]: Operaciones en la tabla
    """

    historial = db.query(HistorialAuditoria)\
        .filter(HistorialAuditoria.tabla_afectada == nombre_tabla)\
        .order_by(HistorialAuditoria.fecha_operacion.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()

    return historial


# ========================================
# ENDPOINT: FILTRAR POR OPERACIÓN
# ========================================
@router.get(
    "/operacion/{tipo_operacion}",
    response_model=List[AuditoriaResponse],
    summary="Ver operaciones de un tipo",
    description="Obtiene todas las operaciones de un tipo específico (CREATE, UPDATE, DELETE)."
)
async def historial_por_operacion(
    tipo_operacion: str,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Filtra el historial por tipo de operación.

    - **tipo_operacion**: Tipo de operación (CREATE, UPDATE, DELETE)

    Returns:
        List[AuditoriaResponse]: Operaciones del tipo especificado
    """

    historial = db.query(HistorialAuditoria)\
        .filter(HistorialAuditoria.operacion == tipo_operacion.upper())\
        .order_by(HistorialAuditoria.fecha_operacion.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()

    return historial


# ========================================
# ENDPOINT: HISTORIAL DE UN REGISTRO
# ========================================
@router.get(
    "/registro/{tabla}/{id_registro}",
    response_model=List[AuditoriaResponse],
    summary="Ver historial de un registro específico",
    description="Obtiene todo el historial de un producto o cliente específico."
)
async def historial_de_registro(
    tabla: str,
    id_registro: int,
    db: Session = Depends(get_db)
):
    """
    Obtiene todo el historial de un registro específico.

    - **tabla**: Nombre de la tabla (productos o clientes)
    - **id_registro**: ID del registro

    Returns:
        List[AuditoriaResponse]: Historial completo del registro
    """

    historial = db.query(HistorialAuditoria)\
        .filter(HistorialAuditoria.tabla_afectada == tabla)\
        .filter(HistorialAuditoria.id_registro == id_registro)\
        .order_by(HistorialAuditoria.fecha_operacion.desc())\
        .all()

    return historial
