#1. Desarrollar una función recursiva que permita contar cuantas veces
#aparece una determinada palabra, en un lista de palabras.
def ContPalabraRecursiva(lista, palabra):
    if len(lista) == 0:
        return 0
    else:
        count = 0
        if lista[0] == palabra:
            count = 1
        return count + ContPalabraRecursiva(lista[1:], palabra) #Usando slicing, también se puede hacer con pop
    
listaPalabras = []
añadirPalabra= 0
while añadirPalabra != "S":
    añadirPalabra = input("Ingrese palabra para agregar a la lista de palabras, S para salir: ")
    listaPalabras.append(añadirPalabra)
palabra_buscada = input ("Ingrese la palabra a contar")

contador = ContPalabraRecursiva(listaPalabras, palabra_buscada)
print(f"La palabra '{palabra_buscada}' aparece {contador} veces en la lista.")