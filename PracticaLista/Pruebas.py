from lista import Lista

#2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.
# ListaAuxiliar=["hola","que","tal"]
# ListaCaracteres = Lista()

# for i in ListaAuxiliar:
#     ListaCaracteres.insert(i)

# print(ListaCaracteres.barrido())
# ListaCaracteres.order_by()

# lista_prueba = Lista()
# lista_valores = []

class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.edad}'


lista_prueba = Lista()
lista_valores = []

def cargar_lista(lista_aux):
    personas = [
        ['Juana', 'Gomez', 34],
        ['Mario', 'Impini', 47],
        ['Laurato', 'Perez', 19],
        ['Leo', 'Impini', 33],
        ['Maria', 'Sittoni', 7],
        ['Julieta', 'Alem', 20],
    ]
    for persona in personas:
        lista_valores.append(Persona(persona[0], persona[1], persona[2]))
        lista_prueba.insert(Persona(persona[0], persona[1], persona[2]), 'edad')

cargar_lista(lista_prueba)
lista_prueba.barrido()

# def apellido_nombre(item):
#     return item.apellido+item.nombre

# def nombre_apellido(item):
#     return item.nombre+item.apellido

# lista_valores.sort(key=nombre_apellido)


# for persona in lista_valores:
#     print(persona)