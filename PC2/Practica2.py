# 1. CREA UN MENU ITERACTIVO QUE CUENTE CON LOS SIGUIENTES OPCIONES
# 2. Mostrar el listado de ventas => puedes usar print(f"")
# 3. Añadir un producto
# 4. Calcular la suma total de las ventas
# 5. Calcular el promedio de ventas
# 6. Mostar el producto mas unidades vendidas
# 7. Mostrar el listado de productos

ventas = [
    {"fecha": "12-01-2025", "producto": "Producto_cebada", "cantidad": 850, "precio": 95.00, "promocion": True},
    {"fecha": "11-01-2025", "producto": "Producto_avena", "cantidad": 960, "precio": 110.00, "promocion": False},
    {"fecha": "10-01-2025", "producto": "Producto_cacao", "cantidad": 1920, "precio": 150.00, "promocion": False},
    {"fecha": "11-01-2025", "producto": "Producto_azucar", "cantidad": 1110, "precio": 140.00, "promocion": False},
    {"fecha": "11-01-2025", "producto": "Producto_arroz", "cantidad": 1200, "precio": 127.00, "promocion": True},
]

# Funciones básicas1
def mostrar_ventas():
    print("\nListado de ventas:")
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

def agregar_producto():
    print("\nAñadir un nuevo producto:")
    fecha = input("Fecha (DD-MM-YYYY): ")
    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    promocion = input("¿En promoción? (s/n): ").lower() == 's'
    ventas.append({"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion})
    print("Producto añadido.")

def calcular_suma_total():
    total = 0
    for venta in ventas:
        total += venta["cantidad"] * venta["precio"]
    print(f"\nLa suma total de las ventas es: {total:.2f}")

def producto_mas_vendido():
    if ventas:
        mas_vendido = ventas[0]
        for venta in ventas:
            if venta["cantidad"] > mas_vendido["cantidad"]:
                mas_vendido = venta
        print(f"\nEl producto más vendido es {mas_vendido['producto']} con {mas_vendido['cantidad']} unidades.")
    else:
        print("\nNo hay ventas registradas.")

# Menú principal
while True:
    print("\n==== MENÚ ====")
    print("1. Mostrar el listado de ventas")
    print("2. Añadir un producto")
    print("3. Calcular la suma total de las ventas")
    print("4. Mostrar el producto más vendido")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        mostrar_ventas()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        calcular_suma_total()
    elif opcion == "4":
        producto_mas_vendido()
    elif opcion == "5":
        print("\n¡Gracias por su tiempo en nuestro servicio! Adiós.")
        break
    else:
        print("\nOpción inválida. Por favor, intente de nuevo.")