'''
Se desea escribir un programa para el cálculo del área de diversas superficies: 
cuadrado, rectángulo, círculo, triángulo y trapecio. El programa mostrará al inicio el siguiente menú

Seguidamente leerá de la entrada estándar un valor que estará comprendido entre 1 y 5, 
indicando el tipo de superficie cuya área se desea calcular.  
El programa leerá entonces los datos que necesite para calcular el área en cuestión.  
El resultado se mostrará en la salida estándar, tras lo cual el programa terminará.
'''
def calcular_area():
    for _ in range(5):
        print("===============================================")
        print(" CÁLCULO DE SUPERFICIES (versión 1.0)")
        print("===============================================")
        print(" 1. Cuadrado         lado*lado")
        print(" 2. Círculo         pi*radio*radio")
        print(" 3. Rectángulo       base*altura")
        print(" 4. Trapecio        (base1+base2)*altura/2")
        print(" 5. Triángulo       (base*altura)/2")
        print("===============================================")
        
        opcion = int(input("Ingrese un número entre 1 y 5: "))
        
        if opcion == 1:  # Cuadrado
            lado = float(input("Ingrese la longitud del lado: "))
            area = lado ** 2
            print(f"El área del cuadrado es: {area}")

        elif opcion == 2:  # Círculo
            radio = float(input("Ingrese el radio: "))
            area = 3.14159 * (radio ** 2)
            print(f"El área del círculo es: {area}")
        
        elif opcion == 3:  # Rectángulo
            largo = float(input("Ingrese la longitud: "))
            ancho = float(input("Ingrese el ancho: "))
            area = largo * ancho
            print(f"El área del rectángulo es: {area}")
        
        elif opcion == 4:  # Trapecio
            base_mayor = float(input("Ingrese la base mayor: "))
            base_menor = float(input("Ingrese la base menor: "))
            altura = float(input("Ingrese la altura: "))
            area = ((base_mayor + base_menor) * altura) / 2
            print(f"El área del trapecio es: {area}")
        
        elif opcion == 5:  # Triángulo
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = (base * altura) / 2
            print(f"El área del triángulo es: {area}")
        
        
        
        else:
            print("Opción no válida. Intente de nuevo.")

# Llamar a la función para ejecutar el programa
calcular_area()