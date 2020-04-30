print("Revisaremos si la palabra es palíndromo!")
palabra1 = input("Ingrese la palabra a revisar: ")
palabra1 = palabra1.lower()
palabra2 = palabra1[::-1]
palabra2 = palabra2.lower()

if palabra1 == palabra2:
    print("La palabra es palíndromo!")
else:
    print("La palabra no es palíndromo!")