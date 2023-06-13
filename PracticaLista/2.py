from lista import Lista

#2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

Palabra = str(input("Ingrese la palabra: "))

listaLetras = Lista()

for letra in Palabra:
    listaLetras.insert(letra)

vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    listaLetras.delete(vocal)

listaLetras.barrido()