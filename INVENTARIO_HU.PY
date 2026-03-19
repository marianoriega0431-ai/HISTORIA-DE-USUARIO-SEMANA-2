
inventario = []

def agregar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Error: ingrese solo letras, sin números ni símbolos.")

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("Error: el precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Error: debe ingresar un número válido.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("Error: la cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Error: debe ingresar un número entero válido.")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)

    print("Producto agregado correctamente.")

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        print("\n=== INVENTARIO ===")
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def calcular_estadisticas():
    if len(inventario) == 0:
        print("No hay productos registrados.")
    else:
        valor_total = 0
        total_productos = 0

        for producto in inventario:
            valor_total = valor_total + (producto["precio"] * producto["cantidad"])
            total_productos = total_productos + producto["cantidad"]

        print("\n=== ESTADÍSTICAS ===")
        print("Valor total del inventario:", valor_total)
        print("Cantidad total de productos:", total_productos)

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo.")