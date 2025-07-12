celulares = {
    'A52S': ['Samsung', 15, 259990],
    'IP12': ['Apple', 3, 599990],
    'M13': ['Xiaomi', 0, 199990],
    'NOKG21': ['Nokia', 20, 149990]
}

def ver_stock(marca_buscada):
    total_stock = 0
    for modelo in celulares:
        marca = celulares[modelo][0]
        cantidad = celulares[modelo][1]
        if marca == marca_buscada:
            total_stock += cantidad
    print("Stock de", marca_buscada, ":", total_stock)

while True:
    print("\n-------MENÚ--------")
    print("1. Ver stock por marca")
    print("2. Buscar por precio")
    print("3. Cambiar precio")
    print("4. Salir")
    opcion = input("Opcion elegida: ")

    if opcion == "1":
        marca_input = input("Escribe la marca: ")
        ver_stock(marca_input)

    elif opcion == "2":
        precio_minimo = int(input("Precio minimo: "))
        precio_maximo = int(input("Precio maximo: "))
        for modelo in celulares:
            marca = celulares[modelo][0]
            cantidad = celulares[modelo][1]
            precio = celulares[modelo][2]
            if precio_minimo <= precio <= precio_maximo and cantidad > 0:
                print(modelo, "-", marca, "-", "Precio:", precio)

    elif opcion == "3":
        modelo_elegido = input("Modelo a cambiar precio: ")
        if modelo_elegido in celulares:
            nuevo_precio = int(input("Nuevo precio: "))
            celulares[modelo_elegido][2] = nuevo_precio
            print("Precio cambiado con exito")
        else:
            print("Modelo no encontrado")

    elif opcion == "4":
        print("Programa terminado.")
        break

    else:
        print("Intenta otra vez")
