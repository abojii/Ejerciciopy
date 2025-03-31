''' 
Desarrolla un programa que calcule el importe a pagar por un vehículo al circular por una autopista. 
El vehículo puede ser una bicicleta, una moto, un carro o un camión. 
Para definir el conjunto de vehículos deben utilizar una estructura adecuada. 
El importe se calculará según los siguientes datos:

a) Un importe fijo de 100 córdobas para la bicicleta.
b) Las motos y los carros pagarán 30 córdobas por Km.
c) Los camiones pagarán 30 córdobas por Km. más 25 córdobas por toneladas. 
'''
tarifas = {
    "a": 100,
    "b": 30,
    "c": 30,
    "d": (30, 25)  # (tarifa por Km, tarifa por tonelada)
}

for i in range(5):  # Ciclo que se repite 5 veces
    print("Seleccione el tipo de vehículo:")
    print("a) Bicicleta")
    print("b) Moto")
    print("c) Carro")
    print("d) Camión")
    tipo_vehiculo = input("Ingrese la opción del tipo de vehículo: ").lower()
    
    if tipo_vehiculo not in tarifas:
        print("Tipo de vehículo no válido. Intente de nuevo.")
        continue  # Vuelve a pedir el tipo de vehículo si es inválido


    if tipo_vehiculo == "a":
        importe = tarifas[tipo_vehiculo]  # Importe fijo para bicicleta
    else:
        distancia = float(input("Ingrese la distancia en kilómetros: "))
        if tipo_vehiculo == "d":
            toneladas = float(input("Ingrese el peso en toneladas: "))
            importe = (tarifas[tipo_vehiculo][0] * distancia) + (tarifas[tipo_vehiculo][1] * toneladas)
        else:
            importe = tarifas[tipo_vehiculo] * distancia

    print(f"El importe a pagar es: {importe} córdobas\n")
