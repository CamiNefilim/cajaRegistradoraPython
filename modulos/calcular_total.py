# Función para calcular el total
def calcular_total(productos):
    total = 0
    for producto in productos:
        total += producto.cantidad * producto.precio
    return total