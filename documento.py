def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

# Ejemplo de uso:
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2))
print("Multiplicación:", multiplicar(num1, num2))
print("División:", dividir(num1, num2))