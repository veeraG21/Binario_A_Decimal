# Pasar de binario a decimal sin funciones
num_binario = input("Introduce un número binario:")

# Con el bucle for recorremos cada dígito (que es un string) para operar con cada uno de forma independiente
for digito_string in num_binario:
	digito = int(digito_string)

# Averiguamos la posición de los digitos restándole 1
posicion = len(num_binario) - 1

for digito_string in num_binario:
    digito = int(digito_string)
    posicion -= 1 #Le vamos restando 1 a la posición con cada vuelta del bucle

# enumerate va recorriendo dos listas simultáneamente, el número y la posición
for posicion, digito_string in enumerate(num_binario[::-1]):
	digito = int(digito_string)
	multiplicacion = digito * 2 ** posicion

# Suma del resultado de cada multiplicación
numero_decimal = 0

# Finalmente sumamos el resultado de todas las multiplicaciones
for posicion, digito_string in enumerate(num_binario[::-1]):
    numero_decimal += int(digito_string) * 2 ** posicion

print(f'El número decimal es {numero_decimal}')