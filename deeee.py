def sumar_positivos(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        return "Ingrese numeros validos"
    
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

sumar = sumar_positivos(a, b)

print(sumar)