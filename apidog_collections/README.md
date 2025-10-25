# 📁 Colecciones de ApiDog para API FUMC

Esta carpeta contiene las colecciones de API pre-configuradas para **ApiDog**.

> 💡 **¿Prefieres Postman?** También hay colecciones en la carpeta `postman_collections/`

## 📦 Archivos Incluidos

1. **01_Productos.json** - 7 endpoints para gestionar productos
   - ✅ Crear producto
   - ✅ Listar productos (con y sin filtros)
   - ✅ Obtener producto por ID
   - ✅ Buscar por nombre
   - ✅ Actualizar producto
   - ✅ Eliminar producto (lógico)

2. **02_Clientes.json** - 9 endpoints para gestionar clientes
   - ✅ Crear cliente
   - ✅ Listar clientes (con y sin filtros)
   - ✅ Obtener cliente por ID
   - ✅ Buscar por email
   - ✅ Buscar por nombre
   - ✅ Filtrar por ciudad
   - ✅ Actualizar cliente
   - ✅ Eliminar cliente (lógico)

3. **03_Auditoria.json** - 5 endpoints para consultar auditoría
   - ✅ Listar todo el historial
   - ✅ Historial de un grupo
   - ✅ Historial de una tabla
   - ✅ Historial por tipo de operación
   - ✅ Historial de un registro específico

---

## 🚀 Cómo Importar en ApiDog

### Opción 1: Importar Archivo JSON

1. Abre **ApiDog**
2. Ve a tu proyecto o crea uno nuevo
3. Haz clic en **"Import"** (Importar)
4. Selecciona **"Import from file"** (Importar desde archivo)
5. Busca y selecciona uno de los archivos `.json` de esta carpeta
6. Haz clic en **"Import"** (Importar)
7. **Repite** para los otros 2 archivos JSON

### Opción 2: Importar Todos a la Vez

1. Selecciona los 3 archivos `.json` a la vez
2. Arrástralos a la ventana de ApiDog
3. ApiDog importará las 3 colecciones automáticamente

---

## 🚀 Cómo Importar en Postman

> ℹ️ **Nota**: Si usas Postman, te recomendamos usar las colecciones de la carpeta `postman_collections/` que están específicamente optimizadas para Postman.

También puedes importar estos archivos en **Postman**:

1. Abre **Postman**
2. Haz clic en **"Import"** (esquina superior izquierda)
3. Arrastra los archivos `.json` o selecciónalos manualmente
4. Haz clic en **"Import"**

---

## ✅ Verificar la Importación

Después de importar, deberías ver:

```
📂 API FUMC - Productos (7 requests)
   ├── 1️⃣ Crear Producto
   ├── 2️⃣ Listar Productos (Todos)
   ├── 3️⃣ Listar Productos (Con Filtros)
   ├── 4️⃣ Obtener Producto por ID
   ├── 5️⃣ Buscar Productos por Nombre
   ├── 6️⃣ Actualizar Producto
   └── 7️⃣ Eliminar Producto (Lógico)

📂 API FUMC - Clientes (9 requests)
   ├── 1️⃣ Crear Cliente
   ├── 2️⃣ Listar Clientes (Todos)
   ├── 3️⃣ Listar Clientes (Con Filtros)
   ├── 4️⃣ Obtener Cliente por ID
   ├── 5️⃣ Buscar Cliente por Email
   ├── 6️⃣ Buscar Clientes por Nombre
   ├── 7️⃣ Listar Clientes por Ciudad
   ├── 8️⃣ Actualizar Cliente
   └── 9️⃣ Eliminar Cliente (Lógico)

📂 API FUMC - Auditoría (5 requests)
   ├── 1️⃣ Listar Todo el Historial
   ├── 2️⃣ Historial de un Grupo
   ├── 3️⃣ Historial de una Tabla
   ├── 4️⃣ Historial por Tipo de Operación
   └── 5️⃣ Historial de un Registro Específico
```

---

## 🔧 Configuración Inicial

Todas las colecciones están pre-configuradas para:

- **URL Base**: `http://localhost:8000`
- **Puerto**: `8000` (el puerto por defecto de la API)

### ⚠️ Si tu API usa otro puerto:

1. En ApiDog/Postman, ve a cada colección
2. Haz clic en **"Edit"** (Editar)
3. En **"Variables"** o directamente en cada request
4. Cambia `localhost:8000` por tu URL/puerto

**Ejemplo**: Si tu API corre en el puerto 9000:
- Cambia `http://localhost:8000` → `http://localhost:9000`

---

## 📝 Cómo Usar las Colecciones

### 1️⃣ Iniciar la API

Antes de usar las colecciones, asegúrate de que la API esté corriendo:

**Opción 1 - VS Code (Recomendado)**:
- Presiona **F5** en VS Code (instala dependencias y ejecuta automáticamente)

**Opción 2 - Manual desde CMD**:
```cmd
# Activar el entorno virtual
venv\Scripts\activate.bat

# Iniciar la API
python main.py
```

### 2️⃣ Probar un Endpoint

1. Selecciona un request de la colección (ej: "Crear Producto")
2. Revisa el **body** (datos a enviar) si aplica
3. Haz clic en **"Send"** (Enviar)
4. Revisa la **respuesta** en la parte inferior

### 3️⃣ Orden Sugerido para Probar

**Para Productos:**
1. Crear Producto (POST)
2. Listar Productos (GET)
3. Obtener Producto por ID (GET)
4. Actualizar Producto (PUT)
5. Buscar por Nombre (GET)
6. Eliminar Producto (DELETE)

**Para Clientes:**
1. Crear Cliente (POST)
2. Listar Clientes (GET)
3. Obtener Cliente por ID (GET)
4. Buscar por Email (GET)
5. Actualizar Cliente (PUT)
6. Eliminar Cliente (DELETE)

**Para Auditoría:**
1. Después de hacer algunas operaciones en productos/clientes
2. Consulta el historial para ver las operaciones registradas

---

## 🎯 Ejemplos de Uso

### Crear un Producto

Request ya configurado en la colección:
```json
{
  "nombre": "Laptop HP Pavilion",
  "descripcion": "Laptop HP Pavilion 15.6 pulgadas",
  "precio": 1899000,
  "stock": 15,
  "categoria": "Electrónica",
  "imagen_url": "https://example.com/images/laptop-hp.jpg"
}
```

### Buscar Productos por Nombre

URL ya configurada:
```
GET http://localhost:8000/productos/buscar/nombre?q=laptop
```

### Ver Historial de tu Grupo

URL ya configurada (cambia `GRUPO_1` por tu grupo):
```
GET http://localhost:8000/auditoria/grupo/GRUPO_1
```

---

## ❓ Troubleshooting

### Error: "Could not send request"

**Problema**: La API no está corriendo.

**Solución**:
- Presiona **F5** en VS Code

O manualmente:
```cmd
venv\Scripts\activate.bat
python main.py
```

### Error: "Connection refused"

**Problema**: Puerto incorrecto.

**Solución**: Verifica el puerto en la terminal donde corre la API y actualiza las URLs en las colecciones.

### Error 404 en todos los endpoints

**Problema**: URL base incorrecta.

**Solución**: Asegúrate de que la URL sea `http://localhost:8000` (sin `s` en http).

---

## 💡 Tips para Estudiantes

1. **Lee las descripciones**: Cada request tiene una descripción detallada de qué hace
2. **Experimenta**: Cambia los valores en el body y observa las respuestas
3. **Prueba los errores**: Intenta enviar datos inválidos para ver cómo responde la API
4. **Usa Auditoría**: Consulta el historial para ver cómo se registran tus operaciones
5. **Comparte**: Puedes exportar estas colecciones y compartirlas con tus compañeros

---

## 📚 Recursos Adicionales

- **Documentación Interactiva**: `http://localhost:8000/docs`
- **README Principal**: `../README.md`
- **Código Fuente**: `../app/`

---

## ✉️ Soporte

Si tienes dudas sobre cómo usar estas colecciones:

1. Consulta el **README.md** principal del proyecto
2. Revisa la documentación interactiva en `/docs`
3. Consulta con tu instructor

---

**¡Listo para probar la API! 🚀**
