# 🚀 INICIO RÁPIDO - Para Estudiantes

> **¿Primera vez con este proyecto?** Sigue estos pasos simples.

---

## 📋 Requisitos Previos

Antes de empezar, asegúrate de tener instalado:

1. ✅ **Python 3.8 o superior** - https://www.python.org/downloads/
   - ⚠️ Al instalar, marca la opción "Add Python to PATH"
   
2. ✅ **Git** - https://git-scm.com/downloads

3. ✅ **VS Code** - https://code.visualstudio.com/

4. ✅ **Extensión de Python para VS Code**
   - Abre VS Code → Extensions (Ctrl+Shift+X) → Busca "Python" → Instala

---

## ⚡ Configuración Inicial (Solo UNA vez)

### 1️⃣ Descargar el Proyecto

```cmd
# Abre Command Prompt (CMD) y ejecuta:

# Clonar el repositorio
git clone https://github.com/heldigard/trabajo-final-backend-fumc.git

# Entrar a la carpeta
cd trabajo-final-backend-fumc
```

### 2️⃣ Crear Entorno Virtual

```cmd
# Crear el entorno virtual (solo la primera vez)
python -m venv venv
```

**⚙️ NOTA IMPORTANTE**: Este proyecto está configurado para usar **Command Prompt (CMD)** porque el entorno virtual se activa mejor con `activate.bat` en los equipos de los estudiantes.

### 3️⃣ Configurar Variables de Entorno

```cmd
# Copiar el archivo de ejemplo
copy .env.example .env
```

Ahora **edita el archivo `.env`** y cambia `GRUPO_ESTUDIANTES`:

```env
# ⚠️ IMPORTANTE: Cambia GRUPO_1 por el nombre de tu grupo
GRUPO_ESTUDIANTES=GRUPO_1  # ← Cámbialo a GRUPO_2, GRUPO_3, etc.
```

**Los demás valores ya vienen configurados**, revisa `DB_PASSWORD=`.
Solo verifica que esa contraseña NO quede en blanco y recuerda no compartirla públicamente.

### 4️⃣ Abrir en VS Code

```cmd
# Abre el proyecto en VS Code
code .
```

---

## 🎯 Ejecutar la API (Cada vez que trabajes)

### ✨ MÉTODO SIMPLE (Recomendado)

1. Abre VS Code con el proyecto
2. **Presiona `F5`** (o ve a `Run → Start Debugging`)
3. Espera unos segundos...
4. ¡Listo! La API está corriendo

**VS Code automáticamente**:
- ✅ Instala las librerías que falten
- ✅ Inicia la API
- ✅ Todo sin que escribas ningún comando

**💡 TIP**: La primera vez puede tardar 1-2 minutos instalando librerías. Las siguientes veces será casi instantáneo.

### 🌐 Verificar que Funciona

Abre tu navegador y visita:

**http://localhost:8000/docs**

Deberías ver una interfaz como esta:

```
FastAPI
API Tienda Virtual - FUMC

Docs  /docs
Endpoints
  ▼ productos
  ▼ clientes
  ▼ auditoria
```

Si ves eso, **¡FELICIDADES!** ✅ Tu API está funcionando.

---

## 📱 Probar la API

Tienes **3 opciones** para probar los endpoints:

### Opción 1: Swagger UI (Más Fácil)

1. Abre: http://localhost:8000/docs
2. Haz clic en un endpoint (ej: `POST /productos/`)
3. Click en "Try it out"
4. Llena los datos
5. Click en "Execute"
6. Ve la respuesta

### Opción 2: ApiDog (Recomendado)

1. **Instala ApiDog**: https://apidog.com/
2. **Importa las colecciones**:
   - Abre ApiDog
   - Click en "Import"
   - Selecciona los archivos de la carpeta `apidog_collections/`:
     - `01_Productos.json`
     - `02_Clientes.json`
     - `03_Auditoria.json`
3. **Probar**:
   - Selecciona un endpoint
   - Click en "Send"
   - Ve la respuesta

**📚 Guía Detallada**: Lee `apidog_collections/README.md`

### Opción 3: Postman

1. **Instala Postman**: https://www.postman.com/downloads/
2. Importa los mismos archivos JSON de `apidog_collections/`
3. Usa igual que ApiDog

---

## 🆘 Solución de Problemas Comunes

### ❌ Error: "ModuleNotFoundError: No module named 'fastapi'"

**Solución Simple**:
- Presiona `F5` de nuevo
- VS Code instalará automáticamente lo que falta

**Solución Manual (si es necesario)**:
```cmd
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### ❌ Error al activar el entorno virtual

**Si usas CMD** (recomendado):
```cmd
venv\Scripts\activate.bat
```

**Si usas PowerShell** y aparece error de permisos:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### ❌ Error: "Puerto 8000 ya está en uso"

**Solución**:
```cmd
# Ver qué proceso usa el puerto
netstat -ano | findstr :8000

# Detener el proceso (reemplaza <PID> con el número que aparece)
taskkill /PID <PID> /F
```

### ❌ La API no responde o hay errores raros

**Solución**:
1. Detén la API (click en el cuadrado rojo en VS Code)
2. `Ctrl+Shift+P`
3. Escribe "Tasks: Run Task"
4. Selecciona "Limpiar Cache Python"
5. Presiona `F5` de nuevo

### ❌ No puedo conectarme a la base de datos

**Verificar**:
1. Tienes conexión a internet
2. El archivo `.env` tiene el nombre correcto de tu grupo en `GRUPO_ESTUDIANTES`
3. No cambiaste las demás variables del `.env`

---

## 📚 Documentación Adicional

- **README Completo**: `README.md` (documentación detallada)
- **Guía ApiDog**: `apidog_collections/README.md`
- **Cambios Recientes**: `CAMBIOS_REALIZADOS.md`

---

## 🎓 Flujo de Trabajo Típico

```
1. Abrir VS Code
   ↓
2. Presionar F5
   ↓
3. Esperar a que inicie la API (10-30 segundos)
   ↓
4. Abrir http://localhost:8000/docs O usar ApiDog
   ↓
5. Probar endpoints
   ↓
6. Modificar código si es necesario
   ↓
7. Guardar (Ctrl+S)
   ↓
8. Los cambios se reflejan automáticamente
   ↓
9. Cuando termines: Detener API (cuadrado rojo en VS Code)
```

---

## ✅ Checklist de Primer Uso

Marca cada paso que completes:

- [ ] Python instalado (verifica: `python --version`)
- [ ] Git instalado (verifica: `git --version`)
- [ ] VS Code instalado con extensión de Python
- [ ] Proyecto clonado desde GitHub
- [ ] Entorno virtual creado (`venv` folder existe)
- [ ] Archivo `.env` creado y configurado con tu grupo
- [ ] Primera ejecución con F5 exitosa
- [ ] Swagger UI abierto en http://localhost:8000/docs
- [ ] ApiDog instalado (opcional pero recomendado)
- [ ] Colecciones importadas en ApiDog
- [ ] Primer endpoint probado exitosamente

---

## 🎯 Próximos Pasos

Una vez que tu API esté corriendo:

1. **Lee los modelos** para entender la estructura:
   - `app/models/producto.py` - Tabla de productos
   - `app/models/cliente.py` - Tabla de clientes
   - `app/models/auditoria.py` - Sistema de auditoría

2. **Prueba todos los endpoints** usando ApiDog o Swagger UI

3. **Experimenta**:
   - Crea productos
   - Crea clientes
   - Consulta el historial de auditoría
   - Ve cómo queda registrado tu grupo en cada operación

4. **Aprende** leyendo el código con los comentarios

---

## 💡 Tips Importantes

1. **No necesitas escribir comandos de terminal** - VS Code hace todo con F5
2. **La base de datos ya está lista** - NO ejecutes scripts SQL
3. **Todos los grupos comparten la misma BD** - Por eso es importante que cada grupo tenga un nombre único
4. **Los emails y documentos son únicos** - No puede haber dos clientes con el mismo email en TODA la base de datos
5. **El sistema de auditoría registra TODO** - Cada operación queda registrada con el nombre de tu grupo

---

## 🆘 ¿Necesitas Ayuda?

1. **Revisa la sección de troubleshooting arriba** ☝️
2. **Lee el README completo** (`README.md`)
3. **Consulta con tus compañeros de grupo**
4. **Pregunta al instructor**

---

**¡Buena suerte con tu proyecto! 🚀**
