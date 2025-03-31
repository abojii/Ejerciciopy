''' Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número. '''

for i in range(5):
    numero = input("\nIngrese un número de tres cifras: ")
    
    if len(numero) == 3 and numero.isdigit():
        numero_reverso = numero[::-1]  # Reversar el número
        if numero == numero_reverso:
            print(f"{numero} es igual a su reverso.")
        else:
            print(f"{numero} no es igual a su reverso.")
    else:
        print("Por favor, ingrese un número válido de tres cifras.")