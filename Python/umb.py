class Producto:
    def __init__(self, codigo, nombre, descripcion, stock_actual):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.stock_actual = stock_actual

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Stock: {self.stock_actual}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, codigo):
        self.productos = [p for p in self.productos if p.codigo != codigo]

    def modificar_stock(self, codigo, nuevo_stock):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.stock_actual = nuevo_stock

    def mostrar_stock_critico(self, stock_critico):
        productos_criticos = [p for p in self.productos if p.stock_actual <= stock_critico]
        for producto in productos_criticos:
            print(producto)


# Ejemplo de uso
inventario = Inventario()

# Agregar productos
producto1 = Producto("001", "Producto 1", "Descripción del Producto 1", 5)
producto2 = Producto("002", "Producto 2", "Descripción del Producto 2", 1)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

# Mostrar productos con stock crítico (ejemplo: stock crítico <= 2)
print("Productos con stock crítico:")
inventario.mostrar_stock_critico(2)

# Modificar stock de un producto (ejemplo: modificar stock de Producto 1 a 3)
inventario.modificar_stock("001", 3)

# Mostrar productos con stock crítico después de la modificación
print("Productos con stock crítico después de la modificación:")
inventario.mostrar_stock_critico(2)

# Eliminar un producto (ejemplo: eliminar Producto 2)
inventario.eliminar_producto("002")

# Mostrar productos con stock crítico después de la eliminación
print("Productos con stock crítico después de la eliminación:")
inventario.mostrar_stock_critico(2)