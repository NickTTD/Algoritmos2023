# Importamos la clase 'Lista' desde el módulo 'lista' (presumiblemente un archivo personalizado).
from lista import Lista

# Creamos una lista llamada 'listaAux' que contiene números enteros.
listaAux = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

# Creamos tres listas vacías: 'listaNumeros', 'listaPares', y 'listaImpares'.
listaNumeros = Lista()
listaPares = Lista()
listaImpares = Lista()

# Recorremos los elementos de 'listaAux' e insertamos cada número en 'listaNumeros'.
for Numero in listaAux:
    listaNumeros.insert(Numero)

# Iteramos a través de los índices de 'listaNumeros'.
for Numero in range(listaNumeros.size()):
    # Verificamos si el número en la posición actual es par.
    if listaNumeros.get_element_by_index(Numero) % 2 == 0:
        # Si es par, lo insertamos en 'listaPares'.
        listaPares.insert(listaNumeros.get_element_by_index(Numero))
    else:
        # Si es impar, lo insertamos en 'listaImpares'.
        listaImpares.insert(listaNumeros.get_element_by_index(Numero))

# Imprimimos los números pares.
print("Pares")
listaPares.barrido()

# Imprimimos los números impares.
print("Impares")
listaImpares.barrido()