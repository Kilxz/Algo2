

def escalon(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return (escalon(n-1) + escalon(n-2))
    
n = int(input("Ingrese número de escalones: "))

while n <= 0:
    print("Número ingresado no válido, vuelva a ingresar: ")
    n = int(input(" "))


print("El número de combinaciones posibles es: ", escalon(n))