#Práctica diagnostico_nombre.py
# Simulador de ticket de venta
#Objetivo: Aplicar funciones, bucles, condiciones,
#listas y variables.
#Elegir una tematica de un negocio que vende 3 productos

productos =["porche","mustang","dodge charger"]

precios = [5000000, 780000, 1000000]

#Funcion para calcular el total
def calcular_total(cantidades, precios):
    total = 0
    for i in range (len(cantidades)):
        total += cantidades[i]* precios[i]
    return total

# Menú de usuario
print("Bievenido a car auto")

nombre = input("Ingresa tu nombre:")

cantidades =[]
print("Selecciona tu pedido:")
for i in range(len(productos)):
    print(f"{1+1}.{productos[i]} - ${precios[i]}") 
    cantidad = int(input(f"Cuantos {productos[i]} quieres?"))
    cantidades.append(cantidad)

total= calcular_total(cantidades,precios)   

# Imprimir ticket
print("\n" + "="*40)
print(f"{'TICKET DE VENTA':^40}")
print(f"{'Car Auto':^40}")
print("="*40)
print(f"Cliente: {nombre}")
print("-"*40)
print(f"{'Producto':<20} {'Cantidad':<10} {'Precio':<10}")
print("-"*40)
for i in range(len(productos)):
    if cantidades[i] > 0: 
        print(f"{productos[i]:<20} {cantidades[i]:<10} ${precios[i]*cantidades[i]:,.2f}")
print("-"*40)
print(f"{'TOTAL':<30} ${total:,.2f}")
print("="*40)
print("Gracias por su compra!")

