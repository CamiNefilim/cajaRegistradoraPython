# Función para mostrar las compras del dia

def mostrar_compras_dia(compras):
    print(compras)
    if len(compras) > 0:
        for compra in compras:
            print(compra.__str__())
    else:
        print("No se han registrado compras aún.")
    return True