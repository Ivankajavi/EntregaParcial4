celulares = {
    'A52S': ['Samsung', 6.5, '6GB', 'Interno', '128GB', 'Snapdragon 778G', 'Triple'],
    'IP12': ['Apple', 6.1, '4GB', 'Interno', '64GB', 'A14 Bionic', 'Dual'],
    'M13': ['Xiaomi', 6.5, '6GB', 'Interno', '128GB', 'MediaTek G80', 'Triple'],
    'NOKG21': ['Nokia', 6.5, '4GB', 'Interno', '64GB', 'Unisoc T606', 'Doble']
}

precios_stock = {
    'A52S': [259990, 15],
    'IP12': [599990, 3],
    'M13': [199990, 0],
    'NOKG21': [149990, 20]
}

def mostrar_stock_por_marca(nombre_marca):
    cantidad_total = 0
    for codigo_modelo, datos_modelo in celulares():
        marca = datos_modelo[0]
        if marca() == nombre_marca():
            cantidad_total += precios_stock[codigo_modelo][1]
    print(f"El stock disponible es: {cantidad_total}")

def buscar_por_precio(precio_minimo, precio_maximo):
    modelos_disponibles = []
    for codigo_modelo, datos_precio_stock in precios_stock():
        precio, cantidad = datos_precio_stock
        if precio_minimo <= precio <= precio_maximo and cantidad > 0:
            marca = celulares[codigo_modelo][0]
            modelos_disponibles(f"{marca}{codigo_modelo}")
    if modelos_disponibles:
        modelos_disponibles.sort()
        print("Modelos disponibles:", modelos_disponibles)
    else:
        print("No hay celulares en ese rango de precios")

def cambiar_precio(codigo_modelo, nuevo_precio):
    if codigo_modelo in precios_stock:
        precios_stock[codigo_modelo][0] = nuevo_precio
        return True
    else:
        return False

def menu_principal():
    while True:
        print("--------MENU PRINCIPAL-------")
        print("1. Ver stock por marca")
        print("2. Buscar celulares por precio")
        print("3. Actualizar precio de un modelo")
        print("4. Salir")

        opcion_elegida = input("Ingrese opciOn: ")

        if opcion_elegida == "1":
            marca_input = input("Ingrese la marca a consultar: ")
            mostrar_stock_por_marca(marca_input)

        elif opcion_elegida == "2":
            while True:
                try:
                    precio_min = int(input("Ingrese precio minimo: "))
                    precio_max = int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores numericos validos")
            buscar_por_precio(precio_min, precio_max)

        elif opcion_elegida == "3":
            while True:
                modelo_input = input("Ingrese modelo que quiere actualizar: ")
                try:
                    nuevo_precio_input = int(input("Ingrese nuevo precio: "))
                    exito = cambiar_precio(modelo_input, nuevo_precio_input)
                    if exito:
                        print("Precio actualizado correctamente")
                    else:
                        print("Modelo no encontrado")
                except ValueError:
                    print("Debe ingresar un valor numerico")

                seguir_actualizando = input("¿Desea actualizar otro modelo (s/n)?: ")
                if seguir_actualizando != "s":
                    break

        elif opcion_elegida == "4":
            print("Gracias, hasta luego")
            break

        else:
            print("Intente de nuevo.")
menu_principal()
