# main.py
from cliente import Cliente
from producto import Producto

# Crear instancias de la clase Cliente
cliente1 = Cliente("Jack", "jack@gmail.com")
cliente2 = Cliente("Roxie", "Roxie@gmail.com")

# Crear instancias de la clase Producto
celular = Producto("Smartphone", "Celulares", 599.99)
auriculares = Producto("Auriculares Bluetooth", "Accesorios", 89.99)
laptop = Producto("Laptop", "Computadoras", 1299.99)
libro = Producto("Libro", "Libros", 19.99)
ropa = Producto("Camiseta", "Ropa", 29.99)

# Agregar productos al carrito
cliente1.agregar_producto_al_carrito(celular)
cliente1.agregar_producto_al_carrito(auriculares)
cliente2.agregar_producto_al_carrito(laptop)
cliente2.agregar_producto_al_carrito(libro)
cliente2.agregar_producto_al_carrito(ropa)

# Realizar compras
cliente1.realizar_compra()
cliente2.realizar_compra()
