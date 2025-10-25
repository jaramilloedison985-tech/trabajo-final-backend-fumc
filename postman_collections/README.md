# 📮 Colecciones para Postman

Esta carpeta contiene las colecciones de la API FUMC en formato **Postman v2.1.0**, listas para importar directamente en **Postman**.

## 📦 Archivos Disponibles

| Archivo | Descripción | Endpoints |
|---------|-------------|-----------|
| `01_Productos.json` | Gestión de productos de la tienda | 7 endpoints |
| `02_Clientes.json` | Gestión de clientes | 9 endpoints |
| `03_Auditoria.json` | Consulta de historial de auditoría | 5 endpoints |

## 🚀 Cómo Importar en Postman

### Método 1: Importación Directa
1. Abre **Postman**
2. Haz clic en el botón **"Import"** (esquina superior izquierda)
3. Arrastra y suelta los archivos `.json` o haz clic en **"Upload Files"**
4. Selecciona los archivos que quieras importar
5. Haz clic en **"Import"**

### Método 2: Desde el Menú
1. En Postman, ve a **File → Import**
2. Selecciona la pestaña **"File"**
3. Navega hasta esta carpeta `postman_collections`
4. Selecciona los archivos `.json`
5. Confirma la importación

## ✅ Verificación

Después de importar, deberías ver 3 nuevas colecciones en tu sidebar de Postman:
- ✅ **API FUMC - Productos**
- ✅ **API FUMC - Clientes**
- ✅ **API FUMC - Auditoría**

## 🔧 Configuración

Antes de usar las colecciones, asegúrate de:

1. **Tener el servidor corriendo:**
   ```bash
   python main.py
   ```
   El servidor debe estar activo en `http://localhost:8000`

2. **Verificar que la base de datos esté inicializada:**
   - Consulta el archivo `INICIO_RAPIDO.md` para instrucciones de configuración

## 📝 Compatibilidad

Estas colecciones son compatibles con:
- ✅ **Postman** (Desktop y Web)
- ✅ **Apidog** (también disponibles en la carpeta `apidog_collections`)
- ✅ Cualquier cliente HTTP que soporte formato Postman v2.1.0

## 🆚 Diferencia con Apidog Collections

Ambas carpetas (`postman_collections` y `apidog_collections`) contienen **el mismo contenido** en formato compatible con ambas herramientas:

- **`postman_collections/`** ← Esta carpeta (diseñada para Postman)
- **`apidog_collections/`** ← Mismas colecciones (diseñadas para Apidog)

Puedes usar cualquiera de las dos dependiendo de tu herramienta preferida.

## 💡 Ayuda

Si tienes problemas al importar las colecciones:
1. Verifica que estás usando **Postman v8 o superior**
2. Asegúrate de que los archivos `.json` no estén corruptos
3. Consulta la documentación oficial de Postman: https://learning.postman.com/docs/getting-started/importing-and-exporting-data/

---

**Hecho con ❤️ para estudiantes de FUMC**
