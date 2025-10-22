"""
========================================
ROUTER DE CLIENTES
========================================
Este archivo contiene todos los endpoints relacionados con clientes.
Similar a productos.py pero para gestionar clientes de la tienda.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import json

from ..database import get_db
from ..models import Cliente, HistorialAuditoria
from ..schemas import ClienteCreate, ClienteUpdate, ClienteResponse, MensajeResponse
from ..config import settings

# ========================================
# CREAR EL ROUTER
# ========================================
router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"],
    responses={
        404: {"description": "Cliente no encontrado"},
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
    """Registra operaciones en el historial de auditoría"""
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
# ENDPOINT: CREAR CLIENTE
# ========================================
@router.post(
    "/",
    response_model=ClienteResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo cliente",
    description="Registra un nuevo cliente en la tienda virtual."
)
async def crear_cliente(
    cliente: ClienteCreate,
    db: Session = Depends(get_db)
):
    """
    Crea un nuevo cliente.

    - **nombre**: Nombre completo (obligatorio, 3-100 caracteres)
    - **email**: Correo electrónico (obligatorio, debe ser único)
    - **telefono**: Número de teléfono (opcional)
    - **direccion**: Dirección de entrega (opcional)
    - **ciudad**: Ciudad de residencia (opcional)
    - **documento**: Número de documento (opcional, debe ser único)

    Returns:
        ClienteResponse: Cliente creado con todos sus campos

    Raises:
        HTTPException 400: Si el email o documento ya existen
    """

    # Verificar si el email ya existe
    cliente_existente = db.query(Cliente).filter(Cliente.email == cliente.email).first()
    if cliente_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ya existe un cliente con el email '{cliente.email}'"
        )

    # Verificar si el documento ya existe (si se proporcionó)
    if cliente.documento:
        doc_existente = db.query(Cliente).filter(Cliente.documento == cliente.documento).first()
        if doc_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ya existe un cliente con el documento '{cliente.documento}'"
            )

    # Crear el cliente
    cliente_dict = cliente.model_dump()
    db_cliente = Cliente(
        **cliente_dict,
        grupo_creador=settings.GRUPO_ESTUDIANTES
    )

    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)

    # Registrar en auditoría
    registrar_auditoria(
        db=db,
        tabla="clientes",
        id_registro=db_cliente.id,
        operacion="CREATE",
        datos_nuevos=cliente_dict,
        observaciones=f"Cliente '{db_cliente.nombre}' creado por {settings.GRUPO_ESTUDIANTES}"
    )

    return db_cliente


# ========================================
# ENDPOINT: LISTAR CLIENTES
# ========================================
@router.get(
    "/",
    response_model=List[ClienteResponse],
    summary="Listar todos los clientes",
    description="Obtiene la lista de todos los clientes activos."
)
async def listar_clientes(
    skip: int = 0,
    limit: int = 100,
    incluir_inactivos: bool = False,
    ciudad: str = None,
    db: Session = Depends(get_db)
):
    """
    Lista clientes con opciones de filtrado y paginación.

    - **skip**: Número de clientes a saltar
    - **limit**: Máximo de clientes a devolver
    - **incluir_inactivos**: Si es True, incluye clientes inactivos
    - **ciudad**: Filtrar por ciudad específica

    Returns:
        List[ClienteResponse]: Lista de clientes
    """

    query = db.query(Cliente)

    if not incluir_inactivos:
        query = query.filter(Cliente.activo == True)

    if ciudad:
        query = query.filter(Cliente.ciudad == ciudad)

    query = query.order_by(Cliente.fecha_creacion.desc())
    clientes = query.offset(skip).limit(limit).all()

    return clientes


# ========================================
# ENDPOINT: OBTENER CLIENTE POR ID
# ========================================
@router.get(
    "/{cliente_id}",
    response_model=ClienteResponse,
    summary="Obtener un cliente específico",
    description="Obtiene los detalles de un cliente por su ID."
)
async def obtener_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    """
    Obtiene un cliente por su ID.

    - **cliente_id**: ID del cliente a buscar

    Returns:
        ClienteResponse: Datos del cliente

    Raises:
        HTTPException 404: Si el cliente no existe
    """

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {cliente_id} no encontrado"
        )

    return cliente


# ========================================
# ENDPOINT: ACTUALIZAR CLIENTE
# ========================================
@router.put(
    "/{cliente_id}",
    response_model=ClienteResponse,
    summary="Actualizar un cliente",
    description="Actualiza los datos de un cliente existente."
)
async def actualizar_cliente(
    cliente_id: int,
    cliente_actualizado: ClienteUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualiza un cliente existente.

    - **cliente_id**: ID del cliente a actualizar
    - Campos opcionales: nombre, email, telefono, direccion, ciudad, documento, activo

    Returns:
        ClienteResponse: Cliente actualizado

    Raises:
        HTTPException 404: Si el cliente no existe
        HTTPException 400: Si el email o documento ya existen
    """

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {cliente_id} no encontrado"
        )

    # Verificar email único si se va a actualizar
    update_data = cliente_actualizado.model_dump(exclude_unset=True)

    if "email" in update_data and update_data["email"] != cliente.email:
        email_existente = db.query(Cliente).filter(Cliente.email == update_data["email"]).first()
        if email_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ya existe un cliente con el email '{update_data['email']}'"
            )

    # Verificar documento único si se va a actualizar
    if "documento" in update_data and update_data["documento"] != cliente.documento:
        if update_data["documento"]:  # Solo si no es None
            doc_existente = db.query(Cliente).filter(Cliente.documento == update_data["documento"]).first()
            if doc_existente:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Ya existe un cliente con el documento '{update_data['documento']}'"
                )

    # Guardar datos anteriores
    datos_anteriores = {
        "nombre": cliente.nombre,
        "email": cliente.email,
        "telefono": cliente.telefono,
        "direccion": cliente.direccion,
        "ciudad": cliente.ciudad,
        "documento": cliente.documento,
        "activo": cliente.activo
    }

    # Actualizar campos
    for campo, valor in update_data.items():
        setattr(cliente, campo, valor)

    cliente.grupo_ultima_modificacion = settings.GRUPO_ESTUDIANTES

    db.commit()
    db.refresh(cliente)

    # Registrar en auditoría
    registrar_auditoria(
        db=db,
        tabla="clientes",
        id_registro=cliente.id,
        operacion="UPDATE",
        datos_anteriores=datos_anteriores,
        datos_nuevos=update_data,
        observaciones=f"Cliente '{cliente.nombre}' actualizado por {settings.GRUPO_ESTUDIANTES}"
    )

    return cliente


# ========================================
# ENDPOINT: ELIMINAR CLIENTE (LÓGICO)
# ========================================
@router.delete(
    "/{cliente_id}",
    response_model=MensajeResponse,
    summary="Eliminar un cliente (eliminación lógica)",
    description="Marca un cliente como inactivo."
)
async def eliminar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    """
    Elimina un cliente de forma lógica.

    - **cliente_id**: ID del cliente a eliminar

    Returns:
        MensajeResponse: Confirmación de eliminación

    Raises:
        HTTPException 404: Si el cliente no existe
        HTTPException 400: Si el cliente ya está inactivo
    """

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con ID {cliente_id} no encontrado"
        )

    if not cliente.activo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente '{cliente.nombre}' ya está inactivo"
        )

    datos_anteriores = {
        "nombre": cliente.nombre,
        "activo": cliente.activo
    }

    cliente.activo = False
    cliente.grupo_ultima_modificacion = settings.GRUPO_ESTUDIANTES

    db.commit()

    registrar_auditoria(
        db=db,
        tabla="clientes",
        id_registro=cliente.id,
        operacion="DELETE",
        datos_anteriores=datos_anteriores,
        datos_nuevos={"activo": False},
        observaciones=f"Cliente '{cliente.nombre}' eliminado (lógicamente) por {settings.GRUPO_ESTUDIANTES}"
    )

    return MensajeResponse(
        mensaje=f"Cliente '{cliente.nombre}' eliminado correctamente",
        detalle="Eliminación lógica: el cliente está marcado como inactivo"
    )


# ========================================
# ENDPOINT: BUSCAR CLIENTES
# ========================================
@router.get(
    "/buscar/nombre",
    response_model=List[ClienteResponse],
    summary="Buscar clientes por nombre",
    description="Busca clientes que contengan el texto especificado en su nombre."
)
async def buscar_clientes_por_nombre(
    query: str,
    db: Session = Depends(get_db)
):
    """
    Busca clientes por nombre.

    - **query**: Texto a buscar en el nombre

    Returns:
        List[ClienteResponse]: Clientes que coinciden
    """

    if not query or len(query) < 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La búsqueda debe tener al menos 2 caracteres"
        )

    clientes = db.query(Cliente)\
        .filter(Cliente.activo == True)\
        .filter(Cliente.nombre.ilike(f"%{query}%"))\
        .all()

    return clientes


# ========================================
# ENDPOINT: BUSCAR CLIENTE POR EMAIL
# ========================================
@router.get(
    "/buscar/email/{email}",
    response_model=ClienteResponse,
    summary="Buscar cliente por email",
    description="Busca un cliente por su dirección de email."
)
async def buscar_cliente_por_email(
    email: str,
    db: Session = Depends(get_db)
):
    """
    Busca un cliente por email.

    - **email**: Email del cliente a buscar

    Returns:
        ClienteResponse: Cliente encontrado

    Raises:
        HTTPException 404: Si no se encuentra el cliente
    """

    cliente = db.query(Cliente)\
        .filter(Cliente.email == email)\
        .filter(Cliente.activo == True)\
        .first()

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontró un cliente con el email '{email}'"
        )

    return cliente
