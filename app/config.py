"""
========================================
CONFIGURACIÓN DE LA APLICACIÓN
========================================
Este archivo maneja la configuración de la aplicación,
incluyendo las credenciales de la base de datos y
el nombre del grupo de estudiantes.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Clase que define todas las configuraciones de la aplicación.

    Pydantic leerá automáticamente las variables del archivo .env
    y las asignará a estos atributos.
    """

    # ========================================
    # CONFIGURACIÓN DE BASE DE DATOS
    # ========================================

    DB_HOST: str  # Dirección del servidor de base de datos
    DB_PORT: int = 5432  # Puerto de PostgreSQL (5432 es el predeterminado)
    DB_NAME: str  # Nombre de la base de datos
    DB_USER: str  # Usuario de la base de datos
    DB_PASSWORD: str  # Contraseña del usuario

    # ========================================
    # IDENTIFICACIÓN DEL GRUPO
    # ========================================

    GRUPO_ESTUDIANTES: str = "GRUPO_1"  # Nombre del grupo que usa la API

    class Config:
        """
        Configuración adicional de Pydantic.
        Le indica que lea las variables desde el archivo .env
        """
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def database_url(self) -> str:
        """
        Construye la URL de conexión a PostgreSQL.

        Formato: postgresql://usuario:contraseña@host:puerto/nombre_bd

        Returns:
            str: URL completa de conexión a la base de datos
        """
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


# ========================================
# INSTANCIA GLOBAL DE CONFIGURACIÓN
# ========================================
# Esta instancia se importará en otros archivos para acceder a la configuración
settings = Settings()
