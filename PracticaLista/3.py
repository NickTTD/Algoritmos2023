#3. Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
#una que contenga los números pares y otra para los números impares.

from lista import Lista

listaAux = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
listaNumeros = Lista()
listaPares = Lista()
listaImpares = Lista()


for Numero in listaAux:
    listaNumeros.insert(Numero)


for Numero in range(listaNumeros.size()):
    if listaNumeros.get_element_by_index(Numero) %2 == 0:
        listaPares.insert(listaNumeros.get_element_by_index(Numero))
    else:
        listaImpares.insert(listaNumeros.get_element_by_index(Numero))

print("Pares")
listaPares.barrido()
print("Impares")
listaImpares.barrido()