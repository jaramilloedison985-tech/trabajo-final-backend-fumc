# 🎯 RETOS DEL PROYECTO - API Tienda Virtual FUMC

> **Importante**: Este proyecto se evalúa mediante los **registros de auditoría** en la base de datos.  
> Todas las operaciones que realices quedarán registradas con el nombre de tu grupo.

---

## 📋 Información General

### ¿Cómo Funciona la Evaluación?

1. **NO necesitas subir código a GitHub** (solo clonas el repositorio)
2. **Todas tus operaciones quedan registradas** en la tabla `historial_auditoria`
3. **El instructor revisa la base de datos** para ver qué hizo cada grupo
4. **Cada operación tiene un puntaje** según la dificultad y completitud

### ¿Qué Queda Registrado?

Cada vez que tu grupo:
- ✅ Crea un producto o cliente
- ✅ Actualiza un producto o cliente
- ✅ Elimina un producto o cliente
- ✅ Consulta el historial de auditoría

Se guarda automáticamente:
- El nombre de tu grupo
- Qué operación realizaste (CREATE, UPDATE, DELETE)
- En qué tabla (productos o clientes)
- Qué datos modificaste (antes y después)
- Cuándo lo hiciste (fecha y hora)

### Configuración Inicial ⚠️

**ANTES DE EMPEZAR**, asegúrate de configurar tu archivo `.env`:

```env
# Cambia GRUPO_1 por el nombre de tu grupo
GRUPO_ESTUDIANTES=GRUPO_1  # ← TU GRUPO AQUÍ (ej: GRUPO_2, GRUPO_3, etc.)
```

**Este nombre es TU IDENTIFICADOR en la base de datos**. Todo lo que hagas quedará registrado con ese nombre.

---

## 🎯 RETOS POR NIVELES

El proyecto tiene **4 niveles de dificultad**. Puedes completar los retos en el orden que prefieras.

### 📊 Puntaje Total: 100 puntos

| Nivel | Puntos | Descripción |
|-------|--------|-------------|
| **Nivel 1** | 25 pts | Operaciones básicas (CRUD simple) |
| **Nivel 2** | 25 pts | Operaciones intermedias (Búsquedas y filtros) |
| **Nivel 3** | 30 pts | Operaciones avanzadas (Actualizaciones complejas) |
| **Nivel 4** | 20 pts | Demostración de dominio (Consultas de auditoría) |

---

## 🟢 NIVEL 1: Operaciones Básicas (25 puntos)

**Objetivo**: Demostrar que puedes realizar operaciones CRUD básicas.

### Reto 1.1: Crear Productos (10 puntos)

**Tarea**: Crear **5 productos diferentes** para tu tienda virtual.

**Requisitos**:
- ✅ Cada producto debe tener **todos los campos** completos
- ✅ Precios **mayores a 0**
- ✅ Stock **mayor o igual a 0**
- ✅ Al menos **3 categorías diferentes**
- ✅ Nombres **únicos** y descriptivos

**Ejemplo de producto válido**:
```json
{
  "nombre": "Laptop HP Pavilion 15",
  "descripcion": "Laptop con 16GB RAM, 512GB SSD, pantalla 15.6 pulgadas",
  "precio": 2500000,
  "stock": 10,
  "categoria": "Electrónica",
  "imagen_url": "https://example.com/laptop-hp.jpg"
}
```

**Puntaje**:
- 5 productos válidos: **10 puntos**
- 3-4 productos válidos: **7 puntos**
- 1-2 productos válidos: **4 puntos**

**Endpoint**: `POST /productos/`

---

### Reto 1.2: Crear Clientes (10 puntos)

**Tarea**: Crear **5 clientes diferentes**.

**Requisitos**:
- ✅ Cada cliente debe tener **todos los campos** completos
- ✅ Emails **únicos y válidos** (formato correcto)
- ✅ Documentos **únicos**
- ✅ Al menos **3 ciudades diferentes**
- ✅ Teléfonos con formato válido

**Ejemplo de cliente válido**:
```json
{
  "nombre": "Juan Pérez Gómez",
  "email": "juan.perez.grupo1@example.com",
  "telefono": "+57 300 123 4567",
  "direccion": "Calle 10 # 20-30, Apto 301",
  "ciudad": "Medellín",
  "documento": "1234567890"
}
```

**⚠️ IMPORTANTE**: 
- Los emails y documentos son **únicos a nivel GLOBAL** (toda la base de datos)
- Si otro grupo ya usó un email/documento, debes usar otro diferente
- **Tip**: Incluye el nombre de tu grupo en el email (ej: `cliente1.grupo2@example.com`)

**Puntaje**:
- 5 clientes válidos: **10 puntos**
- 3-4 clientes válidos: **7 puntos**
- 1-2 clientes válidos: **4 puntos**

**Endpoint**: `POST /clientes/`

---

### Reto 1.3: Eliminar Registros (5 puntos)

**Tarea**: Eliminar (soft delete) **2 productos** y **2 clientes** que hayas creado.

**Requisitos**:
- ✅ Solo eliminar registros que **TU GRUPO creó**
- ✅ Verificar que el campo `activo` cambie a `false`
- ✅ Los registros deben seguir existiendo en la BD (eliminación lógica)

**Puntaje**:
- 4 eliminaciones correctas: **5 puntos**
- 2-3 eliminaciones correctas: **3 puntos**
- 1 eliminación correcta: **1 punto**

**Endpoints**:
- `DELETE /productos/{id}`
- `DELETE /clientes/{id}`

---

## 🟡 NIVEL 2: Operaciones Intermedias (25 puntos)

**Objetivo**: Demostrar que puedes buscar y filtrar información.

### Reto 2.1: Búsquedas por Nombre (10 puntos)

**Tarea**: Realizar **búsquedas exitosas** usando los endpoints de búsqueda.

**Requisitos**:
- ✅ Buscar **3 productos diferentes** por nombre
- ✅ Buscar **3 clientes diferentes** por nombre
- ✅ Las búsquedas deben **encontrar resultados**

**Puntaje**:
- 6 búsquedas exitosas: **10 puntos**
- 4-5 búsquedas exitosas: **7 puntos**
- 2-3 búsquedas exitosas: **4 puntos**

**Endpoints**:
- `GET /productos/buscar/nombre?q=laptop`
- `GET /clientes/buscar/nombre?q=juan`

**Nota**: Para que haya resultados, primero debes haber creado productos/clientes con esos nombres.

---

### Reto 2.2: Búsqueda por Email (5 puntos)

**Tarea**: Buscar **3 clientes diferentes** por su email.

**Requisitos**:
- ✅ Los emails deben **existir en la BD**
- ✅ Cada búsqueda debe retornar el cliente correcto

**Puntaje**:
- 3 búsquedas exitosas: **5 puntos**
- 2 búsquedas exitosas: **3 puntos**
- 1 búsqueda exitosa: **1 punto**

**Endpoint**: `GET /clientes/buscar/email/{email}`

---

### Reto 2.3: Filtros por Ciudad (5 puntos)

**Tarea**: Filtrar clientes por **ciudad**.

**Requisitos**:
- ✅ Filtrar por **al menos 2 ciudades diferentes**
- ✅ Debe haber clientes en esas ciudades

**Puntaje**:
- 2+ filtros exitosos: **5 puntos**
- 1 filtro exitoso: **2 puntos**

**Endpoint**: `GET /clientes/buscar/ciudad/{ciudad}`

---

### Reto 2.4: Obtener por ID (5 puntos)

**Tarea**: Obtener registros específicos por ID.

**Requisitos**:
- ✅ Obtener **3 productos diferentes** por ID
- ✅ Obtener **3 clientes diferentes** por ID

**Puntaje**:
- 6 consultas exitosas: **5 puntos**
- 4-5 consultas exitosas: **3 puntos**
- 2-3 consultas exitosas: **1 punto**

**Endpoints**:
- `GET /productos/{id}`
- `GET /clientes/{id}`

---

## 🟠 NIVEL 3: Operaciones Avanzadas (30 puntos)

**Objetivo**: Demostrar que puedes actualizar registros de forma correcta.

### Reto 3.1: Actualizar Productos (15 puntos)

**Tarea**: Actualizar **5 productos** que hayas creado.

**Requisitos para cada actualización**:
- ✅ Solo actualizar productos que **TU GRUPO creó**
- ✅ Modificar **al menos 2 campos** por actualización
- ✅ Los cambios deben ser **significativos** (no solo cambiar una letra)
- ✅ Al menos **3 actualizaciones** deben incluir cambio de precio

**Ejemplos de actualizaciones válidas**:
1. Cambiar precio de $2,500,000 a $2,200,000 (descuento)
2. Actualizar stock de 10 a 5 unidades (por ventas)
3. Cambiar categoría de "Electrónica" a "Computadoras"
4. Actualizar descripción para incluir más detalles
5. Cambiar imagen_url a una nueva URL

**Puntaje**:
- 5 actualizaciones válidas: **15 puntos**
- 3-4 actualizaciones válidas: **10 puntos**
- 1-2 actualizaciones válidas: **5 puntos**

**Endpoint**: `PUT /productos/{id}`

**Verificación**: El instructor verá en `datos_anteriores` y `datos_nuevos` qué cambió.

---

### Reto 3.2: Actualizar Clientes (15 puntos)

**Tarea**: Actualizar **5 clientes** que hayas creado.

**Requisitos para cada actualización**:
- ✅ Solo actualizar clientes que **TU GRUPO creó**
- ✅ Modificar **al menos 2 campos** por actualización
- ✅ Al menos **2 actualizaciones** deben incluir cambio de dirección
- ✅ Al menos **2 actualizaciones** deben incluir cambio de teléfono

**Ejemplos de actualizaciones válidas**:
1. Cambiar dirección de "Calle 10" a "Calle 20" (se mudó)
2. Actualizar teléfono (cambió de número)
3. Cambiar ciudad de "Medellín" a "Bogotá" (se mudó de ciudad)
4. Actualizar nombre completo (se casó, cambió apellido)

**⚠️ IMPORTANTE**: NO puedes cambiar el email a uno que ya existe en la BD.

**Puntaje**:
- 5 actualizaciones válidas: **15 puntos**
- 3-4 actualizaciones válidas: **10 puntos**
- 1-2 actualizaciones válidas: **5 puntos**

**Endpoint**: `PUT /clientes/{id}`

---

## 🔴 NIVEL 4: Demostración de Dominio (20 puntos)

**Objetivo**: Demostrar que entiendes el sistema de auditoría y puedes consultar información.

### Reto 4.1: Consultar Historial de Tu Grupo (5 puntos)

**Tarea**: Consultar el historial de operaciones de **TU GRUPO**.

**Requisitos**:
- ✅ Hacer al menos **1 consulta** al endpoint de auditoría por grupo
- ✅ Debe retornar las operaciones que tu grupo ha realizado

**Puntaje**:
- Consulta exitosa: **5 puntos**

**Endpoint**: `GET /auditoria/grupo/{nombre_grupo}`

**Ejemplo**: `GET /auditoria/grupo/GRUPO_1`

---

### Reto 4.2: Consultar por Tipo de Operación (5 puntos)

**Tarea**: Consultar el historial por **tipo de operación**.

**Requisitos**:
- ✅ Consultar operaciones de tipo **CREATE**
- ✅ Consultar operaciones de tipo **UPDATE**
- ✅ Consultar operaciones de tipo **DELETE**

**Puntaje**:
- 3 consultas (CREATE, UPDATE, DELETE): **5 puntos**
- 2 consultas: **3 puntos**
- 1 consulta: **1 punto**

**Endpoint**: `GET /auditoria/operacion/{tipo}`

**Ejemplos**:
- `GET /auditoria/operacion/CREATE`
- `GET /auditoria/operacion/UPDATE`
- `GET /auditoria/operacion/DELETE`

---

### Reto 4.3: Consultar Historial de un Registro (5 puntos)

**Tarea**: Consultar el historial completo de **un producto** y **un cliente** específicos.

**Requisitos**:
- ✅ Consultar historial de 1 producto que hayas modificado varias veces
- ✅ Consultar historial de 1 cliente que hayas modificado varias veces
- ✅ Debe mostrar todas las operaciones sobre ese registro

**Puntaje**:
- 2 consultas exitosas: **5 puntos**
- 1 consulta exitosa: **2 puntos**

**Endpoint**: `GET /auditoria/registro/{tabla}/{id_registro}`

**Ejemplos**:
- `GET /auditoria/registro/productos/30`
- `GET /auditoria/registro/clientes/20`

---

### Reto 4.4: Variedad de Operaciones (5 puntos - BONUS)

**Tarea**: Demostrar **variedad** en tus operaciones.

**Requisitos**:
- ✅ Al menos **10 operaciones CREATE**
- ✅ Al menos **10 operaciones UPDATE**
- ✅ Al menos **4 operaciones DELETE**
- ✅ Operaciones realizadas en **diferentes días/horarios** (no todo junto)

**Puntaje**:
- Todos los requisitos cumplidos: **5 puntos BONUS**
- 3 requisitos cumplidos: **3 puntos**
- 2 requisitos cumplidos: **1 punto**

**Verificación**: El instructor revisa la tabla `historial_auditoria` completa de tu grupo.

---

## 📊 Resumen de Puntaje

| Nivel | Reto | Puntos |
|-------|------|--------|
| **Nivel 1** | 1.1 Crear 5 productos | 10 |
| | 1.2 Crear 5 clientes | 10 |
| | 1.3 Eliminar 2+2 registros | 5 |
| **Nivel 2** | 2.1 Búsquedas por nombre | 10 |
| | 2.2 Búsquedas por email | 5 |
| | 2.3 Filtros por ciudad | 5 |
| | 2.4 Obtener por ID | 5 |
| **Nivel 3** | 3.1 Actualizar 5 productos | 15 |
| | 3.2 Actualizar 5 clientes | 15 |
| **Nivel 4** | 4.1 Consultar historial grupo | 5 |
| | 4.2 Consultar por operación | 5 |
| | 4.3 Consultar historial registro | 5 |
| | 4.4 Variedad (BONUS) | 5 |
| | **TOTAL** | **100 puntos** |

---

## 🎯 Estrategia Recomendada

### Niveles 1 y 2 (50 puntos)
1. Configurar `.env` con nombre del grupo
2. Ejecutar la API con F5
3. Crear los 5 productos (Reto 1.1)
4. Crear los 5 clientes (Reto 1.2)
5. Eliminar 2 productos y 2 clientes (Reto 1.3)
6. Hacer todas las búsquedas (Retos 2.1, 2.2, 2.3, 2.4)

### Nivel 3 (30 puntos)
7. Actualizar los 5 productos (Reto 3.1)
8. Actualizar los 5 clientes (Reto 3.2)

### Nivel 4 (20 puntos + BONUS)
9. Consultar historial de tu grupo (Reto 4.1)
10. Consultar por tipo de operación (Reto 4.2)
11. Consultar historial de registros (Reto 4.3)
12. Asegurarte de tener variedad (Reto 4.4)

---

## ⚠️ Reglas Importantes

### ✅ Permitido
- Crear, modificar y eliminar TUS PROPIOS registros
- Consultar CUALQUIER registro (de cualquier grupo)
- Experimentar con todos los endpoints
- Hacer pruebas múltiples

### ❌ NO Permitido
- Modificar registros que creó OTRO GRUPO
- Eliminar registros de OTRO GRUPO
- Usar emails/documentos duplicados
- Crear registros con datos inválidos o vacíos
- Hacer trampa (el sistema de auditoría registra TODO)

### 🤝 Buenas Prácticas
- Usa nombres descriptivos en tus productos/clientes
- Incluye el nombre de tu grupo en los emails (para evitar duplicados)
- Haz operaciones en diferentes momentos (no todo de una vez)
- Prueba diferentes categorías, ciudades, precios
- Revisa el historial de auditoría para verificar tus operaciones

---

## 🛠️ Herramientas Recomendadas

### Para Probar los Endpoints

**Opción 1: Swagger UI** (Más fácil para principiantes)
- URL: http://localhost:8000/docs
- Interfaz visual
- Pruebas directas desde el navegador

**Opción 2: Postman** (Recomendado)
- Importa las colecciones de `postman_collections/`
- Todos los endpoints pre-configurados
- Guía: `postman_collections/README.md`

**Opción 3: ApiDog**
- Importa las colecciones de `apidog_collections/`
- Alternativa a Postman
- Guía: `apidog_collections/README.md`

---

## 📝 Cómo Verificar Tu Progreso

Puedes verificar tus operaciones consultando el historial de auditoría:

```
1. Consultar TODAS tus operaciones:
   GET /auditoria/grupo/TU_GRUPO

2. Contar cuántas operaciones CREATE tienes:
   GET /auditoria/operacion/CREATE
   (busca las de tu grupo en los resultados)

3. Ver el historial de un producto específico:
   GET /auditoria/registro/productos/{id}

4. Ver el historial de un cliente específico:
   GET /auditoria/registro/clientes/{id}
```

---

## ❓ Preguntas Frecuentes

### ¿Cómo sé si mis operaciones quedaron registradas?
Consulta el endpoint `/auditoria/grupo/TU_GRUPO` y verás todas tus operaciones.

### ¿Puedo hacer más operaciones de las solicitadas?
¡Sí! Entre más practiques, mejor. El puntaje mínimo es lo requerido, pero puedes hacer más.

### ¿Qué pasa si elimino un producto por error?
La eliminación es lógica (soft delete), el registro sigue en la BD. El instructor puede ver que lo eliminaste.

### ¿Puedo crear más de 5 productos/clientes?
Sí, los 5 son el **mínimo** para obtener puntaje completo. Puedes crear todos los que quieras.

### ¿Qué pasa si mi email/documento ya existe?
Debes usar otro. **Tip**: Incluye el nombre de tu grupo en el email (ej: `cliente1.grupo2@example.com`).

### ¿Cuándo se cierra el plazo de entrega?
[El instructor definirá la fecha límite]

### ¿Puedo trabajar en equipo?
Sí, es un proyecto grupal. Pero todos los integrantes deben entender qué hace cada endpoint.

---

## 🆘 ¿Necesitas Ayuda?

1. **Lee la documentación**:
   - `README.md` - Documentación completa
   - `INICIO_RAPIDO.md` - Guía rápida
   - `apidog_collections/README.md` - Guía de colecciones

2. **Revisa los ejemplos**:
   - Las colecciones de Postman/ApiDog tienen ejemplos de todos los endpoints

3. **Consulta con tu grupo**:
   - Trabaja en equipo

4. **Pregunta al instructor**:
   - En clase o por los canales oficiales

---

## 🎓 Criterios de Evaluación

El instructor evaluará:

1. **Completitud** (40%):
   - ¿Completaste todos los retos?
   - ¿Cumpliste los requisitos de cada uno?

2. **Calidad de los datos** (30%):
   - ¿Usaste datos realistas y descriptivos?
   - ¿Tus registros tienen sentido?

3. **Variedad** (20%):
   - ¿Usaste diferentes categorías, ciudades, precios?
   - ¿Hiciste las operaciones en diferentes momentos?

4. **Uso correcto de la API** (10%):
   - ¿Seguiste las validaciones?
   - ¿Respetaste los registros de otros grupos?

---

## 🎉 ¡Buena Suerte!

Este proyecto te permitirá demostrar tus habilidades en:
- Consumo de APIs REST
- Operaciones CRUD
- Validación de datos
- Búsquedas y filtros
- Comprensión de sistemas de auditoría

**Recuerda**: TODO queda registrado en la auditoría. Trabaja con responsabilidad y demuestra lo que has aprendido.

---

**Fecha de entrega**: [El instructor completará]  
**Valor del proyecto**: 100 puntos  
**Modalidad**: Grupal  
**Entregable**: Operaciones registradas en la base de datos (NO código)
