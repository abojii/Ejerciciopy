''' Escribir un programa que permita emitir la FACTURA correspondiente, 
a una compra de un artículo determinado, del que se adquieren una o varias unidades.
El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad), es mayor de 1000,
se aplicará un descuento del 12%. '''

#Definimos la función calcular_factura con los parametros que son los dos input precio,unitario y cantidad.
def calcular_factura(precio_unitario, cantidad): 
    subtotal = precio_unitario * cantidad
    iva = subtotal * 0.15
#Aplicamos la condición para determinar si el subtotal es mayor que 1000 se aplica el descuento.   
    if subtotal > 1000:
        descuento = subtotal * 0.12
    else:
        descuento = 0

    total = subtotal + iva - descuento
    return subtotal, iva, descuento, total #Devuelve los cuatro valores.

#Inicio del blucle for que se repetirán 5 veces.
for i in range(5):
    while True: #Se repetira gasta que la instrucción break lo detenga, hasta el valor válido.
        try:
            precio_unitario = float(input("Ingrese el precio unitario del artículo: "))
            if precio_unitario <=0:
                print("El precio debe ser un número positivo, intente de nuevo")
                continue
            break
        except ValueError:
            print("Por favor, digite un número.")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de artículos: "))
            if cantidad <=0:
                print("La cantidad debe ser un número postivo, intente de nuevo")
                continue
            break
        except ValueError:
            print("Por favor, digite un número entero.")
    subtotal, iva, descuento, total = calcular_factura(precio_unitario, cantidad) #Se llama la función calcular_facturas.

 #Se imprimen los detalles de la factura.    
    print(f"Factura {i+1}:")
    print(f"Subtotal: {subtotal}")
    print(f"IVA: {iva}")
    print(f"Descuento: {descuento}")
    print(f"Total: {total}\n")
