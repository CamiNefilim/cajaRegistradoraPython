# Importar funcion mostrar_recibo
from modulos.mostrar_recibo import mostrar_recibo

# Definición de clase Compras
class Compra:
    
    def __init__(self, id_compra, productos, total, total_con_descuento):
        self.id_compra = id_compra
        self.productos = productos
        self.total_con_descuento = total_con_descuento
        self.total = total


    def __str__(self):
        return mostrar_recibo(self.id_compra, self.productos, self.total, self.total_con_descuento)