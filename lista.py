numeros = [10, 5, 7, 2, 1]
print(numeros)

numeros[0]= "hola"
print(numeros)

numeros[4]= numeros[0]
print(numeros)

print(numeros[2])

print(len(numeros))

del numeros[1]
print(numeros)

numeros.append(True)
print(numeros)

numeros.append(5.9)
print(numeros)