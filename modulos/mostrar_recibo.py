# Función para mostrar el recibo

def mostrar_recibo(id, productos, total, total_con_descuento):
    
    print(f"\n------ Recibo Detallado compra {id} ------")
    
    #Muestra productos de la compra
    print("\nProductos:\n")
    for producto in productos:
        print(f"- {producto.__str__()}")
    
    #Muestra subtotal y total
    print(f"\nSubtotal: ${total}")
    if total_con_descuento > 0:
        print(f"Total con descuento: ${total_con_descuento}")
    else:
        print(f"Total: ${total}")
        
    print(f"\n------ Fin Recibo Detallado compra {id} ------\n")
    
    return ""
        
        