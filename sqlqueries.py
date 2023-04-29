import sqlite3
from sqlite3 import Error

class QueriesSQLite:
    def create_connection(path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    # added return
    def execute_query(connection, query, data_tuple):
        cursor = connection.cursor()
        try:
            cursor.execute(query, data_tuple)
            connection.commit()
            print("Query executed successfully")
            return cursor.lastrowid
        except Error as e:
            print(f"The error '{e}' occurred")

    # added data_tuple
    def execute_read_query(connection, query, data_tuple=()):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query, data_tuple)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")


    def create_tables():
        connection = QueriesSQLite.create_connection("pdvDB.sqlite")
        # connection.execute("DROP TRIGGER IF EXISTS actualizar_stock_venta;")
        # connection.execute("DROP TRIGGER IF EXISTS actualizar_total_pedido;")
        # connection.execute("DROP TRIGGER IF EXISTS validar_stock;")
        # connection.execute("DROP TRIGGER IF EXISTS nuevo_envio;")
        
        # try:
        #     connection.execute("PRAGMA journal_mode=OFF")
        #     connection.execute("PRAGMA temp_store=MEMORY")
        #     connection.execute("DROP TABLE IF EXISTS respaldo_dummy;")
        #     connection.execute("CREATE TABLE respaldo_dummy(columna1 TEXT, columna2 TEXT, columna3 TEXT, columna4 TEXT, columna5 TEXT);")
        #     connection.execute("INSERT INTO respaldo_dummy SELECT * FROM main.sqlite_master WHERE type='table'")

        #     connection = QueriesSQLite.create_connection("pdvDB.sqlite")
        #     connection.execute("ATTACH DATABASE 'mi_base_datos_respaldo.db' AS respaldo_db")
        #     connection.execute("DROP TABLE IF EXISTS dummy;")
        #     connection.execute("CREATE TABLE dummy AS SELECT * FROM respaldo_dummy;")
        #     connection.execute("DROP TABLE respaldo_dummy;")
        #     connection.execute("ALTER TABLE dummy RENAME TO respaldo_dummy;")
        #     connection.execute("DETACH DATABASE respaldo_db")

        #     connection.execute("DROP TABLE respaldo_dummy")
        #     print("Database backup successful.")
        # except Error as e:
        #     print(f"The error '{e}' occurred")

        # tabla_productos = """
        # CREATE TABLE IF NOT EXISTS productos(
        #  codigo TEXT PRIMARY KEY, 
        #  nombre TEXT NOT NULL, 
        #  precio REAL NOT NULL, 
        #  cantidad INTEGER NOT NULL
        # );
        # """

        # tabla_usuarios = """
        # CREATE TABLE IF NOT EXISTS usuarios(
        #  username TEXT PRIMARY KEY, 
        #  nombre TEXT NOT NULL, 
        #  password TEXT NOT NULL,
        #  tipo TEXT NOT NULL
        # );
        # """

        # tabla_ventas = """
        # CREATE TABLE IF NOT EXISTS ventas(
        #  id INTEGER PRIMARY KEY, 
        #  total REAL NOT NULL, 
        #  fecha TIMESTAMP,
        #  username TEXT  NOT NULL, 
        #  FOREIGN KEY(username) REFERENCES usuarios(username)
        # );
        # """

        # tabla_ventas_detalle = """
        # CREATE TABLE IF NOT EXISTS ventas_detalle(
        #  id INTEGER PRIMARY KEY, 
        #  id_venta TEXT NOT NULL, 
        #  precio REAL NOT NULL,
        #  producto TEXT NOT NULL,
        #  cantidad INTEGER NOT NULL,
        #  FOREIGN KEY(id_venta) REFERENCES ventas(id),
        #  FOREIGN KEY(producto) REFERENCES productos(codigo)
        # );
        # """

        # tabla_clientes = """
        # CREATE TABLE Clientes (
        # ID INTEGER PRIMARY KEY,
        # Nombre TEXT NOT NULL,
        # Apellido TEXT NOT NULL,
        # Direccion TEXT,
        # Correo_electronico TEXT,
        # Telefono TEXT
        # );
        # """

        # tabla_productosFinal = """
        # CREATE TABLE ProductosFinal (
        # ID INTEGER PRIMARY KEY,
        # Nombre TEXT NOT NULL,
        # Descripcion TEXT,
        # Precio REAL NOT NULL,
        # Stock INTEGER NOT NULL
        # );
        # """

        # tabla_categorias = """
        # CREATE TABLE Categorias (
        # ID INTEGER PRIMARY KEY,
        # Nombre TEXT NOT NULL
        # );
        # """

        # tabla_pedidos = """
        # CREATE TABLE Pedidos (
        # ID INTEGER PRIMARY KEY,
        # Fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
        # Cliente INTEGER NOT NULL,
        # Total REAL NOT NULL,
        # FOREIGN KEY (Cliente) REFERENCES Clientes(ID)
        # );
        # """

        # tabla_detalle_pedidos = """
        # CREATE TABLE Detalle_pedidos (
        # ID INTEGER PRIMARY KEY,
        # Pedido INTEGER NOT NULL,
        # Producto INTEGER NOT NULL,
        # Cantidad INTEGER NOT NULL,
        # Precio_unitario REAL NOT NULL,
        # FOREIGN KEY (Pedido) REFERENCES Pedidos(ID),
        # FOREIGN KEY (Producto) REFERENCES Productos(ID)
        # );
        # """

        # tabla_pagos = """
        # CREATE TABLE Pagos (
        # ID INTEGER PRIMARY KEY,
        # Fecha_pago DATETIME DEFAULT CURRENT_TIMESTAMP,
        # Pedido INTEGER NOT NULL,
        # Monto_pago REAL NOT NULL,
        # FOREIGN KEY (Pedido) REFERENCES Pedidos(ID)
        # );
        # """

        # tabla_envios = """
        # CREATE TABLE Envios (
        # ID INTEGER PRIMARY KEY,
        # Fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
        # Pedido INTEGER NOT NULL,
        # Direccion_envio TEXT NOT NULL,
        # FOREIGN KEY (Pedido) REFERENCES Pedidos(ID)
        # );
        # """

        # tabla_categorias_productos = """
        # CREATE TABLE Categorias_productos (
        # Producto INTEGER NOT NULL,
        # Categoria INTEGER NOT NULL,
        # FOREIGN KEY (Producto) REFERENCES Productos(ID),
        # FOREIGN KEY (Categoria) REFERENCES Categorias(ID),
        # PRIMARY KEY (Producto, Categoria)
        # );
        # """

        # Trigger para actualizar el stock cuando se realiza una venta
        # triggerStock = """
        # CREATE TRIGGER actualizar_stock_venta AFTER INSERT ON Ventas
        # BEGIN
        #     UPDATE Productos
        #     SET Stock = Stock - NEW.Cantidad
        #     WHERE id_producto = NEW.id_producto;
        # END;
        # """

        # # Trigger para actualizar el total del pedido cuando se agrega un nuevo producto
        # totalPedidos = """
        # CREATE TRIGGER actualizar_total_pedido AFTER INSERT ON Detalle_pedidos
        # BEGIN
        #     UPDATE Pedidos SET Total = (SELECT SUM(Productos.Precio * Detalle_pedidos.Cantidad) 
        #                                 FROM Detalle_pedidos 
        #                                 INNER JOIN Productos ON Detalle_pedidos.Id_producto = Productos.Id_producto
        #                                 WHERE Detalle_pedidos.Id_pedido = Pedidos.Id_pedido)
        #     WHERE Pedidos.Id_pedido = NEW.Id_pedido;
        # END;
        # """

        # # Trigger para validar que el stock no se vuelva negativo
        # validacionStock = """
        # CREATE TRIGGER validar_stock AFTER UPDATE ON Productos
        # BEGIN
        #     SELECT CASE
        #         WHEN NEW.Stock < 0 THEN RAISE(ABORT, 'No puede haber stock negativo')
        #     END;
        # END;
        # """

        # # Trigger para registrar un nuevo envío cuando se realiza un pago
        # nuevoEnvio = """
        # CREATE TRIGGER nuevo_envio 
        # AFTER INSERT ON Envios
        # FOR EACH ROW 
        # BEGIN
        #     INSERT INTO RegistroEnvios (IdEnvio, FechaRegistro, Estado) 
        #     VALUES (NEW.IdEnvio, datetime('now'), NEW.Estado);
        # END;    
        # """

        # vistaDeUsuarios = """
        # CREATE VIEW vista_usuarios AS
        # SELECT username, password
        # FROM usuarios;
        # """

        # # Creacion de triggers
        # QueriesSQLite.execute_query(connection, triggerStock, tuple()) 
        # QueriesSQLite.execute_query(connection, totalPedidos, tuple()) 
        # QueriesSQLite.execute_query(connection, validacionStock, tuple()) 
        # QueriesSQLite.execute_query(connection, nuevoEnvio, tuple()) 

        #Creacion de tablas
        # QueriesSQLite.execute_query(connection, vistaDeUsuarios, tuple()) 
        # QueriesSQLite.execute_query(connection, "ALTER TABLE usuarios ADD COLUMN correo TEXT;", tuple()) 
        # QueriesSQLite.execute_query(connection, tabla_productos, tuple()) 
        # QueriesSQLite.execute_query(connection, tabla_usuarios, tuple()) 
        # QueriesSQLite.execute_query(connection, tabla_ventas, tuple()) 
        # QueriesSQLite.execute_query(connection, tabla_ventas_detalle, tuple()) 
        # QueriesSQLite.execute_query(connection, tabla_categorias_productos, tuple())
        # QueriesSQLite.execute_query(connection, tabla_envios, tuple())
        # QueriesSQLite.execute_query(connection, tabla_pagos, tuple())
        # QueriesSQLite.execute_query(connection, tabla_detalle_pedidos, tuple())
        # QueriesSQLite.execute_query(connection, tabla_pedidos, tuple())
        # QueriesSQLite.execute_query(connection, tabla_categorias, tuple())
        # QueriesSQLite.execute_query(connection, tabla_productosFinal, tuple())
        # QueriesSQLite.execute_query(connection, tabla_clientes, tuple())


if __name__=="__main__":
    from datetime import datetime, timedelta
    connection = QueriesSQLite.create_connection("pdvDB.sqlite")
    QueriesSQLite.create_tables()

    # fecha1= datetime.today()-timedelta(days=5)
    # neuva_data=(fecha1, 4)
    # actualizar = """
    # UPDATE
    #   ventas
    # SET
    #   fecha=?
    # WHERE
    #   id = ?
    # """

    # QueriesSQLite.execute_query(connection, actualizar, neuva_data)

    # select_ventas = "SELECT * from ventas"
    # ventas = QueriesSQLite.execute_read_query(connection, select_ventas)
    # if ventas:
    #     for venta in ventas:
    #         print("type:", type(venta), "venta:",venta)


    # select_ventas_detalle = "SELECT * from ventas_detalle"
    # ventas_detalle = QueriesSQLite.execute_read_query(connection, select_ventas_detalle)
    # if ventas_detalle:
    #     for venta in ventas_detalle:
    #         print("type:", type(venta), "venta:",venta)

    # crear_producto = """
    # INSERT INTO
    #   productos (codigo, nombre, precio, cantidad)
    # VALUES
    #     ('111', 'leche 1l', 20.0, 20),
    #     ('222', 'cereal 500g', 50.5, 15), 
    #     ('333', 'yogurt 1L', 25.0, 10),
    #     ('444', 'helado 2L', 80.0, 20),
    #     ('555', 'alimento para perro 20kg', 750.0, 5),
    #     ('666', 'shampoo', 100.0, 25),
    #     ('777', 'papel higiénico 4 rollos', 35.5, 30),
    #     ('888', 'jabón para trastes', 65.0, 5)
    # """
    # QueriesSQLite.execute_query(connection, crear_producto, tuple()) 

    # select_products = "SELECT * from productos"
    # productos = QueriesSQLite.execute_read_query(connection, select_products)
    # for producto in productos:
    #     print(producto)


    # usuario_tuple=('test', 'Persona 1', '123', 'admin')
    # crear_usuario = """
    # INSERT INTO
    #   usuarios (username, nombre, password, tipo)
    # VALUES
    #     (?,?,?,?);
    # """
    # QueriesSQLite.execute_query(connection, crear_usuario, usuario_tuple) 


    # select_users = "SELECT * from usuarios"
    # usuarios = QueriesSQLite.execute_read_query(connection, select_users)
    # for usuario in usuarios:
    #     print("type:", type(usuario), "usuario:",usuario)

    # neuva_data=('Persona 55', '123', 'admin', 'persona1')
    # actualizar = """
    # UPDATE
    #   usuarios
    # SET
    #   nombre=?, password=?, tipo = ?
    # WHERE
    #   username = ?
    # """
    # QueriesSQLite.execute_query(connection, actualizar, neuva_data)

    # select_users = "SELECT * from usuarios"
    # usuarios = QueriesSQLite.execute_read_query(connection, select_users)
    # for usuario in usuarios:
    #     print("type:", type(usuario), "usuario:",usuario)



    # select_products = "SELECT * from productos"
    # productos = QueriesSQLite.execute_read_query(connection, select_products)
    # for producto in productos:
    #     print(producto)

    # select_users = "SELECT * from usuarios"
    # usuarios = QueriesSQLite.execute_read_query(connection, select_users)
    # for usuario in usuarios:
    #     print("type:", type(usuario), "usuario:",usuario)

    # producto_a_borrar=('888',)
    # borrar = """DELETE from productos where codigo = ?"""
    # QueriesSQLite.execute_query(connection, borrar, producto_a_borrar)

    # select_products = "SELECT * from productos"
    # productos = QueriesSQLite.execute_read_query(connection, select_products)
    # for producto in productos:
    #     print(producto)

