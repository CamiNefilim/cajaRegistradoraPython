# Importa modulos de caja registradora
from .agregar_producto import agregar_producto
from .calcular_total import calcular_total
from .descuento_fidelizacion import descuento_fidelizacion
from .mostrar_recibo import mostrar_recibo

#Importa clase Compra
from clases import Compra

# Importa módulo random
import random

# Función para agregar productos
def caja_registradora():
    productos = []
    while True:
        productos.append(agregar_producto())
        continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
        if continuar != 's':
            break
    
    # Genera ID compra
    id_compra = random.randint(100,500)
    
    # Calcula el total de la compra
    total = calcular_total(productos)
    
    # Consulta si es cliente frecuente
    tiene_tarjeta = input("¿El cliente tiene tarjeta de fidelización? (s/n): ").lower() == 's'

    total_con_descuento = 0
    # Si aplica hace descuento
    if tiene_tarjeta:
        total_con_descuento = descuento_fidelizacion(total)
    
    # Despliega recibo
    mostrar_recibo(id_compra, productos, total, total_con_descuento)
    
    # Retorna Compra
    return Compra(id_compra,productos,total,total_con_descuento)