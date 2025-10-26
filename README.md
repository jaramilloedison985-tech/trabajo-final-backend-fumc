# 🛒 API de Tienda Virtual - FUMC Backend

> **Proyecto Final del Curso**: Frameworks para desarrollo web - Backend  
> **Institución**: Fundación Universitaria María Cano (FUMC)  
> **Fecha**: Octubre 2025

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [🎯 Retos y Evaluación](#-retos-y-evaluación-del-proyecto)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Características](#-características)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Ejecutar la API](#-ejecutar-la-api)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Endpoints Disponibles](#-endpoints-disponibles)
- [Base de Datos](#-base-de-datos)
- [Sistema de Auditoría](#-sistema-de-auditoría)
- [Trabajo en Grupos](#-trabajo-en-grupos)
- [Documentación Interactiva](#-documentación-interactiva)
- [Solución de Problemas](#-solución-de-problemas)

---

## 📖 Descripción

API REST completa para una **Tienda Virtual** que permite:

- ✅ Gestionar **productos** (crear, listar, actualizar, eliminar)
- ✅ Gestionar **clientes** (CRUD completo)
- ✅ **Sistema de auditoría** que registra todas las operaciones
- ✅ **Eliminación lógica** (soft delete) - los datos no se borran físicamente
- ✅ **Trazabilidad por grupos** - cada operación queda registrada con el nombre del grupo que la realizó

⚠️ **IMPORTANTE**: Esta API está diseñada para que **TODOS los grupos de estudiantes trabajen en LA MISMA base de datos** ubicada en `postgres.corvitmedellin.com`. Cada grupo se identifica mediante su nombre de grupo configurado en el archivo `.env` (`GRUPO_ESTUDIANTES`), pero **todos comparten la misma base de datos `fumc_db`**. Esto significa que:
- Todos los grupos pueden ver los productos/clientes creados por otros grupos
- El sistema de auditoría registra qué grupo creó/modificó cada registro
- Los emails y documentos de clientes deben ser únicos en TODA la base de datos (compartida entre todos los grupos)

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.8+ | Lenguaje de programación |
| **FastAPI** | 0.109.0 | Framework para crear la API REST |
| **PostgreSQL** | 14+ | Base de datos relacional en la nube |
| **SQLAlchemy** | 2.0.25 | ORM para interactuar con la BD |
| **Pydantic** | 2.5.3 | Validación de datos |
| **Uvicorn** | 0.27.0 | Servidor ASGI para ejecutar FastAPI |

---

## ✨ Características

### 🔐 Gestión de Productos
- Crear productos con validación automática
- Listar productos con filtros (categoría, activos/inactivos)
- Buscar productos por nombre
- Actualizar productos (solo los campos necesarios)
- Eliminación lógica (el producto se marca como inactivo)

### 👥 Gestión de Clientes
- Registrar clientes con validación de email único
- Listar clientes con filtros por ciudad
- Buscar por nombre o email
- Actualizar información
- Eliminación lógica

### 📊 Sistema de Auditoría
- **Todas** las operaciones quedan registradas
- Trazabilidad completa: qué grupo hizo qué y cuándo
- Consultar historial por grupo, tabla, operación o registro específico
- Almacena datos antes y después de cada modificación

### 🎨 Características Técnicas
- **Documentación automática** con Swagger UI
- **Validación automática** de datos con Pydantic
- **Manejo de errores** con mensajes descriptivos
- **Códigos de estado HTTP** correctos
- **CORS habilitado** para consumo desde frontend

---

## 📦 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

1. **Python 3.8 o superior**
   - Descarga: https://www.python.org/downloads/
   - ⚠️ Durante la instalación en Windows: marca "Add Python to PATH"

2. **Git** (para clonar el repositorio)
   - Descarga: https://git-scm.com/downloads

3. **VS Code** (recomendado)
   - Descarga: https://code.visualstudio.com/

4. **Extensión de Python para VS Code**
   - Abre VS Code → Extensions (Ctrl+Shift+X) → Busca "Python" → Instala la de Microsoft

---

## 🚀 Instalación y Configuración

### Paso 1: Clonar el repositorio

```bash
# Clona el repositorio (reemplaza con la URL real)
git clone https://github.com/heldigard/trabajo-final-backend-fumc.git

# Entra a la carpeta del proyecto
cd trabajo-final-backend-fumc
```

### Paso 2: Crear entorno virtual

```powershell
# Crear entorno virtual
python -m venv venv
```

⚠️ **IMPORTANTE sobre la activación del entorno virtual**:

**NO necesitas activar el entorno virtual manualmente** si usas VS Code con F5.

VS Code está configurado para usar **Command Prompt (CMD)** que activa automáticamente el entorno virtual con `venv\Scripts\activate.bat`.

**Si necesitas activar manualmente** (para usar la terminal):

```cmd
# En CMD (Command Prompt) - RECOMENDADO
venv\Scripts\activate.bat
```

**Alternativa en PowerShell** (puede requerir permisos):
```powershell
# En PowerShell (solo si prefieres PowerShell)
.\venv\Scripts\Activate.ps1

# Si da error de permisos:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Nota**: Verás `(venv)` al inicio de tu terminal cuando el entorno esté activado.

### Paso 3: Instalar dependencias

**✨ AUTOMÁTICO**: Si usas VS Code y presionas **F5**, las dependencias se instalan automáticamente.

**Manual** (si prefieres instalarlas tú mismo):

```bash
# Actualizar pip (opcional pero recomendado)
python -m pip install --upgrade pip

# Instalar todas las dependencias del proyecto
pip install -r requirements.txt
```

Este comando instalará:
- FastAPI
- Uvicorn (servidor)
- SQLAlchemy (ORM)
- Psycopg2 (driver de PostgreSQL)
- Pydantic (validación)
- Python-dotenv (variables de entorno)

⚠️ **NOTA**: Si usas el método de VS Code (F5), **salta este paso**. Las dependencias se instalarán automáticamente la primera vez que ejecutes la API.

### Paso 4: Configurar variables de entorno

1. **Copia el archivo de ejemplo**:
   ```cmd
   # Windows CMD (Command Prompt)
   copy .env.example .env
   
   # O en PowerShell
   Copy-Item .env.example .env
   ```

2. **Edita el archivo `.env`** con tus datos:
   ```env
   # Configuración de la base de datos (NO CAMBIAR)
   DB_HOST=postgres.corvitmedellin.com
   DB_PORT=5432
   DB_NAME=fumc_db
   DB_USER=fumc_user
   DB_PASSWORD=

   # ⚠️ IMPORTANTE: Cambia esto por el nombre de tu grupo
   GRUPO_ESTUDIANTES=GRUPO_1
   ```

   **Cada grupo debe poner su nombre único**: `GRUPO_1`, `GRUPO_2`, `GRUPO_3`, etc.

### Paso 5: Base de datos ya inicializada ✅

**✅ La base de datos ya está lista para usar.**

El instructor ya ha ejecutado el script `scripts/init_db.sql` que:
- Creó las tablas necesarias (`productos`, `clientes`, `historial_auditoria`)
- Cargó datos de ejemplo (27 productos, 15 clientes)
- Configuró índices y triggers

**NO necesitas ejecutar ningún script SQL**. Solo asegúrate de configurar correctamente tu archivo `.env` con el nombre de tu grupo.

📝 **Nota**: El script SQL está en `scripts/init_db.sql` solo como referencia para que veas cómo se creó la base de datos.

---

## ▶️ Ejecutar la API

### Opción 1: Con VS Code (⭐ RECOMENDADO Y AUTOMATIZADO)

**✨ TODO ES AUTOMÁTICO - Solo presiona F5**

1. **Abre el proyecto en VS Code**:
   ```bash
   code .
   ```

2. **Presiona `F5`** o ve a `Run → Start Debugging`

3. **Selecciona** la configuración **"🚀 FastAPI - Tienda Virtual"**

4. **VS Code automáticamente**:
   - ✅ Verifica que pip esté actualizado
   - ✅ Instala todas las dependencias de `requirements.txt`
   - ✅ Inicia la API en modo desarrollo
   - ✅ Todo sin que tengas que escribir ningún comando

5. ¡Listo! La API estará corriendo en: **http://127.0.0.1:8000**

**🎯 VENTAJAS**:
- **No necesitas ejecutar `pip install`** manualmente
- **No necesitas activar el entorno virtual** manualmente
- **No necesitas escribir comandos** en la terminal
- Si faltan dependencias, se instalan automáticamente
- Si ya están instaladas, el proceso es muy rápido (solo verifica)

**💡 TIP**: La primera vez puede tardar un poco instalando las dependencias. Las siguientes veces será casi instantáneo.

**⚙️ CONFIGURACIÓN IMPORTANTE**: VS Code está configurado para usar **Command Prompt (CMD)** en lugar de PowerShell, ya que el entorno virtual se activa mejor con `activate.bat` en los equipos de los estudiantes.

### Opción 2: Desde la terminal (Manual)

Si prefieres hacerlo manualmente:

```cmd
# === USANDO CMD (RECOMENDADO) ===

# 1. Asegúrate de tener el entorno virtual activado
venv\Scripts\activate.bat

# 2. Instala dependencias (solo la primera vez)
pip install -r requirements.txt

# 3. Ejecutar con Uvicorn
uvicorn main:app --reload

# O ejecutar main.py directamente
python main.py
```

**Alternativa en PowerShell**:
```powershell
# 1. Activar entorno (puede requerir permisos)
.\venv\Scripts\Activate.ps1

# 2-3. (Mismo que arriba)
```

### Verificar que funciona

Abre tu navegador y visita:

- **API raíz**: http://127.0.0.1:8000/
- **Documentación interactiva**: http://127.0.0.1:8000/docs
- **Documentación alternativa**: http://127.0.0.1:8000/redoc
- **Health check**: http://127.0.0.1:8000/health

---

## 📁 Estructura del Proyecto

```
trabajo-final-backend-fumc/
│
├── app/                          # Código principal de la aplicación
│   ├── models/                   # Modelos de base de datos (SQLAlchemy)
│   │   ├── __init__.py          # Importa todos los modelos
│   │   ├── producto.py          # Modelo Producto (tabla productos)
│   │   ├── cliente.py           # Modelo Cliente (tabla clientes)
│   │   └── auditoria.py         # Modelo HistorialAuditoria
│   │
│   ├── schemas/                  # Esquemas de validación (Pydantic)
│   │   ├── __init__.py
│   │   └── schemas.py            # ProductoCreate, ClienteResponse, etc.
│   │
│   ├── routers/                  # Endpoints organizados por módulo
│   │   ├── __init__.py
│   │   ├── productos.py          # CRUD de productos
│   │   ├── clientes.py           # CRUD de clientes
│   │   └── auditoria.py          # Consultas de auditoría
│   │
│   ├── __init__.py
│   ├── config.py                 # Configuración (lee .env)
│   └── database.py               # Conexión a PostgreSQL
│
├── apidog_collections/           # 🆕 Colecciones para ApiDog
│   ├── 01_Productos.json        # Endpoints de productos
│   ├── 02_Clientes.json         # Endpoints de clientes
│   ├── 03_Auditoria.json        # Endpoints de auditoría
│   └── README.md                # Guía de uso de las colecciones
│
├── postman_collections/          # 🆕 Colecciones para Postman
│   ├── 01_Productos.json        # Endpoints de productos
│   ├── 02_Clientes.json         # Endpoints de clientes
│   ├── 03_Auditoria.json        # Endpoints de auditoría
│   └── README.md                # Guía de uso de las colecciones
│
├── scripts/                      # Scripts SQL
│   └── init_db.sql              # Inicializa BD con datos de ejemplo
│
├── .vscode/                      # Configuración de VS Code
│   ├── launch.json              # Para ejecutar con F5
│   └── settings.json            # Configuración del editor
│
├── main.py                       # Archivo principal de la API
├── requirements.txt              # Dependencias de Python
├── .env.example                  # Ejemplo de variables de entorno
├── .env                          # TUS variables (NO subir a Git)
├── .gitignore                    # Archivos ignorados por Git
└── README.md                     # Este archivo
```

### 💡 Notas sobre la Estructura

- **`app/models/`**: Los modelos están **divididos en archivos separados** para facilitar la comprensión. Cada archivo representa UNA tabla de la base de datos.
- **`apidog_collections/`**: Contiene colecciones pre-configuradas con **todos los endpoints** listos para importar en ApiDog o Postman. Esto facilita probar la API sin escribir requests manualmente.

---

## 🌐 Endpoints Disponibles

### 📦 Productos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/productos/` | Listar todos los productos |
| `GET` | `/productos/{id}` | Obtener un producto específico |
| `POST` | `/productos/` | Crear un nuevo producto |
| `PUT` | `/productos/{id}` | Actualizar un producto |
| `DELETE` | `/productos/{id}` | Eliminar producto (lógico) |
| `GET` | `/productos/buscar/nombre?query=...` | Buscar por nombre |

### 👥 Clientes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/clientes/` | Listar todos los clientes |
| `GET` | `/clientes/{id}` | Obtener un cliente específico |
| `POST` | `/clientes/` | Crear un nuevo cliente |
| `PUT` | `/clientes/{id}` | Actualizar un cliente |
| `DELETE` | `/clientes/{id}` | Eliminar cliente (lógico) |
| `GET` | `/clientes/buscar/nombre?query=...` | Buscar por nombre |
| `GET` | `/clientes/buscar/email/{email}` | Buscar por email |

### 📊 Auditoría

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/auditoria/` | Historial completo |
| `GET` | `/auditoria/grupo/{nombre}` | Operaciones de un grupo |
| `GET` | `/auditoria/tabla/{tabla}` | Operaciones en una tabla |
| `GET` | `/auditoria/operacion/{tipo}` | Por tipo (CREATE/UPDATE/DELETE) |
| `GET` | `/auditoria/registro/{tabla}/{id}` | Historial de un registro |

---

## 💾 Base de Datos

### Conexión

La base de datos está alojada en la nube:

- **Host**: `postgres.corvitmedellin.com:5432`
- **Base de datos**: `fumc_db`
- **Usuario**: `fumc_user`
- **Contraseña**: ``

### Tablas

#### `productos`
```sql
- id (serial primary key)
- nombre (varchar 200) NOT NULL
- descripcion (text)
- precio (numeric 10,2) NOT NULL
- stock (integer) DEFAULT 0
- categoria (varchar 100)
- imagen_url (varchar 500)
- activo (boolean) DEFAULT TRUE
- fecha_creacion (timestamp)
- fecha_actualizacion (timestamp)
- grupo_creador (varchar 50)
- grupo_ultima_modificacion (varchar 50)
```

#### `clientes`
```sql
- id (serial primary key)
- nombre (varchar 100) NOT NULL
- email (varchar 150) UNIQUE NOT NULL
- telefono (varchar 20)
- direccion (text)
- ciudad (varchar 100)
- documento (varchar 20) UNIQUE
- activo (boolean) DEFAULT TRUE
- fecha_creacion (timestamp)
- fecha_actualizacion (timestamp)
- grupo_creador (varchar 50)
- grupo_ultima_modificacion (varchar 50)
```

#### `historial_auditoria`
```sql
- id (serial primary key)
- tabla_afectada (varchar 50)
- id_registro (integer)
- operacion (varchar 20) - CREATE/UPDATE/DELETE
- grupo_responsable (varchar 50)
- datos_anteriores (text) - JSON
- datos_nuevos (text) - JSON
- fecha_operacion (timestamp)
- observaciones (text)
```

---

## 🔍 Sistema de Auditoría

Cada vez que un grupo realiza una operación (crear, actualizar, eliminar), se registra automáticamente:

- ✅ Qué grupo lo hizo
- ✅ Qué operación realizó (CREATE/UPDATE/DELETE)
- ✅ En qué tabla y registro
- ✅ Cuándo lo hizo (fecha y hora)
- ✅ Qué datos cambió (antes y después)

### Ejemplo de consulta de auditoría

**Ver qué hizo mi grupo**:
```
GET /auditoria/grupo/GRUPO_1
```

**Ver todas las operaciones en productos**:
```
GET /auditoria/tabla/productos
```

**Ver historial de un producto específico**:
```
GET /auditoria/registro/productos/5
```

---

## 👥 Trabajo en Grupos

### Configuración de Grupo

1. **Cada grupo** debe tener un nombre único en `.env`:
   ```env
   GRUPO_ESTUDIANTES=GRUPO_1
   ```

2. **Coordinar con otros grupos** para no usar el mismo nombre:
   - `GRUPO_1`, `GRUPO_2`, `GRUPO_3`...
   - O nombres creativos: `LOS_PROGRAMADORES`, `TEAM_BACKEND`, etc.

3. **Todas las operaciones** de tu grupo quedarán registradas con este nombre

### Buenas Prácticas

✅ **Sí hacer**:
- Crear productos propios de tu grupo
- Actualizar productos que creó tu grupo
- Experimentar con diferentes categorías
- Probar todos los endpoints

❌ **Evitar**:
- Eliminar productos de otros grupos (sin autorización)
- Usar datos ofensivos o inapropiados
- Modificar masivamente datos de otros grupos

---

## 📚 Documentación Interactiva

FastAPI genera documentación automática interactiva:

### Swagger UI (Recomendado)
**URL**: http://127.0.0.1:8000/docs

**Características**:
- Probar todos los endpoints directamente
- Ver los schemas de entrada/salida
- Ejecutar requests sin necesidad de Postman
- Ver códigos de respuesta

**Cómo usar**:
1. Abre `/docs` en tu navegador
2. Haz clic en cualquier endpoint
3. Click en "Try it out"
4. Completa los datos
5. Click en "Execute"
6. Ver la respuesta

### ReDoc
**URL**: http://127.0.0.1:8000/redoc

Documentación alternativa más enfocada en lectura.

### 🆕 ApiDog / Postman (Recomendado para estudiantes)

**¿Qué son estas herramientas?**
Son herramientas profesionales para probar APIs. Hemos creado **colecciones pre-configuradas** con TODOS los endpoints listos para usar.

**Ventajas**:
- ✅ No necesitas escribir requests manualmente
- ✅ Todos los endpoints están organizados y documentados
- ✅ Ejemplos de datos incluidos
- ✅ Fácil de usar para principiantes

**Elige tu herramienta favorita**:

| Herramienta | Carpeta | Descarga |
|-------------|---------|----------|
| 📮 **Postman** | `postman_collections/` | https://www.postman.com/downloads/ |
| 🐕 **ApiDog** | `apidog_collections/` | https://apidog.com/ |

**Cómo usar las colecciones**:

1. **Instalar tu herramienta preferida** (Postman o ApiDog)

2. **Importar las colecciones**:
   - Abre Postman o ApiDog
   - Click en "Import"
   - Busca la carpeta correspondiente:
     - `postman_collections/` para Postman
     - `apidog_collections/` para ApiDog
   - Importa los 3 archivos JSON:
     - `01_Productos.json`
     - `02_Clientes.json`
     - `03_Auditoria.json`

3. **Empezar a probar**:
   - Asegúrate de que tu API esté corriendo (F5 en VS Code)
   - Selecciona un request de la colección
   - Click en "Send"
   - ¡Listo! Ver respuesta

**📚 Guías Detalladas**:
- Para Postman: Lee `postman_collections/README.md`
- Para ApiDog: Lee `apidog_collections/README.md`

---

## 🔧 Solución de Problemas

### Problema: `ModuleNotFoundError: No module named 'fastapi'`

**Solución Automática** (Recomendada):
- Simplemente **presiona F5** de nuevo en VS Code
- El sistema instalará automáticamente las dependencias faltantes

**Solución Manual**:
```bash
# Verifica que el entorno virtual esté activado
# Debes ver (venv) al inicio de tu terminal

# Si no está activado:
.\venv\Scripts\Activate.ps1

# Instala las dependencias
pip install -r requirements.txt
```

**Verificar instalación**:
- En VS Code: `Ctrl+Shift+P` → "Tasks: Run Task" → "Listar Dependencias Instaladas"

### Problema: Las dependencias no se instalan automáticamente

**Solución**:

1. **Verificar que VS Code tiene Python configurado**:
   - `Ctrl+Shift+P` → "Python: Select Interpreter"
   - Selecciona el intérprete de `venv` (debe aparecer como `.\venv\Scripts\python.exe`)

2. **Ejecutar tarea manualmente**:
   - `Ctrl+Shift+P` → "Tasks: Run Task"
   - Seleccionar "Instalar Dependencias"

3. **Verificar entorno**:
   - `Ctrl+Shift+P` → "Tasks: Run Task"
   - Seleccionar "Verificar Entorno"
   - Debe mostrar versiones de Python y pip

### Problema: Error de conexión a PostgreSQL

**Verificar**:
1. Archivo `.env` tiene los datos correctos (especialmente `GRUPO_ESTUDIANTES`)
2. Tienes conexión a internet
3. El servidor de base de datos está disponible

**Probar conexión**:
```python
# Ejecuta en Python
from app.config import settings
print(settings.database_url)
```

### Problema: `PowerShell cannot be loaded because running scripts is disabled`

**Solución**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: Puerto 8000 ya está en uso

**Solución**:

**Opción 1**: Detener el proceso que usa el puerto:
```powershell
# Ver qué proceso usa el puerto 8000
netstat -ano | findstr :8000

# Detener el proceso (reemplaza PID con el número que aparece)
taskkill /PID <PID> /F
```

**Opción 2**: Cambiar el puerto en `launch.json`:
```json
"args": [
    "main:app",
    "--reload",
    "--host", "0.0.0.0",
    "--port", "8001"  // Cambiar a otro puerto
]
```

### Problema: Los cambios en el código no se reflejan

**Verificar**:
- El servidor está corriendo con `--reload` (automático si usas F5)
- Guardaste el archivo (Ctrl+S)
- No hay errores de sintaxis en Python

**Solución**: Reinicia el servidor (Stop + F5)

### Problema: Archivos .pyc o caché causando problemas

**Solución**:
- `Ctrl+Shift+P` → "Tasks: Run Task" → "Limpiar Cache Python"
- Esto elimina todos los archivos `__pycache__` y `.pyc`

---

## 🛠️ Tareas Útiles de VS Code

Además de ejecutar la API con F5, tienes estas tareas disponibles:

**Acceder a las tareas**:
1. Presiona `Ctrl+Shift+P`
2. Escribe "Tasks: Run Task"
3. Selecciona la tarea que necesitas

**Tareas disponibles**:

| Tarea | Descripción |
|-------|-------------|
| ✅ **Instalar Dependencias** | Instala/actualiza todas las librerías de requirements.txt |
| 🧹 **Limpiar Cache Python** | Elimina archivos __pycache__ y .pyc |
| 🔍 **Verificar Entorno** | Muestra versiones de Python y pip |
| 📦 **Listar Dependencias Instaladas** | Muestra todas las librerías instaladas |

**💡 TIP**: Estas tareas son útiles cuando tienes problemas con módulos o quieres verificar tu entorno.

---

## 📝 Ejemplos de Uso

### Crear un Producto

**Request**:
```bash
POST /productos/
Content-Type: application/json

{
  "nombre": "Laptop Dell Inspiron",
  "descripcion": "Laptop con 16GB RAM y 512GB SSD",
  "precio": 2500000,
  "stock": 5,
  "categoria": "Electrónica",
  "imagen_url": "https://ejemplo.com/laptop.jpg"
}
```

**Response** (201 Created):
```json
{
  "id": 30,
  "nombre": "Laptop Dell Inspiron",
  "descripcion": "Laptop con 16GB RAM y 512GB SSD",
  "precio": 2500000.00,
  "stock": 5,
  "categoria": "Electrónica",
  "imagen_url": "https://ejemplo.com/laptop.jpg",
  "activo": true,
  "fecha_creacion": "2025-10-22T10:30:00Z",
  "fecha_actualizacion": "2025-10-22T10:30:00Z",
  "grupo_creador": "GRUPO_1",
  "grupo_ultima_modificacion": null
}
```

### Listar Productos

**Request**:
```bash
GET /productos/?categoria=Electrónica&limit=10
```

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "nombre": "Laptop HP Pavilion 15",
    "precio": 1850000.00,
    ...
  },
  {
    "id": 2,
    "nombre": "iPhone 13 Pro Max",
    "precio": 4500000.00,
    ...
  }
]
```

---

## � Retos y Evaluación del Proyecto

Este proyecto se evalúa mediante el **sistema de auditoría** en la base de datos. NO necesitas subir código a GitHub.

### 📚 Documentos Importantes

1. **`RETOS_ESTUDIANTES.md`** - 🎯 **LEE ESTO PRIMERO**
   - Define los retos que debes completar (4 niveles)
   - Sistema de puntaje detallado (100 puntos)
   - Todas tus operaciones quedan registradas en la BD
   - La evaluación es 100% basada en auditoría

2. **`RUBRICA_EVALUACION.md`** - 📊 Para el instructor
   - Criterios de evaluación detallados
   - Queries SQL para verificar cada reto
   - Sistema de calificación objetivo

3. **`GUIA_CALIFICACION.md`** - ⚡ Para el instructor
   - Guía rápida de evaluación
   - Scripts automatizados de SQL
   - Proceso paso a paso

### 🎯 Cómo Funciona la Evaluación

1. **Configuras tu grupo** en el archivo `.env`:
   ```env
   GRUPO_ESTUDIANTES=GRUPO_1  # TU IDENTIFICADOR
   ```

2. **Realizas operaciones** usando la API:
   - Crear productos y clientes
   - Actualizar registros
   - Eliminar registros (soft delete)
   - Consultar auditoría

3. **TODO queda registrado** en la tabla `historial_auditoria`:
   - Qué grupo lo hizo
   - Qué operación (CREATE/UPDATE/DELETE)
   - Cuándo lo hizo
   - Qué datos cambió

4. **El instructor revisa la BD** y califica según los retos completados

**📖 Detalles completos en**: `RETOS_ESTUDIANTES.md`

---

## �🎓 Conceptos Aprendidos

Al completar este proyecto habrás trabajado con:

- ✅ **FastAPI**: Framework moderno de Python para APIs
- ✅ **PostgreSQL**: Base de datos relacional en producción
- ✅ **SQLAlchemy**: ORM para trabajar con BD
- ✅ **Pydantic**: Validación de datos
- ✅ **REST API**: Arquitectura de APIs web
- ✅ **CRUD**: Operaciones básicas de bases de datos
- ✅ **Git**: Control de versiones
- ✅ **Entornos virtuales**: Gestión de dependencias
- ✅ **Variables de entorno**: Configuración segura
- ✅ **Documentación automática**: OpenAPI/Swagger
- ✅ **Soft Delete**: Eliminación lógica de datos
- ✅ **Auditoría**: Trazabilidad de operaciones

---

## 🤝 Contribuciones

Si encuentras errores o tienes sugerencias:

1. Reporta el problema al instructor
2. O crea un **Issue** en GitHub (si aplica)
3. Documenta bien el problema encontrado

---

## 📧 Soporte

**Instructor**: [Nombre del instructor]  
**Email**: [email del instructor]  
**Horario de clase**: [Horarios]

---

## 📄 Licencia

Este proyecto es parte del curso de Backend en FUMC y está diseñado con fines educativos.

---

## 🎉 ¡Felicitaciones!

Si llegaste hasta aquí y tu API está funcionando:

🎊 **¡Felicitaciones!** Has creado una API REST completa con:
- Base de datos en la nube
- Sistema de auditoría
- Validación automática
- Documentación interactiva

**Próximos pasos**:
1. Prueba todos los endpoints
2. Crea productos y clientes de tu grupo
3. Consulta el historial de auditoría
4. Experimenta actualizando y eliminando datos

---

**¡Éxitos en tu proyecto final! 🚀**
