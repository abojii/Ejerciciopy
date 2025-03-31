''' 
Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, 
ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. 
Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3. 
Diseñe un programa que determine el monto de la compra, el monto del descuento, 
el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.
'''

def calcular_compra(docenas):
    precio_por_docena = 100  # Precio de una docena
    if docenas > 3:
        descuento = 0.15
        unidades_obsequio = docenas - 3
    else:
        descuento = 0.10
        unidades_obsequio = 0

    monto_compra = docenas * precio_por_docena
    monto_descuento = monto_compra * descuento
    monto_a_pagar = monto_compra - monto_descuento

    return monto_compra, monto_descuento, monto_a_pagar, unidades_obsequio

# Ciclo que se repite 5 veces
for i in range(5):
    docenas = int(input("Ingrese la cantidad de docenas: "))
    monto_compra, monto_descuento, monto_a_pagar, unidades_obsequio = calcular_compra(docenas)
    
    print(f"\nMonto de la compra: {monto_compra}")
    print(f"Monto del descuento: {monto_descuento}")
    print(f"Monto a pagar: {monto_a_pagar}")
    print(f"Número de unidades de obsequio: {unidades_obsequio}\n") 