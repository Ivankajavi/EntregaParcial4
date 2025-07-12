compradores_viernes = []
compradores_sabado = []
stock_viernes = 150
stock_sabado = 180

def comprar(compradores_viernes, compradores_sabado, stock_viernes, stock_sabado):
    nombre = input("Nombre del comprador: ")
    if nombre in compradores_viernes or nombre in compradores_sabado:
        print("Ese nombre ya esta registrado")
        return compradores_viernes, compradores_sabado, stock_viernes, stock_sabado

    print("Funciones:\n1. Cats Dia Viernes\n2. Cats Dia Sabado")
    opcion_funcion = input("Seleccione funcion (1 o 2): ")

    if opcion_funcion == "1" and stock_viernes > 0:
        compradores_viernes(nombre)
        stock_viernes -= 1
        print("Compra exitosa para viernes")
    elif opcion_funcion == "2" and stock_sabado > 0:
        compradores_sabado(nombre)
        stock_sabado -= 1
        print("Compra exitosa para sabado")
    else:
        print("Función inválida o sin stock")

    return compradores_viernes, compradores_sabado, stock_viernes, stock_sabado

def cambiar(compradores_viernes, compradores_sabado, stock_viernes, stock_sabado):
    nombre = input("Nombre del comprador: ")

    if nombre in compradores_viernes and stock_sabado > 0:
        cambiar = input("¿Cambiar a sabado? (si/no): ")
        if cambiar == "si":
            compradores_viernes(nombre)
            compradores_sabado(nombre)
            stock_viernes += 1
            stock_sabado -= 1
            print("Cambio realizado")
    elif nombre in compradores_sabado and stock_viernes > 0:
        cambiar = input("¿Cambiar a viernes? (si/no): ")
        if cambiar == "si":
            compradores_sabado(nombre)
            compradores_viernes(nombre)
            stock_sabado += 1
            stock_viernes -= 1
            print("Cambio realizado")
    else:
        print("No se pudo realizar el cambio (nombre no encontrado o sin stock)")

    return compradores_viernes, compradores_sabado, stock_viernes, stock_sabado

def mostrar_stock(stock_viernes, stock_sabado):
    vendidos_viernes = 150 - stock_viernes
    vendidos_sabado = 180 - stock_sabado
    total_vendidos = vendidos_viernes + vendidos_sabado

    print("Entradas disponibles - Viernes:", stock_viernes)
    print("Entradas disponibles - Sabado:", stock_sabado)
    print("Entradas vendidas total:", total_vendidos)

def salir():
    print("Programa terminado")

def iniciar():
    viernes, sabado = compradores_viernes, compradores_sabado
    stock_v, stock_s = stock_viernes, stock_sabado

    while True:
        print("\n---------TOTEM AUTOATENCIÓN CAFECONLECHE-------")
        print("1.- Comprar entrada a Cats")
        print("2.- Cambio de función")
        print("3.- Mostrar stock de funciones")
        print("4.- Salir")
        opcion = input("Seleccione opcion: ")

        if opcion == "1":
            viernes, sabado, stock_v, stock_s = comprar(viernes, sabado, stock_v, stock_s)
        elif opcion == "2":
            viernes, sabado, stock_v, stock_s = cambiar(viernes, sabado, stock_v, stock_s)
        elif opcion == "3":
            mostrar_stock(stock_v, stock_s)
        elif opcion == "4":
            salir()
            break
        else:
            print("Debe ingresar una opcion valida porfavor")

iniciar()

