import sys

def sumar_numeros(a, b):
    resultado = a + b
    return resultado

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            print("Usage: python script.py <num1> <num2>")
            sys.exit(1)

        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        
        suma = sumar_numeros(num1, num2)
        print(f"La suma de {num1} y {num2} es: {suma}")
        
    except ValueError:
        print("Error: Ingresa valores enteros válidos.")
