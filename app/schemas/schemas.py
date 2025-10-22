"""
========================================
SCHEMAS DE PYDANTIC
========================================
Los schemas definen la estructura de datos que entran y salen de la API.
Pydantic se encarga de validar automáticamente que los datos cumplan
con las reglas definidas aquí.
"""

from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import datetime
from decimal import Decimal


# ========================================
# SCHEMAS PARA PRODUCTOS
# ========================================

class ProductoBase(BaseModel):
    """
    Schema base con los campos comunes de Producto.
    Otros schemas heredan de este.
    """
    nombre: str = Field(
        ...,  # ... significa que es obligatorio
        min_length=3,
        max_length=200,
        description="Nombre del producto",
        example="Laptop HP Pavilion 15"
    )
    descripcion: Optional[str] = Field(
        None,  # None = opcional
        max_length=2000,
        description="Descripción detallada del producto",
        example="Laptop con procesador Intel Core i5, 8GB RAM, 256GB SSD"
    )
    precio: Decimal = Field(
        ...,
        gt=0,  # Greater than (mayor que) 0
        decimal_places=2,
        description="Precio en pesos colombianos",
        example=1500000.00
    )
    stock: int = Field(
        default=0,
        ge=0,  # Greater or equal (mayor o igual) a 0
        description="Cantidad disponible en inventario",
        example=10
    )
    categoria: Optional[str] = Field(
        None,
        max_length=100,
        description="Categoría del producto",
        example="Electrónica"
    )
    imagen_url: Optional[str] = Field(
        None,
        max_length=500,
        description="URL de la imagen del producto",
        example="https://ejemplo.com/laptop.jpg"
    )

    @validator('precio')
    def validar_precio(cls, v):
        """
        Validación personalizada para el precio.
        Se ejecuta automáticamente cuando se crea una instancia.
        """
        if v <= 0:
            raise ValueError('El precio debe ser mayor a 0')
        if v > 999999999.99:
            raise ValueError('El precio es demasiado alto')
        return v

    @validator('nombre')
    def validar_nombre(cls, v):
        """Validación personalizada para el nombre"""
        if not v or v.strip() == '':
            raise ValueError('El nombre no puede estar vacío')
        return v.strip()  # Eliminar espacios al inicio y final


class ProductoCreate(ProductoBase):
    """
    Schema para CREAR un producto.
    Se usa en el endpoint POST /productos/

    Hereda todos los campos de ProductoBase.
    No incluye campos como 'id' porque se genera automáticamente.
    """
    pass  # No necesita campos adicionales


class ProductoUpdate(BaseModel):
    """
    Schema para ACTUALIZAR un producto.
    Se usa en el endpoint PUT /productos/{id}

    Todos los campos son opcionales, así el grupo puede actualizar
    solo los campos que necesite sin tener que enviar todos.
    """
    nombre: Optional[str] = Field(None, min_length=3, max_length=200)
    descripcion: Optional[str] = Field(None, max_length=2000)
    precio: Optional[Decimal] = Field(None, gt=0, decimal_places=2)
    stock: Optional[int] = Field(None, ge=0)
    categoria: Optional[str] = Field(None, max_length=100)
    imagen_url: Optional[str] = Field(None, max_length=500)
    activo: Optional[bool] = None  # Permite activar/desactivar el producto


class ProductoResponse(ProductoBase):
    """
    Schema para las RESPUESTAS de la API que incluyen productos.
    Incluye todos los campos de la base de datos, incluyendo auditoría.
    """
    id: int
    activo: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    grupo_creador: str
    grupo_ultima_modificacion: Optional[str] = None

    class Config:
        """
        Configuración de Pydantic.
        orm_mode permite que Pydantic lea datos directamente
        de los objetos de SQLAlchemy.
        """
        from_attributes = True  # Antes era 'orm_mode' en Pydantic v1


# ========================================
# SCHEMAS PARA CLIENTES
# ========================================

class ClienteBase(BaseModel):
    """Schema base con los campos comunes de Cliente"""
    nombre: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Nombre completo del cliente",
        example="Juan Pérez García"
    )
    email: EmailStr = Field(  # EmailStr valida automáticamente el formato de email
        ...,
        description="Correo electrónico del cliente",
        example="juan.perez@example.com"
    )
    telefono: Optional[str] = Field(
        None,
        max_length=20,
        description="Número de teléfono",
        example="+57 300 123 4567"
    )
    direccion: Optional[str] = Field(
        None,
        max_length=500,
        description="Dirección de entrega",
        example="Calle 123 #45-67, Apto 801"
    )
    ciudad: Optional[str] = Field(
        None,
        max_length=100,
        description="Ciudad de residencia",
        example="Medellín"
    )
    documento: Optional[str] = Field(
        None,
        max_length=20,
        description="Número de documento de identidad",
        example="1234567890"
    )

    @validator('nombre')
    def validar_nombre_cliente(cls, v):
        """Validación del nombre del cliente"""
        if not v or v.strip() == '':
            raise ValueError('El nombre no puede estar vacío')
        return v.strip()

    @validator('documento')
    def validar_documento(cls, v):
        """Validación del documento"""
        if v and not v.replace(' ', '').replace('-', '').isdigit():
            raise ValueError('El documento debe contener solo números')
        return v


class ClienteCreate(ClienteBase):
    """
    Schema para CREAR un cliente.
    Se usa en el endpoint POST /clientes/
    """
    pass


class ClienteUpdate(BaseModel):
    """
    Schema para ACTUALIZAR un cliente.
    Todos los campos opcionales.
    """
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=20)
    direccion: Optional[str] = Field(None, max_length=500)
    ciudad: Optional[str] = Field(None, max_length=100)
    documento: Optional[str] = Field(None, max_length=20)
    activo: Optional[bool] = None


class ClienteResponse(ClienteBase):
    """
    Schema para las respuestas de la API que incluyen clientes.
    """
    id: int
    activo: bool
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    grupo_creador: str
    grupo_ultima_modificacion: Optional[str] = None

    class Config:
        from_attributes = True


# ========================================
# SCHEMAS PARA AUDITORÍA
# ========================================

class AuditoriaResponse(BaseModel):
    """
    Schema para consultar el historial de auditoría.
    """
    id: int
    tabla_afectada: str
    id_registro: int
    operacion: str  # CREATE, UPDATE, DELETE
    grupo_responsable: str
    datos_anteriores: Optional[str] = None
    datos_nuevos: Optional[str] = None
    fecha_operacion: datetime
    observaciones: Optional[str] = None

    class Config:
        from_attributes = True


# ========================================
# SCHEMAS AUXILIARES
# ========================================

class MensajeResponse(BaseModel):
    """Schema para respuestas simples con mensajes"""
    mensaje: str
    detalle: Optional[str] = None


class ErrorResponse(BaseModel):
    """Schema para respuestas de error"""
    error: str
    detalle: Optional[str] = None
    codigo: Optional[int] = None
