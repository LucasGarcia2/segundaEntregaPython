class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.comprador = None

    def asignar_comprador(self, cliente):
        self.comprador = cliente

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - ${self.precio}"
