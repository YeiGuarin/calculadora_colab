def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division (a, b):
    if b != 0:
        return a / b
    else:
        print("Indefinido. No se puede dividir por cero")

def main():
    while(True):
        print("Calculadora Básica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")	

        if opcion == "5":
            print("Saliendo de la calculadora...")
            break

        try:
            a = int(input("Ingresa el primer número: "))
            b = int(input("Ingresa el segundo numero: "))

        except ValueError:
                print("Error, debes ingresar numeros validos")
                continue

        if opcion == "1":
            print("El resultado de la suma es: ", suma(a, b))

        elif opcion == "2":
            print("Resultado de la resta: ", resta(a,b))

        elif opcion == "3":
            print("El resultado de la multiplicacion es: ", multiplicacion(a, b))

        elif opcion == "4":
            resultado = division(a, b)
            print("El resultado de la division es: ", resultado)

        else:
            print("Opcion no valida, prfavor ngresa una opcion del 1 al 5")

main()