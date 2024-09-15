# Importa módulo de caja registradora
from modulos import caja_registradora,mostrar_compras_dia

# Importa modulo de tiempo
import time

# Define variables globales
compras = []

#Inicia compra
while True:
    print("Menú")
    print("1. Ingresar nueva compra")    
    print("2. Ver compras del día")
    print("3. Salir")
    opcion = input("Seleccione opción: ")
    
    # Evalúa las opciones
    match opcion:
        case "1":
            compras.append(caja_registradora())
        case "2":
            mostrar_compras_dia(compras)
        case "3":
            print("Muchas gracias por usar mi caja registradora.")
            break
        case _:
            print("No existe la opción ingresada")
    
    # Espera unos segundos para desplegar el menú
    time.sleep(2)    