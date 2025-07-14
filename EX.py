productos = {
    '8475FHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050Ti'],
    'jjFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050Ti'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475FHD': [1879000, 4],
    '2175HD': [2098000, 3],
    'jjFHD': [4249900, 7],
    'fgxFHD': [669000, 2],
    '123FHD': [849000, 1],
    '342FHD': [1890000, 5],
    'GF75HD': [749000, 2],
    'UWU131HD': [349900, 1]
}

def mostrar_stock_por_marca():
    marca = input("Ingrese la marca: ")
    for modelo in productos:
        if productos[modelo][0].lower() == marca.lower():
            print(f"Modelo: {modelo}, Stock: {stock[modelo][1]}")

def buscar_por_precio():
    try:
        minimo = int(input("Ingrese el precio mínimo: "))
        maximo = int(input("Ingrese el precio máximo: "))
        encontrados = False
        for modelo in stock:
            precio = stock[modelo][0]
            cantidad = stock[modelo][1]
            if cantidad > 0 and minimo <= precio <= maximo:
                print(f"{productos[modelo][0]}-{modelo}")
                encontrados = True
        if not encontrados:
            print("No hay notebooks en ese rango de precios.")
    except:
        print("Debe ingresar valores enteros!!")

def actualizar_precio():
    modelo = input("Ingrese el modelo: ")
    if modelo in stock:
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            stock[modelo][0] = nuevo_precio
            print("Precio actualizado!!")
        except:
            print("Debe ingresar un número entero.")
    else:
        print("El modelo no existe!!")

def menu():
    opcion = ""
    while opcion != "4":
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_stock_por_marca()
        elif opcion == "2":
            buscar_por_precio()
        elif opcion == "3":
            actualizar_precio()
            otra = input("¿Desea actualizar otro precio? (sí/no): ")
            if otra.lower() != "sí":
                continue
        elif opcion == "4":
            print("Programa finalizado.")
        else:
            print("Debe seleccionar una opción válida!!")

menu()
