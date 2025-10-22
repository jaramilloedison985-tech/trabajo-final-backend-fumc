-- ========================================
-- SCRIPT DE INICIALIZACIÓN DE BASE DE DATOS
-- ========================================
-- Este script crea las tablas y popula la base de datos con datos de ejemplo
-- para el proyecto final del curso de Backend - FUMC
--
-- INSTRUCCIONES:
-- 1. Conéctate a PostgreSQL con el usuario fumc_user
-- 2. Asegúrate de estar en la base de datos fumc_db
-- 3. Ejecuta este script completo
--
-- Autor: Curso Backend FUMC
-- Fecha: Octubre 2025
-- ========================================

-- ========================================
-- ELIMINAR TABLAS SI EXISTEN (OPCIONAL)
-- ========================================
-- ⚠️ CUIDADO: Esto eliminará todas las tablas y sus datos
-- Descomenta las siguientes líneas solo si quieres empezar desde cero

-- DROP TABLE IF EXISTS historial_auditoria CASCADE;
-- DROP TABLE IF EXISTS productos CASCADE;
-- DROP TABLE IF EXISTS clientes CASCADE;


-- ========================================
-- CREAR TABLAS
-- ========================================
-- Nota: FastAPI creará estas tablas automáticamente,
-- pero las incluimos aquí por referencia

-- Tabla de PRODUCTOS
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    precio NUMERIC(10, 2) NOT NULL CHECK (precio > 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    categoria VARCHAR(100),
    imagen_url VARCHAR(500),
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    fecha_creacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    fecha_actualizacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    grupo_creador VARCHAR(50) NOT NULL,
    grupo_ultima_modificacion VARCHAR(50)
);

-- Índices para mejorar el rendimiento de búsquedas
CREATE INDEX IF NOT EXISTS idx_productos_nombre ON productos(nombre);
CREATE INDEX IF NOT EXISTS idx_productos_categoria ON productos(categoria);
CREATE INDEX IF NOT EXISTS idx_productos_grupo_creador ON productos(grupo_creador);
CREATE INDEX IF NOT EXISTS idx_productos_activo ON productos(activo);

-- Tabla de CLIENTES
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    direccion TEXT,
    ciudad VARCHAR(100),
    documento VARCHAR(20) UNIQUE,
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    fecha_creacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    fecha_actualizacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    grupo_creador VARCHAR(50) NOT NULL,
    grupo_ultima_modificacion VARCHAR(50)
);

-- Índices
CREATE INDEX IF NOT EXISTS idx_clientes_email ON clientes(email);
CREATE INDEX IF NOT EXISTS idx_clientes_documento ON clientes(documento);
CREATE INDEX IF NOT EXISTS idx_clientes_ciudad ON clientes(ciudad);
CREATE INDEX IF NOT EXISTS idx_clientes_grupo_creador ON clientes(grupo_creador);
CREATE INDEX IF NOT EXISTS idx_clientes_activo ON clientes(activo);

-- Tabla de HISTORIAL DE AUDITORÍA
CREATE TABLE IF NOT EXISTS historial_auditoria (
    id SERIAL PRIMARY KEY,
    tabla_afectada VARCHAR(50) NOT NULL,
    id_registro INTEGER NOT NULL,
    operacion VARCHAR(20) NOT NULL CHECK (operacion IN ('CREATE', 'UPDATE', 'DELETE')),
    grupo_responsable VARCHAR(50) NOT NULL,
    datos_anteriores TEXT,
    datos_nuevos TEXT,
    fecha_operacion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    observaciones TEXT
);

-- Índices
CREATE INDEX IF NOT EXISTS idx_auditoria_tabla ON historial_auditoria(tabla_afectada);
CREATE INDEX IF NOT EXISTS idx_auditoria_id_registro ON historial_auditoria(id_registro);
CREATE INDEX IF NOT EXISTS idx_auditoria_operacion ON historial_auditoria(operacion);
CREATE INDEX IF NOT EXISTS idx_auditoria_grupo ON historial_auditoria(grupo_responsable);
CREATE INDEX IF NOT EXISTS idx_auditoria_fecha ON historial_auditoria(fecha_operacion);


-- ========================================
-- INSERTAR DATOS DE EJEMPLO - PRODUCTOS
-- ========================================

INSERT INTO productos (nombre, descripcion, precio, stock, categoria, imagen_url, grupo_creador) VALUES
-- Categoría: Electrónica
('Laptop HP Pavilion 15', 'Laptop con procesador Intel Core i5, 8GB RAM, 256GB SSD, pantalla 15.6 pulgadas', 1850000.00, 15, 'Electrónica', 'https://picsum.photos/seed/laptop1/400/300', 'DATOS_INICIALES'),
('iPhone 13 Pro Max', 'Smartphone Apple con pantalla Super Retina XDR de 6.7", 256GB, cámara triple', 4500000.00, 8, 'Electrónica', 'https://picsum.photos/seed/iphone/400/300', 'DATOS_INICIALES'),
('Samsung Galaxy S23', 'Smartphone Samsung con pantalla AMOLED 6.1", 128GB, 5G', 2800000.00, 12, 'Electrónica', 'https://picsum.photos/seed/samsung/400/300', 'DATOS_INICIALES'),
('AirPods Pro 2', 'Audífonos inalámbricos con cancelación de ruido activa', 950000.00, 20, 'Electrónica', 'https://picsum.photos/seed/airpods/400/300', 'DATOS_INICIALES'),
('iPad Air 5ta Gen', 'Tablet Apple con chip M1, pantalla Liquid Retina 10.9", 64GB', 2400000.00, 10, 'Electrónica', 'https://picsum.photos/seed/ipad/400/300', 'DATOS_INICIALES'),
('Monitor LG UltraWide 34"', 'Monitor curvo UltraWide 34 pulgadas, resolución 3440x1440, 144Hz', 1650000.00, 5, 'Electrónica', 'https://picsum.photos/seed/monitor/400/300', 'DATOS_INICIALES'),
('Teclado Mecánico Logitech MX Keys', 'Teclado mecánico retroiluminado, conexión Bluetooth y USB', 450000.00, 25, 'Electrónica', 'https://picsum.photos/seed/keyboard/400/300', 'DATOS_INICIALES'),
('Mouse Logitech MX Master 3', 'Mouse ergonómico inalámbrico de alta precisión', 350000.00, 30, 'Electrónica', 'https://picsum.photos/seed/mouse/400/300', 'DATOS_INICIALES'),

-- Categoría: Ropa
('Camiseta Nike Dri-FIT', 'Camiseta deportiva de secado rápido, disponible en varios colores', 85000.00, 50, 'Ropa', 'https://picsum.photos/seed/shirt1/400/300', 'DATOS_INICIALES'),
('Jeans Levi''s 501 Original', 'Jeans clásicos de mezclilla, corte recto', 250000.00, 35, 'Ropa', 'https://picsum.photos/seed/jeans/400/300', 'DATOS_INICIALES'),
('Chaqueta Adidas Original', 'Chaqueta deportiva con capucha, material impermeable', 320000.00, 20, 'Ropa', 'https://picsum.photos/seed/jacket/400/300', 'DATOS_INICIALES'),
('Zapatillas Nike Air Max', 'Zapatillas deportivas con tecnología Air Max', 480000.00, 40, 'Ropa', 'https://picsum.photos/seed/shoes1/400/300', 'DATOS_INICIALES'),
('Vestido Zara Elegante', 'Vestido elegante para ocasiones especiales, talla S-M-L', 180000.00, 25, 'Ropa', 'https://picsum.photos/seed/dress/400/300', 'DATOS_INICIALES'),

-- Categoría: Hogar
('Cafetera Oster Programable', 'Cafetera de 12 tazas con temporizador programable', 220000.00, 15, 'Hogar', 'https://picsum.photos/seed/coffee/400/300', 'DATOS_INICIALES'),
('Licuadora Oster Reversible', 'Licuadora de 600W con 3 velocidades y función reversible', 180000.00, 22, 'Hogar', 'https://picsum.photos/seed/blender/400/300', 'DATOS_INICIALES'),
('Juego de Ollas T-fal', 'Set de 10 piezas antiadherente', 350000.00, 12, 'Hogar', 'https://picsum.photos/seed/pots/400/300', 'DATOS_INICIALES'),
('Aspiradora Xiaomi Robot', 'Aspiradora robot con mapeo inteligente y app móvil', 850000.00, 8, 'Hogar', 'https://picsum.photos/seed/vacuum/400/300', 'DATOS_INICIALES'),
('Ventilador de Torre Rowenta', 'Ventilador de torre oscilante con control remoto', 280000.00, 18, 'Hogar', 'https://picsum.photos/seed/fan/400/300', 'DATOS_INICIALES'),

-- Categoría: Deportes
('Bicicleta de Montaña Trek', 'Bicicleta MTB aro 29, suspensión delantera, 21 velocidades', 1850000.00, 6, 'Deportes', 'https://picsum.photos/seed/bike/400/300', 'DATOS_INICIALES'),
('Mancuernas Ajustables 20kg', 'Par de mancuernas ajustables de 5 a 20kg cada una', 320000.00, 15, 'Deportes', 'https://picsum.photos/seed/weights/400/300', 'DATOS_INICIALES'),
('Colchoneta Yoga Premium', 'Colchoneta antideslizante de 6mm con bolsa de transporte', 85000.00, 40, 'Deportes', 'https://picsum.photos/seed/yoga/400/300', 'DATOS_INICIALES'),
('Balón de Fútbol Adidas', 'Balón oficial de fútbol, tamaño 5', 120000.00, 30, 'Deportes', 'https://picsum.photos/seed/ball/400/300', 'DATOS_INICIALES'),

-- Categoría: Libros
('Cien Años de Soledad - García Márquez', 'Novela clásica de la literatura latinoamericana', 45000.00, 25, 'Libros', 'https://picsum.photos/seed/book1/400/300', 'DATOS_INICIALES'),
('El Principito - Antoine de Saint-Exupéry', 'Libro infantil filosófico ilustrado', 35000.00, 30, 'Libros', 'https://picsum.photos/seed/book2/400/300', 'DATOS_INICIALES'),
('Python Crash Course - Eric Matthes', 'Libro de programación en Python para principiantes', 85000.00, 15, 'Libros', 'https://picsum.photos/seed/book3/400/300', 'DATOS_INICIALES'),
('Clean Code - Robert Martin', 'Guía de buenas prácticas de programación', 95000.00, 12, 'Libros', 'https://picsum.photos/seed/book4/400/300', 'DATOS_INICIALES');


-- ========================================
-- INSERTAR DATOS DE EJEMPLO - CLIENTES
-- ========================================

INSERT INTO clientes (nombre, email, telefono, direccion, ciudad, documento, grupo_creador) VALUES
('María González Pérez', 'maria.gonzalez@email.com', '+57 300 123 4567', 'Calle 50 #45-67, Apto 301', 'Medellín', '1234567890', 'DATOS_INICIALES'),
('Carlos Andrés Rodríguez', 'carlos.rodriguez@email.com', '+57 310 234 5678', 'Carrera 70 #32-45', 'Bogotá', '9876543210', 'DATOS_INICIALES'),
('Laura Fernández Castro', 'laura.fernandez@email.com', '+57 320 345 6789', 'Avenida El Poblado #12-34', 'Medellín', '5555666677', 'DATOS_INICIALES'),
('Juan Pablo Martínez', 'juan.martinez@email.com', '+57 315 456 7890', 'Calle 100 #15-20, Torre A', 'Bogotá', '1122334455', 'DATOS_INICIALES'),
('Andrea Sánchez Gómez', 'andrea.sanchez@email.com', '+57 301 567 8901', 'Carrera 43A #5-67', 'Medellín', '9988776655', 'DATOS_INICIALES'),
('Diego López Torres', 'diego.lopez@email.com', '+57 312 678 9012', 'Calle 85 #22-10', 'Bogotá', '4433221100', 'DATOS_INICIALES'),
('Valentina Ramírez Silva', 'valentina.ramirez@email.com', '+57 318 789 0123', 'Avenida Las Palmas #456', 'Medellín', '7766554433', 'DATOS_INICIALES'),
('Santiago Herrera Muñoz', 'santiago.herrera@email.com', '+57 305 890 1234', 'Carrera 7 #80-50', 'Bogotá', '2211009988', 'DATOS_INICIALES'),
('Camila Torres Díaz', 'camila.torres@email.com', '+57 316 901 2345', 'Calle 10 Sur #43-21', 'Medellín', '6655443322', 'DATOS_INICIALES'),
('Sebastián Morales Ruiz', 'sebastian.morales@email.com', '+57 319 012 3456', 'Carrera 15 #120-30', 'Bogotá', '3344556677', 'DATOS_INICIALES'),
('Isabella Castro Vargas', 'isabella.castro@email.com', '+57 302 123 4567', 'Calle 33 #70-10', 'Cali', '8899001122', 'DATOS_INICIALES'),
('Mateo Jiménez Ortiz', 'mateo.jimenez@email.com', '+57 313 234 5678', 'Avenida 6N #25-50', 'Cali', '5566778899', 'DATOS_INICIALES'),
('Sofía Parra Acosta', 'sofia.parra@email.com', '+57 317 345 6789', 'Carrera 80 #45-32', 'Barranquilla', '1010202030', 'DATOS_INICIALES'),
('Nicolás Mejía Cardona', 'nicolas.mejia@email.com', '+57 304 456 7890', 'Calle 72 #52-100', 'Barranquilla', '4040505060', 'DATOS_INICIALES'),
('Mariana Ríos Salazar', 'mariana.rios@email.com', '+57 311 567 8901', 'Carrera 10 #34-56', 'Cartagena', '7070808090', 'DATOS_INICIALES');


-- ========================================
-- INSERTAR REGISTROS DE AUDITORÍA INICIALES
-- ========================================

INSERT INTO historial_auditoria (tabla_afectada, id_registro, operacion, grupo_responsable, datos_nuevos, observaciones) VALUES
('productos', 1, 'CREATE', 'DATOS_INICIALES', '{"nombre": "Laptop HP Pavilion 15", "precio": 1850000}', 'Carga inicial de datos de ejemplo'),
('productos', 2, 'CREATE', 'DATOS_INICIALES', '{"nombre": "iPhone 13 Pro Max", "precio": 4500000}', 'Carga inicial de datos de ejemplo'),
('clientes', 1, 'CREATE', 'DATOS_INICIALES', '{"nombre": "María González Pérez", "email": "maria.gonzalez@email.com"}', 'Carga inicial de datos de ejemplo'),
('clientes', 2, 'CREATE', 'DATOS_INICIALES', '{"nombre": "Carlos Andrés Rodríguez", "email": "carlos.rodriguez@email.com"}', 'Carga inicial de datos de ejemplo');


-- ========================================
-- ACTUALIZAR SECUENCIAS
-- ========================================
-- Asegurar que las secuencias de IDs continúen correctamente

SELECT setval('productos_id_seq', (SELECT MAX(id) FROM productos));
SELECT setval('clientes_id_seq', (SELECT MAX(id) FROM clientes));
SELECT setval('historial_auditoria_id_seq', (SELECT MAX(id) FROM historial_auditoria));


-- ========================================
-- VERIFICAR DATOS INSERTADOS
-- ========================================

-- Contar productos por categoría
SELECT categoria, COUNT(*) as cantidad, SUM(stock) as stock_total
FROM productos
WHERE activo = TRUE
GROUP BY categoria
ORDER BY cantidad DESC;

-- Contar clientes por ciudad
SELECT ciudad, COUNT(*) as cantidad
FROM clientes
WHERE activo = TRUE
GROUP BY ciudad
ORDER BY cantidad DESC;

-- Ver últimas operaciones de auditoría
SELECT * FROM historial_auditoria
ORDER BY fecha_operacion DESC
LIMIT 10;


-- ========================================
-- FUNCIONES ÚTILES (OPCIONAL)
-- ========================================

-- Función para actualizar automáticamente fecha_actualizacion
CREATE OR REPLACE FUNCTION actualizar_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.fecha_actualizacion = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger para productos
DROP TRIGGER IF EXISTS trigger_actualizar_productos ON productos;
CREATE TRIGGER trigger_actualizar_productos
    BEFORE UPDATE ON productos
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_timestamp();

-- Trigger para clientes
DROP TRIGGER IF EXISTS trigger_actualizar_clientes ON clientes;
CREATE TRIGGER trigger_actualizar_clientes
    BEFORE UPDATE ON clientes
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_timestamp();


-- ========================================
-- INFORMACIÓN FINAL
-- ========================================

SELECT '✅ Base de datos inicializada correctamente' as mensaje;
SELECT 'Total de productos: ' || COUNT(*) FROM productos;
SELECT 'Total de clientes: ' || COUNT(*) FROM clientes;
SELECT 'Total de registros de auditoría: ' || COUNT(*) FROM historial_auditoria;

-- ========================================
-- FIN DEL SCRIPT
-- ========================================
