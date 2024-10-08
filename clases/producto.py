#Definición de clase Producto
class Producto:
    
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_total(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f"{self.nombre} (x{self.cantidad}): ${self.precio} c/u"