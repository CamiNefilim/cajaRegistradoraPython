# Importa clase productos
from clases import Producto

# Función para agregar productos
def agregar_producto():
    # Solicita datos del producto
    nombre = input("Ingrese el nombre del producto: ")
    while (True):        
        try:
            #Validación de datos
            cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
            precio = int(input(f"Ingrese el precio por unidad de {nombre}: "))
            return Producto(nombre, cantidad, precio)
        except ValueError:
            # Imprime error
            print("Para ingresar el producto debe ingresar valores válidos.")