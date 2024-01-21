from producto import Producto

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.carrito_compras = []

    def agregar_producto_al_carrito(self, producto):
        producto.asignar_comprador(self)
        self.carrito_compras.append(producto)
        print(f"{producto.nombre} agregado al carrito de {self.nombre}")

    def realizar_compra(self):
        if self.carrito_compras:
            print(f"{self.nombre} ({self.email}) ha realizado la compra de los siguientes productos:")
            for producto in self.carrito_compras:
                print(producto)
            total = sum(producto.precio for producto in self.carrito_compras)
            print(f"Total a pagar: ${total}")
            print("¡Gracias por tu compra!")
            self.carrito_compras = []
        else:
            print(f"{self.nombre}, tu carrito de compras está vacío.")
